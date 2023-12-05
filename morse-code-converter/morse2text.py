import re
import sys

#Building dictionary of morse code
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', ' ': '/'
}

#Function for convertion of morse code into corresponding letter or number
def morse_to_text(morse_code):
    words = morse_code.split('/')
    text = []
    for word in words:
        characters = word.split()
        for character in characters:
            if character in morse_code_dict.values():
                text.append([key for key, value in morse_code_dict.items() if value == character][0])
                
    return ' '.join(text)

#Passing input and output file as arguments 
def main(input_file, output_file):

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        morse_code = infile.read()
        morse_code = re.sub('[^./\s-]', '', morse_code)
        translated_text = morse_to_text(morse_code)
        outfile.write(translated_text)
        #Showing the "Converted Successfully", saving data in output file and showing output file data too 
        print("\n"+"Converted Successfully!!"+ "\n")
        print("Output Text:")
        print(translated_text)

#Error Handling for number of input arguments :)
if __name__ == "__main__":
    if len(sys.argv) != 3:
        #Showing usage of this script If number of arguments are not equal to equal to 3
        print("\n"+"This script doesn't work like this brooo !"+"\n")
        print("Usage: python3 morse2text.py <input_file> <output_file>")
    else:
        #Converting input argument to variables and passing them to main function
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        main(input_file, output_file)
