letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8']

def is_valid_position(pos):
    return pos[0] in letters and pos[1] in numbers

def get_black_pieces(board):
    return {piece[2]: piece[0] for piece in board if piece[1] == 'zwart'}

def toren(position, black_pieces):
    letter = position[0]
    number = position[1]
    attacks = set()
    
    for l in letters:
        if l != letter:
            horizontal_move = l + number
            if horizontal_move in black_pieces:
                attacks.add((horizontal_move, black_pieces[horizontal_move]))

    for n in numbers:
        if n != number:
            vertical_move = letter + n
            if vertical_move in black_pieces:
                attacks.add((vertical_move, black_pieces[vertical_move]))

    return attacks

def loper(position, black_pieces):
    letter = position[0]
    number = position[1]
    attacks = set()
    
    for i in range(1, 8):
        for l in [-1, 1]: 
            new_letter = chr(ord(letter) + l * i)
            if new_letter in letters:
                new_number_up = str(int(number) + i)
                new_number_down = str(int(number) - i)  
                
                if new_number_up in numbers:
                    diagonal_move_up = new_letter + new_number_up
                    if diagonal_move_up in black_pieces:
                        attacks.add((diagonal_move_up, black_pieces[diagonal_move_up]))

                if new_number_down in numbers:
                    diagonal_move_down = new_letter + new_number_down
                    if diagonal_move_down in black_pieces:
                        attacks.add((diagonal_move_down, black_pieces[diagonal_move_down]))

    return attacks

def paard(position, black_pieces):
    letter = position[0]
    number = int(position[1])
    attacks = set()
    moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]
    
    for dx, dy in moves:
        new_letter = chr(ord(letter) + dx)
        new_number = number + dy
        if new_letter in letters and str(new_number) in numbers:
            move = new_letter + str(new_number)
            if move in black_pieces:
                attacks.add((move, black_pieces[move]))

    return attacks

def koningin(position, black_pieces):
    return loper(position, black_pieces).union(toren(position, black_pieces))

def can_strike(board):
    strikes = {}
    black_pieces = get_black_pieces(board)

    for piece in board:
        if piece[1] == 'wit':
            piece_type = piece[0]
            position = piece[2]
            attacks = set()

            if piece_type == 'toren':
                attacks = toren(position, black_pieces)
            elif piece_type == 'loper':
                attacks = loper(position, black_pieces)
            elif piece_type == 'paard':
                attacks = paard(position, black_pieces)
            elif piece_type == "koningin":
                attacks = koningin(position, black_pieces)

            strikes[position] = (piece_type, attacks)

    return strikes

result = can_strike([
    ("toren", "wit", "c5"), 
    ("toren", "wit", "d5"), 
    ("paard", "wit", "c4"), 
    ("loper", "wit", "f4"), 
    ("koningin", "wit", "f2"), 
    ("koningin", "zwart", "h6"), 
    ("toren", "zwart", "d6"), 
    ("toren", "zwart", "f8")
])

print(result)

board = [
    ("toren", "wit", "c5"),
    ("toren", "wit", "d5"),
    ("paard", "wit", "c4"),
    ("loper", "wit", "f4"),
    ("koningin", "wit", "f2"),
    ("koningin", "zwart", "h6"),
    ("toren", "zwart", "d6"),
    ("toren", "zwart", "f8")
]

result = can_strike(board)
print(result)


def test():
    print(can_strike([("paard", "zwart", "c6"), ("paard", "wit", "d4")]))

test()