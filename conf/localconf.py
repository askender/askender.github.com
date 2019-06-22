#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'askender'
SITENAME = u"柏舟志 askender's blog"
SITEURL = '/blog'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None


# Blogroll
LINKS = (
    ('安问 - 创造和分享美好', 'http://anwensf.com/'),
)

# Social widget
SOCIAL = (
    ('twitter', 'https://twitter.com/askenderlee'),
    ('github', 'https://github.com/askender'),
    ('envelope', 'mailto:askender43@gmail.com'),
    ('rss', '/blog/feeds/all.atom.xml'),
)


DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = 'themes/attila'
# THEME = 'themes/pelican-bootstrap3'
# THEME = 'themes2/sneakyidea'
DISPLAY_CATEGORIES_ON_MENU = False

ABOUT_ME = 'My name is Bo Li, I\'m a free develolper interested in AI, NLP, reading, SciFi, dreaming.'

CUSTOM_CSS = 'theme/css/local.css'
TAG_CLOUD_MAX_ITEMS = 8

# BOOTSTRAP_THEME = 'united'
# cerulean 1
# superhero 1
# united red
# cyborg black


# for theme: attila
# HEADER_COVER = 'static/my_image.png'
HEADER_COLOR = 'black'
# COLOR_SCHEME_CSS = 'monokai.css'
# CSS_OVERRIDE = ['css/myblog.css']

AUTHORS_BIO = {
    "askender": {
        "name": "Askender",
        "cover": "/avatar.png",
        "image": "/avatar.png",
        "website": "http://askender.xyz",
        "location": "Hangzhou",
        "bio": "This is the place for blog"
    }
}

# GOOGLE_ANALYTICS
# GAUGES
# GOOGLE_SITE_VERIFICATION
# SHOW_FULL_ARTICLE

# article meta: header_cover
