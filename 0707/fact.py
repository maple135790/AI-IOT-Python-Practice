#  using iteration to achieve factorial function

def factorial(a):
    fList = [i for i in range(1, a+1)]
    while(len(fList) != 1):
        fList[-1] = fList[-1]*fList[-2]
        fList.pop(-2)
        print(fList[1])


# factorial(4)


def forFactorial(a):
    r = 0
    for i in range(1, a+1, 2):
        if(i+1 < a):
            r += i*(i+1)
        else:
            r += i*a
    print(r)
