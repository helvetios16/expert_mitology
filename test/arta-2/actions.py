from typing import Any


def set_diagnosis(diagnosis: str, **kwargs: Any) -> dict[str, str]:
    """Devuelve un diccionario con el diagnóstico."""
    return {"diagnosis": diagnosis}
