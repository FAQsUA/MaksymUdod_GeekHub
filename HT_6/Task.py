'''1. Програма-світлофор.
   Створити програму-емулятор світлофора для авто і пішоходів.
   Після запуска програми на екран виводиться в лівій половині - колір автомобільного, а в правій - пішохідного світлофора.
   Кожну секунду виводиться поточні кольори. Через декілька ітерацій - відбувається зміна кольорів - логіка така сама як і в звичайних світлофорах.
   Приблизний результат роботи наступний:
      Red        Green
      Red        Green
      Red        Green
      Red        Green
      Yellow     Green
      Yellow     Green
      Green      Red
      Green      Red
      Green      Red
      Green      Red
      Yellow     Red
      Yellow     Red
      Red        Green
      .......'''
import time

color_list = ['Red','Yellow','Green']
color_list_2 = {1:'Red',2:'Green'}
i = 0

try:
    while True:
        for color in color_list:

            if color == 'Red':
                while i < 4:
                    i += 1 
                    print(color + '    ' + color_list_2[2])
                    time.sleep(1)

            elif color == 'Yellow':
                while i < 2:
                    i += 1 
                    print(color + '    ' + color_list_2[2])
                    time.sleep(1)

            else:
                while i < 4:
                    i += 1 
                    print(color + '    ' + color_list_2[1])
                    time.sleep(1)

            i = 0
        

except KeyboardInterrupt:
    print('>>>>> EXIT <<<<<')
    exit()