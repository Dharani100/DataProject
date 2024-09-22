# learn project
def fun():
    x = float(input('Enter the first number'))
    y = float(input('Engter the second number'))
    return x+y

num = fun(5,2)
print(num)

def prime(num):
    if num <= 0:
       return '0 or -ve numbers are not prime'
    elif num <= 3:
        return 'Prime'
    else:
        for i in range(2, num):
            if num % i ==0:
                return 'Not Prime'
            return 'prime'

print(prime(num))
       
