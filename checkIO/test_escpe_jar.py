# def escape(jar, fly):
#     W, H, d = jar
#     x, y, vx, vy = fly
#     next_bump = lambda x, y, vx, vy: min(max((W-x)/vx, -x/vx) if vx else 1e9, max((H-y)/vy, -y/vy) if vy else 1e9)
#     for _ in range(20):
#         t = next_bump(x, y, vx, vy)
#         x += vx * t
#         y += vy * t
#         if y == H and (W-d)/2 < x < (W+d)/2:
#             return True
#         if x in (0, W):
#             vx = -vx
#         if y in (0, H):
#             vy = -vy
#     return False


def escape(jar, fly):
    W, H, d = jar
    x0, y0, vx, vy = fly

    health = 100
    px, py = x0, y0
    mx = [0, W][vx > 0]
    my = [0, H][vy > 0]

    while health:
        if vy > 0 and py == H and W / 2 - d / 2 < px < W / 2 + d:
            return True

        if px == mx:
            vx = -vx
            mx = W - mx
        if py == my:
            vy = -vy
            my = H - my

        if vy / (my - py) >= vx / (mx - px):
            ny = my
            nx = (ny - py) / vy * vx + px
        else:
            nx = mx
            ny = (nx - px) / vx * vy + py

        px, py = nx, ny
        health -= 5

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