#num = (1,100)
def fizz_buzz(i):
#for i in num:
    if i % 3 ==0 and i % 5 ==0:
       return 'Fizzbuzz'
    elif i % 3 ==0:
       return 'Fizz'
    elif i % 5 ==0:
        return 'Buzz'
    else:
        return i
for i in range(1,100):
    print(fizz_buzz(i))
    
