import re
res = re.match(r'^[a-zA-Z\_][0-9a-zA-Z\_]*$', 'eeee')

if res:
    print( True )
else:
    print( False )