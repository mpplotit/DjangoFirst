from django.shortcuts import render, HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from MainApp.models import Item

surname = 'Иванов'
firstname = 'Иван'
patronymic = 'Иванович'
phone = '+7(918)777-77-77'
email = 'XXX@mail.ru'

# items = [
#    {"id": 1, "name": "Кроссовки abibas"},
#    {"id": 2, "name": "Куртка кожаная"},
#    {"id": 3, "name": "Coca-cola 1 литр"},
#    {"id": 4, "name": "Картофель фри"},
#    {"id": 5, "name": "Кепка"},
# ]

# items = [
#    {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
#    {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
#    {"id": 3, "name": "Coca-cola 1 литр" ,"quantity":12},
#    {"id": 4, "name": "Картофель фри" ,"quantity":0},
#    {"id": 5, "name": "Кепка" ,"quantity":124},
# ]

items = Item.objects.all()


# Create your views here.
# def home(request):
#     return HttpResponse('''
# <h1>"Изучаем django"</h1>
# <strong>Автор</strong>: <i>Плотицин М. П.</i>
# ''')
def about(request):
    return HttpResponse(f'''
    Имя: <b>{firstname}</b> <br>
    Отчество: <b>{patronymic}</b><br>
    Фамилия: <b>{surname}</b> <br>
    Телефон: <b>{phone}</b> <br>
    email: <b>{email}</b> <br>
    ''')


def get_name_from_item_number(item_number):
    for item in items:
        if item.get('id') == item_number:
            return f'{item.get("name")}<br><a href="/items">Back</a>'
    return f'Товар с id={item_number} не найден'


# def view_item(request, item_number):
# return HttpResponse(get_name_from_item_number(item_number))
# def view_item(request, item_number):
#     for item in items:
#         if item.get('id') == item_number:
#             context = {'item': item}
#     return render(request, 'item.html', context)
def view_item(request, item_number):
    try:
        item = items.get(id=item_number)
    except ObjectDoesNotExist:
        raise Http404
    context = {'item': item,
               'Page': {'title': f'Описание товара {item.name}'}
               }
    return render(request, 'item.html', context)


# def view_all_items(request):
#     text = '<ol>'
#     for item in items:
#         text += f'<a href="item/{item.get("id")}"><li>{item.get("name")}</a></li>'
#     text += '</ol>'
#     return HttpResponse(text)

def home(request):
    context = {'Page': {'title': 'Главная страница сайта'}}
    return render(request, 'Index.html', context)


def view_all_items(request):
    context = {'items': items,
               'Page': {'title': 'Список товаров'}
               }
    return render(request, 'items_list.html', context)
