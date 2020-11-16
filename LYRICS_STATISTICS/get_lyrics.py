import json
import logging
import numpy
import requests
import urllib

logging.basicConfig(filename='logfile.log', level=logging.DEBUG, format='%(levelname)s: %(asctime)s: %(message)s' )

class musicLyrics():
    def __init__(self, artist_name):
        self.artist_name = artist_name

    def get_artist_id(self):
        '''
                Returns artist_id,
                :param name: no params
                :return: artist_id
         '''
        print(f'Getting the artist id .....')
        logging.info(f'Getting the artist id for the artist {self.artist_name} .....')
        url_artist_name = urllib.parse.quote(self.artist_name, safe='')
        url = f'https://musicbrainz.org/ws/2/artist/?query={url_artist_name}&fmt=json'
        try:
            requests.get(url)
            response = requests.get(url)
            logging.info(f'response status code for get_artist_id url: {response.status_code}')
            artist_dic = response.json()['artists']
            for d in artist_dic:
                logging.debug(d['id'])
                if str(d['name'].lower()) == self.artist_name.lower():
                    logging.debug(d['id'])
                    artist_id = d['id']
            logging.info(f'artist id = {artist_id}')
            return(artist_id)
        except Exception as e:
            logging.exception(e)
            print("Sorry, artist name doesn't exist")
            exit()

    def get_songs_list(self, artist_id):
        '''
                Returns songs list,
                :param name: artist_id
                :return: songs_list
        '''

        print('Collecting all the songs list for the artist ...')
        logging.info('Collecting all the songs list for the artist ...')

        url = f'https://musicbrainz.org/ws/2/recording?query=arid:{artist_id}&fmt=json'
        try:
            response = requests.get(url)
            logging.info(f'response status code for get_songs_list url: {response.status_code}')
            songs_list =[]
            recordings = response.json()['recordings']
            for rec in recordings:
                songs_list.append(rec['title'])
            logging.debug(f'List of songs for this artist: {songs_list}')
            return songs_list
        except Exception as e:
            logging.exception(e)
            print("Sorry, no songs exist for this artist")
            exit()

    def get_lyrics_word_count_list(self, songs_list):
        '''
            Returns word count list,
            :param name: songs_list
            :return: word_count_list
        '''
        print('Calculating word count for the lyrics ...')
        logging.info('Calculating word count for each song lyrics ...')
        word_count_list = []
        for song_name in songs_list:
            try:
                #print(song_name)
                logging.debug(f'{song_name}')
                print(f'calculating lyrics word count for {song_name}')

                song_name = urllib.parse.quote(song_name, safe='')
                logging.debug(f'{song_name}')
                lyrics_dict = requests.get(f'https://api.lyrics.ovh/v1/{self.artist_name}/{song_name}').json()
                logging.debug(f'Lyrics dict : {lyrics_dict}')
                word_count = self.get_count(lyrics_dict)
                if word_count != 0:
                    word_count_list.append(word_count)
            except Exception as e:
                logging.exception(e)
                pass

        if int(sum(word_count_list)) == 0:
           print("lyrics doesn't exist for this artist")
           exit()
        else:
            logging.info(f'Word count list: {word_count_list}')
            return word_count_list


    def avg_words(self, word_count_list):
        '''
            Returns average words for the lyrics,
            :param name: word_count_list
            :return: avg_words_per_lyrics
         '''

        print('Calculating average word count for all lyrics ...')
        logging.info('Calculating average word count for all lyrics ...')

        avg_words_per_lyrics = sum(word_count_list)/len(word_count_list)
        return avg_words_per_lyrics

    def get_count(self, lyrics_dict):
        '''
            Returns  word count in the lyrics,
            :param name: lyrics_dict
            :return: word_count
        '''

        logging.info('Calculating word count for each lyrics ...')

        lyrics = lyrics_dict.get('lyrics')
        if lyrics == '':
            word_count = 0
        else:
            lyrics = lyrics_dict.get('lyrics')
            lyrics = lyrics.replace("\n", "")
            lyrics_word_list = lyrics.split(" ")
            #print(len(lyrics_word_list))
            word_count = len(lyrics_word_list)
        logging.debug('Word count for the lyrics: {word_count}')
        return word_count


    def min_words_lyric(self, word_count_list):
        logging.info('Calculating min words in lyrics')
        min_word = min(word_count_list)
        return min_word

    def max_words_lyric(self, word_count_list):
        logging.info('Calculating max words in lyrics')
        max_word = max(word_count_list)
        return max_word

    def get_standard_deviation(self, word_count_list):
        logging.info('Calculating standard deviation')
        std_dev = numpy.std(word_count_list)
        return(round(std_dev, 2))

    def get_variance(self, word_count_list):
        logging.info('Calculating variance')
        var = numpy.var(word_count_list)
        return(round(var, 2))




