import speech_recognition as sr
import pyttsx3
import openai

# Configuração da API do OpenAI
openai.api_key = 'SUA_CHAVE_DE_API_DO_OPENAI'

# Configuração da síntese de fala
engine = pyttsx3.init()

# Função para capturar a voz do usuário
def capture_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Diga algo...")
        audio = r.listen(source)

capture_voice()
    