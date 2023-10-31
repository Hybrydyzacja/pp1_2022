# file = open('countries.txt','r') #bez polskich znakow

file = open("countries.txt", "r", encoding="utf-8") #utf-8 plik bedzie zawieral polskie znaki
file_content = file.read()
print( file_content )
file.close()


# file = open("countries.txt", "r", encoding="utf-8")
 
# l = 1
# for line in file:
#     print(l, line, end="")
#     l += 1
   
# file.close()

