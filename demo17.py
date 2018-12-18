import re
res = re.match(r'^[0-9a-z]+$', '1')

if res:
    print( True )
else:
    print( False )