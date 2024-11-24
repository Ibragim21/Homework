import requests
import logging

# Token for the bot, replace with your actual token
TOKEN = '7222075818:AAErhvr1PpLq4Ul2OAsV61D5C7zkCTRh8Nw'
CHANNEL_ID = 'https://t.me/bookspractise'  # Use the channel's username or the channel ID

BASE_URL = f'https://api.telegram.org/bot{TOKEN}/'

# Setting up logging for errors
logging.basicConfig(level=logging.INFO)

# Function to get chat information
def get_chat_info():
    url = f"{BASE_URL}getChat?chat_id={CHANNEL_ID}"
    response = requests.get(url)
    return response.json()

# Function to fetch the latest messages (You may need to adjust the logic for pagination)
def get_chat_history(limit=10):
    url = f"{BASE_URL}getUpdates?limit={limit}"
    response = requests.get(url)
    updates = response.json()
    return updates['result'] if 'result' in updates else []

# Function to send a message to the user
def send_message(chat_id, text, reply_to_message_id=None):
    url = f"{BASE_URL}sendMessage"
    data = {
        "chat_id": chat_id,
        "text": text
    }
    if reply_to_message_id:
        data['reply_to_message_id'] = reply_to_message_id
    response = requests.post(url, data=data)
    return response.json()

# Function to send a photo
def send_photo(chat_id, photo_url, caption=None):
    url = f"{BASE_URL}sendPhoto"
    data = {
        "chat_id": chat_id,
        "photo": photo_url
    }
    if caption:
        data['caption'] = caption
    response = requests.post(url, data=data)
    return response.json()

# Function to handle the bot's interaction
def handle_user_input(update):
    user_message = update['message']['text']
    user_chat_id = update['message']['chat']['id']

    # List available books if the user types '/books'
    if user_message == '/books':
        # Retrieve recent books/messages from the channel (this is just an example logic)
        updates = get_chat_history(limit=5)
        books = []  # Will hold book names and their associated image links

        for update in updates:
            # Assuming the message contains the book title and an image
            if 'photo' in update.get('message', {}):
                text = update['message'].get('text', 'No text')
                photo_url = update['message']['photo'][0]['file_id']  # Get the first photo in the message
                books.append((text, photo_url))
        
        if books:
            book_list = "\n".join([f"{i+1}. {book[0]}" for i, book in enumerate(books)])
            send_message(user_chat_id, f"Here are the available books:\n\n{book_list}")
        else:
            send_message(user_chat_id, "Sorry, no books found!")

    # Handle selection of a specific book (assumes user types the book number)
    elif user_message.isdigit() and int(user_message) <= len(books):
        book = books[int(user_message) - 1]
        send_photo(user_chat_id, book[1], caption=book[0])
    else:
        send_message(user_chat_id, "Sorry, I couldn't find that book. Please try again.")

# Function to process updates from users
def process_updates():
    # Fetch new updates (messages sent to the bot)
    url = f"{BASE_URL}getUpdates?offset=-1"  # This gets the latest update
    response = requests.get(url)
    updates = response.json().get('result', [])

    for update in updates:
        if 'message' in update:
            handle_user_input(update)

# Run the bot to process updates
if __name__ == "__main__":
    while True:
        process_updates()
