from telebot import *
from telebot.types import LabeledPrice, ShippingOption


rating_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
rating_markup_btn1 = types.KeyboardButton('🔴Nike')
rating_markup_btn2 = types.KeyboardButton('⚫️Puma')
rating_markup_btn3 = types.KeyboardButton('🔵Adidas')
rating_markup_btn4 = types.KeyboardButton('⚪️New Balance')
rating_markup_btn5 = types.KeyboardButton('🔙Назад')
rating_markup.row(rating_markup_btn1, rating_markup_btn2)
rating_markup.row(rating_markup_btn3, rating_markup_btn4)
rating_markup.row(rating_markup_btn5)


menu_m = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
m1 = types.KeyboardButton("Хайтопы")
m2 = types.KeyboardButton("Кроссовки")
m3 = types.KeyboardButton("Кроссовки для тренировок")
m4 = types.KeyboardButton("Коллабы и эксклюзивы")
m5 = types.KeyboardButton("🔶Актуальные модели кроссовок")
menu_m.row(m1, m2)
menu_m.row(m3, m4)
menu_m.row(m5)

nazad1 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
n11 = types.KeyboardButton("🔙Назад")
nazad1.row(n11)

prices = [LabeledPrice(label='Puma Thunder', amount=650000), LabeledPrice('Gift wrapping', 50000)]
price1 = [LabeledPrice(label='Yeezy Boost 500', amount=1050000), LabeledPrice('Gift wrapping', 50000)]
price2 = [LabeledPrice(label='NB me547', amount=400000), LabeledPrice('Gift wrapping', 50000)]
price3 = [LabeledPrice(label='Raf Simons Ozweego', amount=800000), LabeledPrice('Gift wrapping', 50000)]

shipping_options = [
    ShippingOption(id='instant', title='Puma Thunder').add_price(LabeledPrice('Shoes', 1000)),
    ShippingOption(id='pickup', title='Local pickup').add_price(LabeledPrice('Pickup', 300))]