func isPalindrome(s string) bool {
    left, right := 0, len(s)-1

    for left < right {
        // Skip non-alphanumeric characters from left
        for left < right && !isAlphanumeric(s[left]) {
            left++
        }

        // Skip non-alphanumeric characters from right
        for left < right && !isAlphanumeric(s[right]) {
            right--
        }

        // Compare characters (case-insensitive)
        if left < right && toLower(s[left]) != toLower(s[right]) {
            return false
        }

        left++
        right--
    }

    return true
}

// isAlphanumeric checks if a character is a letter or a digit
func isAlphanumeric(c byte) bool{
    return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || (c >= '0' && c <= '9')
}

// toLower converts uppercase letters to lowercase
func toLower(c byte) byte {
    if c >= 'A' && c <= 'Z' {
        return c + 32
    }
    return c
}