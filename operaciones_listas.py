a=[5,3,4,2,1]
b=["a","b","c"]

total = sum(a)
print("toltal: ",total)

a.append(9)
a.append(8)
print(a)

a.pop()
print(a)


# sort

a.sort(reverse=True)
print(a)



# extend

a.extend(b)
print(a)

# insert
a.insert(5,"nuevo")
print(a)

# remove
a.remove(4)
print(a)

# count
print (a.count(9))

# clear

a.clear()
print(a)

