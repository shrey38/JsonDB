import requests

def starz_send_message(message_type, custom_message=None):
    if message_type == 'greeting':

        send_automated_message('Hi! Welcome to STARZ. How can I assist you today?')
    elif message_type == 'away':
       
        set_automated_message('Sorry, I am currently away. I will get back at you soon. Please leave a message for me')
    elif message_type == 'quick':
       
        send_automated_message('Thanks for your message. Please visit our website Straz Ventures for more Details')
    elif message_type == 'custom':
        
        send_automated_message(custom_message)
    elif message_type == 'confirmation':
      
        send_automated_message('Thanks for your message! We will try to get back to you as soon as  possible.')

def send_automated_message(message):

    print('Sending automated message:', message)

def set_automated_message(message):
   
    print('Setting automated message:', message)


starz_send_message('confirmation')
