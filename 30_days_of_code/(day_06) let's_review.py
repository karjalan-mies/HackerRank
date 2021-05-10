strings_list = []
count_strings = int(input())
if 1 <= count_strings <= 10:
    for i in range(count_strings):
        current_string = input()
        if 2 <= len(current_string) <= 10000:
            strings_list.append(current_string)

    for string in strings_list:
        even_indexed = ''
        odd_indexed = ''
        for indx, letter in enumerate(string):
            if indx % 2:
                odd_indexed = odd_indexed + letter
            else:
                even_indexed = even_indexed + letter
        print(f'{even_indexed} {odd_indexed}')
