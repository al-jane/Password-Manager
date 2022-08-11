from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import hashlib
import sqlite3
import json


def window():
	def manage_passwd():

		def listings(event):

			
			selected = []


			for i in listbox.curselection():
				selected.insert(i, listbox.get(i))
				
			for index in selected:
				platform_1 = index

				connection = sqlite3.connect('datas.db')
				c = connection.cursor()

				c.execute("SELECT * FROM user WHERE platform=(?)",(platform_1))
				data = c.fetchall()
				
				c.execute("SELECT email FROM user WHERE platform=(?)",(platform_1))
				email = c.fetchall()
				

				c.execute("SELECT username FROM user WHERE platform=(?)",(platform_1))
				username = c.fetchall()

				c.execute("SELECT password FROM user WHERE platform=(?)",(platform_1))
				password = c.fetchall()

				c.execute("SELECT platform FROM user WHERE platform=(?)",(platform_1))
				platform = c.fetchall()

				
				columns = ['USERNAME','PASSWORD','EMAIL']


				
				global total_columns
				total_columns = len(columns)
				total_rows = len(data)

				
							
							
				
				
				
				# MAIN FRAME
				frame = Frame(passwd, width=660, height=600, bd=1, bg="#9a7b78")

				# USERNAME FRAME
				frame_username = LabelFrame(frame, width=210, height=600,bd=1, text="USERNAME",bg="#9a7b78")

				# EMAIL FRAME
				frame_email = LabelFrame(frame, width=215, height=600,bd=1, text="EMAIL", bg="#9a7b78")

				# PASSWORD FRAME

				frame_password = LabelFrame(frame, width=210, height=600, bd=1, text="PASSWORD", bg="#9a7b78")



				
				rows = len(username)





				

				for i in range(rows):
					
					username_ = Label(frame_username, text=(''.join(username[i])), font=("Constantina",10),anchor='w',bg="#9a7b78", fg="#3b2621")
					username_.pack()

					email_ = Label(frame_email, text=''.join(email[i]),font=("Constantina",10),anchor='w', bg="#9a7b78",fg="#3b2621")
					email_.pack()

					password_ = Label(frame_password, text=''.join(password[i]),font=("Constantina",10),anchor='w', bg="#9a7b78", fg="#3b2621")
					password_.pack()

					

				frame.place(x=690,y=70)
				frame.pack_propagate(0)

				frame_username.place(x=1,y=1)
				frame_username.pack_propagate(0)

				frame_email.place(x=219,y=1)
				frame_email.pack_propagate(0)

				frame_password.place(x=440,y=1)
				frame_password.pack_propagate(0)

			

		passwd = Tk()
		passwd.config(background="#9f8c86")
		passwd.state('zoomed')
		passwd.title("PASSWORD MANAGER")
		passwd.iconbitmap('favicon.ico')
		#passwd.iconphoto(False, photo_icon2)

		title_label = Label(passwd, text="USER'S DATA",font=("JMHTypewriter-Regular",30),bg="#9f8c86",
		fg="#3b2621",padx=10,pady=5)
		title_label.pack()

		connection = sqlite3.connect('datas.db')
		c = connection.cursor()
		c.execute("SELECT platform FROM user")
		platform = c.fetchall()

		listbox = Listbox(passwd,
			bg="#9a7b78",
			fg="#3b2621",
			font=("Constantina", 30),
			width=29,
			selectmode=SINGLE,
			)
		listbox.place(x=30, y=70)

		passwd.bind("<Button-1>", listings)


		

		pltforms = set(platform)
		num = 0
		for i in pltforms:
			num = num + 1
			listbox.insert(num, i)



		passwd.mainloop()
	def create_pass():
		user_var = StringVar()
		pass_var = StringVar()
		email_var = StringVar()
		platform_var = StringVar()



		def saved():




			
			username1 = user_var.get()
			password1 = pass_var.get()
			email = email_var.get()
			platform1 = platform_var.get()

			

			conn = sqlite3.connect('datas.db')

			c = conn.cursor()

			c.execute("""CREATE TABLE IF NOT EXISTS user(
				platform text NOT NULL,
				username text NOT NULL,
				email text NOT NULL,
				password text NOT NULL)""")

			c.execute("""INSERT INTO user (
						platform,
						username,
						email,
						password)
						VALUES
						(?,?,?,?)""",(platform1, username1, email, password1))

			conn.commit()
			c.close()



		canva = Canvas(first_window,height=300,width=500)
		canva.config(bg="#9a7b78",highlightbackground="#9f8c86")
		


		canva.create_text(90,60,text="Username:", font=("JMHTypewriter-Regular",20))
		username_entry = Entry(first_window, textvariable=user_var,font=("JMHTypewriter-Regular",20),bg="#9f8c86").place(x=220,y=290)
		

		canva.create_text(90,110,text="Password:", font=("JMHTypewriter-Regular",20))
		password_entry = Entry(first_window, textvariable=pass_var,font=("JMHTypewriter-Regular",20),bg="#9f8c86").place(x=220,y=340)

		canva.create_text(115,160,text="Email:", font=("JMHTypewriter-Regular",20))
		email_entry = Entry(first_window, textvariable=email_var,font=("JMHTypewriter-Regular",20),bg="#9f8c86").place(x=220,y=390)

		canva.create_text(93,210,text="Platform:", font=("JMHTypewriter-Regular",20))
		platform_entry = Entry(first_window, textvariable=platform_var,font=("JMHTypewriter-Regular",20),bg="#9f8c86").place(x=220,y=440)

		save = Button(first_window, text="Save",
			font=("JMHTypewriter-Regular",10),
			fg="#3b2621", 
			bg="#9f8c86",
			command=saved).place(x=480,y=500)

		delete = Button(first_window, text="reset",
			font=("JMHTypewriter-Regular",10),
			fg="#3b2621", 
			bg="#9f8c86",
			command=create_pass).place(x=410,y=500)

		
		canva.place(x=50,y=250)


	first_window = Tk()
	first_window.iconbitmap('favicon.ico')
	first_window.title("Passworrd Manager")
	first_window.geometry("600x600")
	first_window.config(bg="#9f8c86")
	first_window.resizable(False,False)


	title = Label(first_window, 
		text="PASSWORD MANAGER", 
		font=("Top Secret",40),
		fg="#3b2621", 
		bg="#9f8c86",
		pady=20,
		padx=20)
	title.place(x=1,y=30)

	create = Button(first_window,
		text="Create new one",
		font=("JMHTypewriter-Regular",15),
		fg="#3b2621", 
		bg="#f0eae7",
		pady=20,
		padx=20,
		command=create_pass).place(x=50,y=150)

	manage_password = Button(first_window, 
		text="Manage Passwords",
		font=("JMHTypewriter-Regular",15),
		fg="#3b2621", 
		bg="#f0eae7",
		pady=20,
		padx=20,
		command=manage_passwd).place(x=325,y=150)



	first_window.mainloop()




	



welcome = Tk()
welcome.iconbitmap('favicon.ico')
welcome.title("WELCOME")
welcome.config(bg="#9f8c86")

def reset():
	reset = Toplevel()
	reset.geometry("200x200")

	Q1 = "question.txt"
	A1 = "answer.txt"

	with open(Q1, 'r') as f:
		question = f.read()

	global label1
	label1 = Label(reset, text=f"{question}", font=("JMHTypewriter-Regular",10),
				fg="#3b2621")
	label1.pack()

	answer0 = StringVar()

	global answer
	answer = Entry(reset,font=("JMHTypewriter-Regular",20),textvariable=answer0)
	answer.pack()
	

	


	def check_if_correct(event):
		full1 = answer0.get()
		full = full1.encode()
		hashed = hashlib.blake2s(full).hexdigest()
		with open(A1, 'r') as f:
			real = f.read()
			yours = hashed
			if real == yours:
				def save():
					file = "main_password.json"
					with open(file,'w') as f:
						full = new.get()
						json.dump(full, f)
						f.close()
					with open(file) as x:
						contents = json.load(x)
						tobe = contents.encode()
						hashed = hashlib.blake2s(tobe).hexdigest()
					with open(file, 'w') as i:
						json.dump(hashed, i)
					reset.destroy()

				new = StringVar()

				label1.config(text="NEW PASSWORD:",font=("JMHTypewriter-Regular",20))
				# Label(reset, text="NEW PASSWORD:", font=("JMHTypewriter-Regular",20)).pack()
				answer.config(font=("JMHTypewriter-Regular",20),textvariable=new)
				new_pass = Entry(reset,font=("JMHTypewriter-Regular",20),textvariable=new)
				
				# new_pass.pack()

				Button(reset, text="SAVED NEW PASSWORD",font=("JMHTypewriter-Regular",10),padx=5,pady=5,command=save).pack()

			else:
				pass



	reset.bind("<Return>", check_if_correct)



answer_ = StringVar()
question_ = StringVar()
def keyanswer():
	keyanswer = Toplevel()
	keyanswer.geometry("600x400")


	Label(keyanswer, text="A MUST:",
		font=("JMHTypewriter-Regular",25),
			fg="#3b2621").pack()
	Label(keyanswer, text="make your own question and answer,",
		font=("JMHTypewriter-Regular",15),
			fg="#3b2621").pack()

	Label(keyanswer, text="this is needed to be able to reset your password.",
		font=("JMHTypewriter-Regular",15),
			fg="#3b2621").pack()



	Label(keyanswer, text="Enter your question:",font=("JMHTypewriter-Regular",10),
			fg="#3b2621").pack()

	
	question = Entry(keyanswer,
	font=("JMHTypewriter-Regular",20),textvariable=question_).pack()

	Label(keyanswer, text="Enter your answer:",font=("JMHTypewriter-Regular",10),
			fg="#3b2621").pack()

	
	answer = Entry(keyanswer,
	font=("JMHTypewriter-Regular",20),textvariable=answer_).pack()

	def save():
		Q1 = "question.txt"
		A1 = "answer.txt"
		if (os.path.exists(Q1)) == False:
			with open(Q1, 'w') as f:
				question = question_.get()
				f.write(f"{question}")
			f.close()
			with open(A1, 'w') as i:
				answer = answer_.get()
				i.write(f"{answer}")
			with open(A1, 'r') as x:
				contents = x.read()
				tobe = contents.encode()
				hashed = hashlib.blake2s(tobe).hexdigest()
				with open(A1, 'w') as e:
					e.write(hashed)
				keyanswer.destroy()

		else:
			pass

	submit = Button(keyanswer, text="submit",font=("JMHTypewriter-Regular",10),padx=5,pady=5,command=save)
	submit.pack()

	
	






def access(event):


	file = "main_password.json"
	question2 = "question.txt"
	answer2 = "answer.txt"
	if (os.path.exists(file)) != True:
		with open(file,'w') as f:
			full = your_password.get()
			json.dump(full, f)
			f.close()
			with open(file) as x:
				contents = json.load(x)
				tobe = contents.encode()
				hashed = hashlib.blake2s(tobe).hexdigest()
				with open(file, 'w') as i:
					json.dump(hashed, i)
				if (os.path.exists(question2)) == False:
					if (os.path.exists(answer2)) == False:
						keyanswer()
				

	elif (os.path.exists(file)) == True:
		if (os.path.exists(question2)) == True:
			if (os.path.exists(answer2)) == True:

				full1 = your_password.get()
				full = full1.encode()
				hashed = hashlib.blake2s(full).hexdigest()
				with open(file) as f:
					real = json.load(f)
					yours = hashed
					if real == yours:
						welcome.destroy()

						window()
					else:
						messagebox.askretrycancel(title="WRONG PASSWORD", message="You entered incorrect password, please try again or click 'forget' if you want to reset it.")





your_password = StringVar()

Label(welcome,
	text="Welcome!",
	font=("JMHTypewriter-Regular",50),
	bg="#9f8c86",
	fg="#3b2621").pack()

hello = Label(welcome,
	text="""Let's set up things first before we proceed.
	\nThe first password and email that you will enter here will 
	\nalways be your password from now on.""",
	font=("JMHTypewriter-Regular",10),
	bg="#9f8c86",
	fg="#3b2621").pack()

Label(welcome,
	text="PASSWORD:",
	font=("JMHTypewriter-Regular",10),
	bg="#9f8c86",
	fg="#3b2621",
	pady=10).pack()

new_password = Entry(welcome,
	font=("JMHTypewriter-Regular",20),
	bg="#9a7b78",
	show = "*",
	textvariable=your_password).pack()

reset = Button(welcome,
	text="reset",
	font=("JMHTypewriter-Regular",10),
	bg="#9f8c86",
	fg="#3b2621",
	command=reset)

reset.pack()


Label(welcome,
	text="hit enter if you're done.",
	bg="#9f8c86",
	fg="#3b2621",
	pady=10).pack()

welcome.bind("<Return>", access)
welcome.mainloop()
