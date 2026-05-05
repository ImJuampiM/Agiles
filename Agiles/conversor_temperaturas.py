def _validar_numero(valor):
    """Valida que el valor sea un número."""
    if not isinstance(valor, (int, float)) or isinstance(valor, bool):
        raise TypeError(f"Se esperaba un número, se recibió {type(valor).__name__}")


def celsius_to_fahrenheit(celsius):
    """Convierte temperatura de Celsius a Fahrenheit."""
    _validar_numero(celsius)
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convierte temperatura de Fahrenheit a Celsius."""
    _validar_numero(fahrenheit)
    return (fahrenheit - 32) * 5/9