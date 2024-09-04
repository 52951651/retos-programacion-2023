Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

 def to_leet_speak(text):
    leet_dict = {
        'A': '4', 'B': '8', 'C': '(', 'D': '|)', 'E': '3', 'F': '|=', 'G': '6',
        'H': '#', 'I': '!', 'J': '_|', 'K': '|<', 'L': '1', 'M': '|\/|', 'N': '|\|',
        'O': '0', 'P': '|D', 'Q': '(,)', 'R': '|2', 'S': '5', 'T': '7', 'U': '|_|',
        'V': '\/', 'W': '\/\/', 'X': '><', 'Y': '`/', 'Z': '2',
        '0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6',
        '7': '7', '8': '8', '9': '9'
    }
    
    leet_text = ""
    for char in text.upper():
        leet_text += leet_dict.get(char, char)  # Si no está en el diccionario, deja el carácter igual

    return leet_text

# Ejemplo de uso
texto = "Hola Mundo, esto es un texto en lenguaje hacker!"
leet_texto = to_leet_speak(texto)
print(leet_texto)
