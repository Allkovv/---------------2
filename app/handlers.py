from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, Sticker
from aiogram import Dispatcher

import app.keyboards as kb


router = Router()
shopping_lists = {'Продукты': []}
addp= None
delp = None
addL = None
delL = None
selectList = None
userList = None

def upDate_userList(userText):
    global userList
    userList = userText
    print("List", userList)
    selectList_off()
    return userList

def on_off():
    global addp
    addp = True
    print("add on" ,addp)
    return addp

def test(func):
    global addp
    if func == True:
        print("YES", addp)
    else:
        print("NO", addp)

def off_on():
    global addp
    addp = False
    print("add off",addp)
    return addp

def del_on():
    global delp
    delp = True
    print("del", delp)
    return delp

def del_off():
    global delp
    delp = False
    print("Off del", delp)
    return delp

def add_List_on():
    global addL
    addL = True
    print("add List on",addL)
    return addL

def add_List_off():
    global addL
    addL = False
    print("add List off", addL)
    return addL

def del_List_on():
    global delL
    delL = True
    print("del List on",delL)
    return delL

def del_List_off():
    global delL
    delL = False
    print("del List off",delL)
    return delL

def selectList_on():
    global selectList
    selectList = True
    print("select List on", selectList)
    return selectList

def selectList_off():
    global selectList
    selectList = False
    print("Select List Off", selectList)
    return selectList



@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Привет, {message.from_user.full_name}. Тут вы можете следить за обновлениями, а также составлять свой список покупок =)', reply_markup=kb.start_keyboard)



async def show_lists(message: Message):
    text = "Списки:\n"
    for i, key in enumerate(shopping_lists,start=1):
        text += f"{i}. {key}\n"
    text += "\nВыберите действие или введите название списка, чтобы его открыть:"
    await message.answer(text, reply_markup=kb.lists_keyboard)
    
    
@router.message(F.text.lower() =='обновления')
async def show_menu(message: Message):
    await message.answer("На данный момент обновлений не было. \n Это бета-тест, ваши списки не сохраняются на всё время =))", reply_markup=kb.start_keyboard)

@router.message(F.text.lower() =='меню')
async def show_menu(message: Message):
    await message.answer("Меню", reply_markup=kb.start_keyboard)
    selectList_off()

@router.message(lambda message: message.text.lower() == 'списки')
async def show_shopping_lists(message: Message):
    await show_lists(message)
    return selectList_on()


@router.message(F.text == "1488")
async def pas1(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAEMDzBmOBowY9mvKuKtAAEbwjQzZneKUuUAAt0MAAJuSTBKW-PqgEzb1a01BA', reply_markup=kb.start_keyboard)
    selectList_off()
    add_List_off()
    del_List_off()
    del_off()
    off_on()
    
@router.message(F.text.lower() =='создать список')
async def add_list( message: Message):
    await message.answer("Чтобы создать новый список, напишите его название")
    selectList_off()
    return add_List_on()

@router.message(F.text.lower() =='удалить список')
async def del_list( message: Message):
    await message.answer("Чтобы удалить список, напишите его название")
    selectList_off()
    return del_List_on()

        
@router.message(F.text.lower() =='удалить продукт')
async def delete_product(message: Message):
    await message.answer("Для удаления продукта введите его номер")
    return del_on()


@router.message(F.text.lower() =='добавить продукт')
async def add_product( message: Message):
    await message.answer("Чтобы добавить введите название продукта")
    return on_off()

async def addProduct(message: Message):
    shopping_list = shopping_lists[userList]
    if len(shopping_list) == 0:
        text= "Список пуст\nВыберите действие:"
        await message.answer(text, reply_markup=kb.add_or_del)
    elif len(shopping_list) != 0:
        text = "Список продуктов:\n"
        for i, item in enumerate(shopping_list, start=1):
            text += f"{i}. {item}\n"
        text += "\nВыберите действие:"
        await message.answer(text, reply_markup=kb.add_or_del)
        selectList_off()

@router.message()
async def actions(message: Message):
    if selectList == True:
        try:
            upDate_userList(message.text)
            await addProduct(message)
        except KeyError:
            await message.answer("Неверное название списка")
            return selectList_off()
    elif addp == True:
        product_name = message.text
        shopping_list = shopping_lists[userList]
        shopping_list.append(product_name.lower())
        await message.answer(f"Продукт {product_name} добавлен в список.", reply_markup=kb.lists_keyboard)
        await addProduct(message)
        off_on()
    elif delp == True:
        try:
            input_number = int(message.text)
            shopping_list = shopping_lists[userList]
            if 1 <= input_number <= len(shopping_list):
                deleted_product = shopping_list.pop(input_number - 1)
                await message.answer(f"Продукт {deleted_product} удален из списка.", reply_markup=kb.lists_keyboard)
                await addProduct(message)
                del_off()
            else:
                await message.answer("Неверный номер продукта. Пожалуйста, введите корректный номер.")
        except ValueError:
            await message.answer("Неверный формат ввода. Пожалуйста, введите номер продукта для удаления.")
            del_off()
    elif addL == True:
        list_name = message.text
        shopping_lists[list_name] = []
        await message.answer(f"{list_name} добавлен в списки", reply_markup=kb.lists_keyboard)
        await show_lists(message)
        selectList_on()
        return add_List_off()
    elif delL == True:
        try:
            list_name = message.text
            del shopping_lists[list_name]
            await message.answer(f"{list_name} удалён из списков", reply_markup=kb.lists_keyboard)
            await show_lists(message)
            selectList_on()
            return del_List_off()
        except KeyError:
            await message.answer("Неверное название списка")
            return del_List_off()
    else:
        await message.answer("Список не выбран", reply_markup=kb.lists_keyboard)

