#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""SC3000 Basic Decoder
Reference:
http://www43.tok2.com/home/cmpslv/Sc3000/EnrSCbas.htm
"""

import sys

from command_table import MID_LANG

class MidLangException(Exception):
    pass

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
    print(decode(example_hex_string))

def read_bas_as_hex_string(filepath):
    with open(filepath, "rb") as f:
        content = f.read()
        return content.hex().upper()

def decode(hex_string):
    result = ""
    i = 0
    MIN_COMMAND_LENGTH = 14
    print("Script length: {}".format(len(hex_string)))
    while i < len(hex_string)-MIN_COMMAND_LENGTH:
        if hex_string[i:i+4] == "0000":
            result += "End of script, remaining hex is {}".format(hex_string[i:])
            break
        try:
            di, result_i = decode_command(hex_string[i:])
        except Exception as e:
            di = 2
            result_i = "Cannot parse command: {} -- len={}".format(e, hex_string[i:i+2])
        i += di
        result += "({:04d}) {}\n".format(i, result_i)
    return result

def decode_command(command):
    result = ""
    command_length = int(command[0:2],16)
    di = 10+command_length*2+2
    line_number =  int(command[4:6]+command[2:4],16)
    blank = command[6:10]
    mid_lang_command_hex = command[10:12]

    result += "{: >3} ".format(line_number)
    try:
        mid_lang_command_string = MID_LANG[mid_lang_command_hex]
    except KeyError:
        result += "Cannot decode command {}: {}".format(mid_lang_command_hex, command[:di-2])
    else:
        result += mid_lang_command_string
        result += decode_ascii(command[12:di-2])

    return di, result

def decode_ascii(command):
    result = ""
    for i,k in zip(command[0::2], command[1::2]):
        try:
            result += bytearray.fromhex(i+k).decode()
        except UnicodeDecodeError as e:
            try:
                result += MID_LANG[i+k]
            except:
                result += "\{}{}".format(i,k)
    return result

if __name__ == "__main__":
    if len(sys.argv) > 1:
        basic_script_hex_string = read_bas_as_hex_string(sys.argv[1])
        print(basic_script_hex_string)
        print(decode(basic_script_hex_string))
    else:
        decode_example()
