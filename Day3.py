1.Dictionaries
given a list of numbers (nums = [1, 2, 3]) use dict comprehension to create a dict of squares { 1: 1, 2: 4, 3: 9}
make a list of values alone from the above dictionary [1, 4, 9] using list comprehension

nums = [1,2,3]
nums_dic = {i:i**2 for i in nums}
print(nums_dic)
nums_list = [x for x in nums_dic.values()]
print(nums_list)


2.set comprehension
given a list [1, 2, 5, 2, 3, 1, 4, 5], create squares of unique items using set comprehension. {1, 4, 9, 16, 25}

a_list = [1,2,5,2,3,1,4,5]
#list_set = set(a_list)
#print(list_set)
square_set = {i**2 for i in set(a_list)}
print(square_set)

3.Given a list of tuples with current and min balances: [("Guido", 2000, 500), ("Raymond", -52, 1000), ("Jack", 900, 1000), ("Brandon", 2000, 0)] use comprehensions to get the below:
a. dict of those with proper balances (above or equal min bal) {"Guido": 2000, "Brandon": 2000}
   
a_tuplist = [("Guido", 2000, 500), ("Raymond", -52, 1000), ("Jack", 900, 1000), ("Brandon", 2000, 0)]

a_dict = {x:y for (x,y,z) in a_tuplist if y > z}
print(a_dict)

b.set of all balances {2000, -52, 900}

a_tuplist = [("Guido", 2000, 500), ("Raymond", -52, 1000), ("Jack", 900, 1000), ("Brandon", 2000, 0)]

a_dict = [ z for (x,y,z) in a_tuplist]
print(a_dict)


c.3 list of account holders ["Guido", "Raymond", "Jack", "Brandon"]

a_tuplist = [("Guido", 2000, 500), ("Raymond", -52, 1000), ("Jack", 900, 1000), ("Brandon", 2000, 0)]

a_dict = [ x for (x,y,z) in a_tuplist]
print(a_dict)

d.dict of user and money each need to fulfill the min balance requirement 
(those who already have enough bal should not be in the dict) {"Raymond": 1052, "Jack": 100}

a_tuplist = [("Guido", 2000, 500), ("Raymond", -52, 1000), ("Jack", 900, 1000), ("Brandon", 2000, 0)]

a_dict = {x:(z-y) for (x,y,z) in a_tuplist if y<z}
print(a_dict)


e.list of tuples with name and current balance if the balance is above 0 [("Guide", 2000), ("Jack", 900), ("Brandon", 2000)]
a_tuplist = [("Guido", 2000, 500), ("Raymond", -52, 1000), ("Jack", 900, 1000), ("Brandon", 2000, 0)]

a_dict = {x for (x,y,z) in a_tuplist if y>0}
print(a_dict)



4. Write a Developer class that has a code function and a languages list.

code function should accept a language param and if the language is in the languages list it should print code in <language>.

resume function that prints languages of the developer.

Write a SrDeveloper class that inherits Developer and adds review function. review should also be limited to languages list.

Write a TechLead class that inherits from SrDeveloper and adds design function



class Developer:

 def __init__(self):

    self.langList= []

 def code(self,p_lang):

    if p_lang not in self.langList:

     self.langList.append(p_lang)

    else:

     print(p_lang) 

 def resume(self):

  print( "List", self.langList)



class SrDeveloper(Developer):

  def __init__(self):

    Developer.__init__(self)

  def review(self,lang1):

    self.langList.append(lang1)

    print("Review list", self.langList)

class TechLead(SrDeveloper):

  def __init__(self):

    SrDeveloper.__init__(self)

  def design(self,lang1):

    self.langList.append(lang1)

    print("Design list", self.langList)

o1 = Developer()

o1.code("Python")

o1.code("PLSQL")

o1.code("PLSQL")

o1.resume()

o2= SrDeveloper()

o2.review("Java")

o3= TechLead()

o3.design("C#")



5. create a class that provides the factorials for the list of numbers provided.

import math

class Factclass:

 langList= []

 def __init__(self,num):

   self.num=num

 def fact(self):

   print(math.factorial(self.num))

   #print(self.num)



o1 = Factclass(5)

o1.fact()


6.import a func from a module and call it to print some output

import math 

print("Its square root value is ", math.sqrt(5))

7.import a func and rename it to use in your module from another

# Module Name : MyModule


def add_func(a, b):

    print(int(a) +int(b))



import MyModule as MainModule


print(MainModule.add_func(1,1))


8.create a module that prints "I'm running" only when it's ran as a script (not as a module using import)

def im_running():

    if __name__ == "__main__":

        print("I'm Running")



im_running()

9.use python to open another python source file and print the contents






