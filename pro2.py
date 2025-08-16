import tkinter as tk
from tkinter import messagebox, simpledialog

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.tasks = []

        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        self.add_btn = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_btn.pack(pady=5)

        self.update_btn = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_btn.pack(pady=5)

        self.delete_btn = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_btn.pack(pady=5)

        self.toggle_btn = tk.Button(root, text="Toggle Status", command=self.toggle_task_status)
        self.toggle_btn.pack(pady=5)

    def add_task(self):
        title = simpledialog.askstring("Input", "Enter Task Title:")
        description = simpledialog.askstring("Input", "Enter Task Description:")
        if title:
            self.tasks.append({"title": title, "desc": description, "status": "Pending"})
            self.refresh_tasks()

    def update_task(self):
        index = self.get_index()
        if index is not None:
            new_title = simpledialog.askstring("Input", "Update Title:")
            new_desc = simpledialog.askstring("Input", "Update Description:")
            if new_title:
                self.tasks[index]["title"] = new_title
            if new_desc:
                self.tasks[index]["desc"] = new_desc
            self.refresh_tasks()

    def delete_task(self):
        index = self.get_index()
        if index is not None:
            self.tasks.pop(index)
            self.refresh_tasks()

    def toggle_task_status(self):
        index = self.get_index()
        if index is not None:
            task = self.tasks[index]
            task["status"] = "Completed" if task["status"] == "Pending" else "Pending"
            self.refresh_tasks()

    def get_index(self):
        try:
            return self.task_listbox.curselection()[0]
        except IndexError:
            messagebox.showwarning("Warning", "Select a task first!")
            return None

    def refresh_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for i, task in enumerate(self.tasks):
            display = f"{i+1}. {task['title']} - {task['desc']} [{task['status']}]"
            self.task_listbox.insert(tk.END, display)

# Run the application
root = tk.Tk()
app = ToDoListApp(root)
root.mainloop()
