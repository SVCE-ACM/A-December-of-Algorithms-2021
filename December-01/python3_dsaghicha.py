# #1 Elegant Facelift
# @Author: DSAghicha (Darshaan Aghicha)

def common_char(all_str: list[str]) -> int:
    """
    Identifies common characters in words of a list.

    Keyword Arguments:
    all_str: List of words

    Returns number of letters repeated.
    """
    rep_letters: int = 0
    limit: int = len(all_str)
    char_dict: dict[str: list[int]] = {}

    for word in all_str:
        unique: set[str] = set(word)
        for letter in unique:
            occurrence: int = word.count(letter)
            try:
                char_dict[letter].append(occurrence)
            except KeyError:
                char_dict[letter] = [occurrence]

    for key in char_dict:
        if len(char_dict[key]) == limit:
            rep_letters += 1
    return rep_letters


def main():
    words: list = [word for word in input("Enter space separated list of stones: ").split()]
    print(common_char(words))


if __name__ == '__main__':
    main()
