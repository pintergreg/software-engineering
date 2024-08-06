from fizzbuzz import fizzbuzz


def fizzbuzz_loop(n: int = 100) -> None:
    for i in range(1, n + 1):
        print(fizzbuzz(i))


if __name__ == "__main__":
    fizzbuzz_loop()
