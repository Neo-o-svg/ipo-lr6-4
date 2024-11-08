# Запрашивает у пользователя строку для поиска и сохраняет ее в переменную search_string
search_string = input("Введите строку для поиска: ") 

# Создает пустой список для хранения найденных строк
found_strings = []

# Открывает файл "text.txt" в режиме чтения ('r') с кодировкой UTF-8
with open("text.txt", 'r', encoding='utf-8') as file: 
 # Проходит по каждой строке файла
 for line in file: 
  # Проверяет, содержит ли текущая строка искомую подстроку
  if search_string in line: 
   # Если строка содержит подстроку, добавляет ее в список found_strings 
   # после удаления пробелов в начале и конце строки (с помощью strip())
   found_strings.append(line.strip())


# Сортирует список found_strings по длине строк с помощью sorted(found_strings, key=len) 
# и сохраняет результат в переменную sorted_strings
sorted_strings = sorted(found_strings, key=len) 

# Выводит сообщение с количеством найденных строк, содержащих search_string
print(f"Найдено {len(found_strings)} строк, содержащих '{search_string}':")

# Проходит по каждой строке в списке sorted_strings (отсортированные по длине)
for string in sorted_strings: 
 # Выводит каждую найденную строку
 print(string)
