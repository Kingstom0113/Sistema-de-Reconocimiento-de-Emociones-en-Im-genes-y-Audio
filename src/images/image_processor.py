from deepface import DeepFace

def detectar_emocion_imagen(ruta_imagen):
    try:
        resultado = DeepFace.analyze(img_path=ruta_imagen, actions=['emotion'])
        return resultado[0]['dominant_emotion']
    except Exception as e:
        print(f"❌ Error al analizar la imagen: {e}")
        return None
