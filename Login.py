
from tkinter import*
from tkinter import ttk, messagebox

from Main import *
import csv
from PIL import ImageTk, Image
import PIL.Image

class Login:

    def __init__(self):
        global window1
        window1 = Tk()
        window1.title("Aplikasi Daftar Kontak ")
        window1.geometry("1440x900")

        primaryColor = "#1E4CAD"

        bg = ImageTk.PhotoImage(Image.open("/Users/agussuyono/PycharmProjects/DTS/final_project/gambar/bg-login.png"))
        panel = Label(window1, image=bg)
        panel.pack(side=LEFT)

        exit_button = Button(window1, text="Exit", command=self.exit_btn).pack(side=TOP, padx=(650, 0), pady=20)

        label1 = Label(text='Login Page', width=30, font="Roboto 36 bold italic", fg=primaryColor).pack(pady=(150,0))

        label2 = Label(text='Username', width=15, font="Roboto 18 bold", fg=primaryColor).pack(pady=(50,0))

        self.username = Entry(window1)
        self.username.pack(pady=(5,15))

        label3 = Label(text='Password', width=15, font="Roboto 18 bold", fg=primaryColor).pack()
        self.password= Entry(window1, show="*")
        self.password.pack(pady=(5,15))

        login_button = Button(window1, text='Login', width=20, font="Roboto 20 bold", fg=primaryColor,
                             command=self.validate_login).pack(pady=(30,20))

        window1.mainloop()

    def validate_login(self):
        if self.username.get() == '' or self.password.get() == '':
            messagebox.showerror("Error !", "All Fields are Required !", parent=window1)
        else:
            self.find_user()

    def find_user(self):
        with open('/Users/agussuyono/PycharmProjects/DTS/final_project/db.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            username = self.username.get()

            flag = 0
            for row in csv_reader:
                if row[0] == username:
                    print("Username found",username)
                    user_found = [row[0],row[1]]
                    self.pass_check(user_found)
                    flag = 1
                    break
                else:
                    flag = 0

            if flag == 0:
                print("Not found")
                messagebox.showerror("Error !", "Failed to find username!", parent=window1)

            csv_file.close()

    def pass_check(self,user_found):
        if user_found[1] == self.password.get():
            print("Password match")
            window1.destroy()
            main = Main()
        else:
            print("Password not match")
            messagebox.showerror("Error !", "Password didn't match! Try Again", parent=window1)

    def exit_btn(self):
        window1.destroy()



