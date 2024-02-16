package main

import "fmt"

func DigitReplace(n int) int {
	if n == 0 {
		return 5
	}

	isNegative := n < 0
	if isNegative {
		n = -n
	}

	temp := 0
	for n > 0 {
		lastDigit := n % 10

		if lastDigit == 0 {
			lastDigit = 5
		}

		temp = temp*10 + lastDigit
		n = n / 10
	}

	result := 0
	for temp > 0 {
		result = result*10 + temp%10
		temp = temp / 10
	}

	if isNegative {
		return -result
	} else {
		return result
	}

}

func main() {
	fmt.Println(DigitReplace(50))
}
