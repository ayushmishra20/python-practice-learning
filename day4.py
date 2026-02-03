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
