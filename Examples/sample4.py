def main():
    # Leia o conteúdo de um arquivo de texto chamado plants.txt em uma lista.
    text_list = read_list("plants.txt")
    # O print é para a lista inteira.
    print(text_list)

def read_list(filename):
    """
    Read the contents of a text file into a list and return the list.
    Each element in the list contain one line of text from the text file.
    
    Parameter filename: the name of the text file to read
    Return: a list of strings
    """
    # Crie uma lista vazia que armazenará as linhas de texto do arquivo de texto.
    text_list = []

    # Abra o arquivo de texto para leitura e armazene uma referência ao arquivo aberto em uma variável chamada text_file.
    with open("plants.txt", mode= "rt") as text_file:
        
        for line in text_file: # Leia o conteúdo do arquivo de texto uma linha de cada vez.
            clean_line = line.strip() # Remova o espaço em branco, se houver, do início e do fim da linha.
            text_list.append(clean_line) # Anexe a linha limpa de texto ao final da lista.
        
        return text_list # Retornar a lista que contém as linhas de texto.

if  __name__ == '__main__': # Coloque "main" para iniciar este programa.
    main()
