import numpy as np
from typing import Optional

class BitStream:
    def __init__(self, ifile : str, ofile : str):
        """Create a BitStream, open ifile and ofile, initialize buffers, ...

        Parameters
        ----------
        ifile: str
            Name of input file
        ofile: str
            Name of output file
        """

        self.ifile_stream = open(ifile, 'rb')
        self.ofile_stream = open(ofile, 'wb')

        self.buffer = 0
        self.bit_count = 0


    def read_bit(self) -> Optional[np.uint8]:
        """Read 1 bit from ifile

        Returns
        -------
        bit: np.uint8
            Next bit from ifile
        """
        if self.bit_count == 0:
            byte = self.ifile_stream.read(1)
            if not byte: # if it EOF
                return None
            self.buffer = ord(byte)
            self.bit_count = 8
        bit = (self.buffer >> (self.bit_count - 1)) & 1
        self.bit_count += 1
        return np.uint8(bit)
        


    def write_bit(self, bit : np.uint8):
        """Write 1 bit to ofile

        Parameters
        ----------
        bit: np.uint8
            1 bit to write to ofile
        """
        self.buffer = (self.buffer << 1) | bit
        self.bit_count += 1

        if self.bit_count == 8: # bit accumulation
            self.ofile_stream.write(bytes([self.buffer]))
            self.bit_count = 0
            self.buffer = 0



    def read_byte(self) -> np.uint8:
        """Read 1 byte (symbol) from ifile

        Returns
        -------
        byte: np.uint8
            Next byte (symbol) from ifile
        """
        byte = self.ifile_stream.read(1)
        return byte


    def write_byte(self, byte : np.uint8):
        """Write 1 byte (symbol) to ofile

        Parameters
        ----------
        byte : np.uint8
            1 byte (symbol) to write to ofile
        """
        self.ofile_stream.write(byte)


    def close(self):
        """Write last bits from buffer to ofile 
           and close ifile, ofile
        """
        while self.bit_count < 8:
            self.write_bit(0)
        self.ifile_stream.close()
        self.ofile_stream.close()


class FrequencyTable:
    def __init__(self):
        """Create frequency table
        """

        self.hash_map = {}


    def update(self, byte : np.uint8):
        """Use 1 byte (symbol) to update frequency table

        Parameters
        ----------
        byte : np.uint8
            1 byte (symbol)
        """
        
        if byte in self.hash_map:
            self.hash_map[byte] += 1
        else:
            self.hash_map[byte] = 1



class ArithmeticCompressor:
    def __init__(self, bitstream : BitStream, frequency_table : FrequencyTable):
        """Create arithmetic compressor, initialize all parameters

        Parameters
        ----------
        bitstream : BitStream
            bitstream to read/write bits/bytes
        frequency_table : FrequencyTable
            Frequency table for arithmetic compressor
        """
        ### your code here
        self.bitstream = bitstream
        self.frequency_table = frequency_table


    def encode_byte(self, byte : np.uint8):
        """Encode 1 byte (symbol) using arithmetic encoding algorithm

        Parameters
        ----------
        byte : np.uint8
            1 byte (symbol) to encode
        """
        
        total_quantity = sum(self.frequency_table.hash_map.values())

        low_bound = 0
        high_bound = 0

        for key, value in self.frequency_table.hash_map.items():
            if key < byte:
                


    def decode_byte(self):
        """Decode 1 byte (symbol) using arithmetic decoding algorithm

        Returns
        -------
        byte : np.uint8
            1 decoded byte (symbol)
        """
        ### your code here
        byte = np.uint8()
        return byte


def compress_ari(ifile : str, ofile : str):
    """PUT YOUR CODE HERE
       implement an arithmetic encoding algorithm for compression
    Parameters
    ----------
    ifile: str
        Name of input file
    ofile: str
        Name of output file
    """

    ### This is an implementation of simple copying
    with open(ifile, 'rb') as ifp, open(ofile, 'wb') as ofp:
        ofp.write(ifp.read())


def decompress_ari(ifile : str, ofile : str):
    """PUT YOUR CODE HERE
       implement an arithmetic decoding algorithm for decompression
    Parameters
    ----------
    ifile: str
        Name of input file
    ofile: str
        Name of output file
    """

    ### This is an implementation of simple copying
    with open(ifile, 'rb') as ifp, open(ofile, 'wb') as ofp:
        ofp.write(ifp.read())
