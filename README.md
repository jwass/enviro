enviro
=======

Simple Python module and IPython extension for configuring OS environment variables.

[![Build Status](https://travis-ci.org/jwass/enviro.svg?branch=master)](https://travis-ci.org/jwass/enviro)

In web app and software-as-a-service development, it is widely considered best programming practice to separate application code from its configuration. Temporary or sensitive values such as authorization credentials, database handles, and keys to other services (the config) should be stored in a separate file, never part of the code repository.

This practice should be extended to analysis and interactive environments. 

`enviro` (pronounced en-vye-ro) is a simple Python module and IPython extension that updates the OS environment variables `os.environ` with the contents of an environment file - lines containing key=value pairs.

Usage
-----
Simply import `enviro` and call `conf()`. By default it reads `.env`:
```
import enviro
enviro.conf()  # Load contents of .env into os.environ
```

A different file may be specified:
```
enviro.conf('production.env')
```

IPython Extension
-----------------
`enviro` also provides an IPython extension so that it is always easily available as a line magic function without the need to import:
```
$ ipython

In [1]: %enviro
```
As above, it reads `.env` in the current directory by default, but an alternate file can be specified on the line:
```
In [1]: %enviro production.env
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
>>> import enviro
>>> import os

>>> enviro.conf()
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
pip install enviro
```

To load the IPython extension every time IPython starts, add `'enviro_ipy_ext'` to the extensions in your IPython config file (usually `~/.ipython/profile_default/ipython_config.py`):
```
c.InteractiveShellApp.extensions = [
    'enviro_ipy_ext',
]
```
and
```
c.TerminalIPythonApp.extensions = [
    'enviro_ipy_ext',
]
```

See also
--------
* [The Twelve-Factor App](http://12factor.net/) (particularly the Config section)
* [Using IPython extensions](http://ipython.org/ipython-doc/dev/config/extensions/#using-extensions)
* [heroku-config plugin](https://devcenter.heroku.com/articles/config-vars#using-foreman-and-heroku-config)
* [autoenv](https://github.com/kennethreitz/autoenv)
