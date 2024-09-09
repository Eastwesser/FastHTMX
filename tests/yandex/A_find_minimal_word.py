def find_minimal_word(R, C, crossword):
    words = []

    for row in crossword:
        words_in_row = row.split('#')
        for word in words_in_row:
            if len(word) >= 2:
                words.append(word)

    for col in range(C):
        column = ''.join(crossword[row][col] for row in range(R))
        words_in_col = column.split('#')
        for word in words_in_col:
            if len(word) >= 2:
                words.append(word)

    return min(words)


R, C = map(int, input().split())
crossword = [input().strip() for _ in range(R)]

print(find_minimal_word(R, C, crossword))
