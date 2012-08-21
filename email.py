import getpass, imaplib, code

T=code.InteractiveConsole()
username=T.raw_input('Username:')
M=imaplib.IMAP4_SSL('imap.gmail.com')
M.login(username, getpass.getpass())
M.select()
searchfor=T.raw_input('What do you want to search your inbox for?')
M.search(None,'searchfor')
#M.create('c:\python27\mailboxdata')
#M.copy('1,4','c:\python27\mailboxdata')

#typ, msgnums = M.search(None, 'From', '"Jessica"')
#A=M.fetch("(PW)")
#print x
#What is message_set??The message_set options to commands below 
#is a string specifying one or more messages to be acted upon. 
#It may be a simple message number ('1'), a range of message numbers ('2:4')
#, or a group of non-contiguous ranges separated by commas ('1:3,6:9').
 #A range can contain an asterisk to indicate an infinite upper bound 
 #('3:*').

#What about M.check(),
#Next do select,search, and fetch.