"""
Pin to top plugin for Pelican
================================

Adds .pin variable to article's context and pins the article to the top
 even if it is older than the other articles
"""
from pelican import signals
from pprint import pprint

def update_pinned_articles(generator):
    new_order = []
    # count articles and keep the pinned ordered by date
    pinned = 0;
    for article in generator.articles:
        if hasattr(article,'pin'):
            new_order.insert(pinned,article)
            pinned += 1
        else:
            new_order.append(article)
    generator.articles = new_order

def update_pinned_pages(generator):
    new_order = []
    # count pages and keep the pinned ordered by date
    pinned = 0;
    for page in generator.pages:
        pprint(vars(page))
        if hasattr(page,'pin'):
            new_order.insert(pinned,page)
            pinned += 1
        else:
            new_order.append(page)
    generator.pages = new_order

def register():
	p=0;
    #signals.article_generator_finalized.connect(update_pinned_articles)
    #signals.page_generator_finalized.connect(update_pinned_pages)
