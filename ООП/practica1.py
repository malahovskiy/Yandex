class Bird:
    def __init__(self, name: str, size: str):
        self.name: str = name
        self.size: str = size

    def describe(self, full: bool = False) -> str:
        return f"Размер птицы {self.name} — {self.size}."


class Parrot(Bird):
    def __init__(self, name, size, color):
        super().__init__(name, size)
        self.color: str = color

    def repeat(self, phrase):
        return f"Попугай {self.name} говорит: {phrase}."

    def describe(self, full: bool = False) -> str:
        if full is False:
            return Bird.describe(self)
        else:
            return (f"Попугай {self.name} — заметная тица, "
                    f"окрас её перьев — {self.color}, "
                    f"а размер — {self.size}. "
                    f"Интересный факт: попугаи чувствуют ритм, "
                    f"а вовсе не бездумно двигаются под музыку. "
                    f"Если сменить композицию, "
                    f"то и темп движений птицы изменится.")


class Penguin(Bird):
    def __init__(self, name: str, size: str, genus: str):
        super().__init__(name, size)
        self.genus: str = genus

    def swimming(self) -> str:
        return f"Пингвин {self.name} плавает со средней скоростью 11 км/ч."
        
    def describe(self, full: bool = False) -> str:
        if full is False:
            return Bird.describe(self)
        else:
            return (f"Размер пингвина {self.name} "
                    f"из рода {self.genus} — {self.size}. "
                    f"Интересный факт: однажды группа геологов-разведчиков "
                    f"похитила пингвинье яйцо, и их принялась преследовать "
                    f"вся стая, не пытаясь, впрочем, при этом нападать. "
                    f"Посовещавшись, похитители вернули птицам яйцо, "
                    f"и те отстали."
                    )


kesha = Parrot("Ара", "средний", "красный")
kowalski = Penguin("Королевский", "большой", "Aptenodytes")
print(kesha.repeat('Кеша хороший!'))
print(kowalski.swimming())