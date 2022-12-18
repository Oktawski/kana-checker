from hiragana import Hiragana
from romanji import Romanji

class Game():
    def __init__(self):
        self.current_option: int = 0

        self.options = {
            1: "Hiragana to Romanji",
            2: "Romanji to Hiragana",
            3: "Quit"
        }

        self.hiragana = Hiragana()
        self.romanji = Romanji()

        self.hiragana_to_romanji = {self.hiragana.values[i]: self.romanji.values[i] for i in range(len(self.romanji.values))}
        self.romanji_to_hiragana = {self.romanji.values[i]: self.hiragana.values[i] for i in range(len(self.romanji.values))}

    
    def play(self):
        while self.current_option != 3:
            self.ask_for_input()


    def ask_for_input(self):
        if self.current_option == 0:
            self.current_option = int(input("Choose option:\n1. Hiragana to Romanji.\n2. Romanji to Hiragana.\n3. Quit\n"))

        elif self.current_option == 1:
            is_winner = self.__ask_for_romanji()
            print(is_winner)
        
        elif self.current_option == 2:
            self.__ask_for_hiragana()


    def __ask_for_romanji(self):
        hiraganas = self.hiragana.get_random_words(5, 1)
        print("\n" + "".join(hiraganas[0]))

        words = input("Type above stuff in romanji:\n").split()

        hiraganas_from_input = [self.romanji_to_hiragana[word] for word in words]

        corrects = [hiraganas[0][i] == hiraganas_from_input[i] for i in range(len(hiraganas_from_input))]

        is_winner = all(corrects)

        return is_winner


    def __ask_for_hiragana():
        print("Not yet young one")

    def print_for_winner(self, is_winner: bool):
        if (is_winner):
            print("Good job")
        else: 
            print("LOL no, try again")
