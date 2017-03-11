#!/usr/bin/env python

import random
import sys, os

POSITIVE_STRINGS = ['Nice one!', 'Slick!', 'Great job!', 'Keep it up!', "Heyy! That's pretty good!"]
NEGATIVE_STRINGS = ['Sorry!', 'You dun goofed.', 'Git gud.', 'Pathetic.', 'Come on now...', 'You should uninstall.', "Don't quit your day job."]
PROFANITIES = ['nhedev', 'nhede', 'bhv`l', 'Bhv`l)', 'bhv`l`u', 'ptqp}', 'dhah', 'ftah']

# lol,
def ord_xor_word(word):
    s = ''
    for i, c in enumerate(word):
        s += chr(ord(c) ^ i)
    return s

def handle_profanities(line, censor=True):
    r = []
    for word in line.split(' '):
        w = ord_xor_word(word)
        if censor:
            if word in PROFANITIES:
                w = w[0] + '**' + w[3:]
        r.append(w)
    return ' '.join(r)


def run(censor):
    split = {}
    with open('lyrics_hidden.txt', 'r') as lyrics:
        lines = [line for line in lyrics]
        questions = filter(lambda l: "(xws-" in l or "(omsa," in l, lines)
        for q in questions:
            q = handle_profanities(q, censor)
            qa = q.split('(')
            qa[0] = qa[0].replace(' 7', "'?")
            qa[1] = qa[1].replace(')', '')
            question, answer = qa
            split[question] = answer.replace('(', '')[:-2]
    while True:
        score = 0
        for k, v in split.iteritems():
            a = raw_input(k)
            if a != v:
                print random.choice(NEGATIVE_STRINGS)
                break
            else:
                print random.choice(POSITIVE_STRINGS)
                score += 1
        if score == len(split.keys()):
            print 'You won, pal!'
            r = raw_input('Play again? (y / n)')
            if (r.lower() == 'n'):
                print 'Bye Champ!'
                break
        else:
            r = raw_input('Try again? (y / n)')
            if (r.lower() == 'n'):
                print 'Quitter.'
                break

if __name__ == '__main__':
    censor = True
    try:
       censor = not (sys.argv[1] == '--uncensored')
    except IndexError:
        pass
    try:
        run(censor)
    except KeyboardInterrupt:
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

