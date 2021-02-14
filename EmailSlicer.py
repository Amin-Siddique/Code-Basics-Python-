##getting a list of dummy emails:
emailList = ["mrsam@outlook.com"
,"dougj@me.com"
,"stecoop@optonline.net"
,"bdthomas@icloud.com"
,"oster@outlook.com"
,"crimsane@yahoo.ca"]

for i in emailList:
    username = i[:i.index("@")]
    print(f"user value for - {i} : {username}")
    
for j in emailList:
    address = j[j.index("@")+1:]
    print(f"Address value for - {j} : {address}")   
