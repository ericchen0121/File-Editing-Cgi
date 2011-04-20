#!c:\python27\python.exe

print 'Content-type: text/html\n'

from os.path import join, abspath
import cgi, sha, sys

BASE_DIR = abspath('data')

form = cgi.FieldStorage()

text = form.getvalue('text')
filename = form.getvalue('filename')
password = form.getvalue('password')

if not (filename and text and password):
    print 'Something\'s not right. Check the filename or password (or textbox area).'
    sys.exit()

if sha.sha(password).hexdigest() != '7110eda4d09e062aa5e4a390b0a572ac0d2c0220': 
    print 'That\'s not the correct password. Press back and try again.'
    sys.exit()

print 'Password accepted.'

# if the password matches, it will now save to the file
f = open(join(BASE_DIR, filename), 'w')
f.write(text)
f.close()

print 'Completed saving text to the file.'

