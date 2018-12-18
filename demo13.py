import re
test1 = 'ssssssEEEE'
test2 = '111'
if re.match(r'\d{3}', test1):
    print('ok')
else:
    print('failed')

if re.match(r'\d{3}', test2):
    print('ok')
else:
    print('failed')

test3= '11'

if re.match(r'\d{3,8}', test3):
    print('ok')
else:
    print('failed')