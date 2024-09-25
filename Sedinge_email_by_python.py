import smtplib

my_email = "swarupspacetech@gmail.com"
password = "sahpyuzrzcgxbycy"

"""Creating object for the Simple Mail Transport Protocol"""
connection = smtplib.SMTP("smtp.gmail.com")

"""Establishing the security (Transport Layer Security)"""
connection.starttls()

"""log into the gmail"""
connection.login(user=my_email, password=password)

"""Sending mail"""
connection.sendmail(from_addr=my_email, to_addrs="aasiandme@gmail.com", msg=
"Subject:Hi there..!\n\nThis is the body of email")
connection.close()









