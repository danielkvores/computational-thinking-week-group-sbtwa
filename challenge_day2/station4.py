# this is going to be about prime numbers
# if the input number is prime, return True, else return False


def solution_station_4(number: int) -> bool:
    if number < 2:
        return False

    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            return False

    return True
