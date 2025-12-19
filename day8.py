#lambda function
f=lambda a1,a2:a1+a2
print(f(25,30))

l=[]
for var in [10,20,30,40]:
    r=var+100
    l.append(r)
print(l)

#Using List comprehension:reads "right to left".
li=[var+100 for var in [10,20,30]]
print(li)

ex=[var+100 if var>30 else var+500 for var in [10,20,30,40,50]]
print(ex)

#map(function,Collection)-->Generator
a=list(map(lambda a:a>10,[10,5,56,50]))
print(a)

#3.Generator-> Function returns an iterator i.e Address
#yield->returns an address 
def fx():
    yield 10
    yield 20 
    yield 20+20
    yield [20,10]
gen_obj=fx()
i=1
while(i<=4):
    print(next(gen_obj))
print(type(fx()))

