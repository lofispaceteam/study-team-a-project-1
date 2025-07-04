from fastapi import APIRouter
from datetime import datetime, timezone
import random

# Создаем роутер FastAPI для обработки запросов, связанных с акциями
router = APIRouter()

# Словарь с ассортиментом Bubble Tea и их обычными ценами
bubble_tea_prices = {
    # Классические
    "Классический черный чай с тапиокой": 190,
    "Зелёный чай с молоком": 200,
    "Тайский чай с молоком": 210,
    "Улонг с молоком": 220,
    "Жасминовый чай с молоком": 200,
    "Матча латте": 230,
    "Холодный кофе с тапиокой": 240,

    # Фруктовые
    "Клубничный Bubble Tea": 210,
    "Манго Bubble Tea": 220,
    "Личи Bubble Tea": 210,
    "Маракуйя Bubble Tea": 220,
    "Киви Bubble Tea": 210,
    "Персиковый Bubble Tea": 210,
    "Виноградный Bubble Tea": 220,
    "Апельсиновый Bubble Tea": 210,
    "Ананасовый Bubble Tea": 220,
    "Черника Bubble Tea": 230,
    "Арбузный Bubble Tea": 210,
    "Яблоко с алоэ": 200,

    # Десертные
    "Шоколадный Bubble Tea": 230,
    "Карамельный Bubble Tea": 230,
    "Ванильный Bubble Tea": 220,
    "Клубничный чизкейк": 240,
    "Кукис с кремом": 250,
    "Ореховый Bubble Tea": 230,
    "Латте с печеньем": 240,
    "Молочный улун с карамелью": 250,
    "Солёная карамель": 230,
    "Bubble Tea с маршмеллоу": 250,

    # Специальные
    "Бабл Ти «Радуга»": 260,
    "Фиолетовый Таро": 250,
    "Матча с кокосом": 250,
    "Черный кунжут": 240,
    "Дуриан Bubble Tea": 270,
    "Bubble Tea с сырной шапкой": 260,
    "Лавандовый Bubble Tea": 250,
    "Bubble Tea с васаби": 270,
}


# Эндпоинт для получения случайных промо-акций
@router.get("/promotions")
def get_promotions():
     # Получаем текущее время в UTC
    now = datetime.now(timezone.utc)

    # Используем минуту текущего времени как seed для генератора случайных чисел,
    # чтобы акции менялись каждую минуту, но оставались одинаковыми в течение этой минуты
    random.seed(now.minute)

    # Случайным образом выбираем 1 напиток из ассортимента
    selected = random.sample(list(bubble_tea_prices.items()), k=1)

    promotions = []
    for name, original_price in selected:

        discount_percent = random.randint(10, 40)
        discount_price = round(original_price * (1 - discount_percent / 100))

        # Формируем информацию об акции
        promotions.append({
            "product": name,
            "original_price": original_price,
            "discount_price": discount_price
        })

    # Возвращаем список промо-акций
    return {"promotions": promotions}