import md5
import pyfiglet

from termcolor import colored
from pyfiglet import figlet_format

print((colored(figlet_format("md5 popper"), color="blue")))
print((colored(figlet_format("By: AOD"), color="blue")))


counter = 1

pass_in = raw_input("Please enter the MD5 Hash: ")
pwfile = raw_input("Please enter the password file name: ")

try:
	pwfile = open(pwfile, "r")
except:
	print "\nFile Not Found."
	quit()

for password in pwfile:
	filemd5 = md5.new(password.strip()).hexdigest()
	print "Trying Wordlist Number  %d: %s " % (counter, password.strip())

	counter +=1

	if pass_in == filemd5:
		print "\nHash Located! \nHash's Plaintext: %s" % password
		break

else: print "/nWordlist Not Located."
