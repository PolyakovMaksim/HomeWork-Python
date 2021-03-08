def form(name, surname, burth_year, recidence_city, email, phone):
    print(
        f"Привет, {name} {surname}, расскажи мне про {recidence_city}! Ты живешь там с {burth_year} года? "
        f"Напиши мне с {email} или позвони с {phone}.")
a = input('Введите Ваше имя: ')
b = input('Введите Вашу фамилию: ')
c = input('В каком году Вы родились: ')
d = input('В каком городе вы живете: ')
e = input('Ваш email: ')
f = input('Ваш номер телефона: ')
form(phone = f, email = e, recidence_city = d, burth_year = c, surname = b, name = a)