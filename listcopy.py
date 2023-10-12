import copy 

# Initializing list 
list1 = [ 1, [2, 3] , 4 ] 
print("list 1 before modification:\n", list1) 

# all changes are reflected 
list2 = list1 

# shallow copy - changes to 
# nested list is reflected, 
# same as copy.copy(), slicing 

list3 = list1.copy() 

# deep copy - no change is reflected 
list4 = copy.deepcopy(list1) 

list1.append(5) 
list1[1][1] = 999

print("list 1 after modification:\n", list1) 
print("list 2 after modification:\n", list2) 
print("list 3 after modification:\n", list3) 
print("list 4 after modification:\n", list4)
