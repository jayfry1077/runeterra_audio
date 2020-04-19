import json
import os

DATA_MAP = {}

def card_grab(path_to_file=str, path_to_save=str):
    ''' 
    path_to_file: Should be full path to riots latest json data
    path_to_save: Location to save ouput files
    '''

    if not os.path.isdir(path_to_save):
        os.mkdir(path_to_save)

    # Load the json data into a variable.
    with open (path_to_file, encoding='utf8') as json_file:
        DATA = json.load(json_file)
        
    global DATA_MAP

    for card in DATA:
        DATA_MAP.update({card['cardCode']: card})

    for card in DATA:
        if card['collectible']:
            text = _build_card_text(card)

            f = open(path_to_save + card['cardCode'] + " " + card['name'] + ".txt", 'w')
            f.write(text)
            f.close()

def _build_card_text(card):
    
    text = "Name. {}.\nRegion. {}.\n".format(card['name'], card['region'])
    text += 'Cost. {}.\n'.format(card['cost'])

    if len(card['descriptionRaw'])>0:
        text += "Description. {}.\n".format(card['descriptionRaw'])

    if card['type'] == 'Unit':
        text += 'Attack. {}.\n'.format(card['attack'])
        text += 'Health. {}. \n'.format(card['health'])
        if len(card['keywords'])>0:
            num = 1
            text += 'Keywords.\n'
        
            for keywords in card['keywords']:
                text += "{}. {}.\n".format(num,keywords)
                num += 1

    elif card['type'] == 'Spell':
        text += 'Spell Speed. {}.\n'.format(card['spellSpeed'])

    if len(card['levelupDescriptionRaw'])>0:
        text += "Level up criteria. {}.\n".format(card['levelupDescriptionRaw'])

    if len(card['associatedCardRefs'])>0:
        text += _build_associated_cards_text(card['associatedCardRefs'])


    return text

def _build_associated_cards_text(data):
    associated_num = 1
    associated_text = ''

    # for card in associated card list
    for card in data:
        associated_text += "Associated card {}. Name. {}.\n".format(associated_num, DATA_MAP[card]['name'])
        associated_text += 'Cost. {}.\n'.format(DATA_MAP[card]['cost'])

        if len(DATA_MAP[card]['descriptionRaw'])>0:
            associated_text += "Description. {}.\n".format(DATA_MAP[card]['descriptionRaw'])

        if DATA_MAP[card]['type'] == 'Unit':
            associated_text += 'Attack. {}.\n'.format(DATA_MAP[card]['attack'])
            associated_text += 'Health. {}. \n'.format(DATA_MAP[card]['health'])
            if len(DATA_MAP[card]['keywords'])>0:
                num = 1
                associated_text += 'Keywords.\n'

                for keywords in DATA_MAP[card]['keywords']:
                    associated_text += "{}. {}.\n".format(num,keywords)
                    num += 1
        elif DATA_MAP[card]['type'] == 'Spell':
            associated_text += 'Spell Speed. {}.\n'.format(DATA_MAP[card]['spellSpeed'])
        elif DATA_MAP[card]['type'] == 'Trap':
            # Special Case just for Teemo! Never underestimate the power of the scouts code.
            associated_text += "Description. {}.\n".format(DATA_MAP[card]['descriptionRaw'])
            continue
                
        associated_num += 1

    return associated_text
