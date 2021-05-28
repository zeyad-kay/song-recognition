import librosa

class MP3():
    @staticmethod
    def read(file_name,duration=None):
        data, samplerate = librosa.load(file_name,duration = duration)
        return data , samplerate

    @staticmethod
    def get_spectrogram(data):
        X = librosa.stft(data)
        Xdb = librosa.power_to_db(abs(X) ** 2)
        return Xdb

    @staticmethod
    def get_features(data,spectrum,samplingRate):
        feature_1 = librosa.feature.melspectrogram(y=data, S=spectrum, sr=samplingRate, window="hann")
        feature_2 = librosa.feature.mfcc(y=data.astype('float64'), sr=samplingRate)
        return [feature_1,feature_2]