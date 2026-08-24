file = open('ex.txt', 'r')
ok = file.read() #eikhane shob gula print hobe
print(ok)
file.close()

file = open('ex.txt', 'r')
ok = file.readline() #ikhane shudu first  line print hobe
print(ok)
file.close()

file = open('ex.txt', 'r')
ok = file.readlines() #ikhane  ek  line e list akare print korbe print hobe
print(ok)
file.close()