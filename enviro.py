import os
import re
import shlex


def conf(filename='.env', force=False):
    with open(filename) as f:
        content = f.read()
    envvars = parse(content)
    updateenv(os.environ, envvars, force)


def parse(content):
    """
    Parse the content of a .env file (a line-delimited KEY=value format) into a
    dictionary mapping keys to values.

    This function lifted entirely from Honcho (honcho/environ.py):
    https://github.com/nickstenning/honcho
    
    """
    values = {}
    for line in content.splitlines():
        lexer = shlex.shlex(line, posix=True)
        lexer.wordchars += '/.+-():'
        tokens = list(lexer)

        # parses the assignment statement
        if len(tokens) != 3:
            continue
        name, op, value = tokens
        if op != '=':
            continue
        if not re.match(r'[A-Za-z_][A-Za-z_0-9]*', name):
            continue
        values[name] = value

    return values


def updateenv(env, envvars, force=False):
    if force:
        env.update(envvars)
    else:
        for k, v in envvars.items():
            env.setdefault(k, v)
