#LSM
def last_man_standing(N, C):
    # Create a dp array where dp[i] means if having i balls is a winning position
    dp = [False] * (N + 1)
    
    # Initialize base case
    dp[0] = False  # If there are no balls left, the current player loses

    # Fill the dp array
    for i in range(1, N + 1):
        if (i - 1 >= 0 and not dp[i - 1]) or \
           (i - 2 >= 0 and not dp[i - 2]) or \
           (i - 5 >= 0 and not dp[i - 5]):
            dp[i] = True
    
    # Determine the result
    if dp[N]:
        # The starting player wins if dp[N] is True
        if C == 1:
            print("Lala")
        else:
            print("Lili")
    else:
        # The starting player loses if dp[N] is False
        if C == 1:
            print("Lili")
        else:
            print("Lala")

# Sample input
N, C = map(int, input("masukkan input=>").split())
last_man_standing(N, C)

#dp = [False, True, True, False, True, True, False, True, True]