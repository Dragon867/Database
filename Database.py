lst=['Apple','Pineapple','Banana','Grapes','Kivi']
print("Length of the list :",len(lst))
print("First element",lst[0])
print("Last element",lst[-1])

lst.append('Watermellon')
print("Updated list",lst)
lst.remove('Banana')
print("Updated list",lst)
lst.sort()
print("sorted list",lst)
lst.pop('1')
print("Updated list",lst)
lst.reverse()
print("reversed list",lst)
print("Multipliction on the list",lst*2)

lst=lst[:4]
print("sliced list",lst)
lst.clear()
print("Updated list",lst)