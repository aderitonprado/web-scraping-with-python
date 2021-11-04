#!/usr/bin/env python
# coding: utf-8

# In[19]:


# importar as libs
from datetime import datetime
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

class ExtracaoPortal:
    def __init__(self):
        self.portal = None
        
    def extrair(self, portal):
        self.portal = portal
        
        # capturando os dados
        texto_string = requests.get('https://globoesporte.globo.com/').text
        hora_extracao = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        bsp_texto = bs(texto_string, 'html.parser')
        lista_noticias = bsp_texto.find_all('div', attrs={'class':'feed-post-body'})
        
        # criando a tabela de dados
        dados = []
        
        # percorrendo a lista de noticias encontradas
        for noticia in lista_noticias:
            
            # obtendo as manchetes
            manchete = noticia.contents[1].text.replace('"', "")
            
            # obtendo os links
            link = noticia.find('a').get('href')
            
            # obtendo a descrição das noticias
            descricao = noticia.contents[2].text
            if not descricao:
                descricao = noticia.find('div', attrs={'class':'bstn-related'})
                descricao = descricao.text if descricao else None
            
            # obtendo os metadados das noticias
            metadados = noticia.find('div', attrs={'class':'feed-post-metadata'})
            time_delta = metadados.find('span', attrs={'class': 'feed-post-datetime'})
            secao = metadados.find('span', attrs={'class': 'feed-post-metadata-section'})

            time_delta = time_delta.text if time_delta else None
            secao = secao.text if secao else None
            
            # adicionando dados ao dataframe
            dados.append((manchete, descricao, link, secao, hora_extracao, time_delta))
            df = pd.DataFrame(dados, columns=['manchete', 'descrição', 'link', 'seção', 'hora_extração', 'time_delta'])
       
        # retornando o dataframe com a tabela e dados
        return df

# executando o projeto extraindo os dados do site desejado
df = ExtracaoPortal().extrair("https://globoesporte.globo.com/")
df.head()


# In[12]:


## visualizar os dados

# obter a quantidade de manchetes
print("Quantidade de Manchetes = ", len(lista_noticias))
lista_noticias[0].contents

# obter manchete e o link da noticia
lista_noticias[0].contents[1].text.replace('"',"")
lista_noticias[0].find('a').get('href')

# obter a descrição
descricao = lista_noticias[0].contents[2].text
if not descricao:
    descricao = noticia.find('div', attrs={'class':'bstn-related'})
    
    # somente acessará a propriedade text caso tenha encontrado (find)
    descricao = descricao.text if descricao else None
descricao


# In[13]:


metadados = lista_noticias[0].find('div', attrs={'class':'feed-post-metadata'})
time_delta = metadados.find('span', attrs={'class': 'feed-post-datetime'})
secao = metadados.find('span', attrs={'class': 'feed-post-metadata-section'})

time_delta = time_delta.text if time_delta else None
secao = secao.text if secao else None

print('time_delta = ', time_delta)
print('seção = ', secao)


# In[14]:


# criando a tabela de dados
dados = []

for noticia in lista_noticias:
    manchete = noticia.contents[1].text.replace('"', "")
    link = noticia.find('a').get('href')
    
    descricao = noticia.contents[2].text
    if not descricao:
        descricao = noticia.find('div', attrs={'class':'bstn-related'})
        descricao = descricao.text if descricao else None
        
    metadados = noticia.find('div', attrs={'class':'feed-post-metadata'})
    time_delta = metadados.find('span', attrs={'class': 'feed-post-datetime'})
    secao = metadados.find('span', attrs={'class': 'feed-post-metadata-section'})
    
    time_delta = time_delta.text if time_delta else None
    secao = secao.text if secao else None
    
    dados.append((manchete, descricao, link, secao, hora_extracao, time_delta))


# In[20]:


# Adicionando dados à tabela
df = pd.DataFrame(dados, columns=['manchete', 'descrição', 'link', 'seção', 'hora_extração', 'time_delta'])
df.head()


# In[ ]:




