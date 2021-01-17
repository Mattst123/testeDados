import csv
arquivo1 = open('authors.csv',encoding="utf8")
arquivo2 = open('categories.csv',encoding="utf8")
arquivo3 = open('dataset.csv',encoding="utf8")
arquivo4 = open('formats.csv',encoding="utf8")

#listas que receberao as informações dos arquivos csv.
listaAutores = []
listaCategorias = []
listaDadosAdicionais = []
listaFormatos = []

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
    
#remove a primeira linha que contem o cabecalho de todas as listas
listaAutores.pop(0)
listaCategorias.pop(0)
listaDadosAdicionais.pop(0)
listaFormatos.pop(0)


print(listaCategorias[0][1])
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

print(listaDadosAdicionais[1])
#Qual a quantidade total de livros da base?
#Qual a quantidade de livros que possuí apenas 1 autor?
#Quais os 5 autores com a maior quantidade de livros?
#Qual a quantidade de livros por categoria?
#Quais as 5 categorias com a maior quantidade de livros?
#Qual o formato com a maior quantidade de livros?
#Considerando a coluna “bestsellers-rank”, quais os 10 livros mais bem posicionados?
#Considerando a coluna “rating-avg”, quais os 10 livros mais bem posicionados?
#Quantos livros possuem “rating-avg” maior do que 3,5?
#Quantos livros tem data de publicação (publication-date) maior do que 01-01-2020?
            
            

            

