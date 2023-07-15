def count_substring(string, sub_string):
    count = 0
    if 1 <= len(string) <= 200:
        for i in range(len(string)):
            if string[i:(i + len(sub_string))] == sub_string:
                count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    print(len(string), sub_string.lower(), string.lower())
    count = count_substring(string, sub_string)
    print(count)