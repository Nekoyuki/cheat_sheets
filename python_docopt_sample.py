import os

__doc__ = """
{f}

Usage:
    {f} <file> [-a <value>] [-b <value>]
    {f} -h|--help

Options:
    -a <value>    value
    -b <value>    value  [default: hikari]
    -h --help     help
""".format(f=os.path.basename(__file__))

from docopt import docopt

if __name__ == '__main__':
    args = docopt(__doc__)
