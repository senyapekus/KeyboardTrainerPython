import sys

if len(sys.argv) > 1:
    with open("text_speed_test.txt", "a", encoding='utf8') as file:
        file.write('\n')
        for i in range(len(sys.argv) - 1):
            file.write(sys.argv[i + 1])
            if i != len(sys.argv) - 2:
                file.write(' ')
