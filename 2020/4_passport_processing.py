import re

filename = '4.txt'

with open(filename) as f:
    content = f.read().split('\n\n')

if 



# passport_re = re.compile(r'.*\n\n')

# for passport in passport_re.finditer(content):
#     print(passport.group())
#     print('----')