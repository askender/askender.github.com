

def truncate(text, limit=80):
    return text[:limit] + '...'

from datetime import datetime, timedelta
import md5
import urllib
import settings
import smtplib


def generate_recovery_link(self, user):
    expired = datetime.now() + timedelta(days=1)
    token = md5(
        str(user.id) + expired.strftime("%H:%M:%S %m/%d/%Y")).hexdigest()
    params = urllib.urlencode(dict(token=token))
    return params


def send_recovery_mail(self, user, url):
    smtp_server = self.connect_smtp_server(
        settings.email_host,
        settings.email_port,
        settings.email_host_user,
        settings.email_host_password
    )
    smtp_server.sendmail(
        settings.email_host_user,
        user.email,
        self.build_message(user, url)
    )
    smtp_server.quit()


def connect_smtp_server(self, email_host, email_port, user, password):
    smtp_server = smtplib.SMTP('%s:%s' % (email_host, email_port))
    smtp_server.starttls()
    smtp_server.login(user, password)
    return smtp_server


epoch = datetime(1970, 1, 1)


def epoch_seconds(date):
    """Returns the number of seconds from the epoch to date."""
    td = date - epoch
    return td.days * 86400 + td.seconds + (float(td.microseconds) / 1000000)


from math import log


def hot(ups, downs, date):
    """The hot formula. Should match the equivalent function in postgres."""
    s = ups - downs
    order = log(max(abs(s), 1), 10)
    sign = 1 if s > 0 else -1 if s < 0 else 0
    seconds = epoch_seconds(date) - 1134028003
    return round(order + sign * seconds / 45000, 7)

from math import sqrt


def _confidence(ups, downs):
    n = ups + downs

    if n == 0:
        return 0

    z = 1.0  # 1.0 = 85%, 1.6 = 95%
    phat = float(ups) / n
    return sqrt(phat + z * z / (2 * n) - z * ((phat * (1 - phat) + z * z / (4 * n)) / n)) / (1 + z * z / n)


def confidence(ups, downs):
    if ups + downs == 0:
        return 0
    else:
        return _confidence(ups, downs)


class PostHandler():
    def get(self, slug):
        key = "BlogscokeorgPostOne:%s" % slug
        html_main = self.cache.get(key)
        if html_main is None:
            post = self.get_post_by_slug(slug)
            if not post:
                self.send_error(404)
                return
            post.views += 1
            self.db.add(post)
            self.db.commit()
            self.render('post.html', post=post)
            html_main = self.render_string("post.html", post=post)
            self.cache.set(key, html_main)
            self.cache.expire(key, 3600)
        else:
            self.write(html_main)

import time


def timeit(func):
    def warpper():
        start = time.time()
        func()
        print "used:", time.time() - start
    return warpper


def pretty_date(self, time=False):
    """
    Get a datetime object or a int() Epoch timestamp and return a
    pretty string like 'an hour ago', 'Yesterday', '3 months ago',
    'just now', etc
    """
    if time is None:
        return time

    from datetime import datetime
    now = datetime.now()
    if type(time) is str or type(time) is unicode:
        time = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
    elif type(time) is int:
        diff = now - datetime.fromtimestamp(time)
    elif isinstance(time, datetime):
        diff = now - time
    elif not time:
        diff = now - now
    second_diff = diff.seconds
    day_diff = diff.days

    if day_diff < 0:
        return ''

    if day_diff == 0:
        if second_diff < 10:
            return "刚刚"
        if second_diff < 60:
            return str(second_diff) + " 秒前"
        if second_diff < 120:
            return  "1 分钟前"
        if second_diff < 3600:
            return str(second_diff / 60) + " 分钟前"
        if second_diff < 7200:
            return "1 小时前"
        if second_diff < 86400:
            return str(second_diff / 3600) + " 小时前"
    if day_diff == 1:
        return "昨天"
    if day_diff < 7:
        return str(day_diff) + " 天前"
    if day_diff < 31:
        return str(day_diff / 7) + " 周前"
    if day_diff < 365:
        return str(day_diff / 30) + " 月前"
    return str(day_diff / 365) + " 天前"


def content_process(self, content):
    # render content included gist
    content = re.sub(r'http(s)?:\/\/gist.github.com\/(\d+)(.js)?', r'<script src="http://gist.github.com/\2.js"></script>', content)
    # render sinaimg pictures
    content = re.sub(r'(http:\/\/\w+.sinaimg.cn\/.*?\.(jpg|gif|png))',
                     r'<img src="\1" />', content)
    # render @ mention links
    content = re.sub(r'@(\w+)(\s|)', r'@<a href="/u/\1">\1</a> ', content)
    # render youku videos
    content = re.sub(r'http://v.youku.com/v_show/id_(\w+).html', r'<embed src="http://player.youku.com/player.php/sid/\1/v.swf" quality="high" width="480" height="400" align="middle" allowScriptAccess="sameDomain" allowFullscreen="true" type="application/x-shockwave-flash"></embed>', content)
    return content


import re


def find_mentions(content):
    regex = re.compile(r"@(?P<username>\w+)(\s|$)", re.I)
    return [m.group("username") for m in regex.finditer(content)]


class ObjectDict(dict):
    def __getattr__(self, key):
        if key in self:
            return self[key]
        return None

    def __setattr__(self, key, value):
        self[key] = value


def find_mention(text):
    regex = r'@(\w+)\s'
    return re.findall(regex, text)
