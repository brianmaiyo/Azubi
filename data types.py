#Python Datatypes
#Determining your datatype
c=True
print(type(c))
print()
#transforming a variable into int and float respectively
num=int(4.2)
print(num)
print()
Numb=float(4)
print(Numb)
print()
print(str(10)+' '+'Shillings')

#working with strings

print('my name is brian')

# adding variables

merit=('happy birthday my love')
law = ('happy birthday my love','hi')
print(law)
# using len
print(len(merit)) #showing the length of the characters
print(len(law)) #getting number of items
print()
#checking string
law = ('happy birthday my love')
print('birthday' in law) #birthday is in law variable hence output is True 
print()
#upper and lower cases, capitalize and count
law = ('happy birthday my love')
print(law.upper())
print(law.lower())
print(law.capitalize()) #capitalizes the first letter of the sentence
print(law.count("a"))   #counts the number of character 'a'
print()
#concatenation
a = 'beautiful'
b = 'day'
c= a+' '+b
#or
print(a,b)

print(c)
#or using custom string formatting
d=f'{a} {b}'
print(d)

print()

#list
#arrays contain numerical datatype and must all be same datatype
#Stores anything and any type
students_list = ['brian','Joseph', 'Rafique',10,'clarence','prince',1.0,'Dennis', 'Terence']
print(students_list)
print()

#accessing list items
students_list = ['brian','Joseph', 'Rafique',10,'clarence','prince',1.0,'Dennis', 'Terence']
print(students_list[-1])
print()

#ranges of indexes
students_list = ['brian','Joseph', 'Rafique',10,'clarence','prince',1.0,'Dennis', 'Terence']
print(students_list[2:5])
print(students_list[:5])
print()

#change list items
students_list = ['brian','Joseph', 'Rafique',10,'clarence','prince',1.0,'Dennis', 'Terence']
students_list[5]='george'
print(students_list)
print()

#insert into list
students_list = ['brian','Joseph', 'Rafique',10,'clarence','prince',1.0,'Dennis', 'Terence']
students_list.insert(2,'Nelson')
print(students_list)
print()

#appending
students_list = ['brian','Joseph', 'Rafique',10,'clarence','prince',1.0,'Dennis', 'Terence']
students_list.append('Festus')
print(students_list)
print()

#remove items from list
students_list = ['brian','Joseph', 'Rafique',10,'clarence','prince',1.0,'Dennis', 'Terence']
students_list.remove('Dennis')
print(students_list)
print()


#dictionaries
#stores data in key Value pairs and order not guaranteed
name1 = {}
name1['first']='brian'
name1['last']= 'kipkosgei'
print(name1)

name2 = {}
name2['first']='Mon'
name2['last']= 'Ami'
print(name2)

people =[]
people.append(name1)
people.append(name2)
people.append({'first' :'Bill', 'last': 'Gaither'})
print(people)