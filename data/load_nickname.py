nickname = set()


def load_nickname():
    with open("data/nickname_animal.csv", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            if line == "\n" or len(line) > 7:
                continue
            if line.__contains__("/"):
                temp = line.split("/")
                nickname.update(temp)
            nickname.add(line.strip())
