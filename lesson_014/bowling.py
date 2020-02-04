

TYPE_FRAME_CHAR_DIGIT = '123456789'


class ErrorInputData(Exception):
    pass


class ErrorSumFrame(Exception):
    pass


def get_score(game_result: str = '') -> int:

    frame_code_list = []
    game_result_lst = list(game_result)
    length_game_result = len(game_result_lst)
    i = 0
    score = 0
    while i < length_game_result:
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
                raise ErrorSumFrame(f"Некорректное значание фрэйма <{code_frame}> \n "
                                    f"Сумма {sum_digits} не может быть бользе 9")
        else:
            raise ErrorInputData(f"Некорректное значание фрэйма <{code_frame}> \n "
                                 f"Недопустимые символы или их комбинация")
    return score


if __name__ == '__main__':
    print(get_score(game_result='X4/34-45-23'))
