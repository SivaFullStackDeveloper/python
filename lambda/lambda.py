x = lambda a : a+12
print(x(5))

a = lambda x,y : x*y
print(a(10,10))

x = lambda a,b,c : a+b+c
print(x(1,2,3))

def my_lambda(n):
    return lambda a : a*n

my_lambdaer = my_lambda(10)

print(my_lambdaer(10))


def my_lambda_function(n):
    return lambda a : a*n

mytriple = my_lambda_function(10)

print(mytriple(10))
print("lambda finsihed")