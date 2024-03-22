# Написать функцию с именем strong_password, которая проверяет, является ли пароль надёжным.

# Функция принимает обязательным позиционно-ключевым аргументом пароль в виде объекта str.

# Функция возвращает объект bool.

# Пароль считается надёжным, если соблюдены все нижеследующие условия:
#     - длина пароля составляет восемь символов и более
#     - в пароле присутствуют буквенные символы в обоих регистрах
#     - в пароле присутствуют минимум два символа цифр
#     - кроме символов букв и цифр в пароле присутствуют символы прочих категорий 
#       (пробел, знаки пунктуации, диакритические знаки и т.п.)

# Написанную функцию необходимо протестировать вручную.
# Пример ручного теста:
#     >>> strong_password('aP3:kD_l3')
#     True
#     >>> strong_password('password')
#     False


def strong_password(password: str) -> bool:
    # длина пароля составляет восемь символов и более
    if len(password) < 8:
        return False
    
    # в пароле присутствуют буквенные символы в обоих регистрах
    elif password.isupper() or password.islower():
        return False
    
    # в пароле присутствуют минимум два символа цифр
    elif len(set(password) & set('1234567890')) < 2:
        return False

    # кроме символов букв и цифр в пароле присутствуют символы прочих категорий
    elif len(set(password) & set('!@#$%^&*()_+-=[];:,./<>?')) < 1:
        return False
    else:
        return True


print(strong_password('aP1:kD_l0'))  # True
print(strong_password('password'))  # False