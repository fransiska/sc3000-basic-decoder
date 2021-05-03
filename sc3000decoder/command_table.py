#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""SC3000 Basic Command Table
Reference:
http://www43.tok2.com/home/cmpslv/Sc3000/EnrSCbas.htm
"""

MISSING_COMMAND = [
    "BOOT",
    "CLOAD",
    "COMLOAD",
    "COMSAVE",
    "CSAVE",
    "FILES",
    "LFILES",
    "MAXFILE"
    "MERGE",
    "NEWON",
    "UTILITY",
    "CLOADM",
    "CLOSE",
    "COMSET"
    "CSAVEM",
    "DSKI$",
    "DSKO$",
    "GET",
    "INPUT#",
    "KILL",
    "LIMIT",
    "LOADM",
    "NAME",
    "OPEN",
    "PRINT#",
    "PUT",
    "SAVEM",
    "SET",
    "VERIFYM"
]

MISSING_FUNCTION = [
    "DSKF",
    "EOF",
    "INPUT$",
    "LOC",
    "LOF"
]

COMMAND = {
    "82": "LIST",
    "83": "LLIST",
    "84": "AUTO",
    "85": "DELETE",
    "86": "RUN",
    "87": "CONT",
    "88": "LOAD",
    "89": "SAVE",
    "8A": "VERIFY",
    "8B": "NEW",
    "8C": "RENUM",
    "90": "REM",
    "91": "PRINT", # ?
    "92": "LPRINT", # L?
    "93": "DATA",
    "94": "DEF",
    "95": "INPUT",
    "96": "READ",
    "97": "STOP",
    "98": "END",
    "99": "LET",
    "9A": "DIM",
    "9B": "FOR",
    "9C": "NEXT",
    "9D": "GOTO",
    "9E": "GOSUB",
    "9F": "GO",
    "A0": "ON",
    "A1": "RETURN",
    "A2": "ERASE",
    "A3": "CURSOR",
    "A4": "IF",
    "A5": "RESTORE",
    "A6": "SCREEN",
    "A7": "COLOR",
    "A8": "LINE",
    "A9": "SOUND",
    "AA": "BEEP",
    "AB": "CONSOLE",
    "AC": "CLS",
    "AD": "OUT",
    "AE": "CALL",
    "AF": "POKE",
    "B0": "PSET",
    "B1": "PRESET",
    "B2": "PAINT",
    "B3": "BLINE",
    "B4": "POSITION",
    "B5": "HCOPY",
    "B6": "SPRITE",
    "B7": "PATTERN",
    "B8": "CIRCLE",
    "B9": "BCIRCLE",
    "BA": "MAG",
    "BB": "VPOKE",
    "BC": "MOTOR",
    "C0": "^",
    "C1": "*",
    "C2": "/",
    "C3": "MOD",
    "C4": "+",
    "C5": "-",
    "C6": "<>", # ><
    "C7": ">=", # =>
    "C8": "<=", # =<
    "C9": ">",
    "CA": "<",
    "CB": "=",
    "CC": "NOT",
    "CD": "AND",
    "CE": "OR",
    "CF": "XOR",
    "E0": "FN",
    "E1": "TO",
    "E2": "STEP",
    "E3": "THEN",
    "E4": "TAB",
    "E5": "SPC"
}

# When the byte is 80, the next byte will be of FUNC
FUNCTION = {
    "80":"ABS",
    "81":"RND",
    "82":"SIN",
    "83":"COS",
    "84":"TAN",
    "85":"ASN",
    "86":"ACS",
    "87":"ATN",
    "88":"LOG",
    "89":"LGT",
    "8A":"LTW",
    "8B":"EXP",
    "8C":"RAD",
    "8D":"DEG",
    "8E":"PI",
    "8F":"SQR",
    "90":"INT",
    "91":"SGN",
    "92":"ASC",
    "93":"LEN",
    "94":"VAL",
    "95":"PEEK",
    "96":"INP",
    "97":"FRE",
    "98":"VPEEK",
    "99":"STICK",
    "9A":"STRIG",
    "A0":"CHR$",
    "A1":"HEX$",
    "A2":"INKEY$",
    "A3":"LEFT$",
    "A4":"RIGHT$",
    "A5":"MID$",
    "A6":"STR$",
    "A7":"TIME$"
}
