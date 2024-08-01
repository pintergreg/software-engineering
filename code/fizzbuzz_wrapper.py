def fizzbuzz(i: int) -> str:
    result = ""
    if i % 15 == 0:
        result += "FizzBuzz"
    elif i % 3 == 0:
        result += "Fizz"
    elif i % 5 == 0:
        result += "Buzz"
    else:
        result = str(i)
    return result


def fizzbuzz_loop(n: int = 100) -> None:
    for i in range(1, n + 1):
        print(fizzbuzz(i))


if __name__ == "__main__":
    fizzbuzz_loop()
