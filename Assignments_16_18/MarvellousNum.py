def ChkPrime(no):
    flag = True

    if (no <= 1):
        flag = False
    else:
        for i in range(2, no):
            if (no % i == 0):
                flag = False
    return flag