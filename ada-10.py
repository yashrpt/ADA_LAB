
# Longest Common Subsequence (LCS)
def longestCommonSubsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i][j - 1]
                )

    return dp[m][n]


# Edit Distance (Levenshtein Distance)
def minDistance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Convert word1 prefix to an empty string
    for i in range(m + 1):
        dp[i][0] = i

    # Convert an empty string to word2 prefix
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # Deletion
                    dp[i][j - 1],      # Insertion
                    dp[i - 1][j - 1]   # Replacement
                )

    return dp[m][n]


# Main program
if __name__ == "__main__":
    text1 = "abcde"
    text2 = "ace"

    print("Text 1:", text1)
    print("Text 2:", text2)
    print("Longest Common Subsequence Length:",
          longestCommonSubsequence(text1, text2))

    word1 = "horse"
    word2 = "ros"

    print("\nWord 1:", word1)
    print("Word 2:", word2)
    print("Minimum Edit Distance:",
          minDistance(word1, word2))
