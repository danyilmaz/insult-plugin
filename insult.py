import os
import willie
from willie import module
import random

'''
An insult generator that works off the pricipal of
<adverb><adjective><expletive><concrete noun> = hilarity
You warmly forceful cunt-ghost!

This is not supposed to include aggressively homophobic or racial slurs,
however, the lists of words were copied en mass, so some inoffensive words
may be left with more offence than intended when in the sentence below.
For example, "pinto" has just been removed from the nouns because of its
racial slur connotations
'''


def _word_picker(filename):
    filepath = os.path.join(os.path.dirname(__file__), 'word_lists', filename)
    with open(filepath) as words_file:
        words = words_file.read().splitlines()
        return random.choice(words)


@module.rule('fuck off, jerkins')
@module.rule('fuck off jerkins')
def comment(bot, trigger):

    adverb = _word_picker('adverbs.txt')
    adjective = _word_picker('adjectives.txt')
    expletive = _word_picker('expletives.txt')
    noun = _word_picker('nouns.txt')
    verb = _word_picker('verbs.txt')
    consequence = _word_picker('consequences.txt')

    bot.say('Don\'t tell me to fuck off, you %s %s %s-%s, I %s %s!' % (adverb, adjective, expletive, noun, verb, consequence))
#print 'Don\'t tell me to fuck off, you %s %s %s-%s, I %s %s!' % (adverb, adjective, expletive, noun, verb, consequence)
