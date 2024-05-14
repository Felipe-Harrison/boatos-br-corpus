import requests
from bs4 import BeautifulSoup
from datetime import datetime
from .Crawler import Crawler,PageData
from time import time as now

class Boatos(Crawler):
    # Pegar lista de noticias
    def getNoticias(self,page:BeautifulSoup) -> list:
        noticias = []
        noticias_block = page.find('div',attrs={'class':"posts-wrapper"})
        if noticias_block != None:
            noticias = noticias_block.findAll('div',attrs={'class': "non-grid-content alternative-layout-content"})
        return noticias
    
    # Procurar proxima pagina
    def getNextPage(self,page:BeautifulSoup):
        nextLink = page.find('a', attrs={'class': 'next page-numbers'})
        if nextLink != None:
            self.urls.append(nextLink['href'])
    
    # Pegar dados da noticia
    def getDataFromNoticia(self,noticia:BeautifulSoup) -> PageData:
        
        try:
            titulo = noticia.find("h2",attrs={'class': 'blog-entry-title entry-title'})
            url = titulo.a.get('href')
            titulo_text = titulo.a.get_text()
            
            categoria = [noticia.find('li',attrs={'class','meta category'}).get_text()]
            
            datapublicaco = noticia.find('time')
            data_datetime = datetime.fromisoformat(datapublicaco['datetime'])
            
            conclusao,texto,referencia = self.getDataFromUrl(url)
            
            for palavra in ['Fake news','Boato sem comprovação','Golpe','Enganoso','Exagerado','Verdadeiro','Real com erros','Em apuração']:
                if palavra in conclusao:
                    categoria.append(palavra)
                    break
            
            return PageData(
                url=url,
                titulo=titulo_text,
                dataPublicacao=data_datetime,
                categorias=categoria,
                conclusao=conclusao,
                texto=texto,
                referencia=referencia
            )
            
        except:
            print("Error in: ",url)
            return None
        
    
    # Pegar dados da pagina da noticia
    def getDatafromPage(self,page:BeautifulSoup):
        texto_block = page.find('div',attrs={'class': "nv-content-wrap entry-content"}).findAll(['p','h2'])
        red_elements = page.find_all(style=lambda value: value and "color: #ff0000" in value)
        
        referencia_text = []
        for element in red_elements:
            referencia_text.append(element.text)

        referencia = " ".join(referencia_text)
            
        texto_limpo = ' '.join(texto.get_text() for texto in texto_block)
        
        if "Conclusão" in texto_limpo:
            texto, conclusao = texto_limpo.split("Conclusão")
        else:
            texto = texto_limpo
            conclusao = ""
            
        return conclusao,texto,referencia

if __name__ == "__main__":
    
    urls = [
        "https://www.boatos.org/"
    ]
    
    tempoInicio = now()
    try:   
        modelo = Boatos(urlsIniciais=urls,arquivo="boatosorg")
        modelo.scrape()
            
    except requests.ConnectTimeout:
        print("Erro de timeout")
        
    except KeyboardInterrupt:
        pass
    
    finally:
        print("Tempo gasto Total: ",f"{(now() - tempoInicio):.2f}s")