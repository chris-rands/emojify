import sys

'''
Description:
Emojify your python script by converting an input script to an output script that functions the same (hopefully) but encrypts the characters as emojis.

Usage:
python emojify_python_script.py input_script.py output_script.py

Example:
$ cat input_script.py 
print('hello world')
def add(n1,n2):
    return n1 + n2
print('4 + 4 = {}'.format(add(4,4)))
$ python emojify_python_script.py input_script.py output_script.py
$ cat output_script.py 
exec("".join(map(chr,[int("".join(str({':)': 0, ':D': 1, ':P': 2, ':S': 3, ':(': 4, '=)': 5, '=/': 6, ':/': 7, ':{': 8, ';)': 9}[i]) for i in x.split())) for x in 
":D :D :P  :D :D :(  :D :) =)  :D :D :)  :D :D =/  :( :)  :S ;)  :D :) :(  :D :) :D  :D :) :{  :D :) :{  :D :D :D  :S :P  :D :D ;)  :D :D :D  :D :D :(  :D :) :{  :D :) :)  :S ;)  :( :D  :D :)  :D :) :)  :D :) :D  :D :) :P  :S :P  ;) :/  :D :) :)  :D :) :)  :( :)  :D :D :)  :( ;)  :( :(  :D :D :)  =) :)  :( :D  =) :{  :D :)  :S :P  :S :P  :S :P  :S :P  :D :D :(  :D :) :D  :D :D =/  :D :D :/  :D :D :(  :D :D :)  :S :P  :D :D :)  :( ;)  :S :P  :( :S  :S :P  :D :D :)  =) :)  :D :)  :D :D :P  :D :D :(  :D :) =)  :D :D :)  :D :D =/  :( :)  :S ;)  =) :P  :S :P  :( :S  :S :P  =) :P  :S :P  =/ :D  :S :P  :D :P :S  :D :P =)  :S ;)  :( =/  :D :) :P  :D :D :D  :D :D :(  :D :) ;)  ;) :/  :D :D =/  :( :)  ;) :/  :D :) :)  :D :) :)  :( :)  =) :P  :( :(  =) :P  :( :D  :( :D  :( :D  :D :)"
.split("  ")])))
$ python output_script.py 
hello world
4 + 4 = 8

Disclaimers:
Not tested on complex scripts, so don't rely on this script to work, it is probably very easy to break.
The script will not always produce an identical output for the same input; replace the dictionaries with collections.OrderedDict to achieve that.

Licence:
Copyright (c) 2017, Chris Rands
Redistribution and use of this code, with or without modification, are permitted provided that the the above copyright notice is included.
'''

def main(in_file, out_file):
    emojis = [':)',':D',':P',':S',':(','=)','=/',':/',':{',';)']
    d1 = dict(enumerate(emojis))
    d2 = {v:k for k,v in d1.items()}
    with open(in_file) as in_f, open(out_file,'w') as out_f:
        out_f.write('exec("".join(map(chr,[int("".join(str({}[i]) for i in x.split())) for x in \n"{}"\n.split("  ")])))\n'.format(d2,'  '.join(' '.join(d1[int(i)] for i in str(ord(c))) for c in in_f.read())))

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
