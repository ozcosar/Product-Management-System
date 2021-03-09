import tkinter as tk
import mysql.connector 
from tkinter import messagebox,ttk
import csv

root = tk.Tk()
root.title("Product Management System")

# to center the window on screen
app_width = 1000
app_height = 700
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = int((screen_width / 2) - (app_width / 2))
y = int((screen_height / 2) - (app_height / 2))
root.geometry(f'{app_width}x{app_height}+{x}+{y}')

mydb = mysql.connector.connect(host="localhost",user="root",database="apremen")
mycursor = mydb.cursor()

ctr_left = tk.Frame(root, width=225, height=190)
ctr_right = tk.Frame(root, width=225, height=190, padx=3, pady=3)

root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(2, weight=1)

ctr_left.grid(row=0, column=0, sticky="nw")
ctr_right.grid(row=0, column=2, sticky="ne")

#Label Frame for Searh Part
ctr_left_frame = tk.LabelFrame(ctr_left,text="Search Process",width=300,height=300,pady=20,font=("helvetica","16","bold italic"))
ctr_left_frame.grid(row=0,column=0,padx=100,pady=18)
ctr_left_frame.grid_propagate(False) #in order to block to resize the labelframe
# label for searching entry
search_customer_id = tk.Label(ctr_left_frame,text="Customer ID",font=("helvetica", "11","italic"))
search_customer_id.grid(row=0,column=0,padx=115)
search_product = tk.Label(ctr_left_frame,text="Product Name",font=("helvetica", "11","italic"))
search_product.grid(row=2,column=0)
#entry for searching customers with id
entry_search = tk.Entry(ctr_left_frame)
entry_search.grid(row=1,column=0,padx=35,pady=5)
entry_product = tk.Entry(ctr_left_frame)
entry_product.grid(row=3,column=0,pady=5)


#Label Frame for adding new product for existing customer
ctr_right_frame = tk.LabelFrame(ctr_right,text="New Product",width=300,height=300,pady=20,font=("helvetica","16","bold italic"))
ctr_right_frame.grid(row=0,column=1,padx=100,pady=18)
ctr_right_frame.grid_propagate(False) #in order to block to resize the labelframe
# label for creating new product for existing customer 
customer_id = tk.Label(ctr_right_frame,text="Customer ID",font=("helvetica", "11","italic"))
customer_id.grid(row=0,column=1,padx=115)
customer_id_entry = tk.Entry(ctr_right_frame)
customer_id_entry.grid(row=1,column=1,pady=5)

customer_name = tk.Label(ctr_right_frame,text="Customer Name",font=("helvetica", "11","italic"))
customer_name.grid(row=2,column=1)
customer_name_entry = tk.Entry(ctr_right_frame)
customer_name_entry.grid(row=3,column=1,pady=5)

global product_entry
product_name = tk.Label(ctr_right_frame, text="Product Name",font=("helvetica", "11","italic"))
product_name.grid(row=4,column=1)

product_entry = tk.Entry(ctr_right_frame,width=20)
product_entry.grid(row=5,column=1,pady=5)

#in order to sort the instruction list in ascending order
def order(e):
    #order of instructions is in the last index 
    return e[-1]

def checkBox(pname,num):

    global machine1,machine2,machine3,machine4
    global save_button

    portion_frame = tk.Frame(instruction_page,width=120,height=120)
    portion_frame.grid(row=0, column=1,sticky="nsew",padx=200,pady=20)

    global e1,e2,e3,e4
    global o1,o2,o3,o4
    e1 = tk.Text(portion_frame,height=5,width=20,font=("helvetica", 11))
    e2 = tk.Text(portion_frame,height=5,width=20,font=("helvetica", 11))
    e3 = tk.Text(portion_frame,height=5,width=20,font=("helvetica", 11))
    e4 = tk.Text(portion_frame,height=5,width=20,font=("helvetica", 11))   

    o1 = tk.Entry(portion_frame,width=4,font=("helvetica", 12))
    o2 = tk.Entry(portion_frame,width=4,font=("helvetica", 12))
    o3 = tk.Entry(portion_frame,width=4,font=("helvetica", 12))
    o4 = tk.Entry(portion_frame,width=4,font=("helvetica", 12))

    #Label(portion_frame,text="ORDER",font=("helvetica", 12)).grid(row=1,column=5)

    machine1 = tk.Label(portion_frame,text="MACHINE-1",font=("helvetica", 12))
    if var1.get() == 1:
        machine1.grid(row=2,column=3)
        tk.Label(portion_frame,text="").grid(row=3,column=3)
        e1.grid(row=2, column=4)
        o1.grid(row=2,column=5,padx=5,pady=10,ipady=5)


    machine2 = tk.Label(portion_frame,text="MACHINE-2",font=("helvetica", 12))
    if var2.get() == 1:
        machine2.grid(row=4,column=3)
        tk.Label(portion_frame,text="").grid(row=5,column=3)
        e2.grid(row=4, column=4)
        o2.grid(row=4,column=5,padx=5,pady=10,ipady=5)

    machine3 = tk.Label(portion_frame,text="MACHINE-3",font=("helvetica", 12))
    if var3.get() == 1:
        machine3.grid(row=6,column=3)
        tk.Label(portion_frame,text="").grid(row=7,column=3)
        e3.grid(row=6, column=4)
        o3.grid(row=6,column=5,padx=5,pady=10,ipady=5)
    machine4 = tk.Label(portion_frame,text="MACHINE-4",font=("helvetica", 12))
    if var4.get() == 1:
        machine4.grid(row=8,column=3)
        tk.Label(portion_frame,text="").grid(row=9,column=3)
        e4.grid(row=8, column=4)
        o4.grid(row=8,column=5,padx=5,pady=10,ipady=5)

    #button for saving processes 
    save_button = tk.Button(portion_frame,text="SAVE",font=("helvetica", 12),padx = 9, pady = 2,command=lambda:save(pname,num))
    save_button.grid(row = 9,column=4,pady=10)

    #if all of them goes to uncheck state destroy the SAVE button
    if var1.get() == 0 and var2.get() == 0 and var3.get() == 0 and var4.get() == 0:
        save_button.destroy()
    else:
        tk.Label(portion_frame,text="ORDER",font=("helvetica", 12)).grid(row=1,column=5)
    if var1.get() == 0:
        e1.destroy()
        machine1.destroy()
    if var2.get() == 0:
        e2.destroy()
        machine2.destroy()
    if var3.get() == 0:
        e3.destroy()
        machine3.destroy()
    if var4.get() == 0:
        e4.destroy()
        machine4.destroy()

def save(pname,num):
    z = ""
    if var1.get() == 1:
        x1 = "MACHINE-1 " + str(e1.get("1.0", "end-1c")) +" "+ str(o1.get())+","
        z = z + x1

    if var2.get() == 1:
        x2 = "MACHINE-2 " + str(e2.get("1.0", "end-1c")) +" "+ str(o2.get())+","
        z = z + x2
     
    if var3.get() == 1:
        x3 = "MACHINE-3 " + str(e3.get("1.0", "end-1c")) +" "+ str(o3.get())+","
        z = z + x3

    if var4.get() == 1:
        x4 = "MACHINE-4 " + str(e4.get("1.0", "end-1c")) +" "+ str(o4.get())+","
        z = z + x4
    #in order to put the sorted instruction into database
    ins_list = z.split(",")
    del ins_list[-1]    #remove comma at the end
    ins_list.sort(key=order) #sort them with their orders
    z = ",".join(ins_list) #list to string
    z = z.upper()

    try:
        insert_statement = """UPDATE customer_service SET process = %s WHERE cid = %s AND pName = %s"""
        val = (z,num,pname)
        mycursor.execute(insert_statement,val)
        mydb.commit()
    except mysql.connector.IntegrityError:
        warning_text = str(product_entry.get()) + " " + "has already in the database"
        messagebox.showwarning("Warning", warning_text)
    
#create a new window for saving product name and product's processes
def instructions(pname,num):
    #new window adjustments
    global instruction_page
    instruction_page = tk.Toplevel()
    
    instruction_page.geometry(f'{app_width}x{app_height}+{x}+{y}')
    instruction_page.title("Instruction Page")
    #for moving frames when resize the window 
    instruction_page.grid_rowconfigure(1, weight=1)
    instruction_page.grid_columnconfigure(2, weight=1)
    
    #instruction_page.resizable(width=False,height=False)

    """
    #space between product frame and instruction frame
    space = tk.Label(instruction_page,text="")
    space.grid(row=1,column=0)
    """
    #frame for instructions
    ins_frame = tk.Frame(instruction_page,height=300,width=300)
    ins_frame.grid(row=0,column=0,sticky="nw")

    
 
    instruct = tk.LabelFrame(ins_frame,text="Instructions",height=300,width=300,font=("helvetica", 13))
    instruct.grid(row=0, column=0,padx=50,pady=20)
    instruct.grid_propagate(False) #in order to block to resize the labelframe

    #checkbox variables
    global var1,var2,var3,var4
    var1 = tk.IntVar()
    var2 = tk.IntVar()
    var3 = tk.IntVar()
    var4 = tk.IntVar()

    #checkboxes for processes
    machine1 = tk.Checkbutton(instruct, text='MACHINE-1',font=("helvetica", 12),variable=var1,command=lambda:checkBox(pname,num))
    machine1.grid(row=1,column=0,sticky="w")
    machine2 = tk.Checkbutton(instruct, text='MACHINE-2',variable=var2,font=("helvetica", 12), onvalue=1, offvalue=0,command=lambda:checkBox(pname,num))
    machine2.grid(row=2,column=0,sticky="w")
    machine3 = tk.Checkbutton(instruct, text='MACHINE-3',variable=var3,font=("helvetica", 12),onvalue=1, offvalue=0,command=lambda:checkBox(pname,num))
    machine3.grid(row=3,column=0)
    machine4 = tk.Checkbutton(instruct, text='MACHINE-4',variable=var4, onvalue=1,font=("helvetica", 12), offvalue=0,command=lambda:checkBox(pname,num))
    machine4.grid(row=4,column=0,sticky="w")
    
def search(num,name):
    try:
        int(num)
        str(name)
        sql = """SELECT process FROM customer_service WHERE pName = %s and cid = %s"""
        mycursor.execute(sql,(name,num))
        record = mycursor.fetchall()

        # if there is no such record for given customer name and product name raise an error
        if not record:
            raise UnboundLocalError()
        

        product_page = tk.Toplevel()
        product_page.geometry(f'{app_width}x{app_height}+{x}+{y}')
        product_page.title("Product Details")
        text_frame = tk.Frame(product_page)
        text_frame.pack(pady=200)


        process = list(record[0]) #record tuple has just one element and turn list that element
        process[0] = process[0].replace('\n',' ') #remove the endline char
        tk.Label(text_frame,text=name.upper(),pady=20,font=("helvetica","18")).pack()
        tk.Label(text_frame,text=process[0],font=("helvetica","14"),bd=1,justify="left",relief="sunken",pady=5,padx=5).pack()
        
    except ValueError:
        messagebox.showerror("Error", "Wrong Input Format")
    
    except UnboundLocalError:
        messagebox.showerror("Error","There is no such record")
def create(name,num):
    """
    try:
        str(name)
        int(num)
        # search the database for given customer id and customer name
        sql_find = "SELECT COUNT(*) FROM customer_service WHERE cid = %s OR cName = %s"
        find_customer = (num,name)
        mycursor.execute(sql_find,find_customer)
        result = mycursor.fetchone() # it is return 1 or 0 
        if result[0] == 0: # given customer name and customer id not in the database 
            entry_create_id.delete(0,tk.END)
            entry_create_name.delete(0,tk.END)
            sql = "INSERT INTO customer_service (cid,cName) VALUES (%s,%s)"
            mycursor.execute(sql,(num,name))
            mydb.commit()
            #instructions(name,num) #all attributes are put database in the save function

        else: #if it is in the database throw a warning 
            warning_str = name + " " + str(num) + " " + " has already in the database"
            messagebox.showwarning("Warning",warning_str)
    except ValueError:
        messagebox.showerror("Error", "Wrong Input Format")
    """
def newProduct(name,num,pname):
    try:
        str(name)
        int(num)
        str(pname)
        sql = "SELECT COUNT(*) FROM customer_service WHERE cid = %s" # look the cid to check customer has already in the database or not
        mycursor.execute(sql,(num,))
        record = mycursor.fetchone()
        name = name.upper()
        if record[0] > 0: #if it is in database
            sql2 = "SELECT cName FROM customer_service WHERE cid = %s"
            mycursor.execute(sql2,(num,))
            records = mycursor.fetchall()
            if name != records[0][0]: #checks the given name has correct relation or not with given customer id
                raise UnboundLocalError()

        sql_insert = "INSERT INTO customer_service (cid,cName,pName) VALUES (%s,%s,%s)"
        mycursor.execute(sql_insert,(num,name,pname))
        mydb.commit()

        instructions(pname,num)
        # to make empty entry boxes after goes to a new page
        customer_id_entry.delete(0,tk.END)
        customer_name_entry.delete(0,tk.END)
        product_entry.delete(0,tk.END)
    except ValueError:
        messagebox.showerror("Error", "Wrong Input Format")
    except UnboundLocalError:
        messagebox.showerror("Error", "Customer Not Find")
    except mysql.connector.IntegrityError:
        messagebox.showerror("Error", "Product has already in the database")
    
def see_records(num):
    try:

        int(num)
        sql = """SELECT pName,process FROM customer_service WHERE cid = %s ORDER BY pName"""
        mycursor.execute(sql,(num,))
        result = mycursor.fetchall()
        
        if not result: #if result is empty raise an error
            raise UnboundLocalError()
        
        global records_page
        records_page = tk.Toplevel()
        records_page.geometry(f'{app_width}x{app_height}+{x}+{y}')
        records_page.title("Records")

        tree_frame = tk.Frame(records_page)
        tree_frame.grid(row=0,column=0,columnspan=2,rowspan=2,padx=150,pady=20)

        tree_yscroll = ttk.Scrollbar(tree_frame)
        tree_yscroll.grid(row=0,column=1,sticky="nsew")
    
        tree_xscroll = ttk.Scrollbar(tree_frame,orient="horizontal")
        tree_xscroll.grid(row=1,column=0,sticky="nsew")
    
        # for changing treeview style 
        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('helvetica', 11)) # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('helvetica', 13,'bold')) # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders


        tree = ttk.Treeview(tree_frame,yscrollcommand=tree_yscroll.set,xscrollcommand=tree_xscroll.set,style="mystyle.Treeview")
        tree_yscroll.config(command=tree.yview)
        tree_xscroll.config(command=tree.xview)

        tree['columns'] = ("Name","Process")
        tree.column("#0",width=100,minwidth=40)
        tree.column("Name",width=120,minwidth=80)
        tree.column("Process",width=500,minwidth=40)
        
        tree.heading("#0",text="ID")
        tree.heading("Name",text="Name")
        tree.heading("Process",text="Process")
        #tree.insert(parent='', index='end', iid=0, values=("Product Name", "Process"))
        tree.grid(row = 0, column = 0, sticky= "nsew")

        frame = tk.Frame(records_page,relief="ridge",width=800, height=100)
        frame.grid(row=2,column=0,columnspan=4,rowspan=3)
        count = 0
        for i in result:
            records = list(i)
            process = records[1] #second element in the list gives processes
            process = process.replace('\n',' ') #replace new line char with space
            process_list = process.split(",") #put processes in the list in order to sort them
            str_process = " ".join(process_list) #convert list elements into the one string
            tree.insert(parent='', index='end', iid=count, text=str(num),values=(records[0], str_process))
            count += 1
        #buttons for records page
        delete_button = tk.Button(frame,text="Delete",font=("Helvetica","10"),width=9,padx=10,pady=2,command= lambda: delete(tree,num))
        delete_button.grid(row=1, column=1)
        update_button = tk.Button(frame,text="Update",font=("helvetica","10"),width=9,padx = 10, pady = 2,command = lambda:update(tree,num))
        update_button.grid(row=1,column=2)
        save_excel = tk.Button(frame,text="Save to Excel",font=("helvetica","10"),width=9,padx=10,pady=2,command= lambda:write_excel(result,num))
        save_excel.grid(row=1,column=3)
    
    except ValueError:
        messagebox.showerror("Error", "Wrong Input Format",parent=records_page)
    except UnboundLocalError:
        messagebox.showerror("Error","There is no such record",parent=records_page)
def update(tree,num):
    try:
        selected = tree.focus()
        values = tree.item(selected,'values')
        pname = values[0] #process name is the first element in the tuple
        instructions(pname,num)
    except IndexError:
        messagebox.showerror("Error","Nothing Selected",parent=records_page)
def delete(tree,num):
    try:
        selected = tree.focus()
        values = tree.item(selected,'values')
        pname = values[0]
        msg = "Do you want to delete " + pname + "?"
        result = messagebox.askyesno("Delete",msg,parent=records_page)
        if result == 1:
            tree.delete(selected)
            sql = "DELETE FROM customer_service WHERE cid = %s AND pName = %s"
            val = (num,pname)
            mycursor.execute(sql,val)
            mydb.commit()
    except IndexError:
        messagebox.showerror("Error", "Nothing Selected",parent=records_page)
def write_excel(result,num):
    file_name = str(num) + '.csv'
    with open(file_name,'w') as f:
        w = csv.writer(f,dialect='excel')
        for i in result:
            w.writerow({i[0],i[1]})
#buttons
search_button = tk.Button(ctr_left_frame,text="Search",font=("helvetica","10"),padx = 20, pady = 2, command = lambda: search(entry_search.get(),entry_product.get()))
search_button.grid(row=4,column=0,pady=5)

records_button = tk.Button(ctr_left_frame,text="See Records",font=("helvetica","10"),padx = 15, pady = 2, command=lambda : see_records(entry_search.get()))
records_button.grid(row=5,column=0,pady=5)

new_product = tk.Button(ctr_right_frame,text="Create",font=("helvetica","10"),padx = 20,pady=2,command= lambda: newProduct(customer_name_entry.get(),customer_id_entry.get(),product_entry.get()))
new_product.grid(row=6,column=1,pady=5)

root.mainloop()