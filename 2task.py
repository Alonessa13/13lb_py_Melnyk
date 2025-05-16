import json

# Завантаження даних з JSON-файлу
with open('phones.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Витягуємо тільки товари
products = data['data']  # або data['goods'] — залежно від структури

# Функція сортування
def sort_phones(by='price'):
    if by == 'price':
        return sorted(products, key=lambda x: x.get('price', 0))
    elif by == 'rating':
        return sorted(products, key=lambda x: x.get('rating', 0), reverse=True)
    elif by == 'comments':
        return sorted(products, key=lambda x: x.get('comments_amount', 0), reverse=True)

# Пошук телефону за назвою
search_query = input("Введіть назву або характеристику для пошуку: ").lower()

results = [p for p in products if search_query in p['title'].lower()]
for r in results:
    print(f"{r['title']} – {r.get('price', 'N/A')} грн, рейтинг: {r.get('rating', 'N/A')}")
