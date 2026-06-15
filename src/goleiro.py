import random


def escolher_defesa(zonas):
    """Sorteia, de forma aleatória, uma das zonas para o goleiro defender."""
    return random.choice(list(zonas))
