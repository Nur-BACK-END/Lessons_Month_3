from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from buttons import cancel_markup, start_markup
from aiogram.types import ReplyKeyboardRemove
from db.main_db import sql_insert_store, sql_insert_products_details


class FSMStore(StatesGroup):
    modelname = State()
    size = State()
    category = State()
    price = State()
    photo = State()
    productid = State()
    category_extra = State()
    infoproduct = State()
    Submit = State()

async def start_fsm_store(message: types.Message):
    await message.answer('Введите название модели:', reply_markup=cancel_markup)
    await FSMStore.modelname.set()

async def load_modelname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['modelname'] = message.text

    await FSMStore.next()
    await message.answer('Введите размер : ')

async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

    await FSMStore.next()
    await message.answer('Введите категорию модели: ')

async def load_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text

    await FSMStore.next()
    await message.answer('Введите цену : ')

async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text

    await FSMStore.next()
    await message.answer('Отправьте фото модели: ')

async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id

    await FSMStore.next()
    await message.answer('Введите id продукта: ')

async def load_productid(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['productid'] = message.text

    await FSMStore.next()
    await message.answer('Введите категорию модели: ')

async def load_category_extra(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category_extra'] = message.text

    await FSMStore.next()
    await message.answer('Введите инфопродукт модели: ')

async def load_infoproduct(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['infoproduct'] = message.text

    await FSMStore.next()
    await message.answer(f'вот результат')
    await message.answer_photo(photo=data['photo'],
                               caption=f'model - {data["modelname"]}\n'
                                       f'size - {data["size"]}\n'
                                       f'category - {data["category"]}\n'
                                       f'price - {data["price"]}\n'
                                       f'\n'
                                       f"information about model: \n"
                                       f'product id - {data["productid"]}\n'
                                       f'category - {data["category_extra"]}\n'
                                       f'infoproduct - {data["infoproduct"]}\n')


async def load_submit(message: types.Message, state: FSMContext):
    if message.text.lower().strip() == 'да':
        async with state.proxy() as data:
            await sql_insert_store(
                data['modelname'],
                data['size'],
                data['price'],
                data['productid'],
                data['photo']
            )
            await sql_insert_products_details(
                data['productid'],
                data['category_extra'],
                data['infoproduct']
            )

        await message.answer('все это сохранено')
        await state.finish()

    elif message.text.lower().strip() == 'нет':
        await message.answer('было отменено.', reply_markup=start_markup)
        await state.finish()

    else:
        await message.answer('Введите да или нет.')

async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()

    if current_state is not None:
        await state.finish()
        await message.answer('Было отменено!', reply_markup=start_markup)

def register_fsmstore_handlers(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm, Text(equals='cancel',
                                                 ignore_case=True), state='*')

    dp.register_message_handler(start_fsm_store, commands=['registration_store'])
    dp.register_message_handler(load_modelname, state=FSMStore.modelname)
    dp.register_message_handler(load_size, state=FSMStore.size)
    dp.register_message_handler(load_category, state=FSMStore.category)
    dp.register_message_handler(load_price, state=FSMStore.price)
    dp.register_message_handler(load_photo, state=FSMStore.photo, content_types=['photo'])
    dp.register_message_handler(load_productid, state=FSMStore.productid)
    dp.register_message_handler(load_category_extra, state=FSMStore.category_extra)
    dp.register_message_handler(load_infoproduct , state=FSMStore.infoproduct)
    dp.register_message_handler(load_submit, state=FSMStore.Submit)