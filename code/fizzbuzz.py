def fizzbuzz(i: int) -> None:
    if i % 15 == 0:
        print("" + "FizzBuzz")
    elif i % 3 == 0:
        print("" + "Fizz")
    elif i % 5 == 0:
        print("" + "Buzz")
    else:
        print(i)


def fizzbuzz_range(n: int = 100) -> None:
    for i in range(1, n + 1):
        fizzbuzz(i)


if __name__ == "__main__":
    fizzbuzz()
