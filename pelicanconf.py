#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# Settings for local preview. See publishconf.py for production settings.
from datetime import datetime

AUTHOR = 'Jose Luis Blanco'

SITEURL = ''
RELATIVE_URLS = False

SITENAME = "Jose Luis Blanco Claraco"
SITETITLE = AUTHOR
SITESUBTITLE = 'Professor at <a href="https://www.ual.es/">UAL</a> - Mechanical Engineering & Robotics'
SITEDESCRIPTION = ('Full Professor at the University of Almería: mobile robotics, '
                   'SLAM, multibody dynamics. Lead developer of MRPT and MOLA.')
SITELOGO_PATH = 'imgs/jlblanco.jpg'
FAVICON_PATH = 'imgs/favicon.ico'
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'manni'
THEME_COLOR = "light"
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = False
THEME_COLOR_ENABLE_USER_OVERRIDE = True

ROBOTS = 'index, follow'

THEME = 'themes/Flex'
THEME_TEMPLATES_OVERRIDES = ['templates']
PATH = 'content'
TIMEZONE = 'Europe/Madrid'
DEFAULT_LANG = 'en'
OG_LOCALE = 'en_US'
LOCALE = 'en_US.UTF-8'

# Researcher identifiers, also used in the schema.org metadata
ORCID = '0000-0002-9745-285X'
GOOGLE_SCHOLAR = 'https://scholar.google.com/citations?user=bhDtzKgAAAAJ'

# This is a static site made of pages only: no blog, feeds, or archives
ARTICLE_PATHS = ['posts']
DIRECT_TEMPLATES = []
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
ARCHIVES_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAG_SAVE_AS = ''
TAGS_SAVE_AS = ''

MAIN_MENU = False
DISPLAY_PAGES_ON_MENU = True
DISABLE_URL_HASH = True
PAGES_SORT_ATTRIBUTE = 'myorder'
LINKS_IN_NEW_TAB = 'external'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

LINKS = (
    ('Engineering Dept.', 'https://ingmec.ual.es/area/'),
    ('ARM group', 'https://arm.ual.es/'),
)

SOCIAL = (
    ('orcid', 'https://orcid.org/' + ORCID),
    ('google-scholar', GOOGLE_SCHOLAR),
    ('github', 'https://github.com/jlblancoc'),
    ('linkedin', 'https://www.linkedin.com/in/jose-luis-blanco-claraco-7511b712/'),
    ('youtube', 'https://www.youtube.com/user/jlblanco2006'),
)

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_NAME = SITENAME
COPYRIGHT_YEAR = datetime.now().year

PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['embed_http', 'pelican.plugins.sitemap']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'monthly',
        'pages': 'monthly',
    }
}

STATIC_PATHS = ['imgs', 'docs', 'css', 'extra']

# Legacy URLs and site verification files, served from the site root
EXTRA_PATH_METADATA = {
    'extra/divulgacion.html': {'path': 'divulgacion.html'},
    'extra/docencia.html': {'path': 'docencia.html'},
    'extra/publications.html': {'path': 'publications.html'},
    'extra/software.html': {'path': 'software.html'},
    'extra/videos.html': {'path': 'videos.html'},
    'extra/google9dffe6009a8d8a62.html': {'path': 'google9dffe6009a8d8a62.html'},
}

CUSTOM_CSS = 'css/custom.css'

# Derived from SITEURL; publishconf.py recomputes them after overriding it
SITELOGO = '%s/%s' % (SITEURL, SITELOGO_PATH)
FAVICON = '%s/%s' % (SITEURL, FAVICON_PATH)
