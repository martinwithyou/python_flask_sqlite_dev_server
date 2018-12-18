import re
res = re.match(r'^[0-9]+$', '1')

if res:
    print( True )
else:
    print( False )