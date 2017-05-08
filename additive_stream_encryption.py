# http://cryptowiki.net/index.php?title=Криптографические_генераторы._Поточные_шифры_и_их_криптоанализ
# https://ru.wikipedia.org/wiki/Регистр_сдвига_с_линейной_обратной_связью


def linear_feedback_shift_register(seed):
    # function : number -> bit
    # generation of new bit
    def new_bit(n):
        return ((n >> 31) ^ (n >> 30) ^ (n >> 29) ^ (n >> 27) ^ (n >> 25) ^ n) & 1
    # main loop
    cur = seed
    while True:
        cur = (new_bit(cur) << 31) | (cur >> 1)
        yield cur


def linear_congruential_generator(seed, a=1103515245, c=12345, m=2 ** 31 - 1):
    # using GCC parameters
    # a = 214013
    # c = 2531011
    prev = seed
    while True:
        prev = (a * prev + c) % m
        yield prev


def encoder(input_file_name='input', output_file_name='output',
            generator=linear_congruential_generator(1, 1103515245, 12345)):
    message = ''

    input_file = open(input_file_name, 'r', encoding='utf-8')
    lines = input_file.readlines()
    for line in lines:
        message += line

    encoded_message = ''

    for char in message:
        rand_number = next(generator) % 1000
        encoded_char = chr(ord(char) ^ rand_number)
        encoded_message += encoded_char if encoded_char != '\r' else char

    output_file = open(output_file_name, 'w', encoding='utf-8')
    output_file.write(encoded_message)


if __name__ == "__main__":
    # linear_feedback_shift_register

    lfsr = linear_feedback_shift_register(23)
    st = set()
    for _ in range(33333):
        cur = next(lfsr)
        st.add(cur)
        # print(cur)

    print(len(st))

    exit()

    # linear_congruential_generator

    seed = 361
    data_size = 1000000
    # a = 214013
    # c = 2531011
    # a = 22695477
    # c = 1

    lcg = linear_congruential_generator(seed)
    cnt = [] * 10
    for i in range(10):
        cnt.append([i, 0])

    for _ in range(data_size):
        n = next(lcg) % 1000
        cnt[n % 10][1] += 1
        # print(n)

    cnt = sorted(cnt, key=lambda x: x[1])
    # print('cnt :')
    # for item in cnt:
    # print(item)
    d = cnt[-1][1] - cnt[0][1]
    print('abs : ', d)
    print('rel (%) : ', round(d / data_size * 100, 3))
