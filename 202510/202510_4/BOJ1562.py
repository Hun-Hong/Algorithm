if __name__ == "__main__":
    N = int(input())
    dp = [[[0] * ((1 << 10)) for _ in range(10)] for _ in range(101)]

    for i in range(1, 10):
        dp[1][i][1 << i] = 1
    
    for length in range(1, 100):
        for last_digit in range(10):
            for bit_mask in range((1 << 10)):
                if last_digit < 9:
                    next_mask = bit_mask | (1 << (last_digit + 1))
                    dp[length + 1][last_digit + 1][next_mask] += dp[length][last_digit][bit_mask]
                if last_digit > 0:
                    next_mask = bit_mask | (1 << (last_digit - 1))
                    dp[length + 1][last_digit - 1][next_mask] += dp[length][last_digit][bit_mask]
count = 0
for digit in range(10):
    count += dp[N][digit][0b1111111111]
    count %= 1000000000

print(count)