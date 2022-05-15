#Some basic data types as variables
x="5"
y=5
z=5.1

print(type(x))
print(type(y))
print(type(z))

#Lists
#Implementing list to find factors of a given number
#Used many operators within the functions
def factors(n):
    i=1
    l=[]
    while i<=n:
        if n%i==0:
            l.append(i)
        i=i+1
    return(l)

#Tuples
#Using the above function to find if the given number is prime through typecasting the returned list returned in factor(n) funtion to a tuple and comparing it with another tuple (1,m) + returning one more data type which is a boolean
def prime(m):
    condition=(1,m)
    if m==1:
        return True
    else:
        return (print(tuple(factors(m))==condition))

m=int(input("Enter the number: ")) #Taking an input and typecasting it to an integer because input() takes string as user defined input by default.

prime(m)

#Dictionary

Dict = {'IEEE': "Institute of Electrical and Electronics Engineers", 'WIE': "Women in Engineering", 'RAS': "Robotics and Automation Society"}

keys = Dict.keys()
print("Choose from the keys:\n", keys)

k=input("Enter the Key: ")
print(Dict[k])
