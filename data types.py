#Python Datatypes
#Determining your datatype
c=True
print(type(c))

#working with strings

print('my name is brian')

# adding variables

law = ('happy birthday my love')
print(law)
#showing the length of the characters
print(len(law))

#checking string
law = ('happy birthday my love')
print('birthday' in law) #birthday is in law variable hence output is True 

#upper and lower  cases
law = ('happy birthday my love')
print(law.upper())
print(law.lower())

#concatenation
a = 'beautiful'
b = 'day'
c= a+" "+b
print(c)
#or
d=f"{a} {b}"
print(d)


#list
students_list = ['brian','Joseph', 'Rafique','clarence','prince','Dennis', 'Terence']
print(students_list)

#accessing list items
students_list = ['brian','Joseph', 'Rafique','clarence','prince','Dennis', 'Terence']
print(students_list[-1])

#ranges of indexes
students_list = ['brian','Joseph', 'Rafique','clarence','prince','Dennis'],'Terence'
print(students_list[2:5])
print(students_list[:5])

#change list items
students_list = ['brian','Joseph', 'Rafique','clarence','prince','Dennis', 'Terence']
students_list[5]='george'
print(students_list)

#insert into list
students_list = ['brian','Joseph', 'Rafique','clarence','prince','Dennis', 'Terence']
students_list.insert(2,'Nelson')
print(students_list)

#appending
students_list = ['brian','Joseph', 'Rafique','clarence','prince','Dennis', 'Terence']
students_list.append('Festus')
print(students_list)


#remove items from list
students_list = ['brian','Joseph', 'Rafique','clarence','prince','Dennis', 'Terence']
students_list.remove('Dennis')
print(students_list)

