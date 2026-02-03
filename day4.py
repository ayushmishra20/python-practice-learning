# File IO
# Readlines Method 

f = open("mypython.txt",'r')
i = 0
while True:
    i = i+1
    line = f.readlines()
    if not line:
        break
    m1 = int(line.split(",") [0])
    m2 = int(line.slipt(",") [1])
    m3 = int(line.split(",") [2])

    print(f"marks of student {i} is {m1}")
    print(f"marks of student {i} is {m2}")
    print(f"marks of student {i} is {m3}")

    print(line)


# Writelines method
f = open("myfile.txt", 'w')
lines = ['line\n', 'line2\n', 'line3\n']
f.writelines(lines)
f.close()

# write method

f = ('myfile.txt', 'w')
lines = ['line1', 'line2', 'line3', 'lin4']
for line in lines:
    f.write(line + '\n')
f.close()



# seek and tell

f = open('myfile.txt', 'r')
f.seek(7)
print(f.tell())
data = f.read(10)
print(data)

with open('myfile.txt', 'w') as f:
    f.write("hello world!!")
    f.truncate(5)

with open('myfile.txt', 'r') as f:
    print(f.read())

# Lambda Function
def appli(fx , value):
    return  fx(value) +10

double = lambda x : x*2
cube = lambda x: x*x*x
quad = lambda x: x*x*x*x

print(double(3))
print(appli(cube , 2))

# MAP
def cube(x):
    return x*x*x

l = [1,2,3,4,5,6,7,8,9,10]
newl = list(map(cube() , l))
print(newl)

# Filter
def filter_function(x):
    return x >5

new_l = list(filter(filter_function(l)))
print(new_l)


from functools import reduce

numbers = [1,2,3,4,5,6,7,8]
def mysum(x,y):
    return x+y

sum = reduce(mysum, numbers)
print(sum)

