file = open('text.txt','r+')
changed_text = ''
for word in (file.readline()).split():
    if(word == 'ADJECTIVE'):
        word = input("Writte an adjective:")
    elif(word == 'VERB'):
        word = input("Writte a verb:")
    elif(word == 'NOUN'):
        word = input("Writte a noun:")
    elif(word == 'OBJECT'):
        word = input("Enter an object:")
    changed_text= changed_text + ' ' + word
file.close()
print(changed_text)
f = open('changed_text.txt','w+')
f.write(changed_text)
f.close()