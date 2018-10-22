def get_scores():
    with open("scores.txt", "r+") as file:
        scores_list = file.readlines()
    scores_dict = {}
    for score in scores_list:
        time, player = score.split(" ")
        if player[-1] == "\n":
            player = player[:-1]
        scores_dict.update({time : player})
    return scores_dict
