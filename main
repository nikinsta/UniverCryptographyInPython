import xor_encryption
import additive_stream_encryption

if __name__ == "__main__":
    print('main is running...')

    # 15 XOR-кодирование [русский]
    # xor_encryption.encoder('input_russian', 'output_russian', 'Катерина')
    # xor_encryption.encoder('output_russian', 'input_russian', 'Катерина')

    # 16 XOR-кодирование [английский]
    # xor_encryption.encoder('input_english', 'output_english', 'abacaba')
    # xor_encryption.encoder('output_english', 'input_english', 'abacaba')

    # 21 Гаммирование (Псевдослучайные последовательности) [регистр сдвига с линейной обратной связью] [русский]
    lfsr = additive_stream_encryption.linear_feedback_shift_register(23)
    # additive_stream_encryption.encoder('input_russian', 'output_russian', lfsr)
    # additive_stream_encryption.encoder('output_russian', 'input_russian', lfsr)

    # 22 Гаммирование (Псевдослучайные последовательности) [регистр сдвига с линейной обратной связью] [английский]
    # additive_stream_encryption.encoder('input_english', 'output_english', lfsr)
    # additive_stream_encryption.encoder('output_english', 'input_english', lfsr)

    # 23 Гаммирование (Псевдослучайные последовательности) [конгруэнтный генератор] [русский]
    lcg = additive_stream_encryption.linear_congruential_generator(31, 1103515245, 12345, 2 ** 31 - 1)
    # additive_stream_encryption.encoder('input_russian', 'output_russian', lcg)
    # additive_stream_encryption.encoder('output_russian', 'input_russian', lcg)

    # 24 Гаммирование (Псевдослучайные последовательности) [конгруэнтный генератор] [английский]
    # additive_stream_encryption.encoder('input_english', 'output_english', lcg)
    # additive_stream_encryption.encoder('output_english', 'input_english', lcg)

    ###################################################################
    # g1 = additive_stream_encryption.linear_congruential_generator(1)
    # g2 = additive_stream_encryption.linear_congruential_generator(1)

    # for _ in range(100):
    #   if next(g1) != next(g2):
    #        print('ERROR')

    ###################################################################

    # print(sys.path)
    # for m in sys.modules:
    #   print(m)

    # xor_coding.encoder_russian('input', 'output', 'фыва')
    # encoding='cp1251'
    # ifn = r"C:\Users\User\PycharmProjects\UniversalAlgebra\input.txt"
    # ofn = r"C:\Users\User\PycharmProjects\UniversalAlgebra\output.txt"
