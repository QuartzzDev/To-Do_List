import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()

def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
        save_tasks()
    except IndexError:
        pass

def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        return

def main():
    global entry, listbox

    root = tk.Tk()
    root.title("To-Do List by QuartzzDev")

    
    frame_tasks = tk.Frame(root)
    frame_tasks.pack(pady=10)

    listbox = tk.Listbox(
        frame_tasks,
        width=50,
        height=10,
        font=("Courier New", 12)
    )
    listbox.pack(side=tk.LEFT, fill=tk.BOTH)

    scrollbar = tk.Scrollbar(frame_tasks)
    scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

    frame_entry = tk.Frame(root)
    frame_entry.pack(pady=10)

    entry = tk.Entry(
        frame_entry,
        font=("Courier New", 12)
    )
    entry.pack(side=tk.LEFT, padx=10)

    button_add = tk.Button(
        frame_entry,
        text="Ekle",
        font=("Courier New", 12),
        command=add_task
    )
    button_add.pack(side=tk.LEFT)

    button_delete = tk.Button(
        root,
        text="Sil",
        font=("Courier New", 12),
        command=delete_task
    )
    button_delete.pack(pady=10)

    load_tasks()

    root.mainloop()

if __name__ == "__main__":
    main()
