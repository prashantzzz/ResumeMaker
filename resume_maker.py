#  'Resume Maker' Source Code:

#importing modules
from tkinter import *
import time, webbrowser
from copy import deepcopy

#creating GUI window
root= Tk()
#root.overrideredirect(1)
root.geometry('600x680+160+30')

colourlist=['#005c57','#044721','#82053f','#048a83','#121212','#453f3f','#00185e']
#                                                   deeppink                       black
bgcolour=colourlist[0]

root.config(bg=bgcolour)
root.title('Resume maker')

#setting up variables and images
x_bigcircle=400;y_bigcircle=80
x_circle=30;y_circle=10
image3=PhotoImage(file='circle.png');bigcircle=Label(image=image3,bg=bgcolour)
bigcircle.place(x=x_bigcircle,y=y_bigcircle)
image2=PhotoImage(file='circle2.png');circle=Label(image=image2,bg=bgcolour)
circle.place(x=x_circle,y=y_circle)
image1=PhotoImage(file='img.png');mypic=Label(image=image1)
mypic.grid(row=0,padx=200)
colourpic=PhotoImage(file='colour.png')

#to quit
def leave():
    global effect_run
    effect_run=False
    root.destroy()
root.protocol("WM_DELETE_WINDOW",leave)

def facebook():
    webbrowser.open('http://facebook.com//prashant')


#Default values
home_selected=True
about_selected=False
fun_selected=False
#Binding events for hover and leave button animations:
def home_hover(button):
  if home_selected==False:
    home.config(bg='#29ff2c',fg=bgcolour)
    
def home_leave(button):
  if home_selected==False:
    home.config(fg='#29ff2c',bg=bgcolour)

def about_hover(button):
  if about_selected==False:
    about.config(bg='#29ff2c',fg=bgcolour)
    
def about_leave(button):
  if about_selected==False:
    about.config(fg='#29ff2c',bg=bgcolour)
  
def fun_hover(button):
  if fun_selected==False:
    fun.config(bg='#29ff2c',fg=bgcolour)
  
def fun_leave(button):
  if fun_selected==False:
    fun.config(fg='#29ff2c',bg=bgcolour)
   
#functions for click button animations:
def home_click():
    global home_selected,about_selected,fun_selected
    home_selected=True
    about_selected=fun_selected=False
    home.config(bg='#29ff2c',fg=bgcolour)
    about.config(fg='#29ff2c',bg=bgcolour)
    fun.config(fg='#29ff2c',bg=bgcolour)
    home_action()
    
def about_click():
    global about_selected,home_selected,fun_selected
    about_selected=True
    home_selected=fun_selected=False
    home.config(fg='#29ff2c',bg=bgcolour)
    about.config(bg='#29ff2c',fg=bgcolour)
    fun.config(fg='#29ff2c',bg=bgcolour)
    about_action()
    
def fun_click():
    global about_selected,home_selected,fun_selected
    fun_selected=True
    home_selected=about_selected=False
    home.config(fg='#29ff2c',bg=bgcolour)
    about.config(fg='#29ff2c',bg=bgcolour)
    fun.config(bg='#29ff2c',fg=bgcolour)
    fun_action()

    
def loop(): #for mainloop
    global bgcolour
    for i in colourlist:
        if bgcolour==i and bgcolour!=colourlist[-1]:
            bgcolour=colourlist[colourlist.index(i)+1]
            if bgcolour==colourlist[-1]:
                bgcolour=colourlist[0]
            root.config(bg=bgcolour)
            #Button
            about.config(bg=bgcolour,fg='#29ff2c')
            fun.config(bg=bgcolour,fg='#29ff2c')
            home.config(bg=bgcolour,fg='#29ff2c')
            bcolour.config(bg=bgcolour,activebackground=bgcolour)
            #Label
            text1.config(bg=bgcolour)
            circle.config(bg=bgcolour)
            bigcircle.config(bg=bgcolour)
            break
    
#buttons and frames:
home=Button(root,bg='#29ff2c',fg=bgcolour,text=' Home  ',font=('arial',14),border=0,
        activebackground='#29ff2c',command=home_click)
home.place(x=50,y=210)
about=Button(root,fg='#29ff2c',bg=bgcolour,text=' About   ',font=('arial',14),border=0,
        activebackground='#29ff2c',command=about_click)
about.place(x=140,y=210)
fun=Button(root,fg='#29ff2c',bg=bgcolour,text=' Fun  ',font=('arial',14),border=0,
        activebackground='#29ff2c',command=fun_click)
fun.place(x=235,y=210)
bcolour=Button(root,image=colourpic,bg=bgcolour,activebackground=bgcolour,border=0,command=loop)
bcolour.place(x=310,y=208)

#Variables for handling frames
home_on=True
about_on=False
fun_on=False

#Creating frames:
home_frame=Frame(root)#,bg='green',border=5)
text_home=Label(home_frame,text='Chat Screen',fg='white',bg=bgcolour).grid()
home_frame.place(x=200,y=350)   #placed because home screen is selected by default

about_frame=Frame(root)
text_about=Label(about_frame,text='About Developer(me)',fg='white',bg=bgcolour).grid()

fun_frame=Frame(root)
text_about=Label(fun_frame,text='Anything else',fg='white',bg=bgcolour).grid()


#Placing and unplacing frames:
def home_action(): #for home tab
    global home_on, about_on, fun_on
    if about_on==True:
        about_frame.place_forget()
        about_on=False
    elif fun_on==True:
        fun_frame.place_forget()
        fun_on=False
    home_on=True
    home_frame.place(x=200,y=350)   
    
def about_action(): #for about tab
    global about_on, home_on, fun_on
    if home_on==True:
        home_frame.place_forget()
        home_on=False
    elif fun_on==True:
        fun_frame.place_forget()
        fun_on=False
    about_on=True
    about_frame.place(x=200,y=350)

def fun_action(): 
    global about_on, home_on, fun_on
    if home_on==True:
        home_frame.place_forget()
        home_on=False
    elif about_on==True:
        about_frame.place_forget()
        about_on=False
    fun_on=True
    fun_frame.place(x=200,y=350)

#event handling for hovering on buttons:
home.bind('<Enter>',home_hover) ; home.bind('<Leave>',home_leave)
about.bind('<Enter>',about_hover) ; about.bind('<Leave>',about_leave)
fun.bind('<Enter>',fun_hover) ; fun.bind('<Leave>',fun_leave)

#typewriting text defaults
strg=''
text1=Label(text=strg,bg=bgcolour,fg='#fc5b5e',font=('arial',25))
text1.grid(row=1,padx=30)
text3=[list("Exactly at 10 PM I... "),list("...Created this effect"),list('Dm if you want your text here')]#must contain even no of char.
effect_run=True
#typewriting text animation
def effect():
    global y_bigcircle,x_bigcircle,x_circle,y_circle
    while effect_run:
        text2=deepcopy(text3) #copying list-text3 to list-text2 without linkage

        for j in text2:
            strg=''
            text1.config(text=strg)
            no=0
            for i in j:#28
                no+=1
                strg=strg+i
                text1.config(text=strg+'|')
                text1.update()
                
                if no<=int(len(j)/2):
                    
                    y_bigcircle-=0.7;x_bigcircle+=1
                    bigcircle.place(x=x_bigcircle,y=y_bigcircle)
                    bigcircle.update()
                    x_circle-=1;y_circle+=1
                    circle.place(x=x_circle,y=y_circle)
                    circle.update()
                    time.sleep(0.03)
                    
                elif no>int(len(j)/2):
                    
                    y_bigcircle-=0.7;x_bigcircle-=1
                    bigcircle.place(x=x_bigcircle,y=y_bigcircle)
                    bigcircle.update()
                    x_circle+=1;y_circle+=1
                    circle.place(x=x_circle,y=y_circle)
                    circle.update()
                    time.sleep(0.03)
            
            text1.config(text=strg+'')
            text1.update()

            for i in range(4):
                text1.config(text=strg+'|')
                text1.update()                
                time.sleep(0.08)
                text1.config(text=strg+'/')
                text1.update()                
                time.sleep(0.08)
                text1.config(text=strg+'-')
                text1.update()                
                time.sleep(0.08)
                text1.config(text=strg+'\\')
                text1.update()                
                time.sleep(0.04)
                text1.config(text=strg+'|')
                text1.update()

            no=0
            j2=deepcopy(j) #to get the correct length of j list.
            for i in range(len(j2)):# (24)
                
                j.pop()
                if len(j)!=0:
                    j.pop()
                j.append('|')
                strg=''.join([str(e) for e in j])  #converts each element of a list to string
                text1.config(text=strg)
                text1.update()
                no+=1
                
                if no<=int(len(j2)/2):
                    
                    y_bigcircle+=0.7;x_bigcircle+=1
                    bigcircle.place(x=x_bigcircle,y=y_bigcircle)
                    bigcircle.update()
                    x_circle-=1;y_circle-=1
                    circle.place(x=x_circle,y=y_circle)
                    circle.update()
                    time.sleep(0.02)
                    
                elif no>int(len(j2)/2):
                    
                    y_bigcircle+=0.7;x_bigcircle-=1
                    bigcircle.place(x=x_bigcircle,y=y_bigcircle)
                    bigcircle.update()
                    x_circle+=1;y_circle-=1
                    circle.place(x=x_circle,y=y_circle)
                    circle.update()
                    time.sleep(0.02)

def animation(): #to move the circles
    global y_bigcircle,x_bigcircle,x_circle,y_circle
    while True:
        for i in range (12):
            y_bigcircle-=0.7;x_bigcircle+=1
            bigcircle.place(x=x_bigcircle,y=y_bigcircle)
            bigcircle.update()
            x_circle-=1;y_circle+=1
            circle.place(x=x_circle,y=y_circle)
            circle.update()
            time.sleep(0.05)
            
        for i in range (12):
            y_bigcircle-=0.7;x_bigcircle-=1
            bigcircle.place(x=x_bigcircle,y=y_bigcircle)
            bigcircle.update()
            x_circle+=1;y_circle+=1
            circle.place(x=x_circle,y=y_circle)
            circle.update()
            time.sleep(0.05)
        
        for i in range (12):
            y_bigcircle+=0.7;x_bigcircle+=1
            bigcircle.place(x=x_bigcircle,y=y_bigcircle)
            bigcircle.update()
            x_circle-=1;y_circle-=1
            circle.place(x=x_circle,y=y_circle)
            circle.update()
            time.sleep(0.05)
            
        for i in range (12):
            y_bigcircle+=0.7;x_bigcircle-=1
            bigcircle.place(x=x_bigcircle,y=y_bigcircle)
            bigcircle.update()
            x_circle+=1;y_circle-=1
            circle.place(x=x_circle,y=y_circle)
            circle.update()
            time.sleep(0.05)
effect()
animation() #runs the continuous animation
 
#to continue running after it loads
root.mainloop()

