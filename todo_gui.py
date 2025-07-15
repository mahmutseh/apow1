import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do App")

        # Entry for new tasks
        self.entry = tk.Entry(root, width=40)
        self.entry.grid(row=0, column=0, padx=10, pady=10)

        add_button = tk.Button(root, text="Add", command=self.add_task)
        add_button.grid(row=0, column=1, padx=10, pady=10)

        # Listbox to display tasks
        self.listbox = tk.Listbox(root, width=50, height=15)
        self.listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        del_button = tk.Button(root, text="Delete Selected", command=self.delete_task)
        del_button.grid(row=2, column=0, columnspan=2, pady=(0,10))

    def add_task(self):
        task = self.entry.get().strip()
        if task:
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task")

    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            self.listbox.delete(selected[0])
        else:
            messagebox.showwarning("Warning", "Please select a task to delete")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
