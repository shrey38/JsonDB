def add_tags(chat_id, tags):
   
    chat_data = get_chat_data(chat_id)

    
    for t in tags:
        if t not in chat_data['tags']:
            chat_data['tags'].append(t)

   
    update_chat_data(chat_id, chat_data)

def get_chat_data(chat_id):
   
    chat_data = {
        'id': chat_id,
        'tags': []
    }
    return chat_data

def update_chat_data(chat_id, chat_data):
    
    print(f"Updating chat data for chat {chat_id} with tags {chat_data['tags']}")


add_tags('####', ['star', 'open'])
