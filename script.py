import time
from time import sleep
import os
import sys
from termcolor import colored





banner = """
               \033[0;32m▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞
               ▞▞    \033[31m𝗪𝗘𝗕    \033[0;32m▞▞
               ▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞ """

banner1 = """
               \033[0;32m▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞
               ▞▞  \033[31m𝐌𝐀𝐋𝐖𝐀𝐑𝐄  \033[0;32m▞▞
               ▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞ """

banner2 = """
               \033[0;32m▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞
               ▞▞ \033[31m𝐏𝐑𝐎𝐓𝐎𝐂𝐎𝐋𝐒 \033[0;32m▞▞
               ▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞ """

sleep(3.5)
print(colored("1. netdiscover\n2. Malware\n3. Protocols\n4. Web\n5. sysInfo\n6. imgInfo\n7. exit",'green'))
a = int(input('\033[36mEnter your choise : \033[0m'))

if a == 1:
	os.system("clear && python3 netdiscover.py")
	os.system("python3 script.py")
# -------------- Malware

if a == 2:
	os.system("clear")
	print ("  \t   \t    ",banner1,"\n \n")
	print(colored("1. linux-keylogger\n2. malware-cmd\n3. windows-keylogger.",'red'))
	d = int(input('\033[36mEnter your choise : \033[0m'))
	if d == 1:
		os.system("clear && python3 linux-keylogger.py")
		os.system("python3 script.py")
	if d == 2:
		os.system("clear && python3 malware-cmd.py")
		os.system("python3 script.py")
	if d == 3:
		os.system("clear && python3 windows-keylogger.py")
		os.system("python3 script.py")
# -------------- Protocols

if a == 3:
	os.system("clear")
	print ("  \t   \t    ",banner2,"\n \n")
	print(colored("1. checkFTPanonymousLogin\n2. ftp-bruteforce\n3. ssh-bruteforce.",'red'))
	f = int(input('\033[36mEnter your choise : \033[0m'))
	if f == 1:
		os.system("clear && python3 checkFTPanonymousLogin.py")
		os.system("python3 script.py")
	if f == 2:
		os.system("clear && python3 ftp-bruteforce.py")
		os.system("python3 script.py")
	if f == 3:
		os.system("clear && python3 ssh-bruteforce.py")
		os.system("python3 script.py")
# -------------- Web

if a == 4:
	os.system("clear")
	print ("  \t   \t    ",banner,"\n \n")
	print(colored("1. Site_Tester\n2. XssTester\n3. admin_panel_finder\n4. dos\n5. get_emails_from_url\n6. get_links_from_url\n7. lfi_tester\n8. phpmailer_checker\n9. shodan-prod\n10. XSS\n0. exit",'red'))
	g = int(input('\033[36mEnter your choise : \033[0m'))
	if g == 1:
		os.system("clear && python3 Site_Tester.py")
		os.system("python3 script.py")
	if g == 2:
		os.system("clear && python3 XssTester.py")
		os.system("python3 script.py")
	if g == 3:
		os.system("clear && python3 admin_panel_finder.py")
		os.system("python3 script.py")
	if g == 4:
		os.system("clear && python3 dos.py")
		os.system("python3 script.py")
	if g == 5:
		os.system("clear && python3 get_emails_from_url.py")
		os.system("python3 script.py")
	if g == 6:
		os.system("clear && python3 get_links_from_url.py")
		os.system("python3 script.py")
	if g == 7:
		os.system("clear && python3 lfi_tester.py")
		os.system("python3 script.py")
	if g == 8:
		os.system("clear && python3 phpmailer_checker.py")
		os.system("python3 script.py")
	if g == 9:
		os.system("clear && python3 shodan-prod.py")
		os.system("python3 script.py")
	if g == 10:
		os.system("clear && python3 XSS.py")
		os.system("python3 script.py")
	if g == 0:
		os.system("clear && cd ")
# -------------- sysInfo
if a == 5:
	os.system("clear && python3 sysInfo.py")
	os.system("python3 script.py")
if a == 6:
	os.system("clear && python3 img.py")
	os.system("python3 script.py")
# -------------- exit

if a == 0:
	os.system("clear && cd ")

