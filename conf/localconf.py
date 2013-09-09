#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'askender'
SITENAME = u"柏舟志 askender's blog"
SITEURL = '/blog'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None


# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
        ('Python.org', 'http://python.org/'),
        ('Jinja2', 'http://jinja.pocoo.org/'),
        ('安问-创造和分享美好 毕生的项目 Anwen - Create and share something nice project which spend all my life', 'http://anwensf.com/'),)

# Social widget
SOCIAL = (('github', 'https://github.com/askender'),
          ('twitter', 'https://twitter.com/askenderlee'),
          ('envelope', 'mailto:askender@gmail.com'),
          ('rss', '/blog/feeds/all.atom.xml'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/pelican-bootstrap3'
