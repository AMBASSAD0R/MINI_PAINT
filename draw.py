def draw_field(width, height, background_char):
    for _ in range(height):
        for __ in range(width):
            print(background_char, end=' ')
        print(' ')


def draw_rectangle_fill(X, Y, background_char, r, x, y, width, height, char):
    draw_field(X, Y, background_char)

