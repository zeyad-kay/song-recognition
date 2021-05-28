from librosa import feature
from core import String_Distance
from core import MP3
from core import Hash
import os
import librosa as l
from core import Json

# iterate over songs paths
songs = []
count = 1
strings = ["Full","Music","Vocals"]
for i in range(0,4) :
    arr = []
    for j in strings :
        path = os.path.join("songs","Group18_Song"+ str(count)) + "_" + j + ".mp3"
        # read file
        data,samplingRate = MP3.read(path)
        # get spectrogram
        spectrum = MP3.get_spectrogram(data)
        # hash spectrogram
        specto_hash = Hash.generate_hash_code(spectrum)
        features = MP3.get_features(data,spectrum,samplingRate)

        feature_1_hash = Hash.generate_hash_code(features[0])
        feature_2_hash = Hash.generate_hash_code(features[1])

        song = {
            "songName" : "Song" + str(count) + "_" + j,
            "spectrogram_hash" : specto_hash,
            "feature_1" : feature_1_hash,
            "feature_2" : feature_2_hash
        }
        arr.append(song)        
    count += 1
    songs.append(arr)

count = 1
for i in range(0,4) :
    arr = []
    for j in strings :
        path = os.path.join("Group25","Group25_Song"+ str(count)) + "_" + j + ".mp3"
        # read file
        data,samplingRate = MP3.read(path)
        # get spectrogram
        spectrum = MP3.get_spectrogram(data)
        # hash spectrogram
        specto_hash = Hash.generate_hash_code(spectrum)
        features = MP3.get_features(data,spectrum,samplingRate)

        feature_1_hash = Hash.generate_hash_code(features[0])
        feature_2_hash = Hash.generate_hash_code(features[1])

        song = {
            "songName" : "Song" + str(count) + "_" + j,
            "spectrogram_hash" : specto_hash,
            "feature_1" : feature_1_hash,
            "feature_2" : feature_2_hash
        }
        arr.append(song)
    count += 1
    songs.append(arr)
Json.writer(songs,"DB.json")