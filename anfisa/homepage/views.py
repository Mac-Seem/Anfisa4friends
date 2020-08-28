from django.shortcuts import render
from icecream.models import icecream_db
from anfbot.models import friends_db
from anfbot.services import what_weather


def index(request):

    icecreams = ''
    friends = ''
    city_weather = ''
    friend_output = ''
    # Добавили выбранное мороженное, которое получим из формы
    selected_icecream = ''

    for friend in friends_db:
        # Около каждого имени вставляется radio button,
        # и теперь в форме кликом по кнопочке можно будет выбрать одного из друзей.
        friends += (f'<input type="radio" name="friend"'
                   f' required value="{friend}">{friend}<br>')

    # Из списка ссылок icecreams сделаем список чекбоксов
    for i in range(len(icecream_db)):
        ice_form = ''
        ice_link = f'<a href="icecream/{i}/"> Узнать состав</a>'
        icecreams += (f'<input type="radio" name ="icecream"'
                      f' required value="{icecream_db[i]["name"]}">{icecream_db[i]["name"]} <br>')

    if request.method == 'POST':
        # Извлекли из запроса имя друга
        selected_friend = request.POST['friend']
        # Название мороженого из POST-запроса сохраните в переменную selected_icecream
        selected_icecream = request.POST['icecream']

        # Записали название города в переменную city
        city = friends_db[selected_friend]
        # Запросили погоду в городе city
        weather = what_weather(city)

        # Вместо слова "мороженое" выведите название сорта из запроса.
        friend_output = f'{selected_friend}, тебе прислали {selected_icecream}!'
        city_weather = f'В городе {city} погода: {weather}'

    context = {
        'icecreams': icecreams,
        'friends': friends,
        'friend_output': friend_output,
        'city_weather': city_weather,
    }
    return render(request, 'homepage/index.html', context)
