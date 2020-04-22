import smtplib, ssl

class Emails:

	def __init__(self):
		self.port     = 465  # For SSL
		self.password = 'greenhouse1904$'
		self.context  = ssl.create_default_context()
		self.sender   = "noreplygreenhouse@gmail.com"
		self.receiver = 'guillermo.alvarez@fiexact.com'

	def sendEmail(self, subject, message):
		with smtplib.SMTP_SSL("smtp.gmail.com", port=self.port, context=self.context) as server:
			server.login(self.sender, self.password)
			email = f"From: {self.sender}\nTo: {self.receiver}\nSubject: {subject}\n\n{message}"
			server.sendmail(self.sender, self.receiver, email)