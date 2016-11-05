# -*- coding: utf-8 -*-

# Pelican settings ------------------------------------------------------------

AUTHOR = 'Multiple'
SITENAME = 'Nairobi GNU/Linux Users Group'
# Intentionally left blank, see publishconf.py
SITEURL = ''

TIMEZONE = 'Africa/Nairobi'
DEFAULT_LANG = 'en'
PATH = 'content'
THEME = 'theme/alchemy'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_LANG_SAVE_AS = '{date:%Y}/{date:%m}/{slug}-{lang}.html'
ARTICLE_LANG_URL = '{date:%Y}/{date:%m}/{slug}-{lang}.html'

PAGE_URL = '{date:%Y}/{date:%m}/pages/{slug}.html'
PAGE_SAVE_AS = '{date:%Y}/{date:%m}/pages/{slug}.html'
PAGE_LANG_SAVE_AS = '{date:%Y}/{date:%m}/pages/{slug}-{lang}.html'
PAGE_LANG_URL = '{date:%Y}/{date:%m}/pages/{slug}-{lang}.html'

STATIC_PATHS = [
    'extra/CNAME',
    'extra/favicon.ico',
    'extra/favicon-16x16.png',
    'extra/favicon-32x32.png',
    'extra/favicon-96x96.png',
    'extra/favicon-160x160.png',
    'extra/favicon-196x196.png',
    'images',
]

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/favicon-16x16.png': {'path': 'favicon-16x16.png'},
    'extra/favicon-32x32.png': {'path': 'favicon-32x32.png'},
    'extra/favicon-96x96.png': {'path': 'favicon-96x96.png'},
    'extra/favicon-160x160.png': {'path': 'favicon-160x160.png'},
    'extra/favicon-196x196.png': {'path': 'favicon-196x196.png'},
}

DEFAULT_PAGINATION = 20

# Theme settings --------------------------------------------------------------

SITE_SUBTEXT = 'A lively community of GNU/Linux enthusiasts'
META_DESCRIPTION = 'A not-for-profit community serving the greater Nairobi ' \
                   'area. We are a collection of people dedicated to ' \
                   'GNU/Linux, Free Software, Open Source, and related topics.'

PAGES_ON_MENU = True
PROFILE_IMAGE = '/images/profile.svg width="200" height="200"'
SHOW_ARTICLE_AUTHOR = True
EXTRA_FAVICON = True

MENU_ITEMS = (
    ('IRC', 'http://webchat.freenode.net/?channels=nairobilug'),
    ('Mailing List', 'https://groups.google.com/forum/#!forum/nairobi-gnu'),
)

GITHUB_ADDRESS = 'https://github.com/nairobilug'
TWITTER_ADDRESS = 'https://twitter.com/nairobilug'
GPLUS_ADDRESS = 'https://plus.google.com/communities/107260210367217532462'
