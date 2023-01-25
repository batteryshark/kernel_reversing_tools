# VMLinux bzImage Repacker
import sys,zlib,io,gzip
def usage():
    print("Usage: %s extracted_vmlinux original_bzimage output_bzimage" % sys.argv[0])
    exit(-1)

if len(sys.argv) < 4:
    usage()
    
vmlinux_path = sys.argv[1]
original_bzimage_path = sys.argv[2]
output_bzimage_path = sys.argv[3]

print("Compressing VMLinux...")
vmlinux_data = open(vmlinux_path,'rb').read()
bytes = io.BytesIO()
with gzip.GzipFile(fileobj=bytes, mode='wb',compresslevel=9) as gz:
  gz.write(vmlinux_data)
bytes.seek(0)

vmlinuz_data = bytes.read()
bytes.close()

print("Replacing Original VMLinuz...")
bzimage_data = open(original_bzimage_path,'rb').read()
gzip_start = bzimage_data.find(b'\x1f\x8b\x08\x00')

print("Writing out Modified bzImage")
bzimage_data = bytearray(bzimage_data)
bzimage_data[gzip_start:gzip_start+len(vmlinuz_data)] = vmlinuz_data

with open(output_bzimage_path,'wb') as g:
    g.write(bzimage_data)

print("DonionRingZ!")

