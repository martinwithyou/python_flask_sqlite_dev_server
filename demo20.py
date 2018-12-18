import re
res = re.match(r'^\d+\.\d+$', '2.2')

if res:
    print( True )
else:
    print( False )