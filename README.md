# Para Homónimo

A Spanish homonyms reference utility.

## Description

**Para Homónimo** is a simple Python utility that provides a dictionary of Spanish homonyms (words that sound alike but have different meanings) and functions to look them up.

Homonyms in Spanish can be tricky because words that sound the same often have completely different meanings and spellings. This tool helps learners and native speakers alike to understand and differentiate between these commonly confused words.

## Features

- Look up the meaning of Spanish homonyms
- Find related homonyms for a given word
- List all homonyms in the dictionary

## Usage

### As a Script

Run the script directly to see examples:

```bash
python para_homonimo.py
```

### As a Module

Import and use the functions in your own code:

```python
from para_homonimo import buscar_homonimo, obtener_homonimos, listar_todos

# Look up the meaning of a word
significados = buscar_homonimo("hola")
print(significados)  # ['saludo (greeting)']

# Find homonyms for a word
homonimos = obtener_homonimos("hola")
print(homonimos)  # ['ola']

# List all homonyms
todos = listar_todos()
```

## Examples of Spanish Homonyms

| Word 1 | Meaning | Word 2 | Meaning |
|--------|---------|--------|---------|
| hola | greeting | ola | wave |
| bello | beautiful | vello | soft hair/fuzz |
| tubo | tube/pipe | tuvo | had (verb) |
| caza | hunting | casa | house |

## Requirements

- Python 3.9+

## License

This project is open source.
