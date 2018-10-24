def get_scores():
    try:
        with open("scores.txt", "r+") as file:
            lines = file.readlines()
            pairs = {}
            for line in lines:
                line = line[:-1]
                name, time = line.split(" ")
                pairs.update({name: time})
        return pairs
    except FileNotFoundError:
        file = open("scores.txt", "w")
        return {}

def write_scores(pairs):
    with open("scores.txt", "w") as file:
        data = ""
        for name in pairs:
            line = str(name + " " + pairs[name] + "\n")
            data += line
        file.write(data)
        return
