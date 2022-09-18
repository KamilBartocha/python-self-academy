print("hello universe")

programming_languages = "python", "c", "go", "c#"

for i in programming_languages:
    print(i)

game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]


def game_board(game_map, player=0, row=0, column=0):
    try:
        print("   0  1  2")
        if player != 0:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map
    except:
        print("something went wrong")



game = game_board(game, player=1, row=2, column=1)


x = 1
def test():
    x = 2
test()
print(x) #1


x = 1
def test():
    global x
    x = 2
test()
print(x) #2


x = [1]
def test():
    x = [2]
test()
print(x) # 1


x = [1]
def test():
    global x
    x = [2]
test()
print(x) # 2


x = [1]
def test():
    x[0] = 2
test()
print(x) #2
