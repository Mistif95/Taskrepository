# Versi 1.2
def check_even_odd(num):
    if num % 2 == 1:
        return True
    else:
        return False

for i in range(1, 101):
    if check_even_odd(i):
        print(i)