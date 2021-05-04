#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sc3000basic.command_table import COMMAND, FUNCTION

COMMAND_BY_WORD = {v:k for k,v in COMMAND.items()}

def encode_script_string(script_string, suppress_error = False):
    result = ""
    for line in script_string.split("\n"):
        if not line:
            continue
        result += encode_one_line(line)
    return result

def encode_one_line(line):
    line_number, command = line.split(" ",1)
    encoded_line_number = encode_line_number(line_number)
    encoded_command = encode_command(command)
    encoded_command_length = encode_command_length(encoded_command)
    return (encoded_command_length + encoded_line_number + "0000" + encoded_command + "0D").upper()

def encode_line_number(line_number):
    hex_number = f"{int(line_number):04x}"
    return hex_number[2:4]+hex_number[0:2]

def encode_command(command):
    if command.startswith("REM"):
        return COMMAND_BY_WORD["REM"] + encode_ascii(command[3:])
    elif command.startswith("DATA"):
        return COMMAND_BY_WORD["DATA"] + encode_ascii(command[4:])
    else:
        matching_commands = list(filter(lambda cmd: command.startswith(cmd), COMMAND_BY_WORD.keys()))
        longest_command = max(matching_commands, key=len)
        remaining_command = command[len(longest_command):]
        # TODO: handle multiple commands per line
        return COMMAND_BY_WORD[longest_command] + encode_ascii(remaining_command)

def encode_ascii(command):
    result = ""
    command_iter = iter(command)
    for c in command_iter:
        if c == '\\':
            # TODO: handle basic special escaped characters
            pass
        else:
            result += f"{ord(c):02x}"
    return result

def encode_command_length(encoded_command):
    return f"{int(len(encoded_command)/2):02x}"

def print_encoded(encoded):
    print(encoded)
