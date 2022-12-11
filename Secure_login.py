import hashlib
import os
import getpass
from termcolor import colored, cprint
import time
import datetime

class App:
	def __init__(self,boot):

		self.cred = f"/home/{getpass.getuser()}/.secure-login/credentials.key"
		self.prt_key = f"/home/{getpass.getuser()}/.secure-login/private.key"

		self.direc = f"/home/{getpass.getuser()}/.secure-login"
		self.boot = boot
		if boot:
			self.get_user()
		else:
			self.add_new_user()

	def get_user_details(self):
		uname = colored("Username : ","green",attrs=["bold"])
		pwd = colored("Password : ","green",attrs=["bold"])
		username = input(uname)
		passwd = input(pwd)
		return username,passwd

	def get_user(self):
		uname,pwd = self.get_user_details()
		self.check_password(pwd)

	def add_new_user(self):
		cprint("# Add New User","green",attrs=["bold"])
		uname,pwd = self.get_user_details()
		hashed_pwd,algo = self.hash_algo(pwd)

		with open("credentials.key","a") as credentials:
			credentials.write(f"{uname} {hashed_pwd} {algo}\n")

	def check_password(self,pwd):
		hashed_pwd = self.hash_algo(pwd)
		with open(self.cred,'rb') as pk:
			print(pk.read(),"\n",pwd)

	def hash_algo(self,pwd):
		cprint("# Choose the Algorithm Sequences : ","green",attrs=["bold"])
		print("1. SHA256\n2. SHA384\n3. MD5")
		seq = colored("[#] : ","white",attrs=["bold"])
		algo = ""
		while True:
			algo = input(seq)
			for i in algo.split(""):
				if i>3:
					cprint("# Please Enter Right Sequence","red",attrs=["bold"])
			break
		
		hashed_pwd = self.hash_password(pwd,algo)

		return hashed_pwd,algo

	def hash_password(self,pwd,algo):
		result_hash = pwd
		algo_sequence = algo.split("")
		for i in algo_sequence:
			if i == 1:
				result_hash = self.hash_pwd_sha256(result_hash)
			elif i==2:
				result_hash = self.hash_pwd_sha384(result_hash)
			elif i==3:
				result_hash = self.hash_pwd_md5(result_hash)
		return result_hash


	def hash_pwd_sha384(self,pwd):
		return hashlib.sha384(pwd.encode('utf-8')).hexdigest()

	def hash_pwd_md5(self,pwd):
		return hashlib.md5(pwd.encode('utf-8')).hexdigest()

	def hash_pwd_sha256(self,pwd):
		return hashlib.sha256(pwd.encode('utf-8')).hexdigest()
		





def startup():
	user = getpass.getuser()
	base = f"/home/{user}/.secure-login"
	base_file = f"/home/{user}/.secure-login/credentials.key"
	if (os.path.isdir(base) == False):
		os.mkdir(f"/home/{user}/.secure-login")
		cprint("# [Initializing Directory] : ","green",attrs=["bold"],end="")
		cpcrint(" Success","white",attrs=["bold"])
	if (os.path.isfile(base_file)==False):
		return False
	return True


def main():
	print(
		"""	

         _______ _       _______ _______ _______ _______   ________________                 
|\     /(  ____ ( \     (  ____ (  ___  |       |  ____ \  \__   __(  ___  )                
| )   ( | (    \/ (     | (    \/ (   ) | () () | (    \/     ) (  | (   ) |                
| | _ | | (__   | |     | |     | |   | | || || | (__         | |  | |   | |                
| |( )| |  __)  | |     | |     | |   | | |(_)| |  __)        | |  | |   | |                
| || || | (     | |     | |     | |   | | |   | | (           | |  | |   | |                
| () () | (____/\ (____/\ (____/\ (___) | )   ( | (____/\     | |  | (___) |                
(_______|_______(_______(_______(_______)/     \(_______/     )_(  (_______)                
                                                                                            
 _______ _______ _______         _______ _______    _       _______ _________________       
(  ____ (  ____ (  ____ \\     /(  ____ |  ____ \  ( \     (  ___  |  ____ \__   __( (    /|
| (    \/ (    \/ (    \/ )   ( | (    )| (    \/  | (     | (   ) | (    \/  ) (  |  \  ( |
| (_____| (__   | |     | |   | | (____)| (__      | |     | |   | | |        | |  |   \ | |
(_____  )  __)  | |     | |   | |     __)  __)     | |     | |   | | | ____   | |  | (\ \) |
      ) | (     | |     | |   | | (\ (  | (        | |     | |   | | | \_  )  | |  | | \   |
/\____) | (____/\ (____/\ (___) | ) \ \_| (____/\  | (____/\ (___) | (___) |__) (__| )  \  |
\_______|_______(_______(_______)/   \__(_______/  (_______(_______|_______)_______//    )_)
                                                                                            

		"""
		)
	boot = startup()
	cprint(f"# [Shell Accessed] {datetime.datetime.now()}","blue",attrs=["bold"])
	if boot:
		cprint("# Please Login","white",attrs=["bold"])
	else:
		cprint("# No User Found","red",attrs=["bold"])	

	App(boot)

if __name__ == '__main__':
	main()















