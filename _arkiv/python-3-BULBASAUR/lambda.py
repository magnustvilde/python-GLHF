my_lambda = lambda x : '0'*x if (x>5) and (x < 10) else x*'1'

print(my_lambda(5))
print(my_lambda(1))
print(my_lambda(10))
print(my_lambda(8))

