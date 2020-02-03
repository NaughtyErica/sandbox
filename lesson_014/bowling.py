

TYPE_FRAME_CHAR_GOOD = 'X/-123456789'
TYPE_FRAME_CHAR_DIGIT = '123456789'


def get_score(game_result: str = '') -> int:

    frame_code_list = []
    game_result_lst = []
    for char in game_result:
        if char in TYPE_FRAME_CHAR_GOOD:
            game_result_lst.append(char)
        else:
            score = -1
            return score
    length_game_result = len(game_result_lst)
    i = 0
    score = 0
    while True:
        if game_result_lst[i] == "X":
            code_frame = "X"
            i += 1
        else:
            code_frame = game_result_lst[i]
            i += 1
            if i == length_game_result:
                break
            code_frame += game_result_lst[i]
            i += 1
        frame_code_list.append(code_frame)
        if i == length_game_result:
            break

    print(frame_code_list)
    for code_frame in frame_code_list:
        if code_frame == 'X':
            score += 20
        elif code_frame[0] in TYPE_FRAME_CHAR_DIGIT and code_frame[1] == '/':
            score += 15
        elif code_frame[0] == '-' and code_frame[1] in TYPE_FRAME_CHAR_DIGIT:
            score += int(code_frame[1])
        elif code_frame[0] in TYPE_FRAME_CHAR_DIGIT and code_frame[1] == '-':
            score += int(code_frame[0])
        elif code_frame[0] in TYPE_FRAME_CHAR_DIGIT and code_frame[1] in TYPE_FRAME_CHAR_DIGIT:
            sum_digits = int(code_frame[0]) + int(code_frame[1])
            if sum_digits <= 9:
                score += sum_digits
            else:
                score = -1
                break
        else:
            score = -1
            break
    return score


if __name__ == '__main__':
    print(get_score(game_result='/XX4/34-45-29'))
"""
Error 9X // -- X/ /X -/  /- /9  sum < 10
-79/X4/34-45-23

"""
