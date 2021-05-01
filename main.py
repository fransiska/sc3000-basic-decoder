#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Reference:
http://www43.tok2.com/home/cmpslv/Sc3000/EnrSCbas.htm
"""

MID_LANG = {
    "82": "LIST",
    "90": "REM",
    "91": "PRINT",
    "9D": "GOTO"
}

def main():
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

def decode(hex_string):
    result = ""
    hex_string_split = hex_string.split("0D")
    for command in hex_string_split:
        if command == "0000":
            break
        result += decode_command(command)
        result += "\n"
    return result

def decode_command(command):
    result = ""
    command_length = int(command[0:2],16)
    line_number =  int(command[2:4],16)
    blank = command[4:10]
    mid_lang_command = command[10:12]

    result += "{} ".format(line_number)
    result += MID_LANG[mid_lang_command]
    result += decode_ascii(command[12:])

    return result

def decode_ascii(command):
    result = ""
    for i,k in zip(command[0::2], command[1::2]):
        result += bytearray.fromhex(i+k).decode()
    return result

if __name__ == "__main__":
    # execute only if run as a script
    main()
