import smtplib

def Email(reciever, emailBody):
	emailBody = "\n" + emailBody
	fromaddr = 'FROMADDRESS@FAKEEMAIL.COM'
	toaddrs  = reciever
	username = 'YOUREMAILACCOUNT@FAKEEMAIL.COM'
	password = 'PASSWORDFOREMAILACCOUNT'
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.ehlo()
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr, toaddrs, emailBody)
	server.quit()