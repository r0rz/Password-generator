# Password generator test python program
# Made by @r0rz_

from random import SystemRandom
import sys
from time import sleep

# list of words
lower_list=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
upper_list=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
# To complex list below
# chars=["!","@","#","$","~","€","%","&","/","(",")","=","?","¿","·",'"',"'","ª","º","*","-","+",",",".",";",":","`","^","[","]","{","}","<",">"]
chars=["!","@","#","$","=","?","¿","*","-","+",";",":","[","]","{","}","<",">"]
numbers=["0","1","2","3","4","5","6","7","8","9"]

counts=int(input("How many characters do you want? (ex.: 22)\n>>> "))

# The function that picks randomly from the lists from above
def generate(word_count=counts):
	try:
		sleep(0.5)
		print(''.join(SystemRandom().sample(lower_list+upper_list+chars+numbers, word_count)))
		input()
		print(generate())
	
	except KeyboardInterrupt:
		print("\nCtrl+C was pressed by user....\n")
		sys.exit()

if counts > 87:
	print("Number is to big to generate such a random key.")
	sys.exit()
elif counts < 10:
	ok=input("Password is too week. Are you sure you want to continue?\n>>> ")
	d = ['y','yes']
	while True:
		if ok in d:
			print(generate())
		else:
			print("Exiting then...")
			sys.exit()
else:
	print("Creating random characters:\nPress enter after every generated key to create a new one...\n")

print(generate())
