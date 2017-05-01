# -*- coding:utf-8 -*-

import os
import sys


from setuptools import setup, find_packages
here = os.path.abspath(os.path.dirname(__file__))
try:
    with open(os.path.join(here, 'README.rst')) as f:
        README = f.read()
    with open(os.path.join(here, 'CHANGES.txt')) as f:
        CHANGES = f.read()
except IOError:
    README = CHANGES = ''


install_requires = [
    'dictknife[load]',
]


docs_extras = [
]

tests_require = [
]

testing_extras = tests_require + [
]

setup(name='nejimaki',
      version='0.1.1',
      description='emit files from one yaml file',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Programming Language :: Python",
          "Programming Language :: Python :: Implementation :: CPython",
      ],
      keywords='',
      author="podhmo",
      author_email="ababjam61@gmail.com",
      url="https://github.com/podhmo/nejimaki",
      packages=find_packages(exclude=["nejimaki.tests"]),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      extras_require={
          'testing': testing_extras,
          'docs': docs_extras,
      },
      tests_require=tests_require,
      test_suite="nejimaki.tests",
      entry_points="""
      [console_scripts]
      nejimaki=nejimaki.cmd:main
""")

