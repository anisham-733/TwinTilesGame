from tkinter import *
import random
from tkinter import messagebox
import pygame
from PIL import ImageTk,Image
root=Tk()
root.title('Twin Tiles Game')
root.configure(background='#101B37')
root.geometry('600x550')


global winner,matches,mylabel
matches=[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]
random.shuffle(matches)

winner=0
#button frame
my_frame=Frame(root)
my_frame.pack(pady=10)

count=0
ans_list=[]
ans_dict={}
c=0
def button_click(b,number):
	global count,c,ans_list,ans_dict,winner

	if b["text"]==" " and count<2:
		b['text']=matches[number]
		#add number to list
		ans_list.append(number)
		#add number to dict in key value
		ans_dict[b]=matches[number]

		#increment
	count+=1
	# print(ans_list)
	
	if len(ans_list)==2:
		
		if matches[ans_list[0]]==matches[ans_list[1]]:
			c+=1
			mylabel.config(text=' Its a MATCH..! '+str(c)+' time')
			mylabel.pack(pady=20)
			for key in ans_dict:
				key["state"]="disabled"
			count=0
			
			ans_list=[]
			ans_dict={}
			winner+=1
			if winner==8:
				win()

		else:
			mylabel.pack(pady=20)
			if mylabel.winfo_exists()==1:
				mylabel.config(text="Incorrect match",background='#01C8EE')

				count=0
				ans_list=[]
				messagebox.showinfo('At odds','Incorrect match')
				restart()

	
			
def win():
	mylabel.config(text="Congratulations ..! All the tiles have been matched.You won.!",background="#E41376")
	button_list=[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16]
	for button in button_list:
		button.config(bg="#01C8EE")
def restart():
	mylabel.pack_forget()

	print(mylabel.winfo_exists())
	global ans_dict

	for key in ans_dict:
			key["text"]=" "
	
	ans_dict={}

def new():
	global matches,winner,c
	winner=0
	c=0
	
	matches=[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]
	random.shuffle(matches)
	mylabel.config(text=" ")
	button_list=[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16]
	for button in button_list:
		button.config(text=" ",bg='#E41376',state="normal")
pygame.mixer.init()
def sound():

	pygame.mixer.music.load("/home/lag3rl0f/Major-lazer-cold-water-instrumentalfx.mp3")
	pygame.mixer.music.play(loops=0)
def stop():
	pygame.mixer.music.stop()

b1=Button(my_frame,text=" ",font=('Helvetica',20),background='#E41376',foreground='#01C8EE',activebackground='#E41376',height=3,width=6,command =lambda: button_click(b1,0))
b2=Button(my_frame,text=" ",font=('Helvetica',20),background='#E41376',foreground='#01C8EE',activebackground='#E41376',height=3,width=6,command =lambda : button_click(b2,1))
b3=Button(my_frame,text=" ",font=('Helvetica',20),background='#E41376',foreground='#01C8EE',activebackground='#E41376',height=3,width=6,command =lambda : button_click(b3,2))
b4=Button(my_frame,text=" ",font=('Helvetica',20),background='#E41376',foreground='#01C8EE',activebackground='#E41376',height=3,width=6,command =lambda : button_click(b4,3))
b5=Button(my_frame,text=" ",font=('Helvetica',20),background='#E41376',foreground='#01C8EE',activebackground='#E41376',height=3,width=6,command =lambda : button_click(b5,4))
b6=Button(my_frame,text=" ",font=('Helvetica',20),background='#E41376',foreground='#01C8EE',activebackground='#E41376',height=3,width=6,command =lambda : button_click(b6,5))
b7=Button(my_frame,text=" ",font=('Helvetica',20),background='#E41376',foreground='#01C8EE',activebackground='#E41376',height=3,width=6,command =lambda : button_click(b7,6))
b8=Button(my_frame,text=" ",font=('Helvetica',20),background='#E41376',foreground='#01C8EE',activebackground='#E41376',height=3,width=6,command =lambda : button_click(b8,7))
b9=Button(my_frame,text=" ",font=('Helvetica',20),background='#E41376',foreground='#01C8EE',activebackground='#E41376',height=3,width=6,command =lambda : button_click(b9,8))
b10=Button(my_frame,text=" ",font=('Helvetica',20),background='#E41376',foreground='#01C8EE',activebackground='#E41376',height=3,width=6,command =lambda : button_click(b10,9))
b11=Button(my_frame,text=" ",font=('Helvetica',20),background='#E41376',foreground='#01C8EE',activebackground='#E41376',height=3,width=6,command =lambda : button_click(b11,10))
b12=Button(my_frame,text=" ",font=('Helvetica',20),background='#E41376',foreground='#01C8EE',activebackground='#E41376',height=3,width=6,command =lambda : button_click(b12,11))
b13=Button(my_frame,text=" ",font=('Helvetica',20),background='#E41376',foreground='#01C8EE',activebackground='#E41376',height=3,width=6,command =lambda : button_click(b13,12))
b14=Button(my_frame,text=" ",font=('Helvetica',20),background='#E41376',foreground='#01C8EE',activebackground='#E41376',height=3,width=6,command =lambda : button_click(b14,13))
b15=Button(my_frame,text=" ",font=('Helvetica',20),background='#E41376',foreground='#01C8EE',activebackground='#E41376',height=3,width=6,command =lambda : button_click(b15,14))
b16=Button(my_frame,text=" ",font=('Helvetica',20),background='#E41376',foreground='#01C8EE',activebackground='#E41376',height=3,width=6,command =lambda : button_click(b16,15))
b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)
b4.grid(row=0,column=3)
b5.grid(row=1,column=0)
b6.grid(row=1,column=1)
b7.grid(row=1,column=2)
b8.grid(row=1,column=3)
b9.grid(row=2,column=0)
b10.grid(row=2,column=1)
b11.grid(row=2,column=2)
b12.grid(row=2,column=3)
b13.grid(row=3,column=0)
b14.grid(row=3,column=1)
b15.grid(row=3,column=2)
b16.grid(row=3,column=3)

mylabel=Label(root,text=" ",background='#101B37')
mylabel.pack(pady=25)

my_menu=Menu(root,background='#101B37',foreground='#01C8EE')
root.config(menu=my_menu)

#add options menu
options_menu=Menu(my_menu,tearoff=False,background='black',foreground='#01C8EE')
my_menu.add_cascade(label='Options',menu=options_menu)

#add sub menu
options_menu.add_command(label='New Game',command=new)
# option_menu.add_separator()
options_menu.add_command(label='Exit game',command=root.quit)

# my_img=PhotoImage())
img=ImageTk.PhotoImage(Image.open("/home/lag3rl0f/speakerr.png"))
img_button=Button(root,image=img,command=sound,background='#101B37')
img_button.place(relx=0.87,rely=0.84,relheight=0.12,relwidth=0.12)

stop=Button(root,text="Stop playing",borderwidth=0,font=('Helvetica',8),background='#101B37',foreground='#01C8EE',command=stop)
stop.place(relx=0.87,rely=0.96,relheight=0.05,relwidth=0.15)
root.mainloop()
