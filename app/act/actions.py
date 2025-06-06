from typing import Any


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
