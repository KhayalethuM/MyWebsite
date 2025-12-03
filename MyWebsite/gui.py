import tkinter as tk
from task_manager import TaskManager

tm = TaskManager()
def add_task():
    title = entry.get()
    tm.add(title)
    entry.delete(0, tk.END) #clear textbox
    refresh()
    
def refresh():
    listbox.delete(0, tk.END)
    for t in tm.tasks:
        status = "✔️" if t.done else "❌"
        listbox.insert(tk.END, f"{t.title} [{status}]")
root = tk.Tk()
root.title("student assistant app")

entry = tk.Entry(root)
entry.pack()

btn = tk.Button(root, text = "Add Task", command = add_task)
btn.pack()

listbox = tk.Listbox(root)
listbox.pack()

refresh()
root.mainloop()
    