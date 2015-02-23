import enviro

def func(line):
    line = line.strip()
    if not line:
        enviro.conf()
    else:
        enviro.conf(line)

    # Run 'import os' in the main namespace so that you don't have
    # to do it explicitly
    get_ipython().run_code('import os')


def load_ipython_extension(ip):
    ip.register_magic_function(func, 'line', 'enviro')
