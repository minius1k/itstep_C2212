import colorama

# виводимо назву і шлях до файла

print("Модуль:", colorama.__name__)
print("Файл:", getattr(colorama, "__file__", "N/A"))

# дістаємо тільки нормальні атрибути без службових підкреслень

print("Атрибути:", [a for a in dir(colorama) if not a.startswith("_")])

# Fore/Back/Style — колір тексту, фон і стиль
# Cursor — рух курсора
# init/deinit — старт і вимикання роботи з кольорами

items = [colorama.Fore, colorama.Back, colorama.Style, colorama.Cursor, colorama.init, colorama.deinit]
for item in items:
    print(f"{item.__name__ if hasattr(item, '__name__') else type(item).__name__}: {type(item)}")


# перевірка чи робить колір

colorama.init(autoreset=True)
print(colorama.Fore.GREEN + "Тестовий текст")