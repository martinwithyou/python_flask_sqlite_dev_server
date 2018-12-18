import re
test = 'ssssssEEEE'
if re.match(r'[0-9a-zA-Z\_]+', test):
    print('ok')
else:
    print('failed')