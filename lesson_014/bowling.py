# -*- coding: utf-8 -*-
TYPE_FRAME_CHAR_DIGIT = '123456789'


class ErrorInputData(Exception):
    pass


class ErrorSumFrame(Exception):
    pass


def get_score(game_result: str = '') -> int:

    if game_result is None:
        print('The --game_result parameter in the command line is required or -h for help!')
        exit(1)
    frame_code_list = []
    game_result_lst = list(game_result)
    length_game_result = len(game_result_lst)
    i = 0
    score = 0
    one_digit_in_end_str = False
    while i < length_game_result:
        if game_result_lst[i] == "X":
            code_frame = "X"
            i += 1
        else:
            code_frame = game_result_lst[i]
            i += 1
            if i == length_game_result:
                one_digit_in_end_str = True
                break
            code_frame += game_result_lst[i]
            i += 1
        frame_code_list.append(code_frame)

    if one_digit_in_end_str:
        message_error = f"Недопустимое значание последнего фрэйма <{game_result[-1:]}>\n"
        print(message_error)
        raise ErrorInputData(message_error)

    for code_frame in frame_code_list:
        if code_frame == 'X':
            score += 20
        elif code_frame[0] in TYPE_FRAME_CHAR_DIGIT and code_frame[1] == '/':
            score += 15
        elif code_frame[0] == '-' and code_frame[1] in TYPE_FRAME_CHAR_DIGIT:
            score += int(code_frame[1])
        elif code_frame[0] in TYPE_FRAME_CHAR_DIGIT and code_frame[1] == '-':
            score += int(code_frame[0])
        elif code_frame == '--':
            pass
        elif code_frame[0] in TYPE_FRAME_CHAR_DIGIT and code_frame[1] in TYPE_FRAME_CHAR_DIGIT:
            sum_digits = int(code_frame[0]) + int(code_frame[1])
            if sum_digits <= 9:
                score += sum_digits
            else:
                message_error = f"Некорректное значание фрэйма <{code_frame}> в записи игры {game_result}\n" \
                                f"Сумма {sum_digits} не может быть больше 9"
                print(message_error)
                raise ErrorSumFrame(message_error)

        else:
            message_error = f"Недопустимое значание фрэйма <{code_frame}>\n" \
                            f"Недопустимые символы или их комбинация"
            print(message_error)
            raise ErrorInputData(message_error)

    return score


if __name__ == '__main__':
    game_res = '1X'
    print(get_score(game_result=game_res))
