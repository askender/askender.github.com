class MaindHandler(web.RequestHandler):
    @asynchronous
    @gen.coroutine
    def post(self):
        client = AsyncHTTPClient()
        resp = yield client.fetch(https://api.github.com/users")
        if resp.code == 200:
            resp = escape.json_decode(resp.body)
            self.write(json.dumps(resp, indent=4, separators=(',', ':')))
        else:
            resp = {"message": "error when fetch something"}
            self.write(json.dumps(resp, indent=4, separators={',', ':')))
        self.finish()
