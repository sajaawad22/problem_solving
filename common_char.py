def common_characters(*strings):
    if len(strings) == 0:
        return ''

    first_string = strings[0]
    common_chars = ''

    for char in first_string:
        if char == ' ' or char in common_chars:
            continue

        is_common = True
        for i in range(1, len(strings)):
            if char not in strings[i]:
                is_common = False
                break

        if is_common:
            common_chars += char

    return common_chars


print(common_characters("hello", "world", "hold"))
