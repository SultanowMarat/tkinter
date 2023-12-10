import tkinter as tk

# Главное окно
root = tk.Tk()

# Заголовок программы
root.title('Дисплей покупателя 1С')

# Если картинка имеет расширение ico устанавливает логотип программы в скобках указывает путь к лого
# root.iconbitmap(test.ico)

# Если фото обычного формата
# main_image = tk.PhotoImage(file='Путь к фотографии') путь к фотографии
# root.iconphoto(False,main_image) # второй параметр путь к фото


# Размеры окна
width = int(root.winfo_screenwidth() / 2)  # ширина экрана данного компютера
height = int(root.winfo_screenheight() / 2)  # высота экрана данного компютера

root.geometry(f'{width}x{height}')  # Размер окна
# root.maxsize(600,500)
# root.minsize(600,500)
# root.resizable(False,False) # Запрет изменения окна расширение по высоте


# Изменение фона

# # 1 способ
# root.config(background='red')  # 000000 шестнадцеричный код
# # 2 способ
# root['bg'] = 'silver'


# Главный цикл для показа окна
root.mainloop()
