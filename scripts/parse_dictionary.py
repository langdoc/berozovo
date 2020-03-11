import xml.etree.cElementTree as ET
import pandas as pd

def parse_mansi_lexicon(lift):

    tree = ET.parse(lift)
    root = tree.getroot()

    dictionary = []

    for entry in root.iterfind('.//entry'):

        item = {}
        
        item['lemma'] = entry.find('./lexical-unit/form/text').text

        if entry.find("./sense/gloss[@lang='en']/text") is not None:

            item['en'] = entry.find("./sense/gloss[@lang='en']/text").text

        else:

            item['en'] = '_'

        item['type'] = entry.find('./trait').get('value')

        if entry.find('./sense/grammatical-info') is not None:

            item['pos'] = entry.find('./sense/grammatical-info').get('value')

        else:

            item['pos'] = '_'

        if entry.find("./sense/gloss[@lang='de']/text") is not None:

            item['de'] = entry.find("./sense/gloss[@lang='de']/text").text

        else:

            item['de'] = '_'

        if entry.find("./note/form[@lang='en-x-notefori']/text") is not None:

            item['note'] = entry.find("./note/form[@lang='en-x-notefori']/text").text

        else:

            item['note'] = '_'

        dictionary.append(item)

    df = pd.DataFrame.from_dict(sorted(dictionary, key = lambda i: i['lemma']))

    return(df)

df = parse_mansi_lexicon('data/NM_Lexikon.lift')

df.to_csv("data/NM_Lexikon.csv")

