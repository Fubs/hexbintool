# hexbintool
small tool for converting hexadecimal/binary/integer/octal representations

These are some python convenience functions for converting hex/bin/int/oct numbers. I made this because I found web tools for this to be annoying, and I tend to forget the builtin python functions. The program will try to interpret inputs regardless of type based on the desired conversion, so you can do b2h(11010) and it will take the 1's and 0's to be binary even though its a python integer.

i2b(n) -> int2binary, convert integer n to string of 0's and 1's

b2h(n) -> binary2hex, convert string of 0's and 1's to hex string

o2i(n) -> octal2int, convert octal string to integer

etc...

you can also add prefix=False
to remove 0x/0b/0o prefix from result
like this:

i2h(37, prefix=False)  returns '25' instead of '0x25'

I recommend you install IPython if you haven't and then just run the .py in a terminal to use it as a calculator.
