package main

func main() {
	countBits2(2)
}

// O(nlogn)
func countBits1(n int) []int {
	var answer []int = []int{0}
	for i := 1; i <= n; i++ {
		curr := 0
		for s := i; s > 0; s >>= 1 {
			if s%2 == 1 {
				curr += 1
			}
		}
		answer = append(answer, curr)
	}
	return answer
}

// O(n)
func countBits2(n int) []int {
	var answer []int = []int{0}
	step := 1
	for i := 1; i <= n; i++ {
		if step*2 <= i {
			step *= 2
		}
		answer = append(answer, 1+answer[i-step])
	}
	return answer
}
