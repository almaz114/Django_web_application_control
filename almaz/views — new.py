from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
# from loguru import logger
# from class_json import read_from_json  # для работы с json
import json
# import numpy as np
# from django.contrib.gis.shortcuts import numpy     # эксперимент для numpy
# from django.contrib.gis.shortcuts import numpy
# from django.contrib import numpy        # импорт numpy из папки django

import datetime
from datetime import date, time, timedelta
from datetime import datetime


# -- простой пример вывода
def index(request):
    """простая функция представления"""
    # with open('files/hedge_martin.json') as f:
    #     d = json.load(f)
    #     print(d)

    return HttpResponse("Страница приложения almaz")


# -- пример № 2 применение шаблонов
def index_2(request):
    """простая функция представления"""
    # dict_a = read_from_json(path_file="files/account_info.json")  # read levels from json file
    # login = dict_a["Login"]  # загружаем значения_список для данного ключа

    data = {"header": "Hello Django", "message": "Welcome to Python"}
    return render(request, "almaz/index.html", context=data)
    # return render(request, "almaz/index.html", {"menu": menu})


# -- пример № 3 применение шаблонов: из раных типов массивов данных (списка, словаря)
def index_3(request):
    """простая функция представления"""
    # dict_a = read_from_json(path_file="files/account_info.json")  # read levels from json file
    # login = dict_a["Login"]  # загружаем значения_список для данного ключа

    header = "Personal Data"  # обычная переменная
    langs = ["English", "German", "Spanish"]  # массив
    user = {"name": "Tom", "age": 23}  # словарь
    addr = ("Абрикосовая", 23, 45)  # кортеж
    data = {"header": header, "langs": langs, "user": user, "address": addr}

    return render(request, "almaz/worker.html", context=data)


# -- пример № 4 применение шаблонов и формы для передачи данных из формы
# @logger.catch()
def index_4(request):
    """простая функция представления для hedge_martin"""
    with open('C:/xampp/htdocs/almaz/files/hedge_martin.json') as f:
        dict_a = json.load(f)
        dict_b = dict_a["EURUSD"]

    if request.method == "POST":
        today_time = datetime.today().strftime("%d-%m-%Y-%H:%M")  # получим тек время
        high_level_new = request.POST.get("high_level")
        low_level_new = request.POST.get("low_level")  # получение значения поля age
        step_1, step_2 = request.POST.get("step_1"), request.POST.get("step_2")
        step_3, step_4 = request.POST.get("step_3"), request.POST.get("step_4")
        step_5, step_6 = request.POST.get("step_5"), request.POST.get("step_6")
        step_7 = request.POST.get("step_7")
        # print(f"xxx : {high_level_new} + {low_level_new}")

        dict_b["high_level"] = high_level_new.replace(',', '.')  # присвоим новое
        dict_b["low_level"] = low_level_new.replace(',', '.')   # значение словаря по ключу login
        dict_b["last_update"] = str(today_time)  # add date/time to dict
        steps_temp = [step_1, step_2, step_3, step_4, step_5, step_6, step_7]
        steps_temp_1 = []   # create new empty list for steps
        for step in steps_temp:
            if step != "":
                step_new = step.replace(',', '.')   # замена ","" на "."
                steps_temp_1.append(step_new)       # add new step in list

        new_list = [float(i) for i in steps_temp_1]
        dict_b["steps"] = new_list          # add new list steps for dict

        dict_a["EURUSD"] = dict_b     # create new dict with new data
        # logger.info(f"new dict_a: {dict_a}")

        # --> save new dict to json file
        with open('C:/xampp/htdocs/almaz/files/hedge_martin.json', 'w') as f:
            json.dump(dict_a, f)  # save new dict_a to json file

        return HttpResponse(f"<h2>Hello, {0}</h2>{high_level_new} + {low_level_new}")
    else:
        userform = UserForm()
        return render(request, "almaz/write.html", {"form": userform})


def index_5(request):
    """простая функция представления и редактирования с использованием формы для trade_extremum"""
    trend_new = ""
    with open('C:/xampp/htdocs/almaz/files/trade_extremum.json') as f:
        dict_a = json.load(f)

    if request.method == "POST":
        # now = datetime.now()  # получим тек дату/время
        today_time = datetime.today().strftime("%d-%m-%Y-%H:%M")
        print(f"datetime : {today_time}")
        user_name = request.POST.get("user_name")
        high_level_new = request.POST.get("high_level")  # получаем значения из поля формы high_level
        low_level_new = request.POST.get("low_level")
        trend = request.POST.get("trend")

        print(f"trend: {trend, type(trend)}")
        if trend == "1":
            trend_new = 0   # 0 -> восходящий тренд
            print(f"восходящий тренд")
            # dict_a["trend"] = trend_new  # присвоим новое значение словаря по ключу login
        elif trend == "2":
            trend_new = 1   # -> нисходящий тренд
            print(f"нисходящий тренд")
            # dict_a["trend"] = trend_new  # присвоим новое значение словаря по ключу login

        dict_a["high_level"] = float(high_level_new.replace(',', '.'))  # присвоили новое  полей
        dict_a["low_level"] = float(low_level_new.replace(',', '.'))    # значения для соот-их
        dict_a["trend"] = trend_new  # присвоим новое значение словаря по ключу login
        dict_a["last_update"] = str(today_time)
        # logger.info(f"new dict: {dict}")
        with open('C:/xampp/htdocs/almaz/files/trade_extremum.json', 'w') as f:
            json.dump(dict_a, f)  # save new dict to json file

        return HttpResponse(f"<h2>{user_name}, Вы ввели след значения:</h2>"
                            f"high_level: {high_level_new} and low_level: {low_level_new};"
                            f"  Trend: {trend_new}")
    else:
        userform = Form_Trade_Extremum()  # используем нашу форму для данного алгоритма
        return render(request, "almaz/write.html", {"form": userform})


def index_6(request):
    """простая функция представления для вывода итоговых данных из json файлов"""
    with open('C:/xampp/htdocs/almaz/files/trade_extremum.json') as f:
        dict_a = json.load(f)

    with open('C:/xampp/htdocs/almaz/files/hedge_martin.json') as d:
        dict_b = json.load(d)
        dict_b_2 = dict_b["EURUSD"]
        high_level, low_level = dict_b_2["high_level"], dict_b_2["low_level"]

    header = "Данные отчета с файлов json"  # обычная переменная
    algorithm = ["Hedge_Martin", "Trade_Extremum"]  # массив
    levels_hedge = [high_level, low_level]
    # dict_a
    name = {"name": "Tom", "age": 23}  # словарь
    addr = ("Абрикосовая", 23, 45)  # кортеж
    data = {"header": header, "algorithm": algorithm, "levels": levels_hedge,
            "trade_extremum": dict_a, "user": name, "address": addr}

    return render(request, "almaz/otchet.html", context=data)


def index_7(request):
    """простая функция представления для вывода итоговых данных из json файлов в виде таблицы + css"""
    with open('C:/xampp/htdocs/almaz/files/trade_extremum.json') as f:
        dict_a = json.load(f)

    with open('C:/xampp/htdocs/almaz/files/hedge_martin.json') as d:
        dict_b = json.load(d)
        dict_b_2 = dict_b["EURUSD"]
        high_level, low_level = dict_b_2["high_level"], dict_b_2["low_level"]

    header = "Данные отчета с файлов json"  # обычная переменная
    algorithm = ["Hedge_Martin", "Trade_Extremum"]  # массив
    levels_hedge = [high_level, low_level]
    # dict_a
    name = {"name": "Tom", "age": 23}  # словарь
    addr = ("Абрикосовая", 23, 45)  # кортеж
    data = {"header": header, "algorithm": algorithm, "levels": levels_hedge,
            "trade_extremum": dict_a, "user": name, "address": addr}

    return render(request, "almaz/table_algoritms.html", context=data)
