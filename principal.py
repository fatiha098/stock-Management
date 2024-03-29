from tkinter import *
from subprocess import call

app = Tk()
app.geometry("800x500")
app.title("Stock Management")

# in case of the background image doesn't work
app.config(background="black")

# background 
background_image = PhotoImage(file = r"c:\Users\hp\Desktop\tkinter\projet\secondbg.png")
background_label = Label(app, image=background_image)
background_label.place(relwidth=1, relheight=1)

def purchases():
  app.destroy()
  call(["python", r"C:\Users\hp\Desktop\tkinter\projet\purchases.py"])

def sales():
  app.destroy()
  call(["python", r"C:\Users\hp\Desktop\tkinter\projet\sales.py"])

head = Label(app, text="Here You Go To Manage Your Stock",
              font=("Arial", 20, "bold"),
              fg="black",
              bg="orange",
              pady=20,
              width=300)
head.place(relx=0.5, rely=0.08, anchor=CENTER)

sales_btn = Button(app , text="Sales",width=25,
                  font=("Arial", 17, "bold"), 
                  bg="orange",
                  pady=13,
                  command=sales
                  )
sales_btn.place(relx=0.5,rely=0.5, anchor=E)
sales_btn.config(cursor="hand2")

purchases_btn = Button(app,text="Purchases",width=25, 
                      font=("Arial", 17, "bold"),
                      pady=13, 
                      bg="orange",
                      command=purchases)
purchases_btn.place(relx=0.5,rely=0.5, anchor=W)
purchases_btn.config(cursor="hand2")

app.mainloop()