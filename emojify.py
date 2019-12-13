#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import argparse
from pprint import pformat

__author__ = "Chris Rands"
__copyright__ = "Copyright (c) 2017-2019, Chris Rands"

EMOTICONS = [":)", ":D", ":P", ":S", ":(", "=)", "=/", ":/", ":{", ";)"]
EMOJIS = [
    "\U0001f600",
    "\U0001f603",
    "\U0001f604",
    "\U0001f601",
    "\U0001f605",
    "\U0001f923",
    "\U0001f602",
    "\U0001f609",
    "\U0001f60A",
    "\U0001f61b",
]
MAX_STR_LEN = 70


def run_argparse():
    """User arguments"""
    parser = argparse.ArgumentParser(
        description="""
    Obfuscate your python script by converting an input script to an output 
    script that functions the same (hopefully) but encodes the code as emoji 
    icons, currently emoticons or emojis. -- Chris Rands, 2017-2019"""
    )
    parser.add_argument("-i", "--input", required=True, help="input python script name")
    parser.add_argument(
        "-o", "--output", required=True, help="output python script name"
    )
    parser.add_argument(
        "-e",
        "--emoji",
        dest="emoji",
        action="store_true",
        help="output emojis instead of emoticons",
    )
    parser.set_defaults(emoji=False)
    return parser.parse_args()


def chunk_string(in_s, n):
    """Chunk string to max length of n"""
    return "\n".join(
        "{}\\".format(in_s[i : i + n]) for i in range(0, len(in_s), n)
    ).rstrip("\\")


def encode_string(in_s, alphabet):
    """Convert input string to encoded output string with the given alphabet"""
    # Note prior to Cpython 3.6 output order may differ to due to
    # dicts not retaining insertion order
    d1 = dict(enumerate(alphabet))
    d2 = {v: k for k, v in d1.items()}
    return (
        'exec("".join(map(chr,[int("".join(str({}[i]) for i in x.split())) for x in\n'
        '"{}"\n.split("  ")])))\n'.format(
            pformat(d2),
            chunk_string(
                "  ".join(" ".join(d1[int(i)] for i in str(ord(c))) for c in in_s),
                MAX_STR_LEN,
            ),
        )
    )


def main(in_file, out_file, emoji):
    """Read input and write output file"""
    if emoji:
        alphabet = EMOJIS
    else:
        alphabet = EMOTICONS
    with open(in_file) as in_f, open(out_file, "w") as out_f:
        # Assumes it's ok to read the entire input file into memory
        out_f.write(encode_string(in_f.read(), alphabet))
    print("done {}".format(alphabet[0]))


if __name__ == "__main__":
    args = run_argparse()
    main(args.input, args.output, args.emoji)
