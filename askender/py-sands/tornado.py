# 自己写一个Comet架构程序的服务器端部分
# 理解Tornado web框架
# Twisted ?
# http://golubenco.org/?p=16


def handler_request(self, request):
    self.remote_server.query_async(request, self.response_received)


def response_received(self, request, answ):    # this is called 5 seconds later
    request.write(answ)


def add_handler(self, fd, handler, events):
    """Registers the given handler to receive the given events for fd."""
    self._handlers[fd] = handler
    self._impl.register(fd, events | self.ERROR)
    # self._impl是select.epoll()和selet.select()两者中的一个


def start(self):
    """Starts the I/O loop.
    The loop will run until one of the I/O handlers calls stop(), which
    will make the loop stop after the current event iteration completes.
    """
    self._running = True
    while True:
        print '...'
        if not self._running:
            break
        print '...'
        try:
            event_pairs = self._impl.poll(poll_timeout)
        except Exception, e:
            if e.args == (4, "Interrupted system call"):
                logging.warning("Interrupted system call", exc_info=1)
                continue
            else:
                raise
        # Pop one fd at a time from the set of pending fds and run
        # its handler. Since that handler may perform actions on
        # other file descriptors, there may be reentrant calls to
        # this IOLoop that update self._events
        self._events.update(event_pairs)
        while self._events:
            fd, events = self._events.popitem()
            try:
                self._handlers[fd](fd, events)
            except KeyboardInterrupt:
                raise
            except OSError, e:
                if e[0] == errno.EPIPE:
                    # Happens when the client closes the connection
                    pass
                else:
                    logging.error("Exception in I/O handler for fd %d",
                                  fd, exc_info=True)
            except:
                logging.error("Exception in I/O handler for fd %d",
                              fd, exc_info=True)


def write(self, data, callback=None):
    """Write the given data to this stream.
    If callback is given, we call it when all of the buffered write
    data has been successfully written to the stream. If there was
    previously buffered write data and an old write callback, that
    callback is simply overwritten with this new callback.
    """
    self._check_closed()
    self._write_buffer += data
    self._add_io_state(self.io_loop.WRITE)
    self._write_callback = callback


def _handle_read(self):
    try:
        chunk = self.socket.recv(self.read_chunk_size)
    except socket.error, e:
        if e[0] in (errno.EWOULDBLOCK, errno.EAGAIN):
            return
        else:
            logging.warning("Read error on %d: %s",
                            self.socket.fileno(), e)
            self.close()
            return
    if not chunk:
        self.close()
        return
    self._read_buffer += chunk
    if len(self._read_buffer) >= self.max_buffer_size:
        logging.error("Reached maximum read buffer size")
        self.close()
        return
    if self._read_bytes:
        if len(self._read_buffer) >= self._read_bytes:
            num_bytes = self._read_bytes
            callback = self._read_callback
            self._read_callback = None
            self._read_bytes = None
            callback(self._consume(num_bytes))
    elif self._read_delimiter:
        loc = self._read_buffer.find(self._read_delimiter)
        if loc != -1:
            callback = self._read_callback
            delimiter_len = len(self._read_delimiter)
            self._read_callback = None
            self._read_delimiter = None
            callback(self._consume(loc + delimiter_len))


def listen(self, port, address=""):
    assert not self._socket
    self._socket = socket.(socket.AF_INET, socket.SOCK_STREAM, 0)
    flags = fcntl.fcntl(self._socket.fileno(), fcntl.F_GETFD)
    flags |= fcntl.FD_CLOEXEC
    fcntl.fcntl(self._socket.fileno(), fcntl.F_SETFD, flags)
    self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self._socket.setblocking(0)
    self._socket.bind((address, port))
    self._socket.listen(128)
    self.io_loop.add_handler(self._socket.fileno(), self._handle_events,
                             self.io_loop.READ)

# 如果你很想知道xheaders参数的意义，请看这段注释：

# 如果xheaders为True，我们将支持把所有请求的HTTP头解析成X-Real-Ip和X-Scheme格式，而原先我们将HTTP头解析成remote IP和HTTP scheme格式。这种格式的HTTP头在Tornado运行于反向代理或均衡负载服务器的后端时将非常有用。

# _on_headers()回调函数实际用来解析HTTP头，并在有请求内容的情况下通过使用read_bytes()来读取请求的内容部分。_on_request_body()回调函数用来解析POST的参数并调用应用层提供的回调函数：


def _on_headers(self, data):
    eol = data.find("rn")
    start_line = data[:eol]
    method, uri, version = start_line.split(" ")
    if not version.startswith("HTTP/"):
        raise Exception("Malformed HTTP version in HTTP Request-Line")
    headers = HTTPHeaders.parse(data[eol:])
    self._request = HTTPRequest(
        connection=self, method=method, uri=uri, version=version,
        headers=headers, remote_ip=self.address[0])
    content_length = headers.get("Content-Length")
    if content_length:
        content_length = int(content_length)
        if content_length > self.stream.max_buffer_size:
            raise Exception("Content-Length too long")
        if headers.get("Expect") == "100-continue":
            self.stream.write("HTTP/1.1 100 (Continue)rnrn")
        self.stream.read_bytes(content_length, self._on_request_body)
        return
    self.request_callback(self._request)


def _on_request_body(self, data):
    self._request.body = data
    content_type = self._request.headers.get("Content-Type", "")
    if self._request.method == "POST":
        if content_type.startswith("application/x-www-form-urlencoded"):
            arguments = cgi.parse_qs(self._request.body)
            for name, values in arguments.iteritems():
                values = [v for v in values if v]
                if values:
                    self._request.arguments.setdefault(name, []).extend(
                        values)
        elif content_type.startswith("multipart/form-data"):
            boundary = content_type[30:]
            if boundary:
                self._parse_mime_body(boundary, data)
    self.request_callback(self._request)

将结果写回客户端的工作在HTTPRequest类中处理，你可以在上面的_on_headers()方法中看到具体的实现。HTTPRequest类仅仅将写回的工作代理给了stream对象。


def write(self, chunk):
    assert self._request, "Request closed"
    self.stream.write(chunk, self._on_write_complete)

    import errno
    import functools
    import ioloop
    import socket

    def connection_ready(sock, fd, events):
        while True:
            try:
                connection, address = sock.accept()
            except socket.error, e:
                if e.args[0] not in (errno.EWOULDBLOCK, errno.EAGAIN):
                    raise
                return
            connection.setblocking(0)
            handle_connection(connection, address)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setblocking(0)
    sock.bind(("", port))
    sock.listen(128)

#创建一个ioloop 实例
    io_loop = ioloop.IOLoop.instance()
#冻结 connection_ready 的第一个参数为 sock ,既 socket 的返回值
    callback = functools.partial(connection_ready, sock)
#注册函数，  第一个参数是将 sock 转换为标准的描述符，第二个为回调函数，第三个是事件类型
    io_loop.add_handler(sock.fileno(), callback, io_loop.READ)
#开始~
    io_loop.start()


# 文章属原创，转载请注明出处 联系作者： Email:zhangbo1@ijinshan.com QQ:513364476