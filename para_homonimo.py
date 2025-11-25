#!/usr/bin/env python3
"""
Para Homónimo - A Spanish homonyms reference utility.

This module provides a dictionary of Spanish homonyms (words that sound alike
but have different meanings) and functions to look them up.
"""

# Dictionary of Spanish homonyms with their meanings
HOMONIMOS = {
    "baca": ["portaequipajes del coche (car roof rack)"],
    "vaca": ["animal bovino (cow)"],
    "bello": ["hermoso, bonito (beautiful)"],
    "vello": ["pelo corto y suave (soft hair/fuzz)"],
    "hierba": ["planta pequeña (herb/grass)"],
    "hierva": ["del verbo hervir (from verb 'to boil')"],
    "hola": ["saludo (greeting)"],
    "ola": ["onda de agua (wave)"],
    "hecho": ["participio de hacer (done/made)"],
    "echo": ["del verbo echar (from verb 'to throw')"],
    "hay": ["del verbo haber (there is/are)"],
    "ay": ["exclamación de dolor (exclamation of pain)"],
    "ahí": ["adverbio de lugar (adverb of place - there)"],
    "tubo": ["pieza cilíndrica hueca (tube/pipe)"],
    "tuvo": ["del verbo tener (from verb 'to have')"],
    "caza": ["acción de cazar (hunting)"],
    "casa": ["edificio para vivir (house)"],
    "cima": ["parte más alta (summit/peak)"],
    "sima": ["cavidad grande en la tierra (abyss/chasm)"],
    "cocer": ["preparar alimentos con calor (to cook)"],
    "coser": ["unir con hilo (to sew)"],
    "rallar": ["desmenuzar con rallador (to grate)"],
    "rayar": ["hacer rayas (to scratch/draw lines)"],
    "hasta": ["preposición (until/up to)"],
    "asta": ["cuerno, palo de bandera (horn, flagpole)"],
    "asia": ["continente (continent)"],
    "hacia": ["preposición de dirección (toward)"],
}


def buscar_homonimo(palabra: str) -> list[str] | None:
    """
    Search for homonym meanings of a given word.

    Args:
        palabra: The Spanish word to look up.

    Returns:
        A list of meanings if the word is found, None otherwise.
    """
    return HOMONIMOS.get(palabra.lower())


def obtener_homonimos(palabra: str) -> list[str]:
    """
    Get all homonyms related to a given word.

    Args:
        palabra: The Spanish word to find homonyms for.

    Returns:
        A list of words that are homonyms of the given word.
    """
    palabra = palabra.lower()
    # Common homonym pairs
    pares = [
        ("baca", "vaca"),
        ("bello", "vello"),
        ("hierba", "hierva"),
        ("hola", "ola"),
        ("hecho", "echo"),
        ("hay", "ay", "ahí"),
        ("tubo", "tuvo"),
        ("caza", "casa"),
        ("cima", "sima"),
        ("cocer", "coser"),
        ("rallar", "rayar"),
        ("hasta", "asta"),
        ("asia", "hacia"),
    ]

    for grupo in pares:
        if palabra in grupo:
            return [h for h in grupo if h != palabra]
    return []


def listar_todos() -> dict[str, list[str]]:
    """
    List all homonyms in the dictionary.

    Returns:
        A dictionary of all homonyms and their meanings.
    """
    return HOMONIMOS.copy()


def main():
    """Main function demonstrating usage of the homonym utility."""
    print("=== Para Homónimo - Spanish Homonyms Reference ===\n")

    # Example lookups
    ejemplos = ["hola", "ola", "bello", "vello"]

    for palabra in ejemplos:
        significados = buscar_homonimo(palabra)
        homonimos = obtener_homonimos(palabra)

        print(f"Palabra: {palabra}")
        if significados:
            print(f"  Significado: {', '.join(significados)}")
        if homonimos:
            print(f"  Homónimos: {', '.join(homonimos)}")
        print()


if __name__ == "__main__":
    main()
