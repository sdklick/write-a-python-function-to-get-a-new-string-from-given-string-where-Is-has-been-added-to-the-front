'''
write a python function to get a new string from given string where 'Is'
has been added to the front if the given string already begin with 'Is'
the return the string unchange
'''

def stringfun(string):
    if string[0:2]=='Is':
        return string
    else:
        return 'Is '+string
string=input('Enter string : ')
output=stringfun(string)
print(output)

