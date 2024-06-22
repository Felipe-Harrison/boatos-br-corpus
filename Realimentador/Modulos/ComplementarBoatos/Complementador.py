import nltk
import re

def extractEmojis(text:str):
    emoji_pattern = re.compile(
        r'['
        u'\U0001F600-\U0001F64F'  # Emoticons
        u'\U0001F300-\U0001F5FF'  # Símbolos e pictogramas
        u'\U0001F680-\U0001F6FF'  # Transportes e símbolos de mapa
        u'\U0001F1E0-\U0001F1FF'  # Bandeiras (iOS)
        u'\U00002500-\U00002BEF'  # Formas geométricas
        u'\U00002702-\U000027B0'  # Símbolos adicionais
        u'\U000024C2-\U0001F251'  # Símbolos miscelâneos
        u'\U0001f926-\U0001f937'  # Gestos
        u'\U00010000-\U0010FFFF'  # Caracteres suplementares
        u'\u200d'  # Zero width joiner
        u'\u2640-\u2642'  # Símbolos de gênero
        u'\u2600-\u2B55'  # Diversos símbolos e pictogramas
        u'\u23cf'  # Símbolo de ejeção
        u'\u23e9'  # Símbolos de controle de mídia
        u'\u231a'  # Relógios
        u'\ufe0f'  # Variações de caracteres
        u'\u3030'  # Símbolo de alternância
        ']+', 
        flags=re.UNICODE
    )
    emojis = re.findall(emoji_pattern, text)
    return [list(_emoji) for _emoji in emojis]
    # return [item for sublist in  [list(_emoji) for _emoji in emojis] for item in sublist]

# Palavras em Maiusculo
def getNumeroPalavrasMaiusculo(text:list[str]) -> int:
    words_in_uppercase = [word for word in text if word.isupper()]
    return len(words_in_uppercase)

# Quantidade de emojis
def getNumeroEmojis(text:list[str]) -> int:
    return len(extractEmojis(text))

# Quantidade de verbos
def getNumeroVerbos(text:str) -> int:
    palavras = nltk.tokenize.word_tokenize(text)
    pos_tags = nltk.pos_tag(palavras)
    return len([word for word, pos in pos_tags if pos.startswith('VB')])

# Quantidade de palavras
def getNumeroPalavras(text:list[str]) -> int:
    text_split = text.split()
    return len(text_split)