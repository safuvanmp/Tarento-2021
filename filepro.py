#Write a program to record notes entered by a user. The program should do the following things:
#First asks the users name.
#Asks the user to enter a single-line note. After the user enters the note, it should get stored in USERNAME_notes.txt on a new line.
#The user will be asked to enter multiple notes in a loop till he/she types exit.

file_name=input("Enter user name :")
string=""
while(string!="exit"):
  string = input("Enter user notes:")
  f=open(file_name,'a')
  f.write(string)
  f.write("\n")
f.close()
