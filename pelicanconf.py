#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import os
from datetime import datetime

AUTHOR = 'Jose Luis Blanco'

#if os.getenv('PELICAN_BUILD_FOR_WEB','0')!='0':
SITEURL = 'https://w3.ual.es/~jlblanco'
#else:
#SITEURL = 'http://localhost/~jlblanco/pelican'

print(('SITEURL: ' + SITEURL))

SITENAME = "Jose Luis Blanco Claraco"
SITETITLE = AUTHOR
SITESUBTITLE = 'Associate Professor at <a href="//w3.ual.es/">UAL</a> - Mechanical Engineering & Robotics'
SITEDESCRIPTION = '%s\'s Thoughts and Writings' % AUTHOR
SITELOGO = '%s/imgs/jlblanco.jpg' % SITEURL
#FAVICON = '/images/favicon.ico'
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'manni'

ROBOTS = 'index, follow'

THEME = 'themes/Flex'
PATH = 'content'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'
OG_LOCALE = 'en_US.UTF-8'
LOCALE = 'en_US.UTF-8'

DATE_FORMATS = {
    'en': '%d %B %Y',
}

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True

ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

LINKS = (
	('News', '%s/archives.html' % SITEURL),
	('Engineering Dept.', 'https://ingmec.ual.es/area/'),
	('ARM group','https://arm.ual.es/')
)


SOCIAL = (('linkedin', 'https://es.linkedin.com/in/jose-luis-blanco-claraco-7511b712/en'),
          ('github', 'https://github.com/jlblancoc'),
	  ('youtube', 'https://www.youtube.com/user/jlblanco2006'),
          ('rss', '%s/feeds/all.atom.xml' % SITEURL))

MENUITEMS = (('News/Noticias', '%s/archives.html' % SITEURL),
	)

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = datetime.now().year

DEFAULT_PAGINATION = 10

PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = [ 'embed_http' ] #,'pin_to_top']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}

DISQUS_SITENAME = "jlblanco-personal-web"

STATIC_PATHS = [ 'imgs', 'docs' ]

#EXTRA_PATH_METADATA = {
#    'imgs/jlblanco.jpg': {'path': 'imgs/jlblanco.jpg'},
#}

#CUSTOM_CSS = 'static/custom.css'

#USE_LESS = True
