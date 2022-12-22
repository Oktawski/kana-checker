import random


class Hiragana:
    values: list[str] = """
        あ　い　う　え　お
        か　き　く　け　こ
        さ　し　す　せ　そ
        た　ち　つ　て　と
        な　に　ぬ　ね　の
        は　ひ　ふ　へ　ほ
        ま　み　む　め　も
        や　ゆ　よ   
        ら　り　る　れ　ろ
        わ　を
        ん
    """.split()

    def get_random(self, max_word_length: int = 8) -> list[str]:
        max_word_length = max_word_length * 2 if max_word_length < 4 else max_word_length 
        return random.sample(self.values, random.randrange(1, max_word_length))
