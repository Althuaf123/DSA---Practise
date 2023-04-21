#find the minimum number of moves required to make all elements equal, where a move is defined as incrementing (n - 1) elements by 1, where n is the length of the array.

def minimum_moves(arr):
    total = sum(arr)
    length = len(arr)
    smallest_val = min(arr)

    moves = total - (length*smallest_val)

    return moves

arr = [1,2,3,4,5]
print(minimum_moves(arr))