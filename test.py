def multiply(i):
    return i * i;

y = lambda x: x * x * x

print(y(2))
print(multiply(3))


z = lambda a: (a * a) + (a * a)

print(z(4))


txt = 'For only {price:.2f} dollars!'
print(txt.format(price = 49))


print('Percentage: {:%}'.format(25/40))

def getSum(num1,num2):
    answer = num1 + num2
    print('The answer is {}.'.format(answer))

myAdd = getSum
myAdd(2,4)


num1 = 3
num2 = 1
answer1 = "The answer is {}.".format(num1 + num2)
print(answer1)


truth1 = True
truth2 = False
print('The truth is always {}.'.format(truth2))
