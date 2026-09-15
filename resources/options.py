import string
import random
from pathlib import Path
import resources.crypton as crypton

class codes:
	@staticmethod
	def No_errors(*args, reset=True):
		return "\033[32m" + "".join(args) + "\033[0m" if reset else "\033[32m" + "".join(args)

	@staticmethod
	def Error(*args, reset=True):
		return "\033[31m" + "".join(args) + "\033[0m" if reset else "\033[31m" + "".join(args)

	@staticmethod
	def Caution(*args, reset=True):
		return "\033[33m" + "".join(args) + "\033[0m" if reset else "\033[33m" + "".join(args)

	@staticmethod
	def Bold(*args, reset=True):
		return "\033[1m" + "".join(args) + "\033[0m" if reset else "\033[1m" + "".join(args)

def waitpoint():
    input(codes.Bold("Press <Enter> to continue..."))

try:
	import pyperclip as clp
except ModuleNotFoundError:
	print(codes.Error('Could not find module '), codes.Bold(codes.Error("pyperclip")), codes.Error(f' , run "pip3 install pyperclip" to enable the clipboard'), sep="")
	waitpoint()

class manager:
	def __init__(self):
		self.characters = list(string.printable[:-6])
		self.file_path = Path(Path(__file__).parent, "shadowed.lst") # Write here the name or the path of the file where the passwords will be save
		self.encoder = crypton.encoder()

	def read_passwds(self):
		with open(self.file_path, "r") as file:
			self.content = [line for line in file.read().split("\n") if line != ""]
			saved_sites = {url:passwd for url, passwd in [site_n_passwd.split(" = ") for site_n_passwd in self.content]}
		return saved_sites

	def new_passwd(self):
		length = int(input("Length of the password: "))
		password = ""

        #creates the password
		for i in range(length+1):
			char = random.choice(self.characters)
			password += char
		try:
			clp.copy(password)
			print(codes.No_errors("It has been already copied to your clipboard"))
		except:
			print(codes.Error('Either you do not have the '), codes.Bold(codes.Error("pyperclip")), codes.Error(', module or there has been an error copying the password to your clipboard'), sep="")
			print(codes.Caution(f'You can copy it manually though\nYour password is: {password}'))
    	#Saving the self.password
		while True:
			save = input("Do you want to save it or not(y, n): ")
			if save == "y":
				url = input("Write the URL: ")
				with open(self.file_path, "a") as f:
					f.write(f"\n{url} = {self.encoder.swap(password)}")
					f.close()
				print(codes.No_errors(f'it has been saved in "{self.file_path}"'))
				break
			elif save == 'n':
				print(codes.No_errors("Okay, thank you"))
				break
				exit()
			else:
				print(codes.Error(f'{save} it is not a valid response\nTry "y" for yes or "n" for no'))

	def show_passwds(self):
		saved_sites = self.read_passwds()
		print(codes.No_errors("+" + "-"*102, "+"))
		for url in saved_sites.keys():
			listURLs = saved_sites[url].strip('\n')
			print(codes.No_errors(f"+{url:^50}||{self.encoder.unswap(listURLs):^50}+"))
			print(codes.No_errors("+" + "-"*102 + "+"))
	
	def show_passwd(self, url):
		saved_sites = self.read_passwds()
		try:
			passwd = saved_sites[url].strip("\n")
			print(codes.No_errors("+" + "-"*102 + "+"))
			print(codes.No_errors(f"+{url:^50}||{self.encoder.unswap(passwd):^50}+"))
			print(codes.No_errors("+" + "-"*102 + "+"))
		except KeyError:
			print(codes.Error("No passwords saved for that URL"))

	def delete_site(self, url):
		while True:
			lastcall = input("Are you completely sure you want to delete it? It will not be reversible(y, n): ")
			if lastcall == "y":
				saved_sites = self.read_passwds()
				flag = False
				for idx, saved_site in enumerate(saved_sites):
					if url == saved_site:
						flag = True
						with open(self.file_path, "w") as file:
							self.content.pop(idx)
							file.write("".join([f"\n{line}" for line in self.content]))
				if not flag:
					print(codes.Error(f"No passwords saved for that URL\nNo changes were made in: {self.file_path}"))
				elif flag:
					print(codes.No_errors("Credentials deleted succesfully!"))
				break
			elif lastcall == "n":
				print(codes.No_errors("Perfect!"))
				break
			else:
				print(codes.Error('Invalid option: only valid options are "y" for yes or "n" for no'))
	
	def backup(self, bu_path):
		self.read_passwds()
		with open(bu_path, "w") as file:
			file.write("".join(self.content))
		print(codes.No_errors(f"Backup created at:\n{bu_path}"))
	
	def restore(self, bu_path):
		while True:
			lastcall = input(f"Are you sure you want to restore the data in {self.file_path} this will not be reversible and you will lose all the credentials that aren't saved in the backup file(y, n): ")
			if lastcall == "y":
				with open(bu_path, "r") as file:
					content = file.read()
				with open(self.file_path, "w") as file:
					file.write(content)
				print(codes.No_errors("Succesfully updated all of your credentials!"))
				break
			elif lastcall == "n":
				print(codes.No_errors("Perfect!"))
				break
			else:
				print(codes.Error('Invalid option: only valid options are "y" for yes or "n" for no'))


if __name__ == "__main__":
	manager = manager()