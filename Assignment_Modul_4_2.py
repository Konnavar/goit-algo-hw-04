def get_cats_info(path):
    cats_info = [] # змінна для зберігання інфи про кожного кота
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_data = line.strip().split(',') # обробляємо рядок з файлу
                cat_dict = { # словник, який містить інфу про одного кота
                    "id": cat_data[0],
                    "name": cat_data[1],
                    "age": int(cat_data[2])
                }
                cats_info.append(cat_dict) # додавання нового словника до списку
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return None
    
    return cats_info

# Приклад використання:
cats_info = get_cats_info("cats_file.txt")
if cats_info is not None:
    print(cats_info)
