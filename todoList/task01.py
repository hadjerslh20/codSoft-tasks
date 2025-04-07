import tkinter as tk 
from tkinter import Toplevel
from PIL import Image, ImageTk
from tkinter import simpledialog, messagebox
# this is personal window
def personal_window():
    for widget in main_window.winfo_children():
        widget.destroy()
    personal_window = tk.Frame(main_window,bg="lightgray", width=280, height=500,background='white')
    personal_window.place(x=1 , y=1)
    # Add tasks
    personal_tasks = []
    text_add =tk.Label(personal_window,text="Write your task ",bg='white',font=('Arial',18,'bold'))
    text_add.place(x=50,y=0)
    entrytask= tk.Entry(personal_window,width=25,font=('Arial',12),bg='#5D80FE',fg='white')
    entrytask.place(x=20 , y=40, height=35)
        #list to show tasks
    listbox = tk.Listbox(personal_window, width=30, height=10, font=("Arial", 12))
    listbox.pack(pady=200)
    # Refresh listbox
    def update_listbox():
        listbox.delete(0, tk.END)
        for task in personal_tasks:
            listbox.insert(tk.END, task)
    # Function to add task
    def add_task():
        task = entrytask.get().strip()
        if task != "":
            personal_tasks.append(task)
            update_listbox()
            entrytask.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Task cannot be empty!")
    # Delete Task
    def delete_task():
        selected = listbox.curselection()
        if selected:
            task_index = selected[0]
            del personal_tasks[task_index]
            update_listbox()
        else:
            messagebox.showwarning("Selection Error", "Select a task to delete!")
    # Update Task
    def update_task():
        selected = listbox.curselection()
        if selected:
            task_index = selected[0]
            new_task = simpledialog.askstring("Update Task", "Enter the updated task:")
            if new_task:
                personal_tasks[task_index] = new_task
                update_listbox()
        else:
            messagebox.showwarning("Selection Error", "Select a task to update!")
    # Add button
    addbtn= tk.Button(personal_window,text='Add',width=8,height=2,relief='flat',font=("Arial", 10, "bold"),bg='#5D80FE',fg='white',command=add_task)
    addbtn.place(y=100)
    # delete button
    deletebtn= tk.Button(personal_window,text='Delete',width=8,height=2,relief='flat',font=("Arial", 10, "bold"),bg='#5D80FE',fg='white',command=delete_task)
    deletebtn.place(y=100, x=100)
    # update button
    deletebtn= tk.Button(personal_window,text='Update',width=8,height=2,relief='flat',font=("Arial", 10, "bold"),bg='#5D80FE',fg='white',command=update_task)
    deletebtn.place(y=100, x=200)
    # previous button
    prebutton =tk.Button(personal_window,text='Previous',width=8,height=2,relief='flat',font=("Arial", 10, "bold"),bg='#5D80FE',fg='white',command=second_window)
    prebutton.place(y=420 , x=40)
    # close button
    prebutton =tk.Button(personal_window,text='Close',width=8,height=2,relief='flat',font=("Arial", 10, "bold"),bg='#5D80FE',fg='white',command=main_window.destroy)
    prebutton.place(y=420 , x=160)

def Wrok_window():
    for widget in main_window.winfo_children():
        widget.destroy()
    work_window = tk.Frame(main_window,bg="lightgray", width=280, height=500,background='white')
    work_window.place(x=1 , y=1)
    # Add tasks
    worktask = []
    text_add =tk.Label(work_window ,text="Write your task ",bg='white',font=('Arial',18,'bold'))
    text_add.place(x=50,y=0)
    entrytask= tk.Entry(work_window ,width=25,font=('Arial',12),bg='#5D80FE',fg='white')
    entrytask.place(x=20 , y=40, height=35)
        #list to show tasks
    listbox = tk.Listbox(work_window , width=30, height=10, font=("Arial", 12))
    listbox.pack(pady=200)
    # Refresh listbox
    def update_listbox():
        listbox.delete(0, tk.END)
        for task in  worktask:
            listbox.insert(tk.END, task)
    # Function to add task
    def add_task():
        task = entrytask.get().strip()
        if task != "":
            worktask.append(task)
            update_listbox()
            entrytask.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Task cannot be empty!")
    # Delete Task
    def delete_task():
        selected = listbox.curselection()
        if selected:
            task_index = selected[0]
            del worktask[task_index]
            update_listbox()
        else:
            messagebox.showwarning("Selection Error", "Select a task to delete!")
    # Update Task
    def update_task():
        selected = listbox.curselection()
        if selected:
            task_index = selected[0]
            new_task = simpledialog.askstring("Update Task", "Enter the updated task:")
            if new_task:
                worktask[task_index] = new_task
                update_listbox()
        else:
            messagebox.showwarning("Selection Error", "Select a task to update!")
    # Add button
    addbtn= tk.Button(work_window,text='Add',width=8,height=2,relief='flat',font=("Arial", 10, "bold"),bg='#5D80FE',fg='white',command=add_task)
    addbtn.place(y=100)
    # delete button
    deletebtn= tk.Button(work_window,text='Delete',width=8,height=2,relief='flat',font=("Arial", 10, "bold"),bg='#5D80FE',fg='white',command=delete_task)
    deletebtn.place(y=100, x=100)
    # update button
    deletebtn= tk.Button(work_window,text='Update',width=8,height=2,relief='flat',font=("Arial", 10, "bold"),bg='#5D80FE',fg='white',command=update_task)
    deletebtn.place(y=100, x=200)
    # previous button
    prebutton =tk.Button(work_window,text='Previous',width=8,height=2,relief='flat',font=("Arial", 10, "bold"),bg='#5D80FE',fg='white',command=second_window)
    prebutton.place(y=420 , x=40)
    # close button
    prebutton =tk.Button(work_window,text='Close',width=8,height=2,relief='flat',font=("Arial", 10, "bold"),bg='#5D80FE',fg='white',command=main_window.destroy)
    prebutton.place(y=420 , x=160)
def shop_window():
    for widget in main_window.winfo_children():
        widget.destroy()
    shop_window = tk.Frame(main_window,bg="lightgray", width=280, height=500,background='white')
    shop_window.place(x=1 , y=1)
    # Add tasks
    worktask = []
    text_add =tk.Label(shop_window ,text="Write your task ",bg='white',font=('Arial',18,'bold'))
    text_add.place(x=50,y=0)
    entrytask= tk.Entry(shop_window ,width=25,font=('Arial',12),bg='#5D80FE',fg='white')
    entrytask.place(x=20 , y=40, height=35)
        #list to show tasks
    listbox = tk.Listbox(shop_window , width=30, height=10, font=("Arial", 12))
    listbox.pack(pady=200)
    # Refresh listbox
    def update_listbox():
        listbox.delete(0, tk.END)
        for task in  worktask:
            listbox.insert(tk.END, task)
    # Function to add task
    def add_task():
        task = entrytask.get().strip()
        if task != "":
            worktask.append(task)
            update_listbox()
            entrytask.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Task cannot be empty!")
    # Delete Task
    def delete_task():
        selected = listbox.curselection()
        if selected:
            task_index = selected[0]
            del worktask[task_index]
            update_listbox()
        else:
            messagebox.showwarning("Selection Error", "Select a task to delete!")
    # Update Task
    def update_task():
        selected = listbox.curselection()
        if selected:
            task_index = selected[0]
            new_task = simpledialog.askstring("Update Task", "Enter the updated task:")
            if new_task:
                worktask[task_index] = new_task
                update_listbox()
        else:
            messagebox.showwarning("Selection Error", "Select a task to update!")
    # Add button
    addbtn= tk.Button(shop_window,text='Add',width=8,height=2,relief='flat',font=("Arial", 10, "bold"),bg='#5D80FE',fg='white',command=add_task)
    addbtn.place(y=100)
    # delete button
    deletebtn= tk.Button(shop_window,text='Delete',width=8,height=2,relief='flat',font=("Arial", 10, "bold"),bg='#5D80FE',fg='white',command=delete_task)
    deletebtn.place(y=100, x=100)
    # update button
    deletebtn= tk.Button(shop_window,text='Update',width=8,height=2,relief='flat',font=("Arial", 10, "bold"),bg='#5D80FE',fg='white',command=update_task)
    deletebtn.place(y=100, x=200)
    # previous button
    prebutton =tk.Button(shop_window,text='Previous',width=8,height=2,relief='flat',font=("Arial", 10, "bold"),bg='#5D80FE',fg='white',command=second_window)
    prebutton.place(y=420 , x=40)
    # close button
    prebutton =tk.Button(shop_window,text='Close',width=8,height=2,relief='flat',font=("Arial", 10, "bold"),bg='#5D80FE',fg='white',command=main_window.destroy)
    prebutton.place(y=420 , x=160)
# this is second window
def second_window():
    # to hide first screen
    for widget in main_window.winfo_children():
        widget.destroy()
    # start second page 
    inside_window = tk.Frame(main_window,bg="lightgray", width=280, height=500,background='white')
    inside_window.place(x=1 , y=1)
    # first frame 
    firstFrame = tk.Frame(inside_window, width=280 ,height=100,bg="#5D80FE")
    firstFrame.pack_propagate(0)
    firstFrame.pack()
    welc_text = tk.Label(firstFrame,text="Hello!",font=("Arial", 20, "bold"),bg="#5D80FE",fg='white')
    welc_text.place(x=0 , y=0)
    welc_text_p = tk.Label(firstFrame,text="Please choose your suitable list",font=("Arial", 10, "bold"),bg="#5D80FE",fg='white')
    welc_text_p.place(x=0 , y=40)
    # second frame 
    secondFrame = tk.Frame(inside_window, width=280, height=400, bg="white")
    secondFrame.pack_propagate(0)
    secondFrame.pack()
    # choosing the list's type
    btOne = tk.Button(secondFrame,text="Personal",width=20,height=2,relief='flat',font=("Arial", 10, "bold"),bg="#5D80FE",fg='white',command=personal_window)
    btOne.pack(pady=50)

    btTwo = tk.Button(secondFrame,text="Work",width=20,height=2,relief='flat',font=("Arial", 10, "bold"),bg="#5D80FE",fg='white',command=Wrok_window)
    btTwo.pack()

    btThree = tk.Button(secondFrame,text="Shopping",width=20,height=2,relief='flat',font=("Arial", 10, "bold"),bg="#5D80FE",fg='white',command=shop_window)
    btThree.pack(pady=50)

# this is main window
main_window =tk.Tk()
main_window.geometry('280x500')
main_window.config(background='white')
main_window.resizable(False ,False)
main_window.iconbitmap("C:\\Users\\hadje\\Desktop\\codSoft\\im.ico")
main_window.title('SimpleToDoList')
firstImage=Image.open(r"C:\\Users\\hadje\\Desktop\\codSoft\\todo.png")
resizedImage = firstImage.resize((280, 250))
photo = ImageTk.PhotoImage(resizedImage)
imagePlace = tk.Label(main_window,image=photo)
imagePlace.pack()
imagePlace.image = photo  
titleWelc = tk.Label(main_window,text="My To-Do List", font=("Arial", 16, "bold"),bg='white')
desctext = tk.Label(main_window,text="A simple and user-friendly To-Do\nList appbuilt with Python and Tkinter.\nIt helps you organize tasks,set priorities\nand track progress efficiently.", font=("Arial", 10),bg='white')
titleWelc.pack(pady=20)
desctext.pack()
startButton =tk.Button(main_window, text="Get Started !", font=("Arial", 14),bg="#5D80FE", fg="white", borderwidth=0, padx=10, pady=5 ,command=second_window)
startButton.pack(pady=20)


main_window.mainloop()