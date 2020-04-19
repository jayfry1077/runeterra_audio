from pylordeckcodes import get_deck_from_code
import sys
import pydub
import wave
import os


def _create_silence(wav_path, silence):
    delay = pydub.AudioSegment.silent(duration=silence * 1000)
    delay.export('{}\\silence.wav'.format(wav_path), format='wav')

def _create_audio(deck_list=list, deck_name=str, wav_path=str, save_path=str):
    audio_data =[]
    print('Creating auido for {}...'.format(deck_name))
    
    for card in deck_list:
        audio_data.append(pydub.AudioSegment.from_wav(card))

    combined_audio = sum(audio_data)
    combined_audio.export(save_path + deck_name + ".mp3", format="mp3")

def _getDeckList(deckcode):
    return get_deck_from_code(deckcode, return_type="strings")

def deck_code_to_audio(deck_code=str, deck_name=str, wav_path=str, save_path=str, silence=2):
    '''
    deck_code: Deck Code.\n
    deck_name: Desired name of your output file.\n
    wav_path: Path to your wav files.\n
    save_path: Where you want to save the mp3 file output.
    silence: amount of silence you want between each card. Does not apply to associated cards.
    '''

    if not os.path.isdir(save_path):
        os.mkdir(save_path)

    _create_silence(wav_path, silence)
    deck = _getDeckList(deck_code)

    deck_list = []

    for cards in deck:
        card = cards.split(":")[1]
        deck_list.append('{}\\{}.wav'.format(wav_path, card))
        deck_list.append('{}\\silence.wav'.format(wav_path))

    _create_audio(deck_list, deck_name, wav_path, save_path)

def regions_to_audio(wav_path=str, save_path=str, silence=2):

    if not os.path.isdir(save_path):
        os.mkdir(save_path)

    demacia = []
    freljord = []
    ionia = []
    noxus = []
    pz = []
    si = []
  
    _create_silence(wav_path, silence)
    silence_path = '{}\\silence.wav'.format(wav_path)

    for file in os.listdir(wav_path):
        if 'DE' in file:
            demacia.append('{}\\{}'.format(wav_path, file))
            demacia.append(silence_path)
        if 'FR' in file:
            freljord.append('{}\\{}'.format(wav_path, file))
            freljord.append(silence_path)
        if 'IO' in file:
            ionia.append('{}\\{}'.format(wav_path, file))
            ionia.append(silence_path)
        if 'NX' in file:
            noxus.append('{}\\{}'.format(wav_path, file))
            noxus.append(silence_path)
        if 'PZ' in file:
            pz.append('{}\\{}'.format(wav_path, file))
            pz.append(silence_path)
        if 'SI' in file:
            si.append('{}\\{}'.format(wav_path, file))
            si.append(silence_path)


    _create_audio(demacia, 'Demacia', wav_path, save_path)
    _create_audio(noxus, "Noxus", wav_path, save_path)
    _create_audio(ionia, "Ionia", wav_path, save_path)
    _create_audio(freljord, "Freljord", wav_path, save_path)
    _create_audio(pz, "Piltover & Zaun", wav_path, save_path)
    _create_audio(si, "Shadow Isles", wav_path, save_path)