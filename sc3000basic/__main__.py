#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""SC3000 Basic Decoder
Reference:
http://www43.tok2.com/home/cmpslv/Sc3000/EnrSCbas.htm
"""

import sys

from sc3000basic.sc3000decoder import read_bas_as_hex_string, decode_hex_string, print_decoded
from sc3000basic.sc3000encoder import encode_script_string, print_encoded

def decode_example():
    example_hex_string = (
        "06"   # Program is 06 bytes
        "0A00" # Program line 10
        "0000"
        "902054455354" # REM TEST
        "0D"   # CR Mark

        "08"   # Program is 08 bytes
        "1400" # Program line 20
        "0000"
        "9120225445535422" # PRINT "TEST"
        "0D"   # CR Mark

        "04"   # Program is 04 bytes
        "1E00" # Program line 30
        "0000"
        "9D203130" # GOTO 10
        "0D"   # CR Mark

        "00"   # End Mark
        "00"
    )
    example_basic_result = (
        '10 REM TEST\n'
        '20 PRINT "TEST"\n'
        '30 GOTO 10\n'
    )
    print("------------------------------------------------------------")
    print("USAGE: python -m sc3000basic COMMAND <filepath> [OPTIONS]")
    print("       Command: encode, decode")
    print("       Option: suppress, pretty")
    print("------------------------------------------------------------")

    decoded = decode_hex_string(example_hex_string)
    print_decoded(decoded, True)

def decode(filepath, pretty_format, suppress_error):
    hex_string = read_bas_as_hex_string(filepath)
    decoded = decode_hex_string(hex_string, suppress_error)
    print_decoded(decoded, pretty_format)

def encode(filepath, pretty_format, suppress_error):
    with open(filepath) as f:
        script_string = f.read()
        encoded = encode_script_string(script_string, suppress_error)
        print_encoded(encoded, pretty_format)

if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "decode":
        decode(sys.argv[2], "pretty" in sys.argv, "suppress" in sys.argv)
    elif len(sys.argv) > 2 and sys.argv[1] == "encode":
        encode(sys.argv[2], "pretty" in sys.argv, "suppress" in sys.argv)
    else:
        decode_example()
