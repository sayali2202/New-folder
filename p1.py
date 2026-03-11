# mylist store values and print the values in variouos ways

mylist = [1, 2, 3, 4, 5]

# print the values in the list
print(mylist)

# print the values in the list using a for loop
for i in mylist:
    print(i)

#take input list of names integers and floats and print the values in the list
mylist2 = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    element = input("Enter the element: ")
    mylist2.append(element)
print(mylist2)

#also print values separately
for i in mylist2:
    print(i)
    
#example
mylist=["inaas","saara","sayali","siddhant", "Viraj", 77, "daphne", 60.52, "lara"]
print(mylist)
print(type(mylist))
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[-1])
print(mylist[2:5])
print(mylist[:5])
print(mylist[1:5])

mylist=["inaas","saara","sayali","siddhant", "Viraj", 77, "daphne", 60.52, "lara"]
mylist.append("twinkle")
print(mylist)
mylist.insert(2, "twinkle")
print(mylist)