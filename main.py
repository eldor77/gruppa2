import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = '6029600676:AAHMpeGdRq-KQCbnnHZpi-w1QI0Po7azhLI'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


bosh_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ichimliklar "),
            KeyboardButton(text="Lavashlar "),
        ],
        [
            KeyboardButton(text="Pitsalar "),
            KeyboardButton(text="Burgerlar ")  
        ],
        [
            KeyboardButton(text="Shirinliklar "),
        ],
        [
            KeyboardButton(text="Manzillar"),
            KeyboardButton(text="Kontaktlar")
        ],
    ],
    resize_keyboard=True
)

ichimliklar_keyboards = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Pepsi"),
            KeyboardButton(text="Coca Sola"),
            KeyboardButton(text="Fanta"),
        ],
        [
            KeyboardButton(text="Orqaga")
        ]
    ],
    resize_keyboard=True
)

 
@dp.message_handler(commands=['start', 'menu'])
async def send_welcome(message: types.Message):
    await message.reply("Hello", reply_markup=bosh_menu)

 
@dp.message_handler(text="Ichimliklar")
async def send_welcome(message: types.Message):
    await message.reply("Mana", reply_markup=ichimliklar_keyboards)
    
 
@dp.message_handler(text="Pepsi")
async def send_welcome(message: types.Message):
    await message.answer_photo("https://zira.uz/wp-content/uploads/2018/07/pepsi-logo-cb80804ead-1.jpg",
                               caption="""
0.5l = 6000 so'm
1.0l = 9000 so'm 
1.5l = 12000 so'm 

""")


@dp.message_handler(text="Coca Sola")
async def send_welcome(message: types.Message):
    await message.answer_photo("https://dobryanka-rus.ru/storage/goods/343_qgTsd.jpg",
                               caption="""
0.5l = 6000 so'm
1.0l = 9000 so'm 
1.5l = 12000 so'm 

""")



@dp.message_handler(text="Fanta")
async def send_welcome(message: types.Message):
    await message.answer_photo("https://api.lochin.uz/media/file/image/2020-11/d5cfefae-ae9d-484c-a3a8-a9cd3f723258.jpg.500x500_q85_crop-scale.jpg",
                               caption="""
0.5l = 6000 so'm
1.0l = 9000 so'm 
1.5l = 12000 so'm 

""")
    

@dp.message_handler(text="Orqaga")
async def send_welcome(message: types.Message):
    await message.reply("Orqaga", reply_markup=bosh_menu)





Pitsalar_keyboards = ReplyKeyboardMarkup(
    keyboard=[      
        [
            KeyboardButton(text="Маргарита пицца"),
            KeyboardButton(text="Лава пицца"),
            KeyboardButton(text="Римская пицца"),
        ],
        [
            KeyboardButton(text="Orqaga")
        ]
    ],
    resize_keyboard=True
)


@dp.message_handler(text="Pitsalar")
async def send_welcome(message: types.Message):
    await message.reply("Mana", reply_markup=Pitsalar_keyboards)
    
 
@dp.message_handler(text="Маргарита пицца")
async def send_welcome(message: types.Message):
    await message.answer_photo("https://s0.tchkcdn.com/i/13/1/649892_3f86fdb4_b29_depositphotos_36567413_l_2015.jpg",
                               caption="""
Маленькая = 56000 so'm
Большая = 79000 so'm 


""")


@dp.message_handler(text="Лава пицца")
async def send_welcome(message: types.Message):
    await message.answer_photo("https://tasteofburlington.ca/wp-content/uploads/2022/01/Lava-Pizza.png",
                               caption="""
Маленькая = 56000 so'm
Большая = 79000 so'm 


""")



@dp.message_handler(text="Римская пицца")
async def send_welcome(message: types.Message):
    await message.answer_photo("https://pizzalider.ru/image/cache/data/pizza_new/pizza-2022-november/diyablo-1080x783.jpg",
                               caption="""
Маленькая = 56000 so'm
Большая = 79000 so'm 


""")
    

@dp.message_handler(text="Orqaga")
async def send_welcome(message: types.Message):
    await message.reply("Orqaga", reply_markup=bosh_menu)




Lavashlar_keyboards = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Дёнер-кебаб"),
            KeyboardButton(text="Лаваш с шашлыком"),
            KeyboardButton(text="Буррито"),
        ],
        [
            KeyboardButton(text="Orqaga")
        ]
    ],
    resize_keyboard=True
)


@dp.message_handler(text="Lavashlar")
async def send_welcome(message: types.Message):
    await message.reply("Mana", reply_markup=Lavashlar_keyboards)
    
 
@dp.message_handler(text="Дёнер-кебаб")
async def send_welcome(message: types.Message):
    await message.answer_photo("https://www.gastronom.ru/binfiles/images/20180729/b8db6c6c.jpg",
                               caption="""
Маленькая = 16000 so'm
Большая = 24000 so'm 


""")


@dp.message_handler(text="Лаваш с шашлыком")
async def send_welcome(message: types.Message):
    await message.answer_photo("https://povar24.info/wp-content/uploads/8/5/e/85e3ae69c965066619096db48d86972a.jpg",
                               caption="""
Маленькая = 26000 so'm
Большая = 39000 so'm 


""")



@dp.message_handler(text="Буррито")
async def send_welcome(message: types.Message):
    await message.answer_photo("https://www.chefmarket.ru/blog/wp-content/uploads/2018/06/3_1525325264_6e290.jpg",
                               caption="""
Маленькая = 19000 so'm
Большая = 27000 so'm 


""")
    

@dp.message_handler(text="Orqaga")
async def send_welcome(message: types.Message):
    await message.reply("Orqaga", reply_markup=bosh_menu)








Burgerlar_keyboards = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Чизбургер"),
            KeyboardButton(text="Черный бургер"),
            KeyboardButton(text="Фишбургер"),
        ],
        [
            KeyboardButton(text="Orqaga")
        ]
    ],
    resize_keyboard=True
)


@dp.message_handler(text="Burgerlar")
async def send_welcome(message: types.Message):
    await message.reply("Mana", reply_markup=Burgerlar_keyboards)
    
 
@dp.message_handler(text="Чизбургер")
async def send_welcome(message: types.Message):
    await message.answer_photo("https://st3.depositphotos.com/3957801/16168/i/600/depositphotos_161686374-stock-photo-bacon-cheese-burger.jpg",
                               caption="""
Маленькая = 29000 so'm
Большая = 37000 so'm 


""")


@dp.message_handler(text="Черный бургер")
async def send_welcome(message: types.Message):
    await message.answer_photo("https://kor.ill.in.ua/m/610x385/1818250.jpg",
                               caption="""
Маленькая = 99999999999999999 so'm
Большая = 9999999999999999999999999999999999 so'm 


""")



@dp.message_handler(text="Фишбургер")
async def send_welcome(message: types.Message):
    await message.answer_photo("https://menu2go.ru/images/food/135/135_252_20210518124723_3147.jpg",
                               caption="""
Маленькая = 24000 so'm
Большая = 32000 so'm 


""")
    

@dp.message_handler(text="Orqaga")
async def send_welcome(message: types.Message):
    await message.reply("Orqaga", reply_markup=bosh_menu)







Shirinliklar_keyboards = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Картошка"),
            KeyboardButton(text="Брауни"),
            KeyboardButton(text="Макарон"),
        ],
        [
            KeyboardButton(text="Orqaga")
        ]
    ],
    resize_keyboard=True
)


@dp.message_handler(text="Shirinliklar")
async def send_welcome(message: types.Message):
    await message.reply("Mana", reply_markup=Shirinliklar_keyboards)
    
 
@dp.message_handler(text="Картошка")
async def send_welcome(message: types.Message):
    await message.answer_photo("https://lifehacker.ru/wp-content/uploads/2019/06/shutterstock_1469365640_1608978931-scaled-e1608978983722.jpg",
                               caption="""
Маленькая = много so'm
Большая = просто дорого 


""")


@dp.message_handler(text="Брауни")
async def send_welcome(message: types.Message):
    await message.answer_photo("https://cdn.lifehacker.ru/wp-content/uploads/2020/02/shutterstock_447951334_1581518494-e1583314972343-1280x640.jpg",
                               caption="""
коробка Брауни = 120000 so'm



""")



@dp.message_handler(text="Макарон")
async def send_welcome(message: types.Message):
    await message.answer_photo("https://irecommend.ru/sites/default/files/imagecache/copyright1/user-images/86756/img_0888.jpg",
                               caption="""

четыре шт = 24000 so'm (штучно не продаем)
восемь шт = 46000 so'm (на две тысячи дешевле!😱)


""")
    

@dp.message_handler(text="Orqaga")
async def send_welcome(message: types.Message):
    await message.reply("Orqaga", reply_markup=bosh_menu)







@dp.message_handler(text="Manzillar")
async def send_welcome(message: types.Message):
    await message.answer_location(41.365790441164094, 69.28688709645179)




@dp.message_handler(text="Kontaktlar")
async def send_welcome(message: types.Message):
    await message.answer_contact(phone_number="+998 99 880 01 08", first_name="te")




@dp.message_handler(text="Video")
async def send_welcome(message: types.Message):
    await message.answer_video(video="https://t.me/groupback447/2")




@dp.message_handler(text="Gif")
async def send_welcome(message: types.Message):
    await message.answer_animation(animation="https://t.me/groupback447/3")





    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)



