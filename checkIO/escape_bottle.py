def escape(jar, fly):
    W, H, d = jar
    x0, y0, vx, vy = fly
    bank_hole_left_x = W / 2 - d / 2
    bank_hole_right_x = bank_hole_left_x + d
    bank_hole_y = H
    num_hits_wall = 0
    while num_hits_wall < 20:
        # если эти времена равны - значит попали в угол
        # если время по X больше - значит попали в горизонтальную стенку, проверяем на дырку
        # если время по Y больше - значит попали в вертикальную стенку
        # вычисляем новые координаты
        # в зависимости от места попадания меняем векторы скорости
        if vx > 0: # вправо
            time_hit_x = abs((W - x0) / vx)
        elif vx < 0:# влево
            time_hit_x = abs(x0 / vx)
        else:# без смещения по Х
            time_hit_x = 0

        if vy > 0:# вверх
            time_hit_y = abs((H - y0) / vy)
        elif vy < 0:# вниз
            time_hit_y = abs(y0 / vy)
        else:# без смещения по Y
            time_hit_y = 0

        if (time_hit_x < time_hit_y or time_hit_y == 0) and not time_hit_x == 0:
            if vx > 0: # врезались в вертикальную стенку правую
                x0 = W
                y0 = y0 + time_hit_x * vy
            elif vx < 0: # врезались в вертикальную стенку левую
                x0 = 0
                y0 = y0 + time_hit_x * vy
            vx = -vx
        elif (time_hit_x > time_hit_y or time_hit_x == 0) and not time_hit_y == 0:
            if vy < 0:  # врезались в нижнюю стенку
                y0 = 0
                x0 = x0 + time_hit_y * vx
            elif vy > 0: # врезались в верхнюю стенку
                y0 = H
                x0 = x0 + time_hit_y * vx
                if bank_hole_left_x < x0 < bank_hole_right_x:
                    return True
                    # print('Муха вылетела')
                    # break
            vy = -vy
        elif time_hit_x == time_hit_y:
            if vx > 0 and vy > 0:
                x0 = W
                y0 = H
            elif vx > 0 and vy < 0:
                x0 = W
                y0 = 0
            elif vx < 0 and vy < 0:
                x0 = 0
                y0 = 0
            elif vx < 0 and vy > 0:
                x0 = 0
                y0 = H
            vx = -vx
            vy = -vy
        num_hits_wall += 1

        # print(f'x0={x0} y0={y0} vx={vx} vy={vy} столкновение {num_hits_wall}')
    return False


if __name__ == '__main__':
    print("Example:")
    assert escape([1000, 1000, 200], [20, 35, 100, 175])

    # These "asserts" are used for self-checking and not for an auto-testing
    assert escape([1000, 1000, 200], [0, 0, 100, 0]) == False, "First"
    assert escape([1000, 1000, 200], [450, 50, 0, -100]) == True, "Second"
    assert escape([1000, 1000, 200], [450, 1000, 100, 0]) == False, "Third"
    assert escape([1000, 1000, 200], [250, 250, -10, -50]) == False, "Fourth"
    assert escape([1000, 2000, 200], [20, 35, 100, 175]) == True, "Fifth"
    print("Coding complete? Click 'Check' to earn cool rewards!")