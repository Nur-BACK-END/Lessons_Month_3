from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from buttons import cancel_markup, start_markup


class FSMShop(StatesGroup):
    model = State()
    size = State()
    category = State()
    price = State()
    photo = State()


async def start_shop(message: types.Message):
    await message.answer("Введите название модели:", reply_markup=cancel_markup)
    await FSMShop.model.set()

async def load_model(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['model'] = message.text
    await FSMShop.next()
    await message.answer("Введите размер:")


async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text
    await FSMShop.next()
    await message.answer("Введите категорию:")


async def load_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text
    await FSMShop.next()
    await message.answer("Введите стоимость:")


async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text
    await FSMShop.next()
    await message.answer("Отправьте фотографию товара:")


async def result(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id
    await message.answer("Данные о товаре:")
    await message.answer_photo(photo=data['photo'], caption=f"Модель: {data['model']}\n"
                                f"Размер: {data['size']}\n"
                                f"Категория: {data['category']}\n"
                                f"Цена: {data['price']}\n")
    await state.finish()


async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer("Добавление товара отменено.", reply_markup=start_markup)


def register_fsm_shop(dp: Dispatcher):
    dp.register_message_handler(cancel_handler, Text(equals='отмена',
                                                     ignore_case=True), state='*')
    dp.register_message_handler(start_shop, commands='buy')
    dp.register_message_handler(load_model, state=FSMShop.model)
    dp.register_message_handler(load_size, state=FSMShop.size)
    dp.register_message_handler(load_category, state=FSMShop.category)
    dp.register_message_handler(load_price, state=FSMShop.price)
    dp.register_message_handler(result, state=FSMShop.photo, content_types=['photo'])

