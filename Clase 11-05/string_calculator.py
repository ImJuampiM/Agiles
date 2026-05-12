def add(numbers):
    if numbers == "":
        return 0
    return sum(int(num) for num in numbers.replace("\n", ",").split(","))


