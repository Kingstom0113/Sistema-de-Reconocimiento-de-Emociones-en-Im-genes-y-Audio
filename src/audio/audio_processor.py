import speech_recognition as sr

def transcribir_audio(ruta_audio):
    recognizer = sr.Recognizer()
    with sr.AudioFile(ruta_audio) as source:
        audio = recognizer.record(source)
    try:
        texto = recognizer.recognize_google(audio, language="es-ES")
        return texto
    except sr.UnknownValueError:
        print("❌ No se pudo entender el audio.")
    except sr.RequestError as e:
        print(f"❌ Error con el servicio de reconocimiento: {e}")
    return None
