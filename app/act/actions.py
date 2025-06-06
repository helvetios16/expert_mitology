from typing import Any
import random


def set_world(cultura: str, **kwargs: Any) -> dict[str, str]:
    """
    Define el mundo elegido.
    """
    options = cultura.split(",")
    cultura = random.choice(options)
    return {"cultura": cultura}


def set_values(value: str, **kwargs: Any) -> dict[str, str]:
    """
    Define el valor elegido.
    """
    options = value.split(",")
    value = random.choice(options)
    return {"value": value}


def set_culture(cultura: str, **kwargs: Any) -> dict[str, str]:
    """
    Define la cultura elegida.
    """
    return {"cultura": cultura}


def set_archetype(arch: str, **kwargs: Any) -> dict[str, str]:
    """
    Define el arquetipo seleccionado.
    """
    return {"archetype": arch}
