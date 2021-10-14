import sys
print('Hello!')
'Hello\n'.encode()
char_count = sys.stdout.buffer.write('Hello!\n'.encode())
print(char_count)
sys.stdout.buffer.write(b'\xf0\x9f\x90\x8d')

