import re
res = re.match(r'^[0-9a-z\_]$', 'TTTTTT')

if res:
    print( True )
else:
    print( False )