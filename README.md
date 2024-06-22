# boatos-br-corpus
👋 Bem-vindo ao Boatos Br Corpus, uma base de dados composta de boatos `falsos` e `verdadeiros` em língua Portuguesa!

## Visão Geral
Este corpus está dividido em três pastas principais, cada uma contendo um modelo diferente da base de dados, em formato `.json`

A seguir, cada pasta será detalhada:

### 📁 base_simples
Esta pasta contém a versão simples do corpus, com menos informações sobre cada boato. Você encontrará os seguintes campos:

- **url**: URL de onde foi obtido o texto.
- **data-publicacao**: Data em que foi publicada a checagem do texto.
- **origem**:  De qual site foi retirado
- **categorias**: Categorias do boato, por exemplo: Política, Saúde, Mundo, entre outras.
- **`texto`**: Texto original do boato que esta circulando na internet
- **texto-normalizado**: Texto normalizado e limpo.
- **`rotulo`**: Atributo alvo da previsão, podendo ser `'verdade'` ou `'falso'`.

### 📁 base_completa
Esta pasta contém a versão mais completa do corpus, com o maior número de informações sobre cada boato. Além dos campos presentes na versão simples, você encontrará os seguintes adicionais:
- **num-emojis**: Quantidade de emojis presentes no boato
- **num-verbos**: Quantidade de verbos presentes no boato
- **num-palavras**: Quantidade de palavras presentes no boato
- **num-palavras-maiusculas**: Quantidade de palavras em maíusculo presentse no boato 
  
### 📁 base_processada
Esta pasta contém a mesma versão da `'base_completa'`, porém, nessa versão os campos **rotulo, data-publicacao, origem** e **categorias** foram transformados em valores numéricos.

## 🤔 Como utilizar esse Corpus ?

1. **Clone este repositório**: Faça a clonagem do repositório para o seu ambiente local, no diretório de sua preferência
```bash
git clone https://github.com/Felipe-Harrison/boatos-br-corpus.git
```
2. **Acesse a Pasta do Corpus**
```bash
cd boatos-br-corpus
```
3. **Escolha a Versão Adequada**: Decida qual pasta (versão) se adequa melhor ao seu projeto e utilize os arquivos conforme necessário.
---

## 🖥️ Um pouco do projeto
O objetivo deste projeto é criar um novo corpus brasileiro voltado para o treinamento de inteligências artificiais para detectar ***fake news***.

Para alcançar este objetivo, foi desenvolvido um *web-crawler* em Python.

O web-crawler coleta dados de sites especializados em identificar e desmentir fake news, sendo o principal deles o [Boatos.org](https://www.boatos.org/).

Este foi um projeto de Conclusão de curso da [Universidade Federal de Uberlândia (UFU)](https://facom.ufu.br/graduacao/sistemas-de-informacao-campus-santa-monica)

## 🧑‍💻 Para devs

Na branch `corpus-processador` é possível encontrar um arquivo no caminho `./Realimentador/boatosbrcorpus_realimentador.ipynb`, que é responsável por realimentar essa base de dados e contém toda a lógica de construção do corpus.

O `Realimentador` esta estruturado da seguinte forma:

```
Realimentador/
├── Class/
│   └── boatosBrData.py -- Classe com os campos dos boatos da base_simples
├── Modulos/
│   ├── ComplementarBoatos/  -- Código para analisar e complementar a base_simples -> base_completa
│   ├── Crawlers/ -- Web-Crawler para coletar novos boatos dos sites
│   └── RotularBoatos/ -- Código para analisar e rotular os novos boatos entre 'verdade' ou 'falso'
├── Processados/
│   ├── categorias/ -- Obter todas as categorias da base_completa, para confeccionar a base_processada
│   ├── origem/ -- Obter todas as origens da base_completa, para confeccionar a base_processada
├── analisaBaseDados.ipynb -- Analisar a base de dados e gerar gráficos
└── boatosbrcorpus_realimentador.ipynb -- Toda a lógica para realimentar o corpus
```
