import random


adverb = ['clumsily',
          'coaxingly',
          'coincidentally',
          'coldly',
          'colorfully',
          'commonly',
          'comfortably',
          'compactly']
adjective = ['tall', 'small', 'wide', 'angry', 'incongruous']
expletive = ['fuck', 'shit', 'arse', 'bum', 'cunt', 'tit']
noun = ['Baboon',
        'Bactrian Camel',
        'Badger',
        'Balinese',
        'Banded Palm Civet',
        'Bandicoot',
        'Barb',
        'Barn Owl',
        'Barnacle',
        'Barracuda',
        'Basenji Dog',
        'Basking Shark',
        'Basset Hound',
        'Bat',
        'Bavarian Mountain Hound',
        'Beagle']

print 'You %s %s %s-%s!' % (random.choice(adverb), random.choice(adjective), random.choice(expletive), random.choice(noun))
