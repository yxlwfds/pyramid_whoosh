import argparse
from pyramid.paster import bootstrap


def create_index():
    pass

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

if __name__ == "__main__":
    main()
