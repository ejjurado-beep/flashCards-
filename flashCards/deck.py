import csv
import random
from flashcard import Flashcard


class Deck:
    def __init__(self, csv_path: str):
        self.cards = self._load_cards(csv_path)
        self.current_index = 0

    def _load_cards(self, csv_path: str):
        cards = []
        with open(csv_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) < 2:
                    continue
                question = row[0].strip()
                answer = row[1].strip()
                cards.append(Flashcard(question, answer))
        return cards

    def shuffle(self):
        random.shuffle(self.cards)
        self.current_index = 0

    def get_current_card(self):
        if not self.cards:
            return None
        return self.cards[self.current_index]

    def next_card(self):
        if not self.cards:
            return None
        self.current_index += 1
        if self.current_index >= len(self.cards):
            self.current_index = 0
        return self.get_current_card()

    def size(self):
        return len(self.cards)
