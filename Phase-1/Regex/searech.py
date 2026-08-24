import re
#it will search the string and find it and use it
text="Worldcup is fun"
pattern=r"fun"    
result=re.search(pattern,text)
if result:
    print("The word exists:",result.group())
else:
    print("No match found")  

#it only checks the first one and stops there

text="Worldcup is fun to play football is more fun"
pattern=r"is"    
result=re.search(pattern,text)
if result:
    print("The word exists:",result.group())
else:
    print("No match found")  
#used the first "is" and avoided the last "is"