def a_n(a_1, r, n):
    return a_1 + (n-1)*r

# ---------------------------------- #
print(a_n(*map(int, input().split())))