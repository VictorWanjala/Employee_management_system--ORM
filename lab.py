import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import database

app = customtkinter.CTk()
app.title('Employee Management System')
app.geometry('900x420')
app.config(bg='#161C25')
app.resizable(False, False)

font1 = ('Arial', 20,'bold')
font2 = ('Arial', 12, 'bold')

id_label = customtkinter.CTkLabel(app,font=font1,text='ID:', text_color='#fff', bg_color='#161C25')
id_label.place(x=20,y=20)
id_entry = customtkinter.CTkEntry(app,font=font1, text_color='#000', fg_color='#fff',width=180)
id_entry.place(x=100,y=20)
name_label = customtkinter.CTkLabel(app,font=font1,text='Name:', text_color='#fff', fg_color='#161C25')
name_label.place(x=20,y=80)
id_entry = customtkinter.CTkEntry(app,font=font1, text_color='#000', fg_color='#fff',width=180)
id_entry.place(x=100,y=80)
role_label = customtkinter.CTkLabel(app,font=font1,text='Role:', text_color='#fff', bg_color='#161C25')
role_label.place(x=20,y=140)
role_entry = customtkinter.CTkEntry(app,font=font1,text_color='#000', fg_color='#fff', width = 180)
role_entry.place(x=100,y=140)

gender_label = customtkinter.CTkLabel(app,font=font1, text='Gender:', text_color='#fff', bg_color='#161C25')
gender_label.place(x=20,y=200)

options = ['Male', 'Female']
Variable1 = StringVar()

gender_options = customtkinter.CTkComboBox(app,font=font1,text_color='#000',dropdown_hover_color='#0C9295',button_color='#0C9295', button_hover_color='#0C9295', width=180, variable=Variable1,values=options, state='readonly')
gender_options.set('Male')
gender_options.place(x=100, y=200)

status_label = customtkinter.CTkLabel(app,font=font1,text='Status:', text_color='#fff', bg_color='#161C25')
status_label.place(x=20,y=260)

status_entry = customtkinter.CTkEntry(app,font=font1,text_color='#000', fg_color='#0C9295',width=180)
status_entry.place(x=100,y=260)



app.mainloop()
