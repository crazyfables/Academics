import struct

# writing files, beware... no really... run
f = open('data.txt', 'w')
f.write('Hello\n')
f.write('World\n')
f.close

packed = struct.pack('>4sh', 7, b'spam', 8)
print(packed)
