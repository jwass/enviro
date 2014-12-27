envconf
=======

Simple environment variable configuration for Python.

[![Build Status](https://travis-ci.org/jwass/envconf.svg?branch=master)](https://travis-ci.org/jwass/envconf)

It is widely considered best programming practice to separate application code from its configuration. Temporary or sensitive values such as authorization credentials, database handles, or keys to other services should be stored in a separate file that never becomes part of the code repository.

Usage
-----
`envconf` is a simple Python module and IPython extension that reads environment files and updates the OS environment variables `os.environ`. To use it, just import `envconf` and call `conf()`. By default it reads `.env`:
```
import envconf
envconf.conf()  # Load .env in the current directory
```

Any other file may also be specified:
```
envconf.conf('production.env')
```

IPython Extension
-----------------
`envconf` also provides an IPython extension so that it is always easily available as a line magic function without the need to import:
```
$ ipython

In [1]: %envconf
```
As above, it reads `.env` in the current directory by default, but an alternate file can be specified on the line:
```
In [1]: %envconf production.env
```

Example
-------
`.env` in the current directory has the following contents:
```
SERVICE_API_KEY = abc123
SERVICE_API_SECRET = def456
DATABASE_URI = postgres://user:password@host/dbname
```

```
>>> import envconf
>>> import os

>>> envconf.conf()
>>> os.environ['SERVICE_API_KEY']
'abc123'
>>> os.environ['SERVICE_API_SECRET']
'def456'
>>> os.environ['DATABASE_URI']
'postgres://user:password@host/dbname'
```

Installation
------------
The easiest way to install is to use `pip`.
```
pip install envconf
```

To load the IPython extension every time IPython starts, add `envconf_ipy_ext` in the extensions in your IPython config file (usually in `~/.ipython/profile_default/ipython_config`):
```
c.InteractiveShellApp.extensions = [
    'envconf_ipy_ext',
]
```
and
```
c.TerminalIPythonApp.extensions = [
    'envconf_ipy_ext',
]
```

See also
--------
* [The Twelve-Factor App](http://12factor.net/) (particularly the Config section)
* [Using IPython extensions](http://ipython.org/ipython-doc/dev/config/extensions/#using-extensions)
* [heroku-config plugin](https://devcenter.heroku.com/articles/config-vars#using-foreman-and-heroku-config)
* [autoenv](https://github.com/kennethreitz/autoenv)
