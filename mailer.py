import csv
import smtplib
 
def sendemail(from_addr, to_addr_list, cc_addr_list,
			  subject, message,
			  login, password,
			  smtpserver='smtp.gmail.com:587'):
	header  = 'From: %s\n' % from_addr
	header += 'To: %s\n' % ','.join(to_addr_list)
	header += 'Cc: %s\n' % ','.join(cc_addr_list)
	header += 'Subject: %s\n' % subject
	message = header + message
 
	server = smtplib.SMTP(smtpserver)
	server.starttls()
	server.login(login,password)
	problems = server.sendmail(from_addr, to_addr_list, message)
	server.quit()


# Program execution starts from here

message_list = []

# Read all message data from the csv file.
with open('content.csv', 'rb') as b:
	messages = csv.reader(b)
	message_list.extend(messages)

receipients = []

# Read list of receipients
with open('receipients.csv', 'rb') as b:
	receivers = b.readlines()
	for receiver in receivers:
		receipients.extend(receiver.split())


# Sending E-Mail
for message_row in message_list:
	if len(message_row) == 1:
		# trying to send a mail
		try:
			sendemail(from_addr    = '', 
                      to_addr_list = receipients,
                      cc_addr_list = [], 
                      subject      = 'Howdy', 
                      message      = message_row[0], 
                      login        = '', 
                      password     = '')

			message_row.append('mail sent')
		except Exception as e:
			raise e
		break

with open('content.csv', 'wb') as b:
	writer = csv.writer(b)
	writer.writerows(message_list)