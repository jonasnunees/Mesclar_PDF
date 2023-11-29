import PyPDF2, os

merger = PyPDF2.PdfMerger()

# lista contendo os arquivos dentro da pasta arquivos
lista_arquivos = os.listdir("arquivos")

# ordenar os arquivos
lista_arquivos.sort()

for arquivo in lista_arquivos:
    # verificando se o arquivo é um pdf
    if ".pdf" in arquivo:
        # mesclando os arquivos pdf
        merger.append(f'arquivos/{arquivo}')

# salvando o arquivo pdf mesclado
merger.write('PDF Final.pdf')