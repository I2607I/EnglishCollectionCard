import random
class Card():
    def __init__(self, name, rarity):
        self.name = name
        self.rarity = rarity

    def __repr__(self):
        return self.name + ' ' + self.rarity



class Pack():
    def __init__(self):
        self.pack  = []
        self.count_common = 8
        self.count_rare = 1
        self.chance_super_rare = 1/8
        self.chance_ultra_rare = 1/64
        self.gen_cards("common", self.count_common)
        self.gen_cards("rare", self.count_rare)
        self.gen_chance_cards("super_rare", self.chance_super_rare)
        self.gen_chance_cards("ultra_rare", self.chance_ultra_rare)


    def gen_cards(self, type_card, count):
        with open(f"cards/{type_card}_cards.txt", "r") as f:
            lines = f.readlines()
        random_lines = random.sample(lines, k=count)
        for line in random_lines:
            line = line.strip()
            line = list(line.split())
            name = line[0]
            self.pack.append(Card(name, type_card))

    def gen_chance_cards(self, type_card, chance):
        with open(f"cards/{type_card}_cards.txt", "r") as f:
            lines = f.readlines()
        line = random.choice(lines)
        line = line.strip()
        line = list(line.split())
        name = line[0]
        if random.random() < chance:
            self.pack.append(Card(name, type_card))
            
           


        
    def __str__(self):
        return "\n".join([repr(card) for card in self.pack])

pack = Pack()
print(pack)

print(random.random())

            

        
