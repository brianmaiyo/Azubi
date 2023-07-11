#Python Datatypes
#Determining your datatype
c=True
print(type(c))
print()
#transforming a variable into int and float respectively
num=int(4.2)
print(num)
print()
Num=float(4)
print(Num)
print()
print(str(10)+' '+'Shillings')

#working with strings

print('my name is brian')

# adding variables

law = ('happy birthday my love')
print(law)
#showing the length of the characters
print(len(law))
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
students_list = ['brian','Joseph', 'Rafique','clarence','prince','Dennis', 'Terence']
print(students_list)
print()

#accessing list items
students_list = ['brian','Joseph', 'Rafique','clarence','prince','Dennis', 'Terence']
print(students_list[-1])
print()

#ranges of indexes
students_list = ['brian','Joseph', 'Rafique','clarence','prince','Dennis','Terence']
print(students_list[2:5])
print(students_list[:5])
print()

#change list items
students_list = ['brian','Joseph', 'Rafique','clarence','prince','Dennis', 'Terence']
students_list[5]='george'
print(students_list)
print()

#insert into list
students_list = ['brian','Joseph', 'Rafique','clarence','prince','Dennis', 'Terence']
students_list.insert(2,'Nelson')
print(students_list)
print()

#appending
students_list = ['brian','Joseph', 'Rafique','clarence','prince','Dennis', 'Terence']
students_list.append('Festus')
print(students_list)
print()

#remove items from list
students_list = ['brian','Joseph', 'Rafique','clarence','prince','Dennis', 'Terence']
students_list.remove('Dennis')
print(students_list)
print()
