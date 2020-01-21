# dog = ("Bruce","Dobberman", 12, False)
# print(f"{dog[0]} is a {dog[1]}")

# arrays are know as list in python
# empty_list = []
# ninjas = ['Rozen', 'KB', 'Oliver']
# print(ninjas[2]) 	# output: Oliver
# ninjas[0] = 'Francis'
# # append function used to add variable to a list
# ninjas.append('Michael')
# print(ninjas)	# output: ['Francis', 'KB', 'Oliver', 'Michael']
# # pop function used to remove a variable from a list
# ninjas.pop()
# print(ninjas)	# output: ['Francis', 'KB', 'Oliver']
# ninjas.pop(1)
# print(ninjas)	# output: ['Francis', 'Oliver']


# # objects are known as dictionaries in python
# empty_dict = {}
# new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
# new_person['name'] = 'Jack'	# updates if the key exists
# new_person['hobbies'] = ['climbing', 'coding']	# adds a key-value pair if the key doesn't exist
# print(new_person)	
# # output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
# w = new_person.pop('weight')	# removes the specified key and returns the value
# print(w)		# output: 160.2
# print(new_person)	
# # output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}        

# my_list = ["stars", 6, "atlantis"]
# print(my_list)
# for i in my_list:
#     print(i)
# x = len(my_list)
# for i in range(0,x,2):
#     print (i,my_list[i])


my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(k)

for k in my_dict:
    print (my_dict, my_dict[k])


