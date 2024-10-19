'''
Python string format:
1. % string
2. format string
3. f.string
'''
name= "Adit Sakata"
age = 19
height = 173
print("My name is", name, "I am", age, "years old and I have a height of", height)

print("_"*25, "string %")
print("My name is %s. I am %i years old, and I am %f cm tall." %(name, age, height))

print("_"*25, "format string")
print("My name is {n}. I am {a} years old, and I am {h} cm tall." .format(n = name, a = age, h = height))
print("My name is {0}. I am {1} years old, and I am {2} cm tall." .format(name, age, height))

print("_"*25, "f.string")
print(f"My name is {name}. I am {age} years old, and I am {height} cm tall.")

print("_"*25, "Alignment - String%")
print( "1. name = [ {nm:<25} ] " .format( nm = 'JD' ) )
print( "2. name = [ {nm:>25} ] " .format( nm = 'JD' ) )
print( "3. name = [ {nm:^25} ] " .format( nm = 'JD' ) )