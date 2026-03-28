import json
import tkinter as tk

def save_tasks():
    with open("tasks.json", "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False)


def load_tasks():
    try:
        with open("tasks.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []
    

tasks = load_tasks()

def add_task():
    task = entry.get().strip()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()

def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
        tasks.pop(index)
        save_tasks()
    except:
        print("Выбери задачу!")


def complete_task():
    try:
        index = listbox.curselection()[0]
        task = tasks[index]
        tasks[index] = "✅ " + task
        listbox.delete(index)
        listbox.insert(index, tasks[index])
        listbox.itemconfig(index, fg="green")
        save_tasks()
    except:
        print("Выбери задачу!")


# Окно
window = tk.Tk()
window.title("Мои задачи")
window.geometry("400x500")
window.resizable(False, False)
window.configure(bg="#f0f0f0")

# Заголовок
title_label = tk.Label(window, text="📝 Мои задачи",
                       font=("Helvetica", 18, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

# Поле ввода + кнопка Добавить в одной строке
input_frame = tk.Frame(window, bg="#f0f0f0")
input_frame.pack(pady=10)

entry = tk.Entry(input_frame, width=25, font=("Helvetica", 12))
entry.pack(side=tk.LEFT, padx=5)

add_button = tk.Button(input_frame, text="Добавить", width=10,
                       bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"),
                       command=add_task)
add_button.pack(side=tk.LEFT, padx=5)

# Listbox с прокруткой
list_frame = tk.Frame(window)
list_frame.pack(pady=10)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(list_frame, width=40, height=15, font=("Helvetica", 12),
                     yscrollcommand=scrollbar.set)
listbox.pack()
for task in tasks:
    listbox.insert(tk.END, task)

scrollbar.config(command=listbox.yview)

# Кнопки Delete и Complete
button_frame = tk.Frame(window, bg="#f0f0f0")
button_frame.pack(pady=5)

delete_button = tk.Button(button_frame, text="Удалить", width=12,
                          bg="#f44336", fg="white", font=("Helvetica", 12, "bold"),
                          command=delete_task)
delete_button.pack(side=tk.LEFT, padx=5)

complete_button = tk.Button(button_frame, text="Выполнено", width=12,
                            bg="#2196F3", fg="white", font=("Helvetica", 12, "bold"),
                            command=complete_task)
complete_button.pack(side=tk.LEFT, padx=5)



window.mainloop()


