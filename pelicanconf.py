#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import datetime

### --------------------- ###
### general site settings ###
### --------------------- ###
SITEURL = 'https://jordynelson.io'
AUTHOR = u'Jordy Nelson'

SITENAME = u'Jordy Nelson'
#SITESUBTITLE              = u''
SHOW_SITESUBTITLE_IN_HTML = False

DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%d %b %Y'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/jordy.nelson248'),
          ('LinkedIn', 'https://www.linkedin.com/in/jordynelson/')
          )

# Pagination
DEFAULT_PAGINATION = 5
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['assets']

EXTRA_PATH_METADATA = {
    'assets/robots.txt': {'path': 'robots.txt'},
    'assets/favicon.ico': {'path': 'favicon.ico'},
    'assets/CNAME': {'path': 'CNAME'}
}

# Post and Pages path
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
PAGE_URL = 'pages/{slug}/.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}.html'

# Tags and Category path
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}.html'
CATEGORIES_SAVE_AS = 'catgegories.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}.html'
TAGS_SAVE_AS = 'tags.html'

# Author
AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = 'author/{slug}.html'
AUTHORS_SAVE_AS = 'authors.html'

# Year
CURR_YEAR = datetime.datetime.now().year

### ------- ###
### Plugins ###
### ------- ###
PLUGINS = ['sitemap',
           'neighbors',
           'render_math',
           'simple_footnotes']
PLUGIN_PATHS = ['pelican-plugins']

# Sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Analytics
GOOGLE_ANALYTICS = "UA-78411303-1"

# GTM
GOOGLE_TAG_MANAGER = "GTM-TJN5JZ6"

# Comments
DISQUS_SITENAME = "jordynelson"

### --------------- ###
### output settings ###
### --------------- ###
# specify where pelican finds content to publish
PATH = 'content'
# specify where pelican publishes content
OUTPUT_PATH = 'output'
# disable cachine
LOAD_CONTENT_CACHE = False
# what slug is generated from
SLUGIFY_SOURCE = 'title'
# port used with `pelican --listen`
PORT = 8000

### -------------- ###
### theme settings ###
### -------------- ###
# directory containing theme
THEME = 'themes/martian'
# subdir in output dir where static files are placed
THEME_STATIC_DIR = 'theme'
# list of theme static paths to copy to THEME_STATIC_DIR
THEME_STATIC_PATHS = ['static',
                      'assets'
                      ]
COLOR_SCHEME_CSS = 'monokai.css'
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = [('home', '/index.html'),
             ('about', '/pages/about.html')
             ]

### ------------------------- ###
### additional theme settings ###
### ------------------------- ###
MP_BOOTSTRAPPED = True
MP_USE_FONTAWESOME = True
CSS_OVERRIDE = [
    #                '{0}/{1}/css/normalize.css'.format(SITEURL, THEME_STATIC_DIR), # normalize styles
    #                '{0}/{1}/css/main.css'.format(SITEURL, THEME_STATIC_DIR),      # main custom styles
    # normalize styles (DEV VERSION)
    'theme/css/normalize.css',
    # main custom styles (DEV VERSION)
    'theme/css/main.css'
]
JS_OVERRIDE = [
    #                '{0}/{1}/js/script.js'.format(SITEURL, THEME_STATIC_DIR),    # normalize styles
    #                '{0}/{1}/js/myscript.js'.format(SITEURL, THEME_STATIC_DIR), # main custom styles
    # normalize styles (DEV VERSION)
    'theme/js/script.js',
    # main custom styles (DEV VERSION)
    'theme/js/myscript.js'
]

# hero, live
FAVICON = '{0}/{1}/assets_images/favicon_jn.png'.format(
    SITEURL, THEME_STATIC_DIR)
# hero, dev
FAVICON = 'theme/assets_images/favicon_jn.png'

# hero, live
HEADER_COVER = '{0}/{1}/assets_images/crater.jpg'.format(
    SITEURL, THEME_STATIC_DIR)
# hero, dev
HEADER_COVER = 'theme/assets_images/crater.jpg'

# list of article.title to ignore in default pagination
PAGINATION_IGNORE = ['404', 'about']

### ------- ###
### authors ###
### ------- ###

AUTHORS_BIO = {
    "jordy": {
        "name": "jordy",
        "cover": "theme/assets_images/jordy.jpg",
        "image": "theme/assets_images/jordy.jpg",
        "website": "https://jordynelson.io",
        "location": "Baltimore",
        "bio": "This is the place for a small biography with max 200 characters. Well, now 100 are left. Cool, hugh?"
    }
}
