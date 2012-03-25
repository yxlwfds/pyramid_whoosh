import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
    'whoosh',
    ]

if sys.version_info < (2, 7):
    requires.append('argparse')

setup(name='pyramid_whoosh',
      version='0.1',
      description='pyramid_whoosh',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Topic :: Text Processing :: Indexing",
        ],
      author='rachid',
      author_email='',
      url='',
      keywords='web pyramid pylons whoosh',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="pyramid_whoosh",
      entry_points = """\
      [console_scripts]
      pwhoosh = pyramid_celery.commands.celeryd:main
      """,
      )

