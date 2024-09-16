import os
from dotenv import load_dotenv
from argparse import ArgumentParser
from speechkit import model_repository, configure_credentials, creds

load_dotenv()
# Аутентификация через API-ключ.
configure_credentials(
    yandex_credentials=creds.YandexCredentials(
        api_key=str(os.getenv("API_KEY")),
    )
)


def synthesize(text: str, export_path: str):
    """Текст в аудио"""

    model = model_repository.synthesis_model()

    # Задайте настройки синтеза.
    model.voice = 'jane'
    model.role = 'good'

    # Синтез речи и создание аудио с результатом.
    result = model.synthesize(text, raw_format=False)
    result.export(f'/YandexSpeechKit/data/{export_path}.wav', 'wav')


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--text', type=str, help='Текст для синтеза', required=True)
    parser.add_argument('--export', type=str, help='Название синтезированного звука', required=False)

    args = parser.parse_args()

    synthesize(args.text, args.export)