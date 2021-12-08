''' 2. Написати функцію, яка приймає два параметри: ім'я файлу та кількість символів.
   На екран повинен вивестись список із трьома блоками - символи з початку, із середини та з кінця файлу.
   Кількість символів в блоках - та, яка введена в другому параметрі.
   Придумайте самі, як обробляти помилку, наприклад, коли кількість символів більша, ніж є в файлі (наприклад, файл із двох символів і треба вивести по одному символу, то що виводити на місці середнього блоку символів?)
   В репозиторій додайте і ті файли, по яким робили тести.
   Як визначати середину файлу (з якої брать необхідні символи) - кількість символів поділити навпіл, а отримане "вікно" символів відцентрувати щодо середини файла і взяти необхідну кількість. В разі необхідності заокруглення одного чи обох параметрів - дивіться на свій розсуд.
   Наприклад:
   █ █ █ ░ ░ ░ ░ ░ █ █ █ ░ ░ ░ ░ ░ █ █ █    - правильно
                     ⏫ центр
   █ █ █ ░ ░ ░ ░ ░ ░ █ █ █ ░ ░ ░ ░ █ █ █    - неправильно '''

from pathlib import Path
import math

def func(file, chars):
   list_blocks = []

   with open(Path("Task_2", file), 'r', encoding='utf-8') as fake_file:
      file_len = str(fake_file.read()).replace('\n','')
   
   if len(file_len) <= chars:
      print(f'Довдина рядка в файлі = {len(file_len)} , введіть меньше число')
      return True

   elif len(file_len)/2 < chars:
      with open(Path("Task_2", file), 'r', encoding='utf-8') as fake_file:
         fake_file.seek(0,0)
         file_content = str(fake_file.read()).replace('\n','')

         #############################>START<###########################################
         list_blocks.append(file_content[0:chars])
         #############################>MID<#############################################
         list_blocks.append(" ### Ти на міді ### ")
         #############################>END<#############################################
         list_blocks.append(file_content[-chars:])
         print(list_blocks)
         return False
   else:
      with open(Path("Task_2", file), 'r', encoding='utf-8') as fake_file:
         fake_file.seek(0,0)
         file_content = str(fake_file.read()).replace('\n','')

         #############################>START<###########################################
         list_blocks.append(file_content[0:chars])
         #############################>MID<#############################################
         mid_text_first = file_content[0:int(len(file_content)/2)]
         mid_text_second = file_content[int(len(file_content)/2):]
         mid_slice = mid_text_first[int(-chars/2):] + mid_text_second[0:math.ceil(chars/2)]
         list_blocks.append(mid_slice)
         #############################>END<#############################################
         list_blocks.append(file_content[-chars:])
         print(list_blocks)
         return False

file = "file.txt"
flag = True

while True:
   try:
      if flag:
         chars = int(input('Введіть кількість символів --> '))
         flag = func(file, chars)
      else:
         break

   except ValueError:
      print('Помилка, спробуйте ще раз')
      continue


