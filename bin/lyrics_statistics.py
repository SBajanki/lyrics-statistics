from LYRICS_STATISTICS import *
import fire

def average_lyric_word_count(artist):
    '''
        Returns an average word count per lyric, standard deviation, variance,
        min and max words in the lyrics
        :param name: artist
        :return: average word count
    '''

    ml = musicLyrics(artist)
    artist_id = ml.get_artist_id()
    songs_list = ml.get_songs_list(artist_id)
    word_count_list = ml.get_lyrics_word_count_list(songs_list)
    avg_count = ml.avg_words(word_count_list)
    print('\n')
    print(f'LYRICS STATISTICS FOR {artist}:')
    print('---------------------------------')
    print(f'Average lyrics word count  is {avg_count}')
    std_dev = ml.get_standard_deviation(word_count_list)
    print(f'Standard deviation for the lyrics is {std_dev}')
    var = ml.get_variance(word_count_list)
    print(f'Variance for the lyrics is {var}')
    min_word = ml.min_words_lyric(word_count_list)
    print(f'Minimum words in the lyrics: {min_word}')
    max_word = ml.max_words_lyric(word_count_list)
    print(f'Maximum words in the lyrics: {max_word}')





if __name__ == "__main__":
        fire.Fire(average_lyric_word_count)

