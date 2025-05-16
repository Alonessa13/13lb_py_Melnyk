import tkinter as tk
from tkinter import messagebox
import json

# Завантаження даних
with open('phones.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
products = data['data']

def show_details(product):
    details = f"Назва: {product['title']}\nЦіна: {product.get('price', 'N/A')} грн\nРейтинг: {product.get('rating', 'N/A')}"
    messagebox.showinfo("Деталі телефону", details)

def update_listbox(filter_text=''):
    listbox.delete(0, tk.END)
    for item in products:
        if filter_text.lower() in item['title'].lower():
            listbox.insert(tk.END, item['title'])

def on_select(event):
    index = listbox.curselection()[0]
    title = listbox.get(index)
    for item in products:
        if item['title'] == title:
            show_details(item)
            break

# GUI
root = tk.Tk()
root.title("Список телефонів")

search_entry = tk.Entry(root)
search_entry.pack()

def on_search():
    query = search_entry.get()
    update_listbox(query)

tk.Button(root, text="Пошук", command=on_search).pack()

listbox = tk.Listbox(root, width=80)
listbox.pack()
listbox.bind("<<ListboxSelect>>", on_select)

update_listbox()

root.mainloop()
