#!/usr/bin/env python

'''
emojify_python_script.py

# Description
Obfuscate your python script by converting an input script to an output script
that functions the same (hopefully) but encodes the code as emoji icons.

# Usage
python emojify_python_script.py -h
python emojify_python_script.py --input input_script.py --output output_script.py

# Disclaimer
Not tested on complex scripts, so don't rely on this script to work,
not guaranteed to work at all, and it is probably easy to break.
One case it will fail is with non-unicode characters.

# License
Copyright (c) 2018, Chris Rands.
Redistribution and use of this code, with or without modification, are permitted,
provided that the the above copyright notice is included.
'''

import argparse
from collections import OrderedDict
from pprint import pformat

try:
    range = xrange
except NameError:
    pass  # Python 3

__author__ = 'Chris Rands'
__copyright__ = 'Copyright (c) 2018, Chris Rands'

EMOJIS = [':)', ':D', ':P', ':S', ':(', '=)', '=/', ':/', ':{', ';)']
MAX_STR_LEN = 70


def run_argparse():
    """User arguments"""
    parser = argparse.ArgumentParser(description='''
    Obfuscate your python script by converting an input script to an output script
    that functions the same (hopefully) but encodes the code as emoji icons
    -- Chris Rands, 2018''')
    parser.add_argument('-i', '--input', required=True, help='input python script name')
    parser.add_argument('-o', '--output', required=True, help='output python script name')
    return parser.parse_args()


def chunk_string(s, n):
    """Chunk string to max length of n"""
    return '\n'.join('{}\\'.format(s[i:i+n]) for i in range(0, len(s), n)).rstrip('\\')


def emojify_string(in_s):
    """Convert input string to emojified ouput string"""
    # Using OrderedDict to guarantee output order is the same
    d1 = OrderedDict(enumerate(EMOJIS))
    d2 = OrderedDict((v, k) for k, v in d1.items())
    return ('from collections import OrderedDict\n'
           'exec("".join(map(chr,[int("".join(str({}[i]) for i in x.split())) for x in\n'
           '"{}"\n.split("  ")])))\n'.format(pformat(d2), chunk_string('  '.join(
           ' '.join(d1[int(i)] for i in str(ord(c))) for c in in_s), MAX_STR_LEN)))


def main(in_file, out_file):
    """Read input and write output file"""
    with open(in_file) as in_f, open(out_file, 'w') as out_f:
        # This assumes it's ok to read the entire input file into memory
        out_f.write(emojify_string(in_f.read()))


if __name__ == '__main__':
    args = run_argparse()
    main(args.input, args.output)
