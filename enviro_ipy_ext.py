import enviro

def func(line):
    line = line.strip()
    if not line:
        enviro.conf()
    else:
        enviro.conf(line)


def load_ipython_extension(ip):
    ip.register_magic_function(func, 'line', 'enviro')
