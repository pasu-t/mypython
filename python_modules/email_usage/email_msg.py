import smtplib
import os
from email.message import EmailMessage
# import imghdr

def send_email_attachement(list_files,list_contacts)
'''
This method will send the mail to list_contacts with attachments of list_files
''' 
	#contacts = ['pasupathi.thumburu@gmail.com']
	email_address= 'pasupathi.thumburu@gmail.com'
	email_password = os.environ.get('EMAIL_PSWD')
	msg = EmailMessage()
	msg.set_content('Files attached...')
	msg['Subject'] = 'Hey buddy check my files'
	msg['From'] = email_address
	msg['To'] = list_contacts
	files = list_files
	for file in files:
		with open(file, 'rb') as f:
			file_data = f.read()
			file_name = f.name
			msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

	with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
		smtp.login(email_address,email_password)
		smtp.send_message(msg)
