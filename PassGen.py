#!/usr/bin/env python3
# Simple password generator
# Author : James Bryant

import string
import argparse
import random

class PasswordGenerator():
    '''
    Password Generator obj.
    call generate_password() to return a random string
    '''
    def __init__(self, length, letters, digits, punctuation):
        self.length = length
        self.letters = letters
        self.digits = digits
        self.punctuation = punctuation

    def generate_password(self):
        '''Returns a string of random characters.'''
        self.characters = []
        self.password = ''

        if self.letters:
            self.characters += string.ascii_letters
        if self.digits:
            self.characters += string.digits
        if self.punctuation:
            self.characters += string.punctuation

        for x in range(self.length):
            self.password += random.choice(self.characters)

        return self.password

def main():
    parser = argparse.ArgumentParser(
        description='Simple script to generate random passwords')

    parser.add_argument(
        '--length', help='The number of characters you want in your password', 
        type=int, default=8)

    parser.add_argument(
        '--no-letters', help='Whether to have letters in the password or not', 
        dest='letters', action='store_false', default=True)

    parser.add_argument(
        '--no-digits', help='Whether to have digits in the password or not', 
        dest='digits', action='store_false', default=True)

    parser.add_argument(
        '--no-punctuation', help='Whether to have punctuation in the password or not', 
        dest='punctuation', action='store_false', default=True)

    args = parser.parse_args()

    generator = PasswordGenerator(
        args.length, args.letters, 
        args.digits, args.punctuation)
    
    print(generator.generate_password())

if __name__ == '__main__':
    main()

