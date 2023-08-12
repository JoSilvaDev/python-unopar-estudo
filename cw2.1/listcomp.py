#[2*x for x in range(10)]

fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
newlist = []

for x in fruits:
    if 'b' in x:
        newlist.append(x)

print(newlist)