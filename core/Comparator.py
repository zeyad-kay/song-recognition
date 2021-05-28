from .String_Distance import String_Distance
from .Json import Json

class Comparator():
    @staticmethod
    def get_similar_songs(hashes = {}):
        songs_names = []
        songs_similarity = [] 
        songs = Comparator.__get_songs()
        #  loop through Database
        for song in songs :
            sim_arr = []
            for component in song :
                for key in component : 
                    if (key == "songName") : continue
                    # compare hash of spectrogram
                    sim = String_Distance(component[key],hashes[key]).get_similarity_index()
                    sim_arr.append(sim)

            avg = sum(sim_arr) / len(sim_arr) * 100
            songs_names.append((song[0]["songName"]))
            songs_similarity.append(avg)

        sorted_sim = sorted(zip(songs_names,songs_similarity),key = lambda x : x[1],reverse=True)
        return sorted_sim

    def __get_songs():
        return Json.reader(r"C:\Users\Zizo\Desktop\song-recognition\db.json")