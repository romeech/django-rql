from __future__ import unicode_literals

from dj_rql.filter_cls import RQLFilterClass
from dj_rql.constants import FilterLookups
from tests.dj_rf.models import Book


AUTHOR_FILTERS = ['is_male', {
    'filter': 'email',
}, {
    'namespace': 'publisher',
    'filters': ['id']
}]


PAGE_FILTERS = [{
    'filter': 'number',
    'lookups': {FilterLookups.EQ, FilterLookups.NE},
}, {
    'filter': 'id',
    'source': 'uuid',
}]


class BooksFilterClass(RQLFilterClass):
    MODEL = Book
    FILTERS = ['id', 'title', 'current_price', 'written', {
        'filter': 'status',
    }, {
        'filter': 'author__email',
    }, {
        'filter': 'name',
        'source': 'author__name',
    }, {
        'namespace': 'author',
        'filters': AUTHOR_FILTERS,
    }, {
        'namespace': 'page',
        'source': 'pages',
        'filters': PAGE_FILTERS,
    }, {
        'filter': 'published.at',
        'source': 'published_at',
    }, {
        'filter': 'rating.blog',
        'source': 'blog_rating',
        'use_repr': True,
    }, {
        'filter': 'rating.blog_int',
        'source': 'blog_rating',
        'use_repr': False,
    }, {
        'filter': 'amazon_rating',
        'lookups': {FilterLookups.GE, FilterLookups.LT},
    }, {
        'filter': 'url',
        'source': 'publishing_url',
    }, {
        # Sometimes it's needed to filter by several sources at once (distinct is always True).
        # F.e. this could be helpful for searching.
        'filter': 'd_id',
        'sources': {'id', 'author__id'},
    }]
