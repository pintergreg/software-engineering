package fizzbuzz

import (
	"testing"
)

func TestFizzBuzz(t *testing.T) {
	got := fizzbuzz(3)
	if got != "Fizz" {
		t.Errorf("got %v, wanted 'Fizz'", got)
	}
	got = fizzbuzz(5)
	if got != "Buzz" {
		t.Errorf("got %v, wanted 'Buzz'", got)
	}
	got = fizzbuzz(15)
	if got != "FizzBuzz" {
		t.Errorf("got %v, wanted 'FizzBuzz'", got)
	}
	got = fizzbuzz(17)
	if got != "17" {
		t.Errorf("got %v, wanted '17'", got)
	}
}
