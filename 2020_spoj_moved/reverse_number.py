def reverse_number(x):
    reverse = ""
    y = len(x)
    is_inside = False
    for i in range(0,len(x)):
        if x[y-1] != "0" or is_inside:
            reverse = reverse + x[y-1]
            is_inside = True
        y = y-1
    return(reverse)


m = input()
n = int(m)
for i in range(0,n):
    a0, b0 = input().split(" ")

    a = reverse_number(a0)
    b = reverse_number(b0)

    aint = int(a)
    bint = int(b)
    suma = aint + bint
    print(reverse_number(str(suma)))
