

def minion_game(string):

    # substrings = []
    if 0 < len(string) < 1000000:
        substrings = []
        for i in range(len(string)):
            for j in range(i+1, len(string)+1):
                substrings.append(string[i:j])

        vowels = "AEIOUaeiou"

        kevin_score = 0
        stuart_score = 0

        for i in range(len(substrings)):
            if substrings[i][0] in vowels:
                kevin_score += 1
            else:
                stuart_score += 1


        if kevin_score > stuart_score:
            print("kevin " + str(kevin_score))
        elif kevin_score == stuart_score:
            print("Draw")
        else:
            print("Stuart " + str(stuart_score))


if __name__ == '__main__':
    s = input()
    minion_game(s)