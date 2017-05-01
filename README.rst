nejimaki
========================================

.. image:: https://travis-ci.org/podhmo/nejimaki.svg?branch=master
    :target: https://travis-ci.org/podhmo/nejimaki


generating file tree from one yamle file.

example
----------------------------------------

data.yaml

.. code-block:: yaml

  ./conf:
    ./base:
      base.yaml:
        logging:
          asctime: 2013-04-10 15:39:26,014
          created: 1365604766.014612
          levelname: INFO
          message: test message
          name: logger_name
    dev.yaml:
      debug: true
      $inherits: "./base/base.yaml"
    staging.yaml:
      debug: false
      $inherits: "./base/base.yaml"
    production.yaml:
      $inherits: "./staging.yaml"


.. code-block:: bash

  $ nejimaki examples/readme/data.yaml --position=examples/readme
   INFO	  nejimaki	emit:conf/base/base.yaml
   INFO	  nejimaki	emit:conf/dev.yaml
   INFO	  nejimaki	emit:conf/staging.yaml
   INFO	  nejimaki	emit:conf/production.yaml
  
  $ tree examples/readme/conf
  examples/readme/conf
  ├── base
  │   └── base.yaml
  ├── dev.yaml
  ├── production.yaml
  └── staging.yaml
  
  1 directory, 4 files
  

