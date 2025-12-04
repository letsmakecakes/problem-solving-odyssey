import (
    "math"
)

func reverse(x int) int {
    sign := 1
    if x < 0 {
        sign = -1
        x = -x
    }

    reversed := 0
    for x > 0 {
        digit := x % 10
        
        // Check for overflow before multiplying
        if reversed > math.MaxInt32/10 {
            return 0
        }

        reversed = reversed*10 + digit
        x /= 10
    }

    result := reversed * sign

    // Check if result is within 32-bit signed integer range
    if result < math.MinInt32 || result > math.MaxInt32 {
        return 0
    }

    return result
}