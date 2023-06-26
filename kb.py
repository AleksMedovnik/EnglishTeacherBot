def create_markup(types):
    markup = types.ReplyKeyboardMarkup(
        keyboard=[[types.KeyboardButton(text='Сбросить до буквы "A" с сохранением счета')]],
        resize_keyboard=True
    )
    return markup