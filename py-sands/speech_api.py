#!/usr/bin/env python
# -*- coding: utf-8 -*-

import contextlib
import urllib2


def getwebsite(url, timeout=5):
    """
        This method retrieved the website at the url encoded url
        if this method fails to retrieve the website with the given timeout
        or anything else, None is returned
    """
    try:
        with contextlib.closing(urllib2.urlopen(url, timeout=timeout)) as page:
            body = page.read()
            return body
    except:
        pass
    return None


def run(flac, language, allowcurses):
    url = "https://www.google.com/speech-api/v1/recognize?xjerr=1&client=chromium&pfilter={0}&lang={1}&maxresults=6".format(
        0 if allowcurses else 2, language)
    req = urllib2.Request(
        url,
        data=flac,
        headers={'Content-Type': 'audio/x-flac; rate=16000'})
    return getwebsite(req, timeout=10)

# FILE='1.flac' #这里假设在当前文件夹下有一个叫1.flac的文件被识别
# audio=open(FILE,'rb').read()
# headers = {'Content-Type' : 'audio/x-flac; rate=16000'}
# 【POST】flac文件的数据 22050 Hz+201kbps
# 【URL里可选参数】&maxresults=返回结果数
# response = urllib2.urlopen(req)
# print response.read().decode('UTF-8')
print(run('a', 1, 'zh-CN', ''))
