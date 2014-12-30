======
enviro
======

Simple Python module and IPython extension for setting OS environment variables from config files.

.. image:: https://travis-ci.org/jwass/enviro.svg?branch=master
   :target: https://travis-ci.org/jwass/envior

In web app and software-as-a-service development, it is widely considered best programming practice to separate application code from its configuration. Temporary or sensitive values such as authorization credentials, database handles, and keys to other services should reside in a separate file, never as part of the code repository. The application code should read these values from OS environment variables, which are set by the execution environment. Tools like foreman and honcho read environment files - lines containing key=value settings - and update the OS environment prior to running the server, workers, etc.

This practice should be extended to analysis and interactive environments. Not only is it a good idea to separate config values from the code, but analysis tools often need to be configured from the same source as a deployment, for debugging or other analysis.

``enviro`` (pronounced en-vye-ro) is a simple Python module and IPython extension that can set OS environment variables `os.environ` from environment files.

Usage
=====
Simply import ``enviro`` and call ``conf()``. By default it reads ``.env``:

.. code-block:: python

    import enviro
    enviro.conf()  # Load contents of .env into os.environ

A different file may be specified:

.. code-block:: python

    enviro.conf('production.env')


IPython Extension
=================
``enviro`` also provides an IPython extension so that it is always easily available as a line magic function without the need to import:

.. code-block::

    $ ipython
    In [1]: %enviro

As above, it reads ``.env`` in the current directory by default, but an alternate file can be specified on the line:

.. code-block::

    In [1]: %enviro production.env


Example
=======
``.env`` in the current directory has the following contents:

::

    SERVICE_API_KEY = abc123
    SERVICE_API_SECRET = def456
    DATABASE_URI = postgres://user:password@host/dbname


.. code-block:: python

    >>> import enviro
    >>> import os

    >>> enviro.conf()
    >>> os.environ['SERVICE_API_KEY']
    'abc123'
    >>> os.environ['SERVICE_API_SECRET']
    'def456'
    >>> os.environ['DATABASE_URI']
    'postgres://user:password@host/dbname'

Installation
============
The easiest way to install is to use ``pip``.

.. code-block::

   pip install enviro

To load the IPython extension every time IPython starts, add `'enviro_ipy_ext'` to the extensions in your IPython config file (usually `~/.ipython/profile_default/ipython_config.py`):

.. code-block:: python

    c.InteractiveShellApp.extensions = [
        'enviro_ipy_ext',
    ]

and

.. code-block:: python

    c.TerminalIPythonApp.extensions = [
        'enviro_ipy_ext',
    ]

To load the IPython extension without modifying your ``ipython_config.py`` you can run ``%load_ext enviro_ipy_ext`` to expose the ``%enviro`` magic function, although that's just as easy as importing it directly so best to add it to your config and avoid this step.

See also
========
* `The Twelve-Factor App <http://12factor.net/>`__ (particularly the Config section)
* `Using IPython extensions <http://ipython.org/ipython-doc/dev/config/extensions/#using-extensions>`__
* `heroku-config plugin <https://devcenter.heroku.com/articles/config-vars#using-foreman-and-heroku-config>`__
* `autoenv <https://github.com/kennethreitz/autoenv>`__
