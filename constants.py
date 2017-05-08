russian_alphabet_with_punctuation_and_digits = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя .,\";:'?!()[]-0123456789№";
russian_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя";
english_alphabet_with_punctuation_and_digits = "abcdefghijklmnopqrstuvwxyz .,\";:'?!()[]-&`$0123456789";
english_alphabet = "abcdefghijklmnopqrstuvwxyz";





if __name__ == "__main__":
    print('contants is running...')
    print('input N : ')
    N = int(input())
    print('input ' + str(N - 1) + ' numbers:')
    a = []
    for _ in range(N - 1):
        a.append(int(input()))
    a = sorted(a)
    for i in range(0, N - 2):
        if a[i + 1] - a[i] > 1:
            print('output : ', a[i] + 1)

