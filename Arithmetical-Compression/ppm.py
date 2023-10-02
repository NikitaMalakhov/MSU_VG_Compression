def compress_ppm(ifile : str, ofile : str):
    with open(ifile, 'rb') as ifp, open(ofile, 'wb') as ofp:
        ### PUT YOUR CODE HERE
        ### implement ppm algorithm for compression

        ### This is an implementation of simple copying

        text = ifp.read()
        ofp.write(text)

def decompress_ppm(ifile : str, ofile : str):
    with open(ifile, 'rb') as ifp, open(ofile, 'wb') as ofp:
        ### PUT YOUR CODE HERE
        ### implement ppm algorithm for decompression

        ### This is an implementation of simple copying

        text = ifp.read()
        ofp.write(text)
