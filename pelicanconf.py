#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import datetime

AUTHOR = u'Pawel Wnuk'
SITENAME = u'Deep Data'
SITEURL = 'http://localhost:8000'
SITETITLE = 'DeepData site'
SITESUBTITLE = 'Insights and hints on Data Science, Machine Learning and Deep Learning'
SITEDESCRIPTION = 'My preronal site'
SITELOGO = SITEURL + '/images/logo.jpg'
BROWSER_COLOR = '#333333'
ROBOTS = 'index, follow'
PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'English'

THEME = 'theme/templates/flex'

DISQUS_SITENAME = 'deepdata-com-pl'

#MARKUP = ('md', 'ipynb')
MARKUP = ('md',)
PLUGIN_PATHS = ['./plugins']
#'ipynb.markup',
PLUGINS = [
		   'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', 
		   'ipynb.liquid',
		   'sitemap']
#'liquid_tags.notebook',		   
IGNORE_FILES = [".ipynb_checkpoints"]
#EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

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
    },
	'exclude': ['tag/', 'category/']
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll

USE_FOLDER_AS_CATEGORY = False #categories are not infered from location folder
DEFAULT_CATEGORY = 'article' #in case it is not specified in input file

MAIN_MENU = True
HOME_HIDE_TAGS = True
LINKS = (('Kaggle', 'https://www.kaggle.com'),
         ('DeepData', 'http://www.deepdata.com.pl'),)
		 #those urls ogether with pages in pages folder will be placed in left menu.
MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)
			 #those items are created at top of pages
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/pawel-wnuk-phd-418a9814'),)

COPYRIGHT_YEAR = datetime.datetime.now().year

STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {'extra/custom.css': {'path': 'static/custom.css'},
'extra/favicon.ico': {'path': 'favicon.ico'},
'extra/google1de616436ea43247': {'path': 'google1de616436ea43247.html'},
'extra/robots.txt': {'path': 'robots.txt'},}


CUSTOM_CSS = 'static/custom.css'
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
