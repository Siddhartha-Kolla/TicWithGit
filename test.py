from tkinter import *
def name_extract(player1="Player1",player2="Player2"):

	root = Tk()
	root.geometry("675x400")
	root.resizable(False, False)
	root.title("Tic Tac Toe")
	photo = PhotoImage(file="images/logo.png")
	root.iconphoto(False, photo)

	wel_lbl = Label(root,text="Welcome to Tic Tac Toe game. Please enter your names.",font=('Arial', 13,"bold"))
	wel_lbl.place(relx=0.5,rely=0.1,anchor=CENTER)

	pler_lbl = Label(root,text="Players :",font=('Times New Roman', 13,"bold"))
	pler_lbl.place(relx=0.12+0.075,rely=0.4,anchor=CENTER)

	en_t1 = StringVar()
	en_box1 = Entry(root,textvariable=en_t1,font=('Times New Roman', 12))
	en_box1.place(relx=0.15+0.075+0.2,rely=0.4,anchor=CENTER)
	en_t1.set(player1)

	en_t2 = StringVar()
	en_box2 = Entry(root,textvariable=en_t2,font=('Times New Roman', 12))
	en_box2.place(relx=0.45+0.075+0.2,rely=0.4,anchor=CENTER)
	en_t2.set(player2)

	def submit():
		global name1,name2
		name1 = en_t1.get().strip()
		name1 = name1.replace(" ","")
		# print(name1[:15])
		name2 = en_t2.get().strip()
		name2 = name2.replace(" ","")
		# print(name2[:15])
		root.destroy()
		
	ok_btn = Button(root,text="Submit",font=("Arial",12,"bold"),command=submit)
	ok_btn.place(relx=0.5,rely=0.675,anchor=CENTER,width=100,height=35)


	root.mainloop()
	return (name1[:15],name2[:15])