import tkinter as tk
import time

# Главное окно
main_window = tk.Tk()

# Заголовок программы
main_window.title('Дисплей покупателя 1С')

# Если картинка имеет расширение ico устанавливает логотип программы в скобках указывает путь к лого
# main_window.iconbitmap(test.ico)

# Если фото обычного формата
# main_image = tk.PhotoImage(file='Путь к фотографии') путь к фотографии
# main_window.iconphoto(False,main_image) # второй параметр путь к фото


# Размеры окна
width = int(main_window.winfo_screenwidth() / 2)  # ширина экрана данного компютера
height = int(main_window.winfo_screenheight() / 2)  # высота экрана данного компютера

main_window.geometry(f'{width}x{height}')  # Размер окна


# main_window.maxsize(600,500)
# main_window.minsize(600,500)
# main_window.resizable(False,False) # Запрет изменения окна расширение по высоте


# Изменение фона

# # 1 способ
# main_window.config(background='red')  # 000000 шестнадцеричный код
# # 2 способ
# main_window['bg'] = 'silver'


# Урок номер 2 (69) кнопки

def myfn():
    print('Hello world')
    print(first_button['width'])
    first_button['text'] = 'HAHAHAHA'


def update_time():
    four_button['text'] = 'time :' + time.strftime('%H:%M:%S')



time_now = time.strftime('%H:%M:%S')
# Создание первой кнопки

# first_button = tk.Button(main_window, text='Press me',font=("Times New Roman", 12 ,"bold")) # font шрифт (Лучше использовать безопасные шрифты)

first_button = tk.Button(main_window, text='Press me', font="Verdana 12 bold", width=8, padx=10,
                         command=myfn)  # font шрифт (Лучше использовать безопасные шрифты)
second_button = tk.Button(main_window, text='button1', font="Verdana 12 bold", width=8, padx=10,
                          command=myfn)  # font шрифт (Лучше использовать безопасные шрифты)
third_button = tk.Button(main_window, text='butoon2', font="Verdana 12 bold", width=8, padx=10,command=myfn)  # font шрифт (Лучше использовать безопасные шрифты)
four_button = tk.Button(main_window, text=f'time : {time_now}', font="Verdana 12 bold", padx=10,command=update_time)  # font шрифт (Лучше использовать безопасные шрифты)

# Добавление кнопки на начальную странницу
first_button.pack(pady = 10 ,padx = 20)  # pady высота  padx  ширина
second_button.pack(pady = 10) # pady высота
third_button.pack(pady = 10)  # pady высота
four_button.pack(pady = 10)  # pady высота

# Главный цикл для показа окна
main_window.mainloop()
