import csv
import datetime
arquivo1 = open('authors.csv',encoding="utf8")
arquivo2 = open('categories.csv',encoding="utf8")
arquivo3 = open('dataset.csv',encoding="utf8")
arquivo4 = open('formats.csv',encoding="utf8")

#listas que receberao as informações dos arquivos csv.
listaAutores = []
listaCategorias = []
listaDadosAdicionais = []
listaFormatos = []
listaTemporaria= []

#bloco de código que extrai os dados csv authors
authors= csv.reader(arquivo1)
for author in authors :
    listaAutores.append(author)
    
#bloco de código que extrai os dados do csv categories
categories = csv.reader(arquivo2)
for category in categories :
    listaCategorias.append(category)
    
#bloco de código que extrai os dados do csv dataset    
datasets = csv.reader(arquivo3)
for dataset in datasets :
    listaDadosAdicionais.append(dataset)
    
#bloco de código que extrai os dados do csv dataset
formats = csv.reader(arquivo4)
for format in formats :
    listaFormatos.append(format)
QuantidadeLivros=0
#Qual a quantidade total de livros da base?
for temporario in range(0, len(listaDadosAdicionais)) :
    listaTemporaria.append(listaDadosAdicionais[temporario][25])
listaTemporaria = list(set(listaTemporaria))
print((len(listaTemporaria)-1))
listaTemporaria.clear()
#Qual a quantidade de livros que possuí apenas 1 autor?
for temporario in range(0, len(listaDadosAdicionais)) :
    if("," not in listaDadosAdicionais[temporario][0] ):
     QuantidadeLivros = QuantidadeLivros + 1
print(QuantidadeLivros)
listaTemporaria.clear()
#Quais os 5 autores com a maior quantidade de livros?
#Qual a quantidade de livros por categoria? 
#Quais as 5 categorias com a maior quantidade de livros?
#Qual o formato com a maior quantidade de livros?
for temporario in range(0, len(listaDadosAdicionais)) :
    listaTemporaria.append(listaDadosAdicionais[temporario][10])
MaiorQuantidade = 0
idFormato = 0
for temporario in range ((0),len(listaFormatos)):
    a =  listaFormatos[temporario][0]
    b = listaTemporaria.count(a)
    if( b > MaiorQuantidade):
        MaiorQuantidade = b
        idFormato  = listaFormatos[temporario][0]
for temporario in range ((0),len(listaFormatos)):
     if(listaFormatos[temporario][0]) == idFormato:
        print(listaFormatos[temporario])
listaTemporaria.clear()
#Considerando a coluna “bestsellers-rank”, quais os 10 livros mais bem posicionados?
#Considerando a coluna “rating-avg”, quais os 10 livros mais bem posicionados?
QuantidadeRating = 0
for linha in range(0, len(listaDadosAdicionais)):
    
   if (listaDadosAdicionais[linha][23] == "5.0"):
     listaTemporaria.append(listaDadosAdicionais[linha][25])
listaTemporaria = sorted(listaTemporaria)
i = 0
while i < 5:
    print(listaTemporaria[i])
    i = i +  1
#Quantos livros possuem “rating-avg” maior do que 3,5?
QuantidadeRating = 0
for linha in range(0, len(listaDadosAdicionais)):
   if (listaDadosAdicionais[linha][23]> "3.5"):
       QuantidadeRating = QuantidadeRating + 1

print('Livros que possuem rating-avg maior que 3.5  = ',QuantidadeRating)
#Quantos livros tem data de publicação (publication-date) maior do que 01-01-2020?
quantidadePublicacao = 0
from datetime import datetime
data = "2020-01-01 00:00:00"
listaTemporaria.clear()
for temporario in range(0, len(listaDadosAdicionais)) :
    listaTemporaria.append(listaDadosAdicionais[temporario][21])
for temporario in range(0, len(listaDadosAdicionais)):
    if(datetime.strptime(listaTemporaria[temporario], '%Y-%m-%d %H:%M:%S'))<(datetime.strptime(data,'%Y-%m-%d %H:%M:%S')):
        quantidadePublicacao = quantidadePublicacao + 1
    
print(quantidadePublicacao)           


#cruzamento de dados entre os arquivos authors e dataset
for dts in range(0, len(listaDadosAdicionais)): 
    for i in range(0,len(listaAutores)): 
        if listaAutores[i][0] in listaDadosAdicionais[dts][0]: 
            listaDadosAdicionais[dts].append(listaAutores[i][1])
            
#cruzamento de dados entre os arquivos formats e dataset
for dts in range(0, len(listaDadosAdicionais)): 
    for i in range(0,len(listaFormatos)): 
        if (listaFormatos[i][0] in listaDadosAdicionais[dts][10]): 
            listaDadosAdicionais[dts].append(listaFormatos[i][1])         

#cruzamento de dados entre os arquivos categories e dataset            
for dts in range(0, len(listaDadosAdicionais)): 
    for i in range(0,len(listaCategorias)): 
        if listaCategorias[i][0] in listaDadosAdicionais[dts][2]: 
            listaDadosAdicionais[dts].append(listaCategorias[i][1])
            

