from tkinter import *
from tkinter import ttk, messagebox
from final_project.Login import Login
from Main import *
from PIL import ImageTk, Image
import PIL.Image
import csv

class Register:
    def __init__(self):
        global window2
        primaryColor = "#1E4CAD"
        window2 = Tk()
        window2.title("Aplikasi Daftar Kontak ")
        window2.geometry("1440x900")

        primaryColor = "#1E4CAD"

        bg = ImageTk.PhotoImage(Image.open("/Users/agussuyono/PycharmProjects/DTS/final_project/gambar/bg-register.png"))
        panel = Label(window2, image=bg)
        panel.pack(side=LEFT)

        exit_button = Button(window2, text="Exit", command=self.exit_btn).pack(side=TOP, padx=(650, 0), pady=20)

        label1 = Label(text='Register Page', width=30, font="Roboto 36 bold italic", fg=primaryColor).pack(pady=(100,0))
        label2 = Label(window2,text='Enter your new username', width=25, font="Roboto 18 bold", fg=primaryColor).pack(pady=(50,0))

        self.username = Entry(window2)
        self.username.pack(pady=(5,15))

        label3 = Label(window2,text='Enter your new password', width=25, font="Roboto 18 bold", fg=primaryColor).pack(pady=(5,0))
        self.password = Entry(window2, show="*")
        self.password.pack(pady=(5,15))

        label3 = Label(window2,text='Confirm password', width=25, font="Roboto 18 bold", fg=primaryColor).pack(pady=(0,0))
        self.password_fix = Entry(window2, show="*")
        self.password_fix.pack(pady=(0,0))

        register_button = Button(window2, text='Register', width=15, font="Roboto 20 bold", fg=primaryColor,
                          command=self.validate_regist).pack(pady=(30,20))
        window2.mainloop()

    def get_length(self):
        with open('/Users/agussuyono/PycharmProjects/DTS/final_project/db.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            reader_list = list(csv_reader)

            return len(reader_list)

    def validate_regist(self):
        if self.username.get() == "" or self.password.get() == "":
            messagebox.showerror("Error !","All fields required",parent=window2)
        elif self.password.get() != self.password_fix.get():
            messagebox.showerror("Error !","Confirm password is failed. Please input the same password", parent=window2)
        else:
            fieldnames = ['username','password']
            with open('/Users/agussuyono/PycharmProjects/DTS/final_project/db.csv','a') as csv_file:
                csv_writer = csv.DictWriter(csv_file,fieldnames)
                csv_writer.writerow({
                    "username":self.username.get(),
                    "password":self.password.get()
                })
            window2.destroy()
            login_new = Login()

    def exit_btn(self):
        window2.destroy()



