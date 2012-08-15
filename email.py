import getpass, imaplib

M=imaplib.IMAP4('imap.gmail.com', '993')
M.login(getpass.getpass())
