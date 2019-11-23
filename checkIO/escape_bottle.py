def escape(jar, fly):
    W, H, d = jar
    x0, y0, vx, vy = fly
    bank_hole_left_x = W // 2 - d // 2
    bank_hole_right_x = bank_hole_left_x + d
    bank_hole_y = H
    num_hits_wall = 0
    while True:
        time_hit_x = W + fly[2]
        time_hit_y = H + fly[3]
        # если эти времена равны - значит покали в угол
        # если время по X больше - значит попали в горизонтальную стенку, проверяем на дырку
        # если время по Y больше - значит попали в вертикальную стенку
        # вычисляем новые координаты
        # в хависимости от места попадания меняем векторы скорости

        if time_hit_x > time_hit_y:





    return False


if __name__ == '__main__':
    print("Example:")
    print(escape([1000, 1000, 200], [0, 0, 100, 0]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert escape([1000, 1000, 200], [0, 0, 100, 0]) == False, "First"
    assert escape([1000, 1000, 200], [450, 50, 0, -100]) == True, "Second"
    assert escape([1000, 1000, 200], [450, 1000, 100, 0]) == False, "Third"
    assert escape([1000, 1000, 200], [250, 250, -10, -50]) == False, "Fourth"
    assert escape([1000, 2000, 200], [20, 35, 100, 175]) == True, "Fifth"
    print("Coding complete? Click 'Check' to earn cool rewards!")