import sys,zlib

def usage():
    print("Usage: %s original_bzimage extracted_vmlinux" % sys.argv[0])
    exit(-1)

if len(sys.argv) < 3:
    usage()

input_file = sys.argv[1]
output_file = sys.argv[2]
# Open the file for reading
with open(input_file, 'rb') as f:
    # Read the file into memory
    data = f.read()

# Search for the gzip magic number (1f 8b 08 00)
gzip_start = data.find(b'\x1f\x8b\x08\x00')

# If the magic number was found, extract the gzipped data and un-gzip it
if gzip_start != -1:
    gzip_data = data[gzip_start:]
    
    # Initialize decompressor
    decompressor = zlib.decompressobj(wbits=zlib.MAX_WBITS|16)

    # Decompress chunks of data
    decompressed_data = b''
    while True:
        chunk = gzip_data[:1024]
        gzip_data = gzip_data[1024:]
        if not chunk:
            break
        decompressed_data += decompressor.decompress(chunk)

    # Finish decompression
    decompressed_data += decompressor.flush()
   
    with open(output_file,'wb') as g:
        g.write(decompressed_data)
    print("DonionRingZ")
else:
    print("Gzip magic number not found in file.")