def averageFromList(numbers: list[float]) -> float:
    sum: float = 0.0
    for number in numbers:
        sum += number
    sum /= len(numbers)
    return sum
