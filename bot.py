import logging
import time
import requests

# Configuração de logs
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Token do bot
BOT_TOKEN = '7700543008:AAEnJQQyhHwJaq0cUXV1ENaMwTnZReTOM08'

# IDs dos canais
SOURCE_CHANNEL_ID = 2590813877  # ID do canal de origem
DESTINATION_CHANNEL_ID = 2656975250  # ID do canal de destino

# URL base da API do Telegram
BASE_URL = f'https://api.telegram.org/bot{BOT_TOKEN}'

# Função para obter novas atualizações
def get_updates(offset=None):
    url = f'{BASE_URL}/getUpdates'
    params = {'offset': offset, 'timeout': 10}
    response = requests.get(url, params=params)
    return response.json()

# Função para reenviar mensagens
def forward_message(chat_id, from_chat_id, message_id):
    url = f'{BASE_URL}/copyMessage'
    payload = {
        'chat_id': chat_id,
        'from_chat_id': from_chat_id,
        'message_id': message_id
    }
    response = requests.post(url, data=payload)
    return response.json()

# Loop principal
def main():
    last_update_id = None
    while True:
        try:
            updates = get_updates(last_update_id)
            if updates.get('result'):
                for update in updates['result']:
                    last_update_id = update['update_id'] + 1
                    message = update.get('channel_post')
                    if message and message['chat']['id'] == SOURCE_CHANNEL_ID:
                        logging.info(f"Nova mensagem detectada: {message['message_id']}")
                        forward_message(DESTINATION_CHANNEL_ID, SOURCE_CHANNEL_ID, message['message_id'])
        except Exception as e:
            logging.error(f"Erro: {e}")
        time.sleep(1)

if __name__ == '__main__':
    main()
