import os
from dotenv import load_dotenv
from speechkit import configure_credentials, creds, model_repository
from speechkit.stt import AudioProcessingType, RecognitionModel
from speechkit.tts import SynthesisModel


def yandex_config() -> None:
    """Аутентификация через API-ключ в Яндекс"""

    # Парсинг файла .env
    load_dotenv()

    # Аутентификация через API-ключ.
    configure_credentials(
        yandex_credentials=creds.YandexCredentials(
            api_key=str(os.getenv("API_KEY")),
        )
    )


def recognize_config() -> RecognitionModel:
    """Конфигурация аудио в текст"""

    model = model_repository.recognition_model()

    # Настройки распознавания.
    model.model = 'general'
    model.language = 'ru-RU'
    model.audio_processing_type = AudioProcessingType.Stream

    return model


def synthesize_config() -> SynthesisModel:
    """Конфигурация текст в аудио"""

    model = model_repository.synthesis_model()

    # Настройки синтеза.
    model.voice = 'jane'
    model.role = 'good'

    return model
