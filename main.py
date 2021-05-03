#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""SC3000 Basic Decoder
Reference:
http://www43.tok2.com/home/cmpslv/Sc3000/EnrSCbas.htm
"""

import sys

from command_table import MID_LANG

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
    decoded = decode(example_hex_string)
    print_decoded(decoded)

def read_bas_as_hex_string(filepath):
    with open(filepath, "rb") as f:
        content = f.read()
        return content.hex().upper()

def print_decoded(decoded, pretty_format = True):
    if pretty_format:
        print(decoded["raw"])
        print("Script length: {}".format(len(decoded["raw"])))
        print_format = "({:04d}) {: >5} {}"
    else:
        print_format = "{1} {2}"
    for line in decoded["result"]:
        print(print_format.format(line["byte"], line["line"], line["cmd"]))

def decode(hex_string):
    result = {"raw":hex_string, "result":[]}
    i = 0
    MIN_COMMAND_LENGTH = 14
    while i < len(hex_string)-MIN_COMMAND_LENGTH:
        result_i = {"byte":i, "line":"", "cmd":""}
        if hex_string[i:i+4] == "0000":
            result_i["cmd"] = "End of script, remaining hex is {}".format(hex_string[i:])
            di = len(hex_string) - i
        else:
            di, result_i["line"], result_i["cmd"] = decode_one_line(hex_string[i:])
        i += di
        result["result"].append(result_i)
    return result

def decode_one_line(line):
    result = ""
    command_length = int(line[0:2],16)
    di = 10+command_length*2+2
    line_number =  int(line[4:6]+line[2:4],16)
    blank = line[6:10]
    result = decode_command(line[10:di-2])
    return di, line_number, result

def decode_command(command):
    result = ""
    for i,k in zip(command[0::2], command[1::2]):
        if i+k < "80":
            result += decode_ascii(i+k)
        elif i+k == "80":
            result += "\80"
        else:
            try:
                result += MID_LANG[i+k]
            except KeyError:
                result += "\{}{}".format(i,k)
    return result

def decode_ascii(byte):
    return bytearray.fromhex(byte).decode()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        hex_string = read_bas_as_hex_string(sys.argv[1])
        decoded = decode(hex_string)
        print_decoded(decoded, len(sys.argv) > 2)
    else:
        decode_example()
