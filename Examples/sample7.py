import csv

def main():
    # Read the contents of the dentists.csv file into a compound list.
    dentists_list = read_compound_list("dentists.csv")

    # Print the entire list.
    print(dentists_list)


def read_compound_list(filename):
    """Lê o conteúdo de um arquivo CSV em um composto
    listar e retornar a lista. Cada elemento na lista composta será uma pequena lista que contém os valores de uma linha do arquivo CSV.

    Nome do arquivo do parâmetro: o nome do arquivo CSV a ser lido
    Return: uma lista de listas que contêm cadeias de caracteres
    """
    # Create an empty list that will store the data from the CSV file.
    compound_list = []

    # Open the CSV file for reading and store a reference to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader object that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:

            # If the current row is not blank, append it to the compound_list.
            if len(row_list) != 0:

                # Append one row from the CSV file to the compound list.
                compound_list.append(row_list)

    # Return the compound list.
    return compound_list


# Call main to start this program.
if __name__ == "__main__":
    main()
