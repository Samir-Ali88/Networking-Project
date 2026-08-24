import re
text="Worldcup is fun"
#it will only check first word /case sensitive
pattern=r"Worldcup"
result=re.match(pattern,text)
if result:
    print("The word exists:",result.group())
else:
    print("No match found")    

#there is no fun in first word so it will print none
text="Worldcup is fun"
pattern=r"fun"    
result=re.match(pattern,text)
if result:
    print("The word exists:",result.group())
else:
    print("No match found")    