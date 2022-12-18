import random


class Romanji:
    values: list[str] = """
        a i u e o
        ka ki ku ke ko
        sa shi su se so 
        ta chi tsu te to
        na ni nu ne no
        ha hi fu he ho
        ma mi mu me mo
        ya yu yo    
    """.split()

    def __get_random(self, max_word_length: int) -> str:
        return "".join(random.sample(self.values, random.randrange(1, max_word_length)))

    def get_random_words(self, word_length: int = 3, word_ammount: int = 3) -> list[str]:
        return [self.__get_random(word_length) for i in range(word_ammount)]