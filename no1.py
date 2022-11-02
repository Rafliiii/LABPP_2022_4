import re

s = input('')
regex1 =r'[a-z?A-Z?0?2?4?6?8?]'
regex2 =r'[1?3?5?7?9? ?]'

result1 = re.findall(regex2, s[0:40])
print(result1)

if result1:
    print('false')
    exit() 

result2 = re.findall(regex1, s[40:45])
print(result2)
if result2:
    print('false')
    exit()

if len(s) == 45:
    print('true')


else:
    print('false')

