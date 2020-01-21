# Number 1
# Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}]

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']}

z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)

students[0]["last_name"] = "Bryant"
print(students)

sports_directory["soccer"][0] = "Andres"
print(sports_directory)

z[0]["y"] = 30
print(z)



# Number 2
# Iterate through a list of dictionaries    
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for i in range(len(students)):
        print("first_name" + " - " + students[i]["first_name"] + ", last_name - " + students[i]["last_name"])

iterateDictionary(students)



# Number 3
# Get Values from a List of Dictionaries 
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}]
# Answer by me
def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        print(some_list[i][key_name])

iterateDictionary2("last_name", students)
iterateDictionary2("first_name", students)

#Number 4
# Iterate through a dixtionary withList values
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
# Answer from me
print(dojo.keys())
print(dojo.values())
print(len(dojo["locations"]))
def printInfo(some_dict):
    print(len(some_dict["locations"]), "LOCATIONS")
    for i in range(len(some_dict["locations"])):
        print(some_dict["locations"][i])
    print("\n")
    print(len(some_dict["instructors"]), "INSTRUCTORS")
    for i in range(len(some_dict["instructors"])):
        print(some_dict["instructors"][i])
printInfo(dojo)
# Answer for Number 4 from instructor
def printInfo2(some_dict):
    for key in some_dict.keys():
        print(f"{len(some_dict[key])} {key.upper()}")
        for item in some_dict[key]:
            print(item)
printInfo2(dojo)




