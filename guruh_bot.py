import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# =====================
# SOZLAMALAR (o'zgartiring)
# =====================
BOT_TOKEN = "SIZNING_BOT_TOKENINGIZ"  # @BotFather dan olingan token
GURUH_LINK = "https://t.me/sizning_guruhingiz"  # Guruh linki
GURUH_NOMI = "Mening Guruhim"  # Guruh nomi
GURUH_TAVSIF = "Bu guruhda foydali ma'lumotlar, yangiliklar va ko'p narsalar bor!"

# =====================
# BOT VA DISPATCHER
# =====================
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# =====================
# /start KOMANDASI
# =====================
@dp.message(CommandStart())
async def start_handler(message: types.Message):
    ism = message.from_user.first_name

    # Tugmalar
    tugmalar = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📢 Guruhga qo'shilish", url=GURUH_LINK)],
        [InlineKeyboardButton(text="👥 Do'stga tavsiya qilish", switch_inline_query=f"Qo'shiling! {GURUH_NOMI} - {GURUH_LINK}")]
    ])

    xabar = (
        f"Salom, {ism}! 👋\n\n"
        f"🌟 <b>{GURUH_NOMI}</b> guruhiga xush kelibsiz!\n\n"
        f"📌 <b>Guruh haqida:</b>\n{GURUH_TAVSIF}\n\n"
        f"👇 Quyidagi tugma orqali guruhga qo'shiling yoki do'stlaringizga tavsiya qiling!"
    )

    await message.answer(xabar, parse_mode="HTML", reply_markup=tugmalar)

# =====================
# /tavsiya KOMANDASI
# =====================
@dp.message(Command("tavsiya"))
async def tavsiya_handler(message: types.Message):
    ism = message.from_user.first_name
    user_id = message.from_user.id

    # Do'stga yuborish uchun havola
    tavsiya_matni = (
        f"🔗 Do'stingizga shu xabarni yuboring:\n\n"
        f"👉 {GURUH_NOMI} guruhiga qo'shiling!\n"
        f"{GURUH_TAVSIF}\n\n"
        f"🔗 Link: {GURUH_LINK}"
    )

    tugmalar = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="📤 Do'stga yuborish",
            switch_inline_query=tavsiya_matni
        )]
    ])

    await message.answer(
        f"{ism}, quyidagi xabarni do'stlaringizga yuboring! 👇",
        reply_markup=tugmalar
    )

# =====================
# /guruh KOMANDASI
# =====================
@dp.message(Command("guruh"))
async def guruh_handler(message: types.Message):
    tugmalar = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📢 Guruhga o'tish", url=GURUH_LINK)]
    ])

    await message.answer(
        f"📌 <b>{GURUH_NOMI}</b>\n\n"
        f"{GURUH_TAVSIF}\n\n"
        f"🔗 Link: {GURUH_LINK}",
        parse_mode="HTML",
        reply_markup=tugmalar
    )

# =====================
# BOSHQA XABARLAR
# =====================
@dp.message()
async def boshqa_handler(message: types.Message):
    tugmalar = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📢 Guruhga qo'shilish", url=GURUH_LINK)],
    ])

    await message.answer(
        "Komandalar:\n"
        "/start — Boshlanish\n"
        "/guruh — Guruh haqida\n"
        "/tavsiya — Do'stga tavsiya qilish",
        reply_markup=tugmalar
    )

# =====================
# BOTNI ISHGA TUSHIRISH
# =====================
async def main():
    logging.basicConfig(level=logging.INFO)
    print("Bot ishga tushdi! ✅")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
