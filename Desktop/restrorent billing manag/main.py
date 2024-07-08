import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk
import sys
import os
import Menubar_tkinter as cmenu
from Menubar_tkinter import *
import datetime
import time
from tkinter.ttk import *
from time import strftime
import tabulate
import num2words
import importlib
import themes as TS



top = ctk.CTk()
top.geometry("1200x700")
user_name = ""
top.title("Sample Billing Software - " + user_name)

TS.init_server()
str1, str2 = TS.retrieve()

top.tk.call('source','sun-valley.tcl')
top.tk.call('set_theme',str1)

ctk.set_appearance_mode(str2)  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")



#________________________#

s = tk.ttk.Style()
s.configure('my.TEntry', width = 50, font = ('arial',14,'bold'))
s.configure('my.TNotebook', font = ('arial',11,'bold'), bordercolor = 'red')
s.configure('my.TRadiobutton', font = ('arial',11,'bold'))
s.configure('my.TCheckbutton', font = ('arial',11,'bold'))
s.configure('red.TCheckbutton', font = ('arial',11,'bold'), foreground = 'red')
s.configure('my.Treeview', width = 10, height = 5, font = ('arial',10,'bold'))
s.configure('my.TButton', font = ('arial',11,'bold'))
s.configure('red.TButton', font = ('arial',11,'bold'))
s.configure('green.TButton', font = ('arial',11,'bold'))
s.configure('Accent.TButton', font = ('arial',11,'bold'))


#___________      MENUBAR _____________#



def theme_set():
    global str1
    global str2
    if tk.messagebox.askyesno("Change Theme", "The application will close to save changes."):
        if str1 == 'dark':
            str1 = 'light'
            str2 = 'Light'
##            top.tk.call('set_theme',str1)
##            ctk.set_appearance_mode(str2)
            TS.save(str1,str2)
        else:
            str1 = 'dark'
            str2 = 'Dark'
##            top.tk.call('set_theme',str1)
##            ctk.set_appearance_mode(str2)
            TS.save(str1,str2)
        top.destroy()
        

menubar = cmenu.CustomMenuBar(top, bg='#1c1c1c', fg='white', overbackground='#2C41FF')
menubar.pack(side='top', expand=0, fill='x', anchor='n')
filemenu = tk.Menu(menubar, tearoff = 0)
filemenu.add_command(label = 'New Bill \t (Ctrl+n) or F5')
filemenu.add_command(label = 'Clear Bill')
filemenu.add_separator()
filemenu.add_command(label = 'Save Bill \t (Ctrl+s)')
filemenu.add_command(label = 'Print Bill \t (Ctrl+p)')
filemenu.add_separator()
filemenu.add_command(label = 'Logout and Exit')

menubar.add_menu( '  File  ', filemenu)


helpmenu = tk.Menu(menubar, tearoff = 0)
helpmenu.add_command(label = "About")
helpmenu.add_command(label = "Support")
menubar.add_menu("  Help  ", menu = helpmenu)


settingmenu = tk.Menu(menubar, tearoff = 0)
settingmenu.add_command(label = "Change Password")
settingmenu.add_command(label = "Admin Settings")
# settingmenu.add_command( label = 'Theme Setting ', command = theme_set)
menubar.add_menu("  Settings  ", menu = settingmenu)


top.config(menu = menubar,background='#1c1c1c',cursor='hand2')


#___________      TABS     _____________#

N1 = tk.ttk.Notebook(top)
N1.pack(fill = 'both', expand = True)

tab1 = tk.Frame(N1, padx = 10, pady = 10, bd = 0)
N1.add(tab1,text = '                ')
tab4 = tk.Frame(N1, padx = 10, pady = 10, bd = 0)
##N1.add(tab4,text = '        Tab2        ')
tab2 = tk.Frame(N1, padx = 10, pady = 10, bd = 0)
##N1.add(tab2,text = '        Tab3        ')

tab1_f1 = tk.Frame(tab1, padx = 10, pady = 10, bd = 0)
tab1_f1.grid(row = 1, column = 1)
tab1_f2 = tk.Frame(tab1, padx = 10, pady = 10, bd = 0)
tab1_f2.grid(row =1, column =2)
tab1_f3 = tk.Frame(tab1, padx = 10, pady = 10, bd = 0)
tab1_f3.grid(row =1, column =2)
s1 = tk.ttk.Separator(tab1_f2)
s1.pack(fill = 'y', expand = 1)

tab2_f1 = tk.Frame(tab2, padx = 10, pady = 10, bd = 0)
tab2_f1.grid(row = 1, column = 1)
tab2_f2 = tk.Frame(tab2, padx = 10, pady = 10, bd = 0)
tab2_f2.grid(row =1, column =2)
tab2_f3 = tk.Frame(tab2, padx = 10, pady = 10, bd = 0)
tab2_f3.grid(row =1, column =2)
s2 = tk.ttk.Separator(tab2_f2)
s2.pack(fill = 'y', expand = 1)

tab4_f1 = tk.Frame(tab4, padx = 10, pady = 10, bd = 0)
tab4_f1.grid(row = 1, column = 1)
tab4_f2 = tk.Frame(tab4, padx = 10, pady = 10, bd = 0)
tab4_f2.grid(row =1, column =2)
tab4_f3 = tk.Frame(tab4, padx = 10, pady = 10, bd = 0)
tab4_f3.grid(row =1, column =2)
s4 = tk.ttk.Separator(tab4_f2)
s4.pack(fill = 'y', expand = 1)

tab1.grid_columnconfigure(1,weight=1)
tab1.grid_columnconfigure(3,weight=1)
tab2.grid_columnconfigure(1,weight=1)
tab2.grid_columnconfigure(3,weight=1)
tab4.grid_columnconfigure(1,weight=1)
tab4.grid_columnconfigure(3,weight=1)
tab1.grid_rowconfigure(1,weight=1)
tab2.grid_rowconfigure(1,weight=1)
tab4.grid_rowconfigure(1,weight=1)


#=========================  Customer Details  ============================#


items_list = []
packaging = 0
discount = 0
total = 0

def live_time():
    time_str = strftime('%m/%d/%Y   %H:%M %p %A')
    L_time.configure(text = ''+time_str+'')
    L_time.after(1000,live_time)

    
frame_left = ctk.CTkFrame(master=tab1_f1,width = 600,corner_radius = 10)
frame_left.grid(row=2, column=1, sticky="nswe", padx=10, pady=5,columnspan = 2)
frame_left1 = ctk.CTkFrame(master=tab1_f1,width = 600,corner_radius = 10)
frame_left1.grid(row=3, column=1, sticky="nswe", padx=10, pady=5)
frame_left2 = ctk.CTkFrame(master=tab1_f1,width = 600,corner_radius = 0)
##frame_left2.grid(row=3, column=2, sticky="nswe", padx=10, pady=20)

L_time = ctk.CTkLabel(tab1_f1,text = 'live time',bg_color='#1c1c1c',font = (('times',20,'bold')))
L_time.grid(row = 0, column = 1 ,padx = 5, pady = 5,sticky = 'we',columnspan = 2)

def c_name(Event = None):
    global discount
    global packaging
    global total
    T1.config(state = 'normal')
    T1.delete("7.0",'end')
    try:
        T1.insert("7.0", '\n M/s:   ' + str(E1.get()), "left")
    except:
        T1.insert("7.0", '\n M/s:   ', "left")
    T1.delete("8.0",'end')
    try:
        T1.insert("8.0", '\n Address:  ' + str(E4.get()), "left")
    except:
        T1.insert("8.0", '\n Address:  ', "left")    
    T1.delete("9.0",'end')
    try:
        T1.insert("9.0", '\n GST No.:  ' + str(E5.get()), "left")
    except:
        T1.insert("9.0", '\n GST No.:  ', "left")
    try:    
        date_1 = strftime('%m/%d/%Y')
        T1.insert("10.0", "\n Date: " + date_1, "left")
        time_1 = strftime('%H:%M %p ')
        T1.insert("10.19", "\t\t\tTime: " + time_1 + '                                       ', "left")
    except:
        pass

    table_entry = tabulate.tabulate(items_list, headers = [' Particular', 'Qty', 'Rate', 'CGST', 'SGST', 'Total'], tablefmt = "rst", floatfmt = ".2f")
    total = 0
    for i in items_list:
        total = total + i[5]
    try:
        if C1.get() == 1 and C2.get() == 1:
            packaging = 20
            try:
                discount = (float(E9.get())/100)*total
            except:
                discount = 0
        else:
            if C1.get() == 1:
                packaging = 20
                discount = 0
            elif C2.get() == 1:
                packaging = 0
                try:
                    discount = (float(E9.get())/100)*total
                except:
                    discount = 0
            else:
                packaging = 0
                discount = 0
    except:
        pass
    val = total + packaging - discount
    T1.config(state = 'normal')
    T1.delete("10.999", 'end')
    T1.insert("11.0",'\n'+ table_entry + "\n Packing Charges:  "+str(packaging)+"\n discount:  "+str(round(discount,2))+ "\t\t\t\t\tTotal: ₹ "+str(round(total,2)))
    T1.config(state = 'disabled')
    T1.config(state = 'disabled')



    
L = ctk.CTkLabel(frame_left, text = "Customer Name ")
L.grid(row = 1, column = 1 ,padx = 5, pady = 10,sticky = 'we')
L = ctk.CTkLabel(frame_left, text = "Address ")
L.grid(row = 3, column = 1 ,padx = 5, pady = 10,sticky = 'we')
L = ctk.CTkLabel(frame_left, text = "GSTIN ")
L.grid(row = 4, column = 1 ,padx = 5, pady = 10,sticky = 'we')

E1 = ctk.CTkEntry(frame_left,width = 250)
E1.grid(row = 1, column = 2 ,padx = 5, pady = 10,sticky = 'we',columnspan = 4)
E1.bind('<Return>', c_name)
E4 = ctk.CTkEntry(frame_left)
E4.grid(row = 3, column = 2 ,padx = 5, pady = 10,sticky = 'we',columnspan = 4)
E4.bind('<Return>', c_name)
E5 = ctk.CTkEntry(frame_left)
E5.grid(row = 4, column = 2 ,padx = 5, pady = 10,sticky = 'we',columnspan = 4)
E5.bind('<Return>', c_name)


#--------------------------------- Choose An Item -----------------------------------------------------


test_list = [' Bhelpuri', ' Pav Bhaji', ' Ragda Pattice']
test_list_price = [(' Bhelpuri','20'), (' Pav Bhaji','50'), (' Ragda Pattice','45')]

def on_keyrelease(event):
    # get text from entry
    value = event.widget.get()
    value = value.strip().lower()
    # get data from test_list
    if value == '':
        data = test_list
    else:
        data = []
        for item in test_list:
            if value in item.lower():
                data.append(item)                
    # update data in listbox
    listbox_update(data)

def listbox_update(data):
    # delete previous data
    PL1.delete(0, 'end')
    # sorting data 
    data = sorted(data, key=str.lower)
    # put new data
    for item in data:
        PL1.insert('end', item)
    #listbox.config(value = data)
##    PE1.focus()

def on_select(event):
    # display element selected on list
    item_val = event.widget.get(event.widget.curselection())
    print(item_val)
    E6.delete(0, 'end')
    E6.insert('end', item_val)


def list_focus(x=None):
    PL1.focus()

L = ctk.CTkLabel(frame_left1, text = "Choose an Item ")
L.grid(row = 1, column = 1 ,padx = 10, pady = 10,sticky = 'we')
E6 = ctk.CTkEntry(frame_left1)
E6.grid(row = 1, column = 2 ,padx = 10, pady = 10,sticky = 'we',columnspan = 1)
PL1 = tk.Listbox(frame_left1, width = 26, font = ('arial',10,'bold'))
PL1.grid(row = 2, column = 2 ,padx = 5, pady = 5,sticky = 'we')
PL1.bind('<<ListboxSelect>>', on_select)
listbox_update(test_list)
E6.bind('<KeyRelease>', on_keyrelease)
E6.bind('<Down>', list_focus)


S1 = ctk.CTkScrollbar(frame_left1, command=PL1.yview)
PL1['yscrollcommand'] = S1.set
S1.grid(row = 2, column = 3 ,padx = 5, pady = 5,sticky = 'ns')
PL1.configure(yscrollcommand=S1.set)

L8 = ctk.CTkLabel(frame_left1, text = "Choose Quantity ")
L8.grid(row = 5, column = 1)
P2 = tk.ttk.Spinbox(frame_left1, width = 20, font = ('arial',12,'bold'), from_ = 1, to = 100)
P2.grid(row = 5, column = 2,padx = 5, pady = 5,sticky = 'we')
P2.set(1)

def add_val():
    global items_list
    global total
    name = E1.get()
    addr = E4.get()
    gst = E5.get()
    c_name()
    print(C1.get())
    
    for i in items_list:
        if E6.get() in i[0]:
            new = i[1] + int(P2.get())
            for j in test_list_price:
                if i[0] in j:
                    price = new*float(j[1])
            items_list.remove(i)
            items_list.append([i[0],new,price, round(int(price)*0.06,2),round(int(price)*0.06,2), round((int(price)+(2*int(price)*0.06)),2)])
            total = 0
            for i in items_list:
                print(i[5])
                total = total + i[5]
            table_entry = tabulate.tabulate(items_list, headers = [' Particular', 'Qty', 'Rate', 'CGST', 'SGST', 'Total'], tablefmt = "rst", floatfmt = ".2f")
            T1.config(state = 'normal')
            T1.delete("10.999", 'end')
            T1.insert("11.0",'\n'+ table_entry + "\n Packing Charges:  "+str(packaging)+"\n discount:  "+str(round(discount,2))+ "\t\t\t\t\tTotal: ₹ "+str(round(total,2)))
            T1.config(state = 'disabled')             
            return
        
    for i in test_list_price:
        if E6.get() == i[0]:  
            new_qua = int(P2.get())
            for j in test_list_price:
                if i[0] in j:
                    price = new_qua*float(j[1])
            items_list.append([i[0],new_qua,price, round(int(price)*0.06,2),round(int(price)*0.06,2), round((int(price)+(2*int(price)*0.06)),2)])
            total = 0
            for i in items_list:
                print(i[5])
                total = total + i[5]
            table_entry = tabulate.tabulate(items_list, headers = [' Particular', 'Qty', 'Rate', 'CGST', 'SGST', 'Total'], tablefmt = "rst", floatfmt = ".2f")
            T1.config(state = 'normal')
            T1.delete("10.999", 'end')
            T1.insert("11.0",'\n'+ table_entry + "\n Packing Charges:  "+str(packaging)+"\n discount:  "+str(round(discount,2))+ "\t\t\t\t\tTotal: ₹ "+str(round(total,2)))
            T1.config(state = 'disabled')
            return

        

def remove():
    global items_list
    global total
    c_name
    for i in items_list:
        if E6.get() in i[0]:
            new = max(0, i[1] - int(P2.get()))
            for j in test_list_price:
                if i[0] in j:
                    price = new*float(j[1])
                
            items_list.remove(i) 
            items_list.append([i[0],new,price, round(int(price)*0.06,2),round(int(price)*0.06,2), round((int(price)+(2*int(price)*0.06)),2)])

            total = 0
            for i in items_list:
                print(i[5])
                total = total + i[5]
            table_entry = tabulate.tabulate(items_list, headers = [' Particular', 'Qty', 'Rate', 'CGST', 'SGST', 'Total'], tablefmt = "rst", floatfmt = ".2f")
            T1.config(state = 'normal')
            T1.delete("10.99", 'end')
            T1.insert("11.0",'\n'+ table_entry + "\n Packing Charges:  "+str(packaging)+"\n discount:  "+str(round(discount,2))+ "\t\t\t\t\tTotal: ₹ "+str(round(total,2)))
            T1.config(state = 'disabled')
            return


   
L = ctk.CTkLabel(frame_left1, text = "In Stock ")
L.grid(row = 6, column = 1 ,padx = 5, pady = 10,sticky = 'we')
B1 = ctk.CTkButton(frame_left1, text = "Add", command = add_val)
B1.grid(row = 6, column = 2 ,padx = 5, pady = 4,sticky = 'we')
B1a = ctk.CTkButton(frame_left1, text = "Remove",command = remove)
B1a.grid(row = 7, column = 2 ,padx = 5, pady = (3,10),sticky = 'we')


#------------------------------------ MIDDLE BUTTONS ------------------------------------------------------

frame_right = ctk.CTkFrame(master=tab1_f3,width = 200,corner_radius = 10)
frame_right.grid(row=2, column=2, sticky="nswe", padx=10, pady=5,rowspan = 4)
frame_right1 = ctk.CTkFrame(master=tab1_f3,corner_radius = 10,width = 10)
frame_right1.grid(row=2, column=1, sticky="nswe", padx=1, pady=5)

Lt = ctk.CTkLabel(tab1_f3, text = "BILL  ",font=("Roboto Medium", 12))
##Lt.grid(row = 1, column = 2 ,padx = 50, pady = 10,sticky = 'we')
E7 = ctk.CTkEntry(tab1_f3,width = 225)
##E7.grid(row = 1, column = 2 ,padx = 50, pady = 10,sticky = 'e',columnspan = 1)

#============================== BILLL FORMAT =============================================

if str1 == 'light':
    textbox_c = '#D1D0D0'
else:
    textbox_c = '#1c1c1c'
    
T1 = tk.Text(frame_right, bd=0, bg=textbox_c,height = '28', width="60", font=('Consolas', 10))
T1.grid(row = 2, column = 1 ,padx = 10, pady = 10,sticky = 'we',columnspan = 2)
T1.tag_configure("center", justify = "center")
T1.insert("1.0", "COMPANY NAME\nCOMPANY ADDRESS, COMPANY PIN CODE\nGSTIN: XXXXXXXXXXXXXXX\n", "center")
T1.insert("7.0", "BILL\n", "center")
T1.tag_configure("left", justify = "left")
T1.insert("4.0", " --------------------------------------------------------\n", "left")
T1.insert("6.0", " --------------------------------------------------------\n   ", "left")
T1.tag_configure("left", justify = "left")
T1.insert("7.0", " M/s:   ", "left")
T1.insert("8.0", "\n Address:  ", "left")
T1.insert("9.0", "\n GST No.:  ", "left")
date_1 = strftime('%m/%d/%Y')
T1.insert("10.0", "\n Date: " + date_1, "left")
time_1 = strftime('%H:%M %p ')
T1.insert("10.19", "\t\t\tTime: " + time_1 + '                                       ', "left")
T1.config(state='disabled')

#============================== BILLL FORMAT DONE =============================================



def pack_val():
    global packaging 
    global discount
    global total
    if C1.get() == 1 and C2.get() == 1:
        packaging = 20
        table_entry = tabulate.tabulate(items_list, headers = [' Particular', 'Qty', 'Rate', 'CGST', 'SGST', 'Total'], tablefmt = "rst", floatfmt = ".2f")
        total = 0
        for i in items_list:
            total = total + i[5]
        try:
            discount = (float(E9.get())/100)*total
        except:
            discount = 0

        total = total + packaging - discount
        T1.config(state = 'normal')
        T1.delete("10.999", 'end')
        T1.insert("11.0",'\n'+ table_entry + "\n Packing Charges:  "+str(packaging)+"\n discount:  "+str(round(discount,2))+ "\t\t\t\t\tTotal: ₹ "+str(round(total,2)))
        T1.config(state = 'disabled')
    else:
        print('***********')
        if C1.get() == 1:
            packaging = 20
            discount = 0
            table_entry = tabulate.tabulate(items_list, headers = [' Particular', 'Qty', 'Rate', 'CGST', 'SGST', 'Total'], tablefmt = "rst", floatfmt = ".2f")
            total = 0
            for i in items_list:                
                total = total + i[5]
            total = total + packaging
            print(total)
            T1.config(state = 'normal')
            T1.delete("10.999", 'end')
            T1.insert("11.0",'\n'+ table_entry + "\n Packing Charges:  "+str(packaging)+"\n discount:  "+str(round(discount,2))+ "\t\t\t\t\tTotal: ₹ "+str(round(total,2)))
            T1.config(state = 'disabled')

        elif C2.get() == 1:
            table_entry = tabulate.tabulate(items_list, headers = [' Particular', 'Qty', 'Rate', 'CGST', 'SGST', 'Total'], tablefmt = "rst", floatfmt = ".2f")
            total = 0
            packaging = 0
            for i in items_list:
                total = total + i[5]
            try:
                discount = (float(E9.get())/100)*total
            except:
                discount = 0
            total = total - discount
            T1.config(state = 'normal')
            T1.delete("10.999", 'end')
            T1.insert("11.0",'\n'+ table_entry + "\n Packing Charges:  "+str(packaging)+"\n discount:  "+str(round(discount,2))+ "\t\t\t\t\tTotal: ₹ "+str(round(total,2)))
            T1.config(state = 'disabled')
        else:
            discount = 0
            packaging = 0
            table_entry = tabulate.tabulate(items_list, headers = [' Particular', 'Qty', 'Rate', 'CGST', 'SGST', 'Total'], tablefmt = "rst", floatfmt = ".2f")
            total = 0
            for i in items_list:
                total = total + i[5]
            T1.config(state = 'normal')
            T1.delete("10.999", 'end')
            T1.insert("11.0",'\n'+ table_entry + "\n Packing Charges:  "+str(packaging)+"\n discount:  "+str(round(discount,2))+ "\t\t\t\t\tTotal: ₹ "+str(round(total,2)))
            T1.config(state = 'disabled')
    
 

def new_bill():
    global packaging 
    global discount
    global items_list
    global total
    packaging = 0
    discount = 0
    total = 0
    items_list.clear()
    C1.deselect()
    C2.deselect()
    
    T1.config(state='normal')
    T1.delete("1.0", 'end')
    T1.insert("1.0", "COMPANY NAME\nCOMPANY ADDRESS, COMPANY PIN CODE\nGSTIN: XXXXXXXXXXXXXXX\n", "center")
    T1.insert("7.0", "BILL\n", "center")
    T1.tag_configure("left", justify = "left")
    T1.insert("4.0", " --------------------------------------------------------\n", "left")
    T1.insert("6.0", " --------------------------------------------------------\n   ", "left")
    T1.tag_configure("left", justify = "left")
    T1.insert("7.0", " M/s:   ", "left")
    T1.insert("8.0", "\n Address:  ", "left")
    T1.insert("9.0", "\n GST No.:  ", "left")
    date_1 = strftime('%m/%d/%Y')
    T1.insert("10.0", "\n Date: " + date_1, "left")
    time_1 = strftime('%H:%M %p ')
    T1.insert("10.19", "\t\t\tTime: " + time_1 + '                                       ', "left")
    T1.config(state='disabled')

def clear_bill():
    global packaging 
    global discount
    global items_list
    global total
    packaging = 0
    discount = 0
    total = 0
    items_list.clear()
    C1.deselect()
    C2.deselect()
    
    T1.config(state='normal')
    T1.delete("10.0", 'end')
    date_1 = strftime('%m/%d/%Y')
    T1.insert("10.0", "\n Date: " + date_1, "left")
    time_1 = strftime('%H:%M %p ')
    T1.insert("10.19", "\t\t\tTime: " + time_1 + '                                       ', "left")
    T1.config(state='disabled')

def print_bill():

    if tk.messagebox.askyesno("Save Bill ?", "You cannot Edit this bill after Saving, Printing or Mailing.\nDo you want to proceed ?"):
        dx = T1.get("7.0", 'end')
        print(dx)

def open_calc():
    global total
    editor = ctk.CTkToplevel(top)
    editor.geometry('300x300')
    editor.title('Cash Calculator')
    editor.grab_set()

    def cal():
        print(total)
        v1 = float(E10.get())
        v2 = total

        cash_return = v1-v2
        L_.configure(text = 'Cash Return : '+str(round(cash_return,2)))

        
    L = ctk.CTkLabel(editor, text = "Enter The Cash Given By Customer",font=("Roboto Medium", 12))
    L.grid(row = 1, column = 1 ,padx = 20, pady = 10,sticky = 'we')
    E10 = ctk.CTkEntry(editor,width = 225)
    E10.grid(row = 2, column = 1 ,padx = 20, pady = 10,sticky = 'we',columnspan = 1)
    B = ctk.CTkButton(editor, text = "Calculate", command = cal)
    B.grid(row = 3, column = 1 ,padx = 20, pady = 10,sticky = 'we',columnspan = 1)
    L_ = ctk.CTkLabel(editor, text = " ",font=("Roboto Medium", 12))
    L_.grid(row = 4, column = 1 ,padx = 20, pady = 10,sticky = 'we')
    editor.mainloop()
    
C1 = ctk.CTkCheckBox(frame_right1, text = "Packing Charges")
C1.grid(row = 0, column = 2 ,sticky = 'we',pady = (20,10),padx = 10)
C2 = ctk.CTkCheckBox(frame_right1, text = " % Discount")
C2.grid(row = 1, column = 2 ,sticky = 'we',pady = 10,padx = 10)
E9 = ctk.CTkEntry(frame_right1)
E9.grid(row = 2, column = 2 ,padx = 10, pady = 5,sticky = 'we',columnspan = 1)
B1 = ctk.CTkButton(frame_right1, text = "Apply",command = pack_val)
B1.grid(row = 3, column = 2 ,sticky = 'we',pady = 5,padx = 10)


B1 = ctk.CTkButton(frame_right1, text = "New", command = new_bill)
B1.grid(row = 6, column = 2 ,sticky = 'we',pady = (50,5),padx = 10)
B1 = ctk.CTkButton(frame_right1, text = "Clear", command = clear_bill)
B1.grid(row = 7, column = 2 ,sticky = 'we',pady = 5,padx = 10)
B1 = ctk.CTkButton(frame_right1, text = "Print", command = print_bill)
B1.grid(row = 8, column = 2 ,sticky = 'we',pady = 5,padx = 10)
B1 = ctk.CTkButton(frame_right1, text = "Cash ?",command = open_calc)
B1.grid(row = 9, column = 2 ,sticky = 'we',pady = (5,20),padx = 10)


B11 = ctk.CTkButton(tab1_f3, text = "Send Mail", state = 'disabled')
B11.grid(row = 6, column = 2 ,sticky = 'e')
Le = ctk.CTkLabel(tab1_f3, text = " E-Mail : ",font=("Roboto Medium", 12))
Le.grid(row = 6, column = 1 ,padx = 10, pady = 10,sticky = 'w')
E8 = ctk.CTkEntry(tab1_f3,width = 280)
E8.grid(row = 6, column = 2 ,padx = 10, pady = 10,sticky = 'w',columnspan = 1)



live_time()
top.mainloop()
