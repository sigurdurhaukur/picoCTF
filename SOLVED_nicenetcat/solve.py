from pwn import *


# nc nc mercury.picoctf.net 35652

r = remote('mercury.picoctf.net', 35652)

characters = []


# collect input
while True:
    try:
        c = r.recvline().decode().strip()
        characters.append(c)
    except EOFError:
        break
    except Exception as e:
        print(e)
        break
    except KeyboardInterrupt:
        break

        
# ASCII number to text

flag = [chr(int(c)) for c in characters]
flag = ''.join(flag)

with open('flag.txt', 'w') as f:
    print(flag)
    f.write(flag)

