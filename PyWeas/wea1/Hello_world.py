num = 10
i = 2
is_prime = True
while i < num:
    rnum = num % i
    if rnum == 0:
        is_prime = False
        break
    i+= 1
if is_prime == True:
    print("primo")
else:
    print("Not primo")