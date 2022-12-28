def isPalindrome(x: int) -> bool:
    x = str(x)
    l = []
    for i in range(len(x)):
        if x[i] == x[-i-1]:
            l.append(1)
        else:
            l.append(0)
    if min(l) == 1:
        return True
    else:
        return False

if __name__ == "__main__":
    print(isPalindrome(121))
    print(isPalindrome(11231234))