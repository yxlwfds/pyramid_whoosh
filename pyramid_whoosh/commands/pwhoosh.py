import argparse
from pyramid.paster import bootstrap
import sys
from whoosh import index
from zope.interface.interfaces import ComponentLookupError
from pyramid_whoosh import IDocumentSchema, IWhooshEnvironment


def create_index(reg):
    woosh_env = reg.getUtility(IWhooshEnvironment)
    try:
        docschema = reg.getUtility(IDocumentSchema)
    except ComponentLookupError:
        raise AttributeError('')

    if index.exists_in(woosh_env['index_dir']):
        print >> sys.stderr, 'Index already exist , you need to delete it before build it again'
        exit(-1)
    index.create_in(woosh_env['index_dir'], docschema.Schema)

def delete_index():
    pass

ACTION = {
    "build" : create_index,
    "delete": delete_index
}

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('action', metavar='action', type=str, choices=ACTION.keys(),
                       help='one of this actions: %s' % ','.join(ACTION.keys()))
    parser.add_argument('config_file', metavar='<config file .ini>',
                       help='the path to the config file' )

    args = parser.parse_args()
    env = bootstrap(args.config_file)
    reg = env['registry']
    ACTION.get(args.action,lambda *args : None)(reg)

if __name__ == "__main__":
    main()
