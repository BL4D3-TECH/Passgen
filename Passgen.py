import string
import random
import pyperclip as clp

length = int(input("Length of the password: "))
characters = list(string.printable)
rmv = [' ', '\t', '\n', '\r', '\x0b', '\x0c']
password = ""
file_path = "N-archivo.txt" # Write here the name or the path of the file where the passwords will be save

#Removes the characters that are not necessary
for x in rmv:
	characters.remove(x)

#creates the password
for i in range(length):
	char = random.choice(characters)
	password = password + char

#printing that the process is finished
print(f"Your secure password is {password}.")
try:
	clp.copy(password)
	print("It has been already copied to your clipboard")
except:
	print(f'It has been an error coping the password to your clipboard\nCopy it manually: "{password}"')

#Saving the password
while True:
	save = input("Do you want to save it or not(y, n): ")
	if save == "y":
		url = input("Write the URL: ")
		with open(file_path, "a") as f:
			f.write(f"{url}: {password}")
			f.close()
		print('it has been saved in "./Passwords.txt"')
		break
	elif save == 'n':
		print("Ok, thanks.")
		break
		exit()
	else:
		print(f'{save} it is not a valid response\nTry "y" for yes or "n" for no')