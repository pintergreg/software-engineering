package fizzbuzz

import (
	"strconv"
)

func fizzbuzz(i int) string {
	result := ""
	if i%15 == 0 {
		result = "FizzBuzz"
	} else if i%3 == 0 {
		result = "Fizz"
	} else if i%5 == 0 {
		result = "Buzz"
	} else {
		result = strconv.Itoa(i)
	}
	return result
}

func main() {

}
