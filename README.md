[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)

# Cipher Implementaions

## Caesar Cipher:
### How to run:

#### Encrypt:
```
python main.py -e -m "The message of secret" -k 8
```

#### Decrypt:
```
python main.py -d "APMHUM  IOMHWNH MKZMA" -k 8
```

#### Both:
```
python main.py -ed -m "The message of secret" -k 8
```

- -k/--key is optional as it defaults to 3


## Affine Cipher:
### Comming soon


## Playfair Cipher
### How to run:
#### Encrypt:
```
python main.py -e -m "charlemagne" -k "AACHEN"
```

#### Decrypt:
```
python main.py -d -m "HECQOCKHIEHY" -k "AACHEN"
```

- Encryption is working.
- Code needs optimization.
- Spaces will break the code.
- Double letters are not welcome in message at the moment.
