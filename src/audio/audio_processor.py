import librosa
import numpy as np

def load_audio(file_path):
    # Load audio file from the specified path
    audio_signal, sr = librosa.load(file_path, sr=22050)  # Load with a sample rate of 22.05 kHz
    return audio_signal, sr

def preprocess_audio(audio_signal):
    # Normalize the audio signal
    return audio_signal / np.max(np.abs(audio_signal))

def extract_features(audio_signal, sr):
    # Extract MFCC features from the audio signal
    mfccs = librosa.feature.mfcc(y=audio_signal, sr=sr, n_mfcc=13)
    return np.mean(mfccs.T, axis=0)  # Return the mean of MFCCs