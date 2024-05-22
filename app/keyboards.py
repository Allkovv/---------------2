from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import types

start_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Обновления'), KeyboardButton(text='Списки')]
    ],resize_keyboard=True)

lists_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Меню')],
    [KeyboardButton(text='Создать список'), KeyboardButton(text="Удалить список")]
    ],resize_keyboard=True)

add_or_del = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Добавить продукт'), KeyboardButton(text='Удалить продукт')],
    [KeyboardButton(text=('Списки'))]
    ],resize_keyboard=True)

register = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Пароль")]
], resize_keyboard=True)