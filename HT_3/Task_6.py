# 6. Маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345" -> просто потицяв по клавi
#   Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює наступні випадки:
# -  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть букв та цифр
# -  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр (лише з буквами)
# -  якщо довжина бульше 50 - > ваша фантазiя '''

def function_BLABLA(value):
   digit = 0
   alpha = 0
   digit_summ = 0
   string = ''

   if len(value) >= 30 and len(value) <= 50:
      print('Lengs ', len(value))
      for element in value:
         if element.isdigit():
            digit += 1
         elif element.isalpha():
            alpha += 1
      print('Digit = ', digit)
      print('Alpha = ', alpha)

   elif len(value) < 30: 
      for element in value:
         if element.isdigit():
            digit_summ = digit_summ + int(element)
         elif element.isalpha():
            string = string + str(element)
      print('Digit summ = ', digit_summ)
      print('String = ', string)
   
   elif len(value) > 50:
      pass
   #if element.isdigit():
         
stroka = input('Enter what u want --> ')

function_BLABLA(stroka)
