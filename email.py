import getpass, imaplib

M=imaplib.IMAP4_SSL('imap.gmail.com')

M.login('kevinwpalmer', "jsfern251634")
#IMAP4.select(readonly)

#Next do select,search, and fetch.