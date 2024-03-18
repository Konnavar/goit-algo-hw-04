def total_salary(path):
    total_salary = 0 # кількість розробників у файлі
    num_developers = 0 # загальна сума зарплат усіх розробників
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                name, salary = line.strip().split(',')
                total_salary += int(salary)
                num_developers += 1
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None, None
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return None, None
    
    if num_developers == 0:
        print("Файл пустий.")
        return None, None
    
    average_salary = total_salary / num_developers
    return total_salary, average_salary

total, average = total_salary("salary_file.txt")
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")