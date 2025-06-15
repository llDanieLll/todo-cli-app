import os
import json

FILENAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file)

def list_tasks(tasks):
    if not tasks:
        print("✅ No tasks yet!")
        return
    for i, task in enumerate(tasks, start=1):
        status = "✔" if task["done"] else "❌"
        print(f"{i}. {status} {task['text']}")

def add_task(tasks):
    text = input("Enter task: ").strip()
    if text:
        tasks.append({"text": text, "done": False})
        print("📝 Task added!")

def mark_done(tasks):
    list_tasks(tasks)
    try:
        choice = int(input("Enter task number to mark as done: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["done"] = True
            print("✅ Task marked as done.")
        else:
            print("❗ Invalid choice.")
    except ValueError:
        print("❗ Please enter a number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- TO-DO LIST ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("👋 Goodbye!")
            break
        else:
            print("❗ Invalid choice.")

if __name__ == "__main__":
    main()
