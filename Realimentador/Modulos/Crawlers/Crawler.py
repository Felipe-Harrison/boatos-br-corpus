from datetime import datetime
import requests
from bs4 import BeautifulSoup
import json
from time import time as now

def makeRequest(url) -> BeautifulSoup:
    response = requests.get(url=url)
    content = response.content
    return BeautifulSoup(content,'html.parser')

class PageData:
    def __init__(self,url,titulo,dataPublicacao,categorias,conclusao,texto,referencia) -> None:
        self.url  = url
        self.titulo = titulo
        self.datapublicacao = str(dataPublicacao)
        self.categorias = categorias
        self.conclusao = conclusao
        self.texto = texto
        self.referencia = referencia
    
    def getData(self) -> dict:
        return {
            'url': self.url,
            'titulo': self.titulo,
            'data-publicacao': self.datapublicacao,
            'categorias': self.categorias,
            'conclusao': self.conclusao,
            'rotulo': '',
            'texto': self.texto,
            'referencia': self.referencia
        }
    
class Crawler:
    
    def __init__(self,urlsIniciais:list,salvarEmArquivo:bool=False,arquivo:str='placeholder') -> None:
        self.urls = urlsIniciais
        self.arquivo = arquivo
        self.salvarArquivo = salvarEmArquivo
        
    # Pegar lista de noticias
    def getNoticias(page) -> list:
        pass
    
    # Procurar proxima pagina
    def getNextPage(self,page):
        pass
    
    # Pegar dados da noticia
    def getDataFromNoticia(self,noticia) -> PageData:
        #self.getDataFromUrl(url)
        pass
    
    # Pegar dados da pagina da noticia
    def getDatafromPage(page):
        pass

    def getDataFromUrl(self,url):
        """
        Returns:
            Elementos que forem retornados em getDataFromPage
        """
        paginaNoticia = makeRequest(url)
        return self.getDatafromPage(page=paginaNoticia)
    
    def scrape(self,dateToStop):

        totalData = 0
        Search = True
        data = []
        # Enquanto for para buscar
        while Search:
            
            # Feedback/Analise
            dataPage = 0
            
            tempoInicioPagina = now()
            print("Pagina: ",self.urls[0])
            
            # Pegar página do primeiro link disponivel
            site = makeRequest(url=self.urls[0])
            
            # Procurar por todas as noticias na url atual
            noticias = self.getNoticias(site)

            # Procurar nova página
            self.getNextPage(site)
            
            dataPage = len(noticias)
            # Para cada noticia encontrada buscar dados
            for noticia in noticias:
                
                pageData = self.getDataFromNoticia(noticia)
                
                if pageData != None:
                    pageDataObj = pageData.getData()
                    # Se não for mais noticia nova -> para busca
                    if datetime.fromisoformat(pageDataObj['data-publicacao']) < dateToStop:
                        print("Parando Busca...")
                        Search = False
                        break
                    data.append(pageDataObj)
            
            if(self.salvarArquivo):
                # Salvar as noticias encontradas ate o momento
                with open(f"Resultados/{self.arquivo}_data.json",'a+',encoding="utf8") as f:
                    json.dump(data,f,indent=4,allow_nan=True,ensure_ascii = False)
                    totalData += len(data)
                    print(f"Noticas salvas até o momento: {totalData}, nessa pagina: {len(data)}/{dataPage}")
                    f.close() 
            
            print("Tempo gasto: ",f"{(now() - tempoInicioPagina):.2f}s")
            # Remover link atual
            self.urls.pop(0)
        
        # end while
        return data
