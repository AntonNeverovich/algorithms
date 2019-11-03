import string


def rank(st, we, n):
    if st:
        list_players = []
        name_players = [player for player in st.split(',')]
        if n > len(name_players):
            return 'Not enough participants'
        else:
            if len(name_players) == len(we):
                for i in range(len(name_players)):
                    list_players.append(Player(name_players[i], we[i]))

            sorted_players = sorted(list_players, key=lambda x: x.name)
            sorted_players.sort(key=lambda x: x.winning_number, reverse=True)
            print([str(player) for player in sorted_players])

            return sorted_players[n - 1].name
    else:
        return 'No participants'


class Player:

    def __init__(self, name: str, weight: int) -> None:
        self.name = name
        self.som = self.get_som()
        self.weight = weight
        self.winning_number = self.som * self.weight

    @classmethod
    def letter_rank(cls, s: str):
        l = [b for b in string.ascii_lowercase]
        for i in range(len(l)):
            if s.lower() == l[i]:
                return i + 1

    def get_som(self):
        return len(self.name) + sum([self.letter_rank(s) for s in self.name])

    def __str__(self) -> str:
        return '{0}: {1}'.format(self.name, self.winning_number)


print(rank("Addison,Jayden,Sofia,Michael,Andrwe,Andrew,Benjamin", [4, 2, 1, 4, 3, 3, 2], 4))
