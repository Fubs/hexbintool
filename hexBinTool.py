import IPython

def i2h(n, prefix=True):
    h = hex(int(n))[2:].upper()
    if prefix:
        h = "0x" + h
    return h

def h2i(n):
    k = str(n)
    if k[0:2] == "0x":
        k = k[2:]
    return int(k, 16)

def i2b(n, prefix=True):
    k = int(n)
    result = ""
    while k != 0:
        if k%2 == 0:
            result += "0"
        else:
            result += "1"
        k = k // 2
    if prefix:
        resut = "0b" + result
    return result

def b2i(n):
    k = str(n)
    if k[0:2] == "0b":
        k = k[2:]
    return int(k, 2)

def b2h(n, prefix=True):
    return i2h(b2i(n), prefix)

def h2b(n, prefix=True):
    return i2b(h2i(n), prefix)

def i2o(n, prefix=True):
    k = oct(int(n))
    if not prefix:
        k = k[2:]
    return k

def o2i(n):
    k = str(n)
    if k[:2] == "0o":
        k = k[2:]
    return int(k, 8)

def b2o(n, prefix=True):
    return i2o(b2i(n), prefix)

def o2b(n, prefix=True):
    return i2b(o2i(n), prefix)

def h2o(n, prefix=True):
    return i2o(h2i(n), prefix)

def o2h(n, prefix=True):
    return i2h(o2i(n), prefix)

if __name__ == "__main__":
    print("i2b(n) -> int2binary, convert integer n to string of 0's and 1's")
    print("b2h(n) -> binary2hex, convert string of 0's and 1's to hex string")
    print("o2i(n) -> octal2int, convert octal string to integer")
    print("etc...")
    print("you can also add prefix=False")
    print("to remove 0x/0b/0o prefix from result")
    print("like this: i2h(n, prefix=False)\n")
    IPython.embed()




