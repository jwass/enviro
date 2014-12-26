from __future__ import print_function, unicode_literals

from IPython.core.magic import register_line_magic

try:
    import envconf as ec
    @register_line_magic
    def envconf(line):
        line = line.strip()
        if not line:
            ec.conf()
        else:
            ec.conf(line)
except ImportError:
    msg = """Could not import envconf. Install with `pip install envconf`.
    IPython magic function '%envconf' not registered."""
    print(msg)
