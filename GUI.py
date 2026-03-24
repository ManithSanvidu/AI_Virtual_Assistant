from tkinter import*
from PIL import Image, ImageTk
import speech_to_text  
import action
root=Tk()
root.title("AI Assitant")
root.resizable(False, False)
root.config(bg="#6F8FAF")

window_width=550
window_height=675
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
x=int((screen_width-window_width)/2)
y=int((screen_height-window_height)/2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

#ask function
def ask():
    user_val=speech_to_text.speech_to_text()
    bot_val=action.Action(user_val)
    text.insert(END,'User--->'+user_val+"\n")
    if bot_val!=None:
        text.insert(END,"BOT<---"+str(bot_val)+"\n")
    if bot_val=="ok sir":
        root.destroy()

def send():
    user_val=entry.get()
    bot=action.Action(user_val)
    text.insert(END,'User--->'+user_val+"\n")
    if bot!=None:
        text.insert(END,"BOT<---"+str(bot)+"\n")
    if bot=="ok sir":
        root.destroy()

def del_text():
    text.delete("1.0", "end")

#frame
frame=LabelFrame(root, padx=100,pady=7,borderwidth=3,relief="raised")
frame.config(bg="#6F8FAF")
frame.grid(row=0,column=1,padx=55,pady=10)

#text label
text_label=Label(frame,text="AI Assistant",font=("comic Sans ms",14,"bold"))
text_label.grid(row=0,column=0,padx=20,pady=10)

#image
image=Image.open("images/image.jfif")
image=image.resize((200,200))
image=ImageTk.PhotoImage(image)

image_label=Label(frame,image=image)
image_label.grid(row=1,column=0,pady=20)

#adding a text widget
text=Text(root,font=('courier 10 bold'),bg="#356696")
text.grid(row=2,column=0)
text.place(x=100,y=375,width=375,height=100)

#entry widget
entry=Entry(root,justify=CENTER)
entry.place(x=100,y=500,width=350,height=30)

#buttons
Button1 = Button(root, text="Ask", bg="#356696", fg="white", pady=16, padx=40, borderwidth=3, relief=SOLID, command=ask)
Button1.place(x=70, y=575)

Button2 = Button(root, text="Send", bg="#356696", fg="white", pady=16, padx=40, borderwidth=3, relief=SOLID, command=send)
Button2.place(x=400, y=575)

Button3 = Button(root, text="Delete", bg="#356696", fg="white", pady=16, padx=40, borderwidth=3, relief=SOLID, command=del_text)
Button3.place(x=225, y=575)

root.mainloop()