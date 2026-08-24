file=open('ex.txt','w') #jetobar lekhbo 'w' etobar ager lekha shob muche jabe
file.write("Hello World")
file.close()
file=open('ex.txt','a')
file.write("Ajke ami vat khabo\n kintu keu dibe na\n")
file.write("Igulai basics\n amader alada ki shika lagto?")
file.close()