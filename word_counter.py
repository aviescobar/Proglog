def count_words(filename):
    """Cuenta el número de palabras en un archivo de texto."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"El archivo {filename} no se encuentra.")
        return None

    # Divide el texto en palabras
    words = text.split()
    num_words = len(words)
    return num_words

if __name__ == "__main__":
    filename = input("Introduce el nombre del archivo de texto: ")
    word_count = count_words(filename)
    if word_count is not None:
        print(f"El archivo {filename} contiene {word_count} palabras.")
