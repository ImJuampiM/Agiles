def decimal_to_roman(numero):
    """Convierte un número decimal a números romanos (1-5)."""
    romanos = {
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V"
    }
    return romanos[numero]