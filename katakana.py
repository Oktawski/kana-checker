import random


class Katakana:
    values: list[str] = """
        ア　イ　ウ　エ　オ
        カ　キ　ク　ケ　コ
        サ　シ　ス　セ　ソ
        タ　チ　ツ　テ　ト
        ナ　ニ　ヌ　ネ　ノ
        ハ　ヒ　フ　ヘ　ホ
        マ　ミ　ム　メ　モ
        ヤ　ユ　ヨ
        ラ　リ　ル　レ　ロ
        ワ　ヲ
        ン 
    """

    def get_random(self, max_word_length: int = 8) -> list[str]:
        max_word_length = max_word_length * 2 if max_word_length < 4 else max_word_length 
        return random.sample(self.values, random.randrange(1, max_word_length))
