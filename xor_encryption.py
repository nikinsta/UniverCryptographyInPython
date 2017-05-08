#!/usr/bin/env python
# -*- coding: utf-8 -*-

def encoder(input_file_name='input', output_file_name='output', key=u'абвгд'):
    key = key.lower()
    input_file = open(input_file_name, 'r', encoding='utf-8')  # encoding='cp1251'
    # message = input_file.readline()

    # row_message = input_file.read(2)
    row_message = input_file.readlines()
    message = u''
    for row_line in row_message:
        message += row_line

    encoded_message = u''
    for i in range(len(message)):
        c = chr(ord(message[i]) ^ ord(key[i % len(key)]))
        if c != '\r':
            encoded_message += c
        else:
            encoded_message += message[i]
            # encoded_message += str(ord(message[i]) ^ ord(key[i % len(key)])) + '\n'
            # encoded_message += repr(chr(ord(message[i]) ^ ord(key[i % len(key)])))[1:-1]

    output_file = open(output_file_name, 'w', encoding='utf-8')
    output_file.write(encoded_message)
    # output_file.write(m)

    input_file.close()
    output_file.close()

