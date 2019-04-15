#!/usr/env/python
from pwn import *

r = remote('everland.pwni.ng',7772)

r.sendline("chris")

for j in range(0, 10):
    print(r.recvline())
    r.sendline("forage")
    print(r.recvline())

for k in range(0, 4):
    print(r.recvline())
    r.sendline("use")
    print(r.recvline())
    r.sendline("0")
    print(r.recvline())


for i in range(0, 81):
    print(r.recvline())
    r.sendline("fight")
    print(r.recvline())
    r.sendline("2")
    print(r.recvline())

r.interactive()
