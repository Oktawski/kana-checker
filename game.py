from hiragana import Hiragana
from romaji import Romaji

class Game():
    def __init__(self):
        self.current_option: int = 0

        self.options = {
            1: "Hiragana to Romanji",
            2: "Romaji to Hiragana",
            3: "Quit"
        }

        self.hiragana: Hiragana = Hiragana()
        self.romaji = Romaji()

        self.hiragana_to_romaji = {self.hiragana.values[i]: self.romaji.values[i] for i in range(len(self.romaji.values))}
        self.romaji_to_hiragana = {self.romaji.values[i]: self.hiragana.values[i] for i in range(len(self.romaji.values))}

    
    def play(self):
        while self.current_option != 3:
            self.ask_for_input()


    def ask_for_input(self):
        if self.current_option == 0:
            self.current_option = int(input("Choose option:\n1. Hiragana to Romaji.\n2. Romaji to Hiragana.\n3. Quit\n"))

        elif self.current_option == 1:
            self.__ask_for_romaji()
        
        elif self.current_option == 2:
            self.__ask_for_hiragana()


    def __ask_for_romaji(self):
        try:
            syllables = self.hiragana.get_random()
            print("\n" + "".join(syllables))

            words = input("Type above stuff in romaji:\n").split()

            hiraganas_from_input = [self.romaji_to_hiragana[word] for word in words]

            is_winner = all([syllables[i] == hiraganas_from_input[i] for i in range(len(hiraganas_from_input))])

            correct_answer = " ".join([self.hiragana_to_romaji[i] for i in syllables])

            self.print_for_winner(is_winner, correct_answer)
        except KeyError:
            print("Wrong syllable")



    def __ask_for_hiragana(self):
        print("Not yet young one")
        self.current_option = 0
        self.ask_for_input()


    def print_for_winner(self, is_winner: bool, correct_answer = None):
        if (is_winner):
            print("Good job")
        else: 
            print("LOL no, try again. Should be: " + correct_answer)
