import sys
sys.path.append("..")  # Para permitir imports entre módulos

from images.image_processor import detectar_emocion_imagen
from audio.audio_processor import transcribir_audio
from models.emotion_model import analizar_sentimiento_texto
from utils.helpers import validar_ruta

def menu():
    print("=== Sistema de Reconocimiento de Emociones ===")
    print("1. Analizar emoción en una imagen facial")
    print("2. Analizar emoción desde un archivo de voz")
    opcion = input("Selecciona una opción (1 o 2): ")

    if opcion == "1":
        ruta = input("Ruta de la imagen: ")
        if validar_ruta(ruta):
            emocion = detectar_emocion_imagen(ruta)
            if emocion:
                print(f"🧠 Emoción detectada: {emocion}")
        else:
            print("❌ Imagen no encontrada.")
    elif opcion == "2":
        ruta = input("Ruta del archivo de audio (.wav): ")
        if validar_ruta(ruta):
            texto = transcribir_audio(ruta)
            if texto:
                print(f"🗣 Transcripción: {texto}")
                emocion, score = analizar_sentimiento_texto(texto)
                if emocion:
                    print(f"🧠 Sentimiento detectado: {emocion} (Confianza: {score:.2f})")
        else:
            print("❌ Archivo de audio no encontrado.")
    else:
        print("❌ Opción no válida.")

if __name__ == "__main__":
    menu()
