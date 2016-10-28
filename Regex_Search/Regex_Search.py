import re,os
aux=0
search = re.compile((input("Writte the regex to search: ")))
for file in os.listdir(".\\Texts"):
    if file.endswith(".txt"):
        with open(".\\Texts/"+file) as f:
            for line in f.readlines():
                result = search.search(line)
                if(result != None):
                    print("It founds: " + result.group())
                    aux+=1
if(aux):
    print("The regex was founded %d time (s)" %(aux) )
else:
    print("The regex was not founded.")