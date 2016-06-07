# Bigchain GUI

from tkinter import *

import os
import subprocess
import time

class Application(Frame):
	
	def __init__(self, master):

		Frame.__init__(self, master)
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		
		# Create 1st button
		self.button1 = Button(self, text = "Start Bigchain")
		self.button1["command"] = self.start_bigchain
		self.button1.grid(row=50, column=5)
		

		# Create 2nd button
		self.button2 = Button(self, text = "Load transactions")
		self.button2["command"] = self.load_transactions
		self.button2.grid(row=50, column=9)
	
	def start_bigchain(self):
	
		print("Starting RethinkDB")
		subprocess.call(['gnome-terminal', '-x', 'rethinkdb'])

		time.sleep(10)

		print("Starting Bigchain")
		subprocess.Popen(args=["gnome-terminal","--command= bigchaindb start"])

	def load_transactions(self):

		print("Loading Test Transactions... \nGo to 'localhost:8080'\n ")	
		os.system('bigchaindb load')


root = Tk()
root.title("Bigchain GUI")
root.geometry("500x200")

T= Text(root,height=5, width=80)
T.grid()
text = "1. Click 'Start Bigchain': This starts RethinkDB followed by Bigchain. \n \n \n2. Click 'Load Transaction': This will load test transactions. \n "
T.insert(END, text)

app = Application(root)

root.mainloop()


