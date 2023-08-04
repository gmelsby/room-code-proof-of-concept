def main():
    code_set = set()
    for i in range(26 ** 4 + 1):
        num = ((i * 29311) % (26 ** 4))
        code = encode_num(num)
        if code in code_set:
            print(f'code {code} already in codeset: {i} codes generated')
            break
        code_set.add(code)
        print(code)

def encode_num(number):
    """
    takes a number and encodes it to a 4-letter code
    """
    positions = []

    for i in range(4):
        positions.append(number % 26)
        number = number // 26

    return ''.join([chr(97 + num) for num in positions])

if __name__ == "__main__":
    main()