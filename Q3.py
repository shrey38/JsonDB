def pin_conversation(chat_id):
   
    chat_data = get_chat_data(chat_id)

    
    chat_data['pinned'] = True

    update_chat_data(chat_id, chat_data)

def get_chat_data(chat_id):
    
    chat_data = {
        'id': chat_id,
        'pinned': False
    }
    return chat_data

def update_chat_data(chat_id, chat_data):
    print(f"Updating chat data for chat {chat_id} with pinned flag {chat_data['pinned']}")


pin_conversation('1234')
