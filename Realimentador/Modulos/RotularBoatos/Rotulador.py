from .DicionarioFrasesCategoria import CATEGORIASBOATOSFALSO,CATEGORIASBOATOSVERDADE

def defineRotulo(categorias):
    for categoria in categorias:
        if categoria in CATEGORIASBOATOSFALSO:
            return 'falso'
        if categoria in CATEGORIASBOATOSVERDADE:
            return 'verdade'
    return False

def defineRotulobyText(text):
    for categoria in CATEGORIASBOATOSFALSO:
        if categoria in text:
            return 'falso'
    for categoria in CATEGORIASBOATOSVERDADE:
        if categoria in text:
            return 'verdade'
    return False

def AplicarRotulo(pageData):
    
    # Procura primeiro na categoria
    rotulo = defineRotulo(pageData['categorias'])
    # Se não encontrar procura nos outros atributos
    atributos_verificar = ['texto','conclusao','titulo']
    if not rotulo:
        # Procurar para cada atributo
        for attr in atributos_verificar:
            rotulo = defineRotulobyText(pageData[attr])
            if rotulo != False:
                break
        # Se não encontrar em nenhum
        if not rotulo:
            rotulo = "NDA"
    
    return rotulo