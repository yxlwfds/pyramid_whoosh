import os
from whoosh import index
from zope.interface.interface import Interface
from whoosh.index import EmptyIndexError
from pyramid_whoosh.interfaces import IDocumentSchema

_PREFIX="whoosh"

class IWhooshEnvironment(Interface):
    pass

def add_schema(config,schema):
    config.registry.registerUtility(schema, IDocumentSchema)

def get_whoosh_env(config):
    return config.registry.getUtility(IWhooshEnvironment)

def _base_name(string):
        return '%s.%s' % (_PREFIX, string)

def get_whoosh_env_from_settings(settings):
    if not _base_name('index_dir') in settings:
        raise AttributeError("You need to provide whoosh.index_dir in your configuration")

    index_dir = settings.get(_base_name('index_dir'))
    if not os.path.exists(index_dir):
        raise AttributeError("The directory '%s' doesn't exist, you need to create it" % index_dir)

    env = {'index_dir':index_dir}

    return env

def includeme(config):
    whoosh_env=get_whoosh_env_from_settings(config.registry.settings)
    config.registry.registerUtility(whoosh_env, IWhooshEnvironment)
    config.add_subscriber(add_whoosh_indexer, 'pyramid.events.NewRequest')
    config.add_directive('add_schema', add_schema)

def add_whoosh_indexer(event):
    env = event.request.registry.getUtility(IWhooshEnvironment)
    try:
        event.request.whoosh_ix =  index.open_dir(env['index_dir'])
    except EmptyIndexError as e:
           raise EmptyIndexError("%s, run the pwhoosh command to build the index" % e.message )
        