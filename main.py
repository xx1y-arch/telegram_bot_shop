import telebot
from handlers import *

TOKEN = ''
bot = telebot.TeleBot(TOKEN)


def webhook(request):
    if request.method == "POST":
        bot.process_new_updates([types.Update.de_json(request.get_json(force=True))])
    return "ok", 200


@bot.message_handler(commands=['start'])
def command_pay(message):
    msg = bot.send_message(message.chat.id, "🏠Меню", reply_markup=menu_m)
    bot.register_next_step_handler(msg, brands)


def brands(message):
    chat_id = message.chat.id
    text = message.text
    if text == "Хайтопы":
        msg = bot.send_message(chat_id, 'Выберите бренд хайтопа', reply_markup=rating_markup)
        bot.register_next_step_handler(msg, hightop)
    elif text == "Кроссовки":
        msg1 = bot.send_message(chat_id, 'Выберите бренд кроссовок', reply_markup=rating_markup)
        bot.register_next_step_handler(msg1, krossovki)
    elif text == "Кроссовки для тренировок":
        msg2 = bot.send_message(chat_id, 'Выберите бренд кроссовок для трени', reply_markup=rating_markup)
        bot.register_next_step_handler(msg2, krosovki_sport)
    elif text == "🔶Актуальные модели кроссовок":
        msg3 = bot.send_message(chat_id, 'Hype Beast', reply_markup=rating_markup)
        bot.register_next_step_handler(msg3, trands)
    elif text == "Коллабы и эксклюзивы":
        msg4 = bot.send_message(chat_id, 'Exclusive collaborations', reply_markup=rating_markup)
        bot.register_next_step_handler(msg4, collabs)
    else:
        bot.send_message(chat_id, f"Такого раздела ({message.text}) не существует")


def hightop(message):
    chat_id = message.chat.id
    text = message.text
    if text == 'Nike':
        msg = bot.send_invoice(chat_id, title='Yezzy Boost 500',
                               description='Yezzy boost by kanye west',
                               provider_token="632593626:TEST:i48678063084",
                               currency='uah',
                               photo_url='https://www.flightclub.com/media/catalog/product/cache/1/image/1600x1140'
                                         '/9df78eab33525d08d6e5fb8d27136e95/8/0/804366_01.jpg',
                               photo_height=512,
                               photo_width=512,
                               photo_size=512,
                               is_flexible=False,
                               prices=price1,
                               start_parameter='yeezy-boost-500',
                               invoice_payload='CEBEK GIFT')
        bot.register_next_step_handler(msg, hightop)
    elif text == 'Puma':
        msg1 = bot.send_invoice(message.chat.id, title='Puma Thunder',
                                description='Лучше возьми Yezzy',
                                provider_token="632593626:TEST:i48678063084",
                                currency='uah',
                                photo_url='https://sneakerstudio.com.ua/rus_pl_%D0%9A%D1%80%D0%BE%D1%81%D1%81%D0%BE%D0%B2%D0'
                                          '%BA '
                                          '%D0%B8-Puma-Thunder-Spectra-367516-01-17077_1.jpg',
                                photo_height=512,
                                photo_width=512,
                                photo_size=512,
                                is_flexible=False,
                                prices=prices,
                                start_parameter='puma-thunder',
                                invoice_payload='CEBEK GIFT')
        bot.register_next_step_handler(msg1, hightop)
    elif text == "Adidas":
        msg2 = bot.send_invoice(message.chat.id, title='Raf Simons Ozweego',
                                description='raf simons 600',
                                provider_token="632593626:TEST:i48678063084",
                                currency='uah',
                                photo_url='http://cdn.shopify.com/s/files/1/1500/3934/products/adidas-x-raf-simons-ozweego-iii'
                                          '-purple-black-3_grande.jpg?v=1525816783',
                                photo_height=512,
                                photo_width=1024,
                                photo_size=512,
                                is_flexible=False,
                                prices=price2,
                                start_parameter='yeezy-boost-5000',
                                invoice_payload='CEBEK GIFT')
        bot.register_next_step_handler(msg2, hightop)

    elif text == "New Balance":
        msg3 = bot.send_invoice(message.chat.id, title='NB me546',
                                description='enochki',
                                provider_token="632593626:TEST:i48678063084",
                                currency='uah',
                                photo_url='https://cdn.laredoute.com/products/641by641/1/5/8'
                                          '/158f0d9ac1a8e04ad66837d16d3edfc9.jpg',
                                photo_height=512,
                                photo_width=512,
                                photo_size=512,
                                is_flexible=False,
                                prices=price3,
                                start_parameter='yeezy-boost-50000',
                                invoice_payload='CEBEK GIFT')
        bot.register_next_step_handler(msg3, hightop)
    elif text == "Назад":
        msg7 = bot.send_message(message.chat.id, "🏠Меню", reply_markup=menu_m)
        bot.register_next_step_handler(msg7, brands)


def krossovki(message):
    chat_id = message.chat.id
    text = message.text
    if text == 'Nike':
        msg = bot.send_invoice(chat_id, title='Yezzy Boost 500',
                               description='Yezzy boost by kanye west',
                               provider_token="",
                               currency='uah',
                               photo_url='https://www.flightclub.com/media/catalog/product/cache/1/image/1600x1140'
                                         '/9df78eab33525d08d6e5fb8d27136e95/8/0/804366_01.jpg',
                               photo_height=512,
                               photo_width=512,
                               photo_size=512,
                               is_flexible=False,
                               prices=price1,
                               start_parameter='yeezy-boost-500',
                               invoice_payload='CEBEK GIFT')
        bot.register_next_step_handler(msg, krossovki)
    elif text == 'Puma':
        msg1 = bot.send_invoice(message.chat.id, title='Puma Thunder',
                                description='Лучше возьми Yezzy',
                                provider_token="",
                                currency='uah',
                                photo_url='https://sneakerstudio.com.ua/rus_pl_%D0%9A%D1%80%D0%BE%D1%81%D1%81%D0%BE%D0%B2%D0'
                                          '%BA '
                                          '%D0%B8-Puma-Thunder-Spectra-367516-01-17077_1.jpg',
                                photo_height=512,
                                photo_width=512,
                                photo_size=512,
                                is_flexible=False,
                                prices=prices,
                                start_parameter='puma-thunder',
                                invoice_payload='CEBEK GIFT')
        bot.register_next_step_handler(msg1, krossovki)
    elif text == "Adidas":
        msg2 = bot.send_invoice(message.chat.id, title='Raf Simons Ozweego',
                                description='raf simons 600',
                                provider_token="",
                                currency='uah',
                                photo_url='http://cdn.shopify.com/s/files/1/1500/3934/products/adidas-x-raf-simons-ozweego-iii'
                                          '-purple-black-3_grande.jpg?v=1525816783',
                                photo_height=512,
                                photo_width=1024,
                                photo_size=512,
                                is_flexible=False,
                                prices=price2,
                                start_parameter='yeezy-boost-5000',
                                invoice_payload='CEBEK GIFT')
        bot.register_next_step_handler(msg2, krossovki)

    elif text == "New Balance":
        msg3 = bot.send_invoice(message.chat.id, title='NB me546',
                                description='enochki',
                                provider_token="",
                                currency='uah',
                                photo_url='https://cdn.laredoute.com/products/641by641/1/5/8'
                                          '/158f0d9ac1a8e04ad66837d16d3edfc9.jpg',
                                photo_height=512,
                                photo_width=512,
                                photo_size=512,
                                is_flexible=False,
                                prices=price3,
                                start_parameter='yeezy-boost-50000',
                                invoice_payload='CEBEK GIFT')
        bot.register_next_step_handler(msg3, krossovki)
    elif text == "Назад":
        msg7 = bot.send_message(message.chat.id, "🏠Меню", reply_markup=menu_m)
        bot.register_next_step_handler(msg7, brands)


def krosovki_sport(message):
    chat_id = message.chat.id
    text = message.text
    if text == 'Nike':
        msg = bot.send_invoice(chat_id, title='Yezzy Boost 500',
                               description='Yezzy boost by kanye west',
                               provider_token="",
                               currency='uah',
                               photo_url='https://cdn-images.farfetch-contents.com/13/37/31/57/13373157_15252456_480.jpg',
                               photo_height=512,
                               photo_width=512,
                               photo_size=512,
                               is_flexible=False,
                               prices=price1,
                               start_parameter='yeezy-boost-500',
                               invoice_payload='CEBEK GIFT')
        bot.register_next_step_handler(msg, krosovki_sport)
    elif text == 'Puma':
        msg1 = bot.send_invoice(message.chat.id, title='Puma Thunder',
                                description='Лучше возьми Yezzy',
                                provider_token="",
                                currency='uah',
                                photo_url='https://sneakerstudio.com.ua/rus_pl_%D0%9A%D1%80%D0%BE%D1%81%D1%81%D0%BE%D0%B2%D0'
                                          '%BA '
                                          '%D0%B8-Puma-Thunder-Spectra-367516-01-17077_1.jpg',
                                photo_height=512,
                                photo_width=512,
                                photo_size=512,
                                is_flexible=False,
                                prices=prices,
                                start_parameter='puma-thunder',
                                invoice_payload='CEBEK GIFT')
        bot.register_next_step_handler(msg1, krosovki_sport)
    elif text == "Adidas":
        msg2 = bot.send_invoice(message.chat.id, title='Raf Simons Ozweego',
                                description='raf simons 600',
                                provider_token="",
                                currency='uah',
                                photo_url='https://cdn-images.farfetch-contents.com/13/48/65/77/13486577_15842766_480.jpg',
                                photo_height=512,
                                photo_width=1024,
                                photo_size=512,
                                is_flexible=False,
                                prices=price2,
                                start_parameter='yeezy-boost-5000',
                                invoice_payload='CEBEK GIFT')
        bot.register_next_step_handler(msg2, krosovki_sport)

    elif text == "New Balance":
        msg3 = bot.send_invoice(message.chat.id, title='NB me546',
                                description='enochki',
                                provider_token="6325936:i48678063084",
                                currency='uah',
                                photo_url='https://cdn-images.farfetch-contents.com/13/04/36/93/13043693_14921977_480.jpg',
                                photo_height=512,
                                photo_width=512,
                                photo_size=512,
                                is_flexible=False,
                                prices=price3,
                                start_parameter='yeezy-boost-50000',
                                invoice_payload='CEBEK GIFT')
        bot.register_next_step_handler(msg3, krosovki_sport)
    elif text == "Назад":
        msg7 = bot.send_message(message.chat.id, "🏠Меню", reply_markup=menu_m)
        bot.register_next_step_handler(msg7, brands)


def trands(message):
    chat_id = message.chat.id
    text = message.text
    if text == 'Nike':
        msg = bot.send_invoice(chat_id, title='Yezzy Boost 500',
                               description='Yezzy boost by kanye west',
                               provider_token="",
                               currency='uah',
                               photo_url='https://cdn-images.farfetch-contents.com/13/35/39/54/13353954_16054219_480.jpg',
                               photo_height=512,
                               photo_width=512,
                               photo_size=512,
                               is_flexible=False,
                               prices=price1,
                               start_parameter='yeezy-boost-500',
                               invoice_payload='CEBEK GIFT')
        bot.register_next_step_handler(msg, trands)
    elif text == 'Puma':
        msg1 = bot.send_invoice(message.chat.id, title='Puma Thunder',
                                description='Лучше возьми Yezzy',
                                provider_token="",
                                currency='uah',
                                photo_url='https://cdn-images.farfetch-contents.com/13/38/99/64/13389964_15240291_480.jpg'
                                          '%D0%B8-Puma-Thunder-Spectra-367516-01-17077_1.jpg',
                                photo_height=512,
                                photo_width=512,
                                photo_size=512,
                                is_flexible=False,
                                prices=prices,
                                start_parameter='puma-thunder',
                                invoice_payload='CEBEK GIFT')
        bot.register_next_step_handler(msg1, trands)
    elif text == "Adidas":
        msg2 = bot.send_invoice(message.chat.id, title='Raf Simons Ozweego',
                                description='raf simons 600',
                                provider_token="",
                                currency='uah',
                                photo_url='https://cdn-images.farfetch-contents.com/12/96/03/33/12960333_13486531_480.jpg',
                                photo_height=512,
                                photo_width=1024,
                                photo_size=512,
                                is_flexible=False,
                                prices=price2,
                                start_parameter='yeezy-boost-5000',
                                invoice_payload='CEBEK GIFT')
        bot.register_next_step_handler(msg2, trands)

    elif text == "New Balance":
        msg3 = bot.send_invoice(message.chat.id, title='NB me546',
                                description='enochki',
                                provider_token="",
                                currency='uah',
                                photo_url='https://cdn.laredoute.com/products/641by641/1/5/8'
                                          '/158f0d9ac1a8e04ad66837d16d3edfc9.jpg',
                                photo_height=512,
                                photo_width=512,
                                photo_size=512,
                                is_flexible=False,
                                prices=price3,
                                start_parameter='yeezy-boost-50000',
                                invoice_payload='CEBEK GIFT')
        bot.register_next_step_handler(msg3, trands)
    elif text == "Назад":
        msg7 = bot.send_message(message.chat.id, "🏠Меню", reply_markup=menu_m)
        bot.register_next_step_handler(msg7, brands)


def collabs(message):
    chat_id = message.chat.id
    text = message.text
    if text == 'Nike':
        msg = bot.send_invoice(chat_id, title='Yezzy Boost 500',
                               description='Yezzy boost by kanye west',
                               provider_token="",
                               currency='uah',
                               photo_url='https://cdn-images.farfetch-contents.com/13/31/17/60/13311760_14940306_480.jpg',
                               photo_height=512,
                               photo_width=512,
                               photo_size=512,
                               is_flexible=False,
                               prices=price1,
                               start_parameter='yeezy-boost-500',
                               invoice_payload='CEBEK GIFT')
        bot.register_next_step_handler(msg, collabs)
    elif text == 'Puma':
        msg1 = bot.send_invoice(message.chat.id, title='Puma Thunder',
                                description='Лучше возьми Yezzy',
                                provider_token="",
                                currency='uah',
                                photo_url='https://cdn.laredoute.com/products/641by641/1/5/8'
                                          '/158f0d9ac1a8e04ad66837d16d3edfc9.jpg',
                                photo_height=512,
                                photo_width=512,
                                photo_size=512,
                                is_flexible=False,
                                prices=prices,
                                start_parameter='puma-thunder',
                                invoice_payload='CEBEK GIFT')
        bot.register_next_step_handler(msg1, collabs)
    elif text == "Adidas":
        msg2 = bot.send_invoice(message.chat.id, title='Raf Simons Ozweego',
                                description='raf simons 600',
                                provider_token="6",
                                currency='uah',
                                photo_url='https://cdn-images.farfetch-contents.com/12/96/02/37/12960237_13486444_480.jpg',
                                photo_height=512,
                                photo_width=512,
                                photo_size=512,
                                is_flexible=False,
                                prices=price2,
                                start_parameter='yeezy-boost-5000',
                                invoice_payload='CEBEK GIFT')
        bot.register_next_step_handler(msg2, collabs)

    elif text == "New Balance":
        msg3 = bot.send_invoice(message.chat.id, title='NB me546',
                                description='enochki',
                                provider_token="",
                                currency='uah',
                                photo_url='https://cdn-images.farfetch-contents.com/12/96/09/99/12960999_13547587_480.jpg',
                                photo_height=512,
                                photo_width=512,
                                photo_size=512,
                                is_flexible=False,
                                prices=price3,
                                start_parameter='yeezy-boost-50000',
                                invoice_payload='CEBEK GIFT')
        bot.register_next_step_handler(msg3, collabs)
    elif text == "Назад":
        msg7 = bot.send_message(message.chat.id, "🏠Меню", reply_markup=menu_m)
        bot.register_next_step_handler(msg7, brands)


@bot.shipping_query_handler(func=lambda query: True)
def shipping(shipping_query):
    print(shipping_query)
    bot.answer_shipping_query(shipping_query.id, ok=True, shipping_options=shipping_options,
                              error_message='Oh, seems like our Dog couriers are having a lunch right now. Try again '
                                            'later!')


@bot.pre_checkout_query_handler(func=lambda query: True)
def checkout(pre_checkout_query):
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True,
                                  error_message="Aliens tried to steal your card's CVV, but we successfully protected "
                                                "your credentials, "
                                                " try to pay again in a few minutes, we need a small rest.")


@bot.message_handler(content_types=['successful_payment'])
def got_payment(message):
    bot.send_message(message.chat.id,
                     'Hoooooray! Thanks for payment! We will proceed your order for `{} {}` as fast as possible! '
                     'Stay in touch.\n\nUse /buy again to get a Puma THUNDER for your friend!'.format(
                         message.successful_payment.total_amount / 100, message.successful_payment.currency),
                     parse_mode='Markdown')


