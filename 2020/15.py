p_input = [16,1,0,18,12,14,19]

stat = {}

turn = 1

prev = ''
spoken = ''

while True:
    print(turn)
    if turn <= len(p_input):
        spoken = p_input[turn-1]
        stat[spoken] = [turn]

    else:
        if len(stat[prev]) == 1:
            spoken = 0
            if stat.get(spoken, False):
                stat[spoken].append(turn)
            else:
                stat[spoken] = [turn]
        else:
            spoken = stat[spoken][-1] - stat[spoken][-2]
            if stat.get(spoken, False):
                stat[spoken].append(turn)
            else:
                stat[spoken] = [turn]

    prev = spoken
    if turn == 30000000:
        break

    turn += 1

print(spoken)
