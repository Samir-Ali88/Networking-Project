import re
#\d any digit 1-9
#\w any word 
#s any gap or space
text ="Sapin won the worldcup in 2010 then again won the worldcup in 2026"
p1=r"worldcup"
p2=r"\d"
#worldcup 2 bar ache
print(re.findall(p1,text))
#ar eikhane ja digit ache shob ashbe
print(re.findall(p2,text))