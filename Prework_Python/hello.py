# Create a function that takes a name as an argument and 
# returns a new string that says Hello and then name 
# that was the argument so the output will be Hello "Name"
# Then use this function and ask the user for their name
# and tell them hello

print("Dimitrius")

name = "Dimitrius"
print(name)

print("Hello", name)
print("Hello" + " " + name)

hello_dimitrius = "Hello" + " " + name
print(hello_dimitrius)

print("Our function is defined below.")

def say_hello_print(the_users_name):
    print("Hello " + the_users_name)

print("Using our function with the print statement inside:")
say_hello_print("Dimitrius")

print("Using our function with the return statement inside and not printing:")
result = say_hello_print("Steve")
print(result)  # This line prints: None, as the function does not return a value

def say_hello_return(the_users_name):
    return "Hello " + the_users_name

print("Using our function with the return statement inside:")
print(say_hello_return("Steve"))  # This line prints: Hello Steve
hello_steve = say_hello_return("Steve")
print(hello_steve)


    
