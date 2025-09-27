import json
import os

FILE_PATH = "src/storage.json"

def load_tasks():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ '{task}' eklendi.")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 Henüz görev yok.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"🗑️ '{removed}' silindi.")
    else:
        print("❌ Geçersiz seçim.")

def main():
    while True:
        print("\n--- Yapılacaklar Listesi ---")
        print("1. Görev ekle")
        print("2. Görevleri listele")
        print("3. Görev sil")
        print("4. Çıkış")
        choice = input("Seçimin: ")

        if choice == "1":
            task = input("Görev gir: ")
            add_task(task)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            list_tasks()
            try:
                idx = int(input("Silmek istediğin görev numarası: "))
                delete_task(idx)
            except ValueError:
                print("❌ Geçersiz giriş.")
        elif choice == "4":
            print("👋 Görüşmek üzere!")
            break
        else:
            print("❌ Geçersiz seçim.")

if __name__ == "__main__":
    main()
