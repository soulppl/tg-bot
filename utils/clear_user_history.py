from aiogram.dispatcher import FSMContext


async def clear_user_history(state: FSMContext):
    async with state.proxy() as globalState:
        try:
            cached_message = globalState["_message"]
            if cached_message:
                await cached_message.delete()
            if cached_message.reply_to_message:
                await cached_message.reply_to_message.delete()
        except Exception as inst:
            globalState["_message"] = None
            print('Error: message not found')

    await state.finish()
