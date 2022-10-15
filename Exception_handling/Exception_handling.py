# Exception handling

def func(a,b):
    try:
        c=a+b
        return c
    except:
        print("Erroeeee")

print(func(1,2))
print(func(1,'a'))