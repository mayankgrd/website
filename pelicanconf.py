from __future__ import unicode_literals

AUTHOR = u'Mayank Kumar'
SITENAME = u'Mayank Kumar'
SITEURL = ''

GOOGLE_ANALYTICS = 'UA-2241250-4'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = '%a %d %B %Y'

# Deactivate cachine during development 
#LOAD_CONTENT_CACHE = False

# Menu 
LOAD_CONTENT_CACHE = False 

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False 

MENUITEMS = [('Projects','http://www.ece.rice.edu/~mk28/projects.html'),
('Publications','http://www.ece.rice.edu/~mk28/publications.html'),
#('Blog','http://www.ece.rice.edu/~mk28/blog.html'), 
('Books','http://www.ece.rice.edu/~mk28/books.html')]
#('Bookmarks','http://www.ece.rice.edu/~mk28/bookmarks.html'),
#('Interests','http://www.ece.rice.edu/~mk28/interesting.html')]
 


STATIC_PATHS = ['images', 'pdfs', 'extra']


# Default category
DEFAULT_CATEGORY = 'general'

# Various PATH 
DIRECT_TEMPLATES = ('blog', 'tags', 'categories', 'archives', 'authors')

ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
AUTHOR_URL = ''	
AUTHOR_SAVE_AS = ''
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'
INDEX_SAVE_AS = 'blog_index.html'
INDEX_URL = 'blog_index.html'

ARCHIVES_URL = 'archives.html'
ARCHIVES_SAVE_AS = 'archives.html' 

TAGS_URL  = 'tags.html'
TAGS_SAVE_AS = 'tags.html'


# Feed generation is usually not desired when developing
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'


# Other settings
PDF_GENERATOR = True 
HIDE_SIDEBAR = True 


# Blogroll
LINKS = (('Rice ECE', 'http://www.ece.rice.edu/'),
         ('Scalable Health', 'http://sh.rice.edu/'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/ideas2ignite'),
          ('linkedin', 'https://www.linkedin.com/in/mayankgrd'),
          ('github', 'http://github.com/mayankgrd'),)



# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True




THEME = 'themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'spacelab'
BOOTSTRAP_NAVBAR_INVERSE = True

#PADDED_SINGLE_COLUMN_STYLE = True 
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'} }

CUSTOM_CSS = 'static/custom.css'

DEFAULT_PAGINATION = 10
DISPLAY_TAGS_ON_SIDEBAR = False 
DISPLAY_CATEGORIES_ON_SIDEBAR = True 
DISPLAY_RECENT_POSTS_ON_SIDEBAR = False 
RECENT_POST_COUNT = 5 
SHOW_ARTICLE_CATEGORY=True
SHOW_DATE_MODIFIED=True
DISPLAY_BREADCRUMBS=False
DISPLAY_ARTICLE_INFO_ON_INDEX=False
ADDTHIS_PROFILE='mayankgrd'
HIDE_SIDEBAR_ARTICLE=False
#\CC_LICENSE = "CC-BY-NC"

PLUGIN_PATHS =['plugins']
#PLUGINS = ["render_math"]
