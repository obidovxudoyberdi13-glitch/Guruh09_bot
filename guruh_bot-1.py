import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

# =====================
# SOZLAMALAR
# =====================
BOT_TOKEN = os.getenv("BOT_TOKEN", "SIZNING_BOT_TOKENINGIZ")
GURUH_LINK = "https://t.me/sizning_guruhingiz"
GURUH_NOMI = "Mening Guruhim"
GURUH_TAVSIF = "Bu guruhda foydali ma'lumotlar va ko'p narsalar bor!"

# =====================
# BOT VA DISPATCHER
# =====================
logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# =====================
# /start KOMANDASI
# =====================
@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    ism = message.from_user.first_name
    tugmalar = InlineKeyboardMarkup()
    tugmalar.add(InlineKeyboardButton("📢 Guruhga qo'shilish", url=GURUH_LINK))
    tugmalar.add(InlineKeyboardButton("👥 Do'stga tavsiya", switch_inline_query=f"Qo'shiling! {GURUH_NOMI} - {GURUH_LINK}"))

    await message.answer(
        f"Salom, {ism}! 👋\n\n"
        f"🌟 <b>{GURUH_NOMI}</b> guruhiga xush kelibsiz!\n\n"
        f"📌 {GURUH_TAVSIF}\n\n"
        f"👇 Guruhga qo'shiling yoki do'stlaringizga tavsiya qiling!",
        parse_mode="HTML",
        reply_markup=tugmalar
    )

# =====================
# /guruh KOMANDASI
# =====================
@dp.message_handler(commands=["guruh"])
async def guruh_handler(message: types.Message):
    tugmalar = InlineKeyboardMarkup()
    tugmalar.add(InlineKeyboardButton("📢 Guruhga o'tish", url=GURUH_LINK))
    await message.answer(
        f"📌 <b>{GURUH_NOMI}</b>\n\n{GURUH_TAVSIF}\n\n🔗 {GURUH_LINK}",
        parse_mode="HTML",
        reply_markup=tugmalar
    )

# =====================
# /tavsiya KOMANDASI
# =====================
@dp.message_handler(commands=["tavsiya"])
async def tavsiya_handler(message: types.Message):
    tugmalar = InlineKeyboardMarkup()
    tugmalar.add(InlineKeyboardButton("📤 Do'stga yuborish", switch_inline_query=f"{GURUH_NOMI} - {GURUH_LINK}"))
    await message.answer("Do'stlaringizga yuboring! 👇", reply_markup=tugmalar)

# =====================
# BOSHQA XABARLAR
# =====================
@dp.message_handler()
async def boshqa_handler(message: types.Message):
    tugmalar = InlineKeyboardMarkup()
    tugmalar.add(InlineKeyboardButton("📢 Guruhga qo'shilish", url=GURUH_LINK))
    await message.answer(
        "Komandalar:\n/start — Boshlanish\n/guruh — Guruh haqida\n/tavsiya — Do'stga tavsiya",
        reply_markup=tugmalar
    )

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
