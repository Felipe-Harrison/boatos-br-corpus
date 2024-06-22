
class BoatosBrData:
    """
        Inicializa uma instância da classe BoatosBrData.

        Args:
            url (str): URL de onde foi obtido o texto.
            dataPublicacao (str): Data em que foi publicada a checagem do texto.
            origem (str): De qual site foi retirado.
            categorias (list): Categorias do boato, por exemplo: Política, Saúde, Mundo, entre outras.
            texto (str): Texto original do boato que está circulando na internet.
            textoNormalizado (str): Texto normalizado e limpo.
            rotulo (str): Atributo alvo da previsão, podendo ser Verdadeiro ou Falso.
    """
    def __init__(self,url,dataPublicacao,origem,categorias,texto,textoNormalizado,rotulo) -> None:
        self.url  = url
        self.datapublicacao = str(dataPublicacao)
        self.origem = origem
        self.categorias = categorias
        self.texto = texto
        self.textoNormalizado = textoNormalizado
        self.rotulo = rotulo
    
    def getData(self) -> dict:
        """
        Retorna os dados da instância BoatosBrData em formato de dicionário / json
        """
        return {
            'url': self.url,
            'data-publicacao': self.datapublicacao,
            'origem': self.origem,
            'categorias': self.categorias,
            'texto': self.texto,
            'texto-normalizado': self.textoNormalizado,
            'rotulo': self.rotulo,
        }