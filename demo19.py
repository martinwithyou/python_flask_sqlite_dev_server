import re
res = re.match(r'[^a-zA-Z\_][0-9a-zA-Z\_]{0, 19}$', '22222222222222222222')

if res:
    print( True )
else:
    print( False )