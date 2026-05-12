def add(numbers):
    if numbers == "":
        return 0
    
    # Reemplazar saltos de línea por comas para unificar separadores
    numbers_str = numbers.replace("\n", ",")
    num_list = numbers_str.split(",")
    
    # Validar que no haya números negativos
    for num_str in num_list:
        num = int(num_str)
        if num < 0:
            raise Exception(f"negatives not allowed: {num}")
    
    return sum(int(num) for num in num_list)