def getFibNth(n):
    """
    Naive and simple fibb solution with O(2^n)
    """
    if n == 0:
        return 1
    if n == 1:
        return 1
    return getFibNth(n-1) + getFibNth(n-2)

def getFibNth2(n, calculated={1:1, 2:1}):
    """
    Solution with hash table - dictionary
    """
    if n in calculated:
        return calculated[n]
    calculated[n] = getFibNth2(n-1, calculated) + getFibNth2(n-2, calculated)
    return calculated[n]


def main():
    print(getFibNth(10))
    print(getFibNth2(10))


if __name__ == "__main__":
    main()