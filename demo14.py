import re
res = re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
print( res )
if res:
    print( True )
else:
    print( False )
