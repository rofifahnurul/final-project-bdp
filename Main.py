from tkinter import *
from tkinter import ttk
from tkinter import ttk, messagebox
import pandas as pd
import numpy as np

class Main:
    def __init__(self):
        global window
        window = Tk()
        window.title("Aplikasi Daftar Kontak")
        window.geometry("1440x900")

        bgColor = "#1C1940"

        window.configure(background=bgColor)

        primaryColor = "#1E4CAD"

        exit_button = Button(window, text="Exit", command=self.exit_btn).pack(side=TOP, padx=(850, 0), pady=20)

        label1 = Label(text='Data Customer', width=30, font="Roboto 36 bold italic", fg='white',background=bgColor).pack(pady=(10,0))

        show_button = Button(window, text="Open Data", command=self.file_open)
        show_button.pack(pady=(20,5))

        self.my_frame = Frame(window)
        self.my_frame.pack(pady=20)

        # create treeview
        self.my_tree = ttk.Treeview(self.my_frame)

        # entry
        global name_box, noHp_box, email_box, alamat_box

        label1 = Label(window,text='Nama:', width=15, font="Roboto 18 bold", fg='white',background=bgColor).pack()
        name_box = Entry(window)
        name_box.pack()

        label2 = Label(window, text='No Hp:', width=15, font="Roboto 18 bold", fg='white',background=bgColor).pack()
        noHp_box = Entry(window)
        noHp_box.pack()

        label3 = Label(window, text='Email:', width=15, font="Roboto 18 bold", fg='white',background=bgColor).pack()
        email_box = Entry(window)
        email_box.pack()

        label4 = Label(window, text='Alamat:', width=15, font="Roboto 18 bold", fg='white',background=bgColor).pack()
        alamat_box = Entry(window)
        alamat_box.pack()

        # Button

        add_button = Button(window, text="Add data", font="Roboto 16 bold",fg=bgColor,command=self.add_record)
        add_button.pack(side=LEFT,padx=(450,10))

        remove_all = Button(window, text="Remove all data",font="Roboto 16 bold",fg=bgColor, command=self.remove_all)
        remove_all.pack(side=LEFT,padx=(10,10))

        delete_button = Button(window, text="Delete data you selected", font="Roboto 16 bold",fg=bgColor,command=self.delete_record)
        delete_button.pack(side=LEFT,padx=(10,10))

        select_button = Button(window, text="Edit data", font="Roboto 16 bold",fg=bgColor,command=self.select_record)
        select_button.pack(side=LEFT,padx=(10,10))

        update_button = Button(window, text="Save", font="Roboto 16 bold",fg=bgColor,command=self.update_record)
        update_button.pack(side=LEFT,padx=(10,10))

        #self.my_label = Label(window, text='')
        #self.my_label.pack(pady=10)
        window.mainloop()

    def file_open(self):
        filename = r"/Users/agussuyono/Documents/DTS/customer.xlsx"
        if filename:
            try:
                filename = r"{}".format(filename)
                df = pd.read_excel(io=filename)
            except FileNotFoundError:
                messagebox.showerror("Error !", "File not found!", parent=window)

        self.clear_tree()

        self.my_tree["column"] = list(df.columns)
        self.my_tree["show"] = "headings"

        for column in self.my_tree["columns"]:
            self.my_tree.heading(column, text=column)

        df_rows = df.to_numpy().tolist()
        for row in df_rows:
            self.my_tree.insert("", "end", values=row)

        self.my_tree.pack()

    def clear_tree(self):
        self.my_tree.delete(*self.my_tree.get_children())


    def add_record(self):
        if name_box.get() == "" and noHp_box.get() == "" and email_box.get() =="" and alamat_box.get()=="":
            messagebox.showerror("Error !", "No hp must contain number and name must contain string !", parent=window)
        elif noHp_box.get().isdigit() == True and name_box.get().isalpha() == True:
            self.my_tree.insert(parent='', index='end', text="",values=(name_box.get(), noHp_box.get(), email_box.get(), alamat_box.get()))
            name_box.delete(0, END)
            noHp_box.delete(0, END)
            email_box.delete(0, END)
            alamat_box.delete(0, END)
        else:
            messagebox.showerror("Error !", "No hp must contain number and name must contain string !", parent=window)


    def remove_all(self):
        for record in self.my_tree.get_children():
            self.my_tree.delete(record)

    def delete_record(self):
        x = self.my_tree.selection()[0]
        self.my_tree.delete(x)

    def select_record(self):
        name_box.delete(0, END)
        noHp_box.delete(0, END)
        email_box.delete(0, END)
        alamat_box.delete(0, END)

        # grab record number
        selected = self.my_tree.focus()
        #self.my_label.config(text=selected)

        # grab record values
        values = self.my_tree.item(selected, 'values')

        name_box.insert(0, values[0])
        noHp_box.insert(0, values[1])
        email_box.insert(0, values[2])
        alamat_box.insert(0, values[3])

    def update_record(self):

        selected = self.my_tree.focus()

        # Save new data
        self.my_tree.item(selected, text="", values=(name_box.get(), noHp_box.get(), email_box.get(), alamat_box.get()))

        # Clear box
        name_box.delete(0, END)
        noHp_box.delete(0, END)
        email_box.delete(0, END)
        alamat_box.delete(0, END)

    def exit_btn(self):
        window.destroy()



