

file = open("note.txt", "a")
file.write("\nI am also learning backend development.")
file.close()

print("New content added successfully!")

file=open("note.txt","r")
content= file.read()
file.close()
print(content)
