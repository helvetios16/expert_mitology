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


def set_creature(creature: str, **kwargs: Any) -> dict[str, str]:
    """
    Define la criatura elegida.
    """
    return {"creature": creature}


def set_element(element: str, **kwargs: Any) -> dict[str, str]:
    """
    Define el elemento elegido.
    """
    return {"element": element}


def set_role(role: str, **kwargs: Any) -> dict[str, str]:
    """
    Define el rol elegido.
    """
    return {"role": role}


def set_conflict(conflict: str, **kwargs: Any) -> dict[str, str]:
    """
    Define el conflicto elegido.
    """
    return {"conflict": conflict}


def set_god(god: str, **kwargs: Any) -> dict[str, str]:
    """
    Define el dios elegido.
    """
    return {"god": god}


def set_culture(culture: str, **kwargs: Any) -> dict[str, str]:
    """
    Define la cultura elegida.
    """
    return {"culture": culture}


def set_origin(origin: str, **kwargs: Any) -> dict[str, str]:
    """
    Define el origen elegido.
    """
    return {"origin": origin}


def set_ending(ending: str, **kwargs: Any) -> dict[str, str]:
    """
    Define el final elegido.
    """
    return {"ending": ending}
