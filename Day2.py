name = ['A','B','C','D','E','F']
for ind , name in enumerate(name):
  print(ind,':',name)


person_dict = {"name":"meetal","DOB":"14-08-87","place":"hyd"}
for i in person_dict:
    print(f"{i} => {person_dict[i]}")

num = 0
while num <= 5:
    print(num)
    num += 1
else:
  print("number is greater than 5")


def addfunc(a,b):
    print(f"a => {type(a)}",f"b => {type(b)}")

    return a + b

print(addfunc.__doc__)
print(addfunc(a=10.2,b=20.4))


def argfunc(*args):
 for i in args:
   print(f" parameters {i}")

 print ("1 argument")
argfunc("Hi")
print ("2 argument")
argfunc("good","morning")


def argDemo(**kargs):

 for n in kargs:

   print(f" {n} : {kargs[n]}")
 

print ("one key argument")
argDemo(Name="Joe")
print ("two key argument")
argDemo(Name="Meetal",city="Hyd")
print ("three key argument")
argDemo(Name="Meetal",city="Hyd",age = 30)


def argDemo(**args):

   print(len(args))

print ("one key argument")

argDemo(Name="Joe")

print ("two key argument")

argDemo(Name="Meetal",city="Hyd")

print ("three key argument")

argDemo(Name="Meetal",city="Hyd",age = 30)


a=0
while a < 5:
   print(a)
   a+=1 

else:
  print("While demo finished")

 
 #without else
  a=0
  while a < 5:
    print(a)
    a+=1 


num = [1, 3, 3, 4, 5, 6]
 #1 3 3 5
newlist = [x**2 for x in num if (x%2)>0]
print(newlist)



x = lambda a,b : a /b

num=int(input("Enter a Number- "))

cnt=int(input("Enter a Count- "))

print(x(num,cnt))



dictname = {"firstname":"Meetal", "city":"Hyd","profession":"Engineer", "Birthyear":1990}

newlist = [x for x in dictname.keys() if len(x) > 4]

print(newlist)


StudentDict = {

  "Student1" : {

    "FirstName" : "Meetal",

    "LastName" : "R",

    "Grade" : 1

  },

  "Student2" : {

   "FirstName" : "Swara",

    "LastName" : "U",

    "Grade" : 2

  },

  "Student3" : {

   "FirstName" : "Jack",

    "LastName" : "P",

    "Grade" : 3

  }

}

for dict in StudentDict: