import os
from whoosh import index

_PREFIX="whoosh"
def _base_name(string):
        return '%s.%s' % (prefix, string)

def check_whoosh_env_from_settings(settings):
    if not _base_name('index_dir') in settings:
        raise AttributeError("You need to provide whoosh.index_dir in your configuration")

    index_dir = settings.get(_base_name('index_dir'))
    if not os.path.exists(index_dir):
        raise AttributeError("The directory '%s' doesn't exist, you need to create it")



def includeme(config):
    check_whoosh_env_from_settings(config.registry.settings)
    config.add_subscriber(add_whoosh_indexer, 'pyramid.events.NewRequest')



def add_whoosh_indexer(event):
    settings = event.request.registry.settings
    index_dir = settings.get(_base_name('index_dir'))
    event.request.whoosh_ix =  index.open_dir(index_dir)
