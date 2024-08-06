from fizzbuzz import fizzbuzz
from fizzbuzz_wrapper import fizzbuzz_loop


# def test_fizzbuzz():
#     assert fizzbuzz(3) == "Fizz"
#     assert fizzbuzz(5) == "Buzz"
#     assert fizzbuzz(10) == "Buzz"
#     assert fizzbuzz(12) == "Fizz"
#     assert fizzbuzz(15) == "FizzBuzz"
#     assert fizzbuzz(17) == "17"
#     pass


# def test_fizzbuzz_loop(capfd):
#     fizzbuzz_loop(16)
#     out, _ = capfd.readouterr()
#     expected = (
#         "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n"
#         "11\nFizz\n13\n14\nFizzBuzz\n16\n"
#     )
#     assert out == expected
