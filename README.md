# emojify_python_script

**Description**

Obfuscate your python script by converting an input script to an output script that functions the same (hopefully) but encodes the code as emoji icons, currently emoticons.

**Usage**

`python emojify_python_script.py --input input_script.py --output output_script.py`

For help:
`python emojify_python_script.py --help`

For unit testing:
`python test_emojify_python_script.py`

**Example**

`input_script.py` contains:

    print('hello world')
    def add(n1,n2):
        return n1 + n2
    print('4 + 4 = {}'.format(add(4,4)))

running `python emojify_python_script.py --input input_script.py --output output_script.py`

`output_script.py` contains:

    from collections import OrderedDict
    exec("".join(map(chr,[int("".join(str(OrderedDict([(':)', 0),
                 (':D', 1),
                 (':P', 2),
                 (':S', 3),
                 (':(', 4),
                 ('=)', 5),
                 ('=/', 6),
                 (':/', 7),
                 (':{', 8),
                 (';)', 9)])[i]) for i in x.split())) for x in
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

**Disclaimer**

Not tested on complex scripts, so don't rely on this script to work, not guaranteed to work at all, and it is probably easy to break. One case it will fail is with non-unicode characters. Also note if you want to securely protect your code from the eyes of others, this is NOT a good way, so find another way.

**Licence**

Copyright (c) 2017-2018, Chris Rands.
Redistribution and use of this code, with or without modification, are permitted, provided that the the above copyright notice is included.
