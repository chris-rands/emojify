[![PyPI version](https://badge.fury.io/py/emojify.svg)](https://badge.fury.io/py/emojify)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
# emojify :) 😊

**Description**

Obfuscate your python script (or indeed any plain text file) by converting an input script to an output script that functions the same (hopefully) but encodes the code as emoji icons, currently emoticons or emojis.

**Installation**

`pip install emojify`

If installation fails with `pip` for some reason, you can just clone the repository, since there are no dependancies apart from python 3:
```
git clone https://github.com/chris-rands/emojify;
cd emojify
```

**Usage**

`emojify --input input_script.py --output output_script.py`

For help:
`emojify --help`

For unit testing:
`test_emojify`

**Example**

`input_script.py` contains:

    print('hello world')
    def add(n1,n2):
        return n1 + n2
    print('4 + 4 = {}'.format(add(4,4)))

running `emojify --input input_script.py --output output_script.py`

`output_script.py` contains:

    exec("".join(map(chr,[int("".join(str({':(': 4,
     ':)': 0,
     ':/': 7,
     ':D': 1,
     ':P': 2,
     ':S': 3,
     ':{': 8,
     ';)': 9,
     '=)': 5,
     '=/': 6}[i]) for i in x.split())) for x in
    ":D :D :P  :D :D :(  :D :) =)  :D :D :)  :D :D =/  :( :)  :S ;)  :D :) \
    :(  :D :) :D  :D :) :{  :D :) :{  :D :D :D  :S :P  :D :D ;)  :D :D :D \
     :D :D :(  :D :) :{  :D :) :)  :S ;)  :( :D  :D :)  :D :) :)  :D :) :D\
      :D :) :P  :S :P  ;) :/  :D :) :)  :D :) :)  :( :)  :D :D :)  :( ;)  \
    :( :(  :D :D :)  =) :)  :( :D  =) :{  :D :)  :S :P  :S :P  :S :P  :S :\
    P  :D :D :(  :D :) :D  :D :D =/  :D :D :/  :D :D :(  :D :D :)  :S :P  \
    :D :D :)  :( ;)  :S :P  :( :S  :S :P  :D :D :)  =) :)  :D :)  :D :D :P\
      :D :D :(  :D :) =)  :D :D :)  :D :D =/  :( :)  :S ;)  =) :P  :S :P  \
    :( :S  :S :P  =) :P  :S :P  =/ :D  :S :P  :D :P :S  :D :P =)  :S ;)  :\
    ( =/  :D :) :P  :D :D :D  :D :D :(  :D :) ;)  ;) :/  :D :D =/  :( :)  \
    ;) :/  :D :) :)  :D :) :)  :( :)  =) :P  :( :(  =) :P  :( :D  :( :D  :\
    ( :D  :D :)"
    .split("  ")])))

running `python output_script.py` outputs:

    hello world
    4 + 4 = 8

similarly, running `emojify --input input_script.py --output output_script.py --emoji`

`output_script.py` contains:

    exec("".join(map(chr,[int("".join(str({'😀': 0, '😁': 3, '😂': 6, '😃': 1, '😄': 2, '😅': 4, '😉': 7, '😊': 8, '😛': 9, '🤣': 5}[i]) for i in x.split())) for x in
    "😃 😃 😄  😃 😃 😅  😃 😀 🤣  😃 😃 😀  😃 😃 😂  😅 😀  😁 😛  😃 😀 😅  😃 😀 😃  😃 😀 😊  😃 😀 \
    😊  😃 😃 😃  😁 😄  😃 😃 😛  😃 😃 😃  😃 😃 😅  😃 😀 😊  😃 😀 😀  😁 😛  😅 😃  😃 😀  😃 😀 😀\
      😃 😀 😃  😃 😀 😄  😁 😄  😛 😉  😃 😀 😀  😃 😀 😀  😅 😀  😃 😃 😀  😅 😛  😅 😅  😃 😃 😀  🤣\
     😀  😅 😃  🤣 😊  😃 😀  😁 😄  😁 😄  😁 😄  😁 😄  😃 😃 😅  😃 😀 😃  😃 😃 😂  😃 😃 😉  😃 😃\
     😅  😃 😃 😀  😁 😄  😃 😃 😀  😅 😛  😁 😄  😅 😁  😁 😄  😃 😃 😀  🤣 😀  😃 😀  😃 😃 😄  😃 😃\
     😅  😃 😀 🤣  😃 😃 😀  😃 😃 😂  😅 😀  😁 😛  🤣 😄  😁 😄  😅 😁  😁 😄  🤣 😄  😁 😄  😂 😃  \
    😁 😄  😃 😄 😁  😃 😄 🤣  😁 😛  😅 😂  😃 😀 😄  😃 😃 😃  😃 😃 😅  😃 😀 😛  😛 😉  😃 😃 😂  😅\
     😀  😛 😉  😃 😀 😀  😃 😀 😀  😅 😀  🤣 😄  😅 😅  🤣 😄  😅 😃  😅 😃  😅 😃  😃 😀"
    .split("  ")])))

and running `output_script.py` ouputs the same as above.

**Disclaimer**

Only tested on Python 3.6+ and on CPython. Not tested on complex scripts, so don't rely on this script to work, not guaranteed to work at all, and it is probably easy to break. One case it will fail is with non-unicode characters. Also note, if you want to securely protect your code from the eyes of others, this is NOT a good way.
