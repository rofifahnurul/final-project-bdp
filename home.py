from tkinter import*
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import PIL.Image
from final_project.Login import Login
from final_project.Register import Register

class Home:
    def __init__(self):
        global window
        window = Tk()
        window.title("Aplikasi Daftar Kontak ")
        window.geometry("1440x900")

        primaryColor = "#1E4CAD"

        bg = ImageTk.PhotoImage(Image.open("/Users/agussuyono/PycharmProjects/DTS/final_project/gambar/bg1.png"))
        panel = Label(window, image=bg)
        panel.pack(side=LEFT)

        exit_button = Button(window, text="Exit", command=self.exit_btn).pack(side=TOP,padx=(650,0),pady=20)

        title = Label(window,text='Aplikasi Daftar Kontak', width=30, font="Roboto 36", fg=primaryColor).pack(pady=(260,0))
        title2 = Label(window, text='PT. Maju Mundur', width=30, font="Roboto 36 bold",
                      fg=primaryColor).pack()


        login_button = Button(window,text="Login",width=15,font="Roboto 20 bold",fg=primaryColor,command=self.login).pack(pady=(30,20))
        register_button = Button(window,text="Register",width=15,font="Roboto 20 bold",fg=primaryColor,command=self.register).pack()
        window.mainloop()

    def login(self):
        window.destroy()
        new_login = Login()

    def register(self):
        window.destroy()
        new_regist = Register()

    def exit_btn(self):
        window.destroy()

home = Home()