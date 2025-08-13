def git_func():
    a = 5
    b = 10 
    c = a + b
    return c
result = git_func()
print("the result",result)



def add_fun(a ,b):
    c =a + b
    print( "return value")
    return c
a = 100
b = 200
 
result = add_fun(a,b)
print(result)


def  math_fun( a, b):

    add =a+b
    subtract =a-b
    multiply =a*b
    return{
     "add": add,
      "subtract": subtract,
    " multiply":multiply
    }
result =math_fun(10,20)
print(result)
    

# def my_function(fname):
#   print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")

# ** kwarg 

def my_function(**kwarg):
  print("His fast  name is " + kwarg["fname"])

my_function(fname = "usman", lname = "umer")
#  list loop
# def math_fun(a):
#     for x in a:
#         a =[1,"nothing",3,"i am here",5,6,7,8,9]
# def math_fun(a):

number =[1,"haloo",3,"i am here",5,6]
for number in number:
    print(number)
    if number == 5:
        print (5) 


