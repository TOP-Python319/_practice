# Написать функцию с именем int_base, которая преобразовывает число из произвольной системы счисления в произвольную.

# Функция принимает обязательными аргументами строковую запись числа, основание исходной системы счисления и основание целевой системы счисления.
    
#     Все аргументы должны быть позиционно-ключевыми.
    
#     Преобразовываемое число принимается в виде объекта str.
    
#     Основания систем счисления принимаются в виде объектов int, в диапазоне от 2 до 36 включительно.
#         Для записи дополнительных цифр в системах счисления с основанием больше десяти используйте латинские буквы от 'a' до 'z'. Имеет смысл сгенерировать словарь, задающий соотношения между числами в десятичной системе счисления и цифрами в системах счисления с бо́льшим основанием.
#         Следите за регистром буквенных символов.

# Функция возвращает строковое представление числа в целевой системе счисления или None в случае возникновения ошибок.

#     Ошибки могут возникать в следующих случаях:
#         - исходное или целевое основание системы счисления находится за пределами обозначенного выше диапазона
#         - строковое представление числа не соответствует заявленной исходной системе счисления
    
# Преобразования такого рода можно производить напрямую, но это потребует более сложной математики. В рамках данной задачи имеет смысл реализовать двойное преобразование: из исходной системы счисления в десятичную и затем из десятичной системы счисления в целевую. 

#     Представляется целесообразным каждое из этих двух преобразований реализовать в виде отдельной функции. Продумайте самостоятельно сигнатуры этих функций (набор параметров, их типы, возвращаемые значения).
    
#     О математике преобразований между системами счисления:
#         http://math-info.hse.ru/a/2021-22/ling-dm/lectures/lecture9_delim.pdf

# Написанную функцию необходимо протестировать вручную.
# Пример ручного теста:
#     >>> int_base('ff00', 16, 2)
#     '1111111100000000'
#     >>> int_base('1101010', 2, 30)
#     '3g'
