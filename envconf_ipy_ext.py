import envconf

def func(line):
    line = line.strip()
    if not line:
        envconf.conf()
    else:
        envconf.conf(line)


def load_ipython_extension(ip):
    ip.register_magic_function(func, 'line', 'envconf')
