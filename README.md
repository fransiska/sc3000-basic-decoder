### Python Version

python 3.7.3

### How to Run

Example and help

```bash
python -m sc3000basic decode
```

From file

```bash
python -m sc3000basic decode /path/to/file.BAS
```

To pretty print

```bash
python -m sc3000basic decode /path/to/file.BAS pretty
```

To suppress error

```bash
python -m sc3000basic decode /path/to/file.BAS suppress
python -m sc3000basic decode /path/to/file.BAS pretty suppress
```

To save
- decoded file will be saved to `<filepath>.txt`
- encoded file will be saved to `<filepath>.bas`

```bash
python -m sc3000basic decode /path/to/file.BAS save
```

### Reference

http://www43.tok2.com/home/cmpslv/Sc3000/EnrSCbas.htm
