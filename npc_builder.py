#Nat'l Parks' NPC generator
#this was programed in python 3.9.4
'''this NPC generator is meant to help with quick NPC generation, putting out a
couple of NPCs with description and characteristics, not stats aside
from a high stat/low stat for physical description.'''
#high stat/low stat tbd
#motivations tbd

'''core archetecture is going to be basic: lists of traits and random selection
among them.  i may revisit if/when i have more skill.
Program will deliver a dictionary, then print using key:item pairings.'''

from random import randint  #getting the random number finder first

#apperance in a broad/generl sense
apper = ['athletic', 'barrel-chested', 'boney',  'brawny',  'brutish',  'bull-necked',  'chiseled',  'coltish',  'craggy', \
         'delicate',  'furrowed',  'gaunt',  'gorgeous',  'grizzled',  'haggard',  'handsome',  'hideous',  'lanky',  'pudgy', \
         'ripped',  'rosey',  'scrawny',  'sinewy',  'slender',  'slumped',  'solid',  'square-jawed',  'towering',  'trim', \
         'weathered',  'willowy',  'wiry',  'wrinkled']
#notable physical traits
phys_trait = ['accent', 'acid scars',  'battle scars',  'birthmark',  'braided hair',  'brand mark',  'broken nose',  'burn scars', \
              'bushy eyebrows',  'curly hair',  'dark skinned',  'dreadlocks',  'flogging scars',  'freckles',  'gold tooth',  \
              'hoarse voice',  'huge beard',  'long hair',  'missing ear', 'missing teeth', 'mustache',  'nine fingers',  'slicked hair', \
              'one-eyed',  'pale skinned',  'piercings',  'ritual scars',  'sallow skin',  'shaved head',  'sunburned',  'tattoos',  \
              'topknot']
#core personality (product of two merged lists, so not alphabetical
perso = ['bitter', 'brave',  'cautious',  'chipper',  'contrary',  'cowardly',  'cunning',  'driven',  'entitled',  'gregarious',  \
         'grumpy',  'heartless',  'honor-bound',  'hotheaded',  'inquisitive',  'jolly',  'lazy',  'loyal',  'menacing',  \
         'mopey',  'nervous',  'protective',  'righteous',  'rude',  'sarcastic',  'savage',  'scheming',  'serene',  'spacey', \
         'stoic',  'stubborn',  'stuck-up',  'suspicious',  'wisecracking',  'aggressive',  'angry',  'awkward',  'belittling',  \
         'capricious',  'charmless',  'cheerless',  'compulsive',  'cruel--overtly',  'cruel--secretively',  'cunning',  \
         'deceitful',  'delusional',  'dour',  'draconian', 'erratic',  'faded', 'greedy',  'hungry',  'hyper',  'immature', \
         'irritable',  'isolated',  'jealous',  'lazy',  'manipulative',  'meek',  'melodramatic',  'merciless',  'miserable', \
         'moody',  'narcissistic',  'opinionated',  'outrageous',  'paranoid',  'pathetic',  'pessimist',  'precise',  'puritanical', \
         'racist',  'repressed',  'scathing',  'self-important',  'self-indulgent',  'selfish',  'timid',  'troubled',  'vain', \
         'vindictive',  'vulgar']
#two job lists, one for country and one for city
job_city = ['acolyte',  'actor',  'apothecary',  'baker',  'barber',  'blacksmith',  'brewer',  'bureaucrat',  'butcher',  'carpenter', \
            'clockmaker',  'courier',  'courtier',  'diplomat',  'fishmonger',  'guard',  'haberdasher',  'innkeeper',  \
            'merchant',  'jeweler',  'knight',  'locksmith',  'mason',  'mercenary', 'miller',  'musician',  'noble',  'painter',  \
            'priest',  'scholar',  'scribe',  'sculptor',  'shipwright',  'soldier',  'tailor',  'taxidermist',  'wigmaker',  \
            'alchemist',  'bounty-hunter',  'burglar',  'chimney-sweep',  'cutpurse',  'forger',  'fortune-teller',  \
            'gambler',  'gravedigger',  'headsman',  'hedge-knight',  'highwayman',  'peddler',  'rat-catcher',  'sellsword',  \
            'smuggler',  'street-performer',  'tattooist',  'urchin', 'arcanist']
job_rural = ['bandit',  'caravaneer',  'druid',  'exile',  'explorer',  'farmer',  'fisherman',  'fugitive',  'hermit',  'hunter',  \
             'messager',  'monk',  'outlander',  'tinker',  'pilgrim',  'ranger',  'sheppard',  'surveyor',  'trader',  'trapper', \
             'troubadour',  'wood-cutter',  'witch/wizard']
#importing the ancestry system from my character builder here (between the three # marks):

###
#ancestry uses a percentile system between common, uncommon, and rare ancestries
#rarity is based on my homebrew world, with the following percentages:
#35% human, 35% common, 20% uncommon, and 10% rare.
anc_h = ["human"]  #the first ancesty list is just human
anc_c = ["orc", "lizardfolk", 'kobold', 'hobgoblin',\
         'goblin', 'halfling', 'elf', \
         'dwarf']  #these are the common ancestires
anc_uc = ['yuan-ti pureblood', 'triton', 'tabaxi', 'kenku', 'goliath', \
          'firbolg', 'bugbear', 'tiefling', 'half-orc', 'half-elf', \
          'gnome', 'dragonborn', 'dragonborn (Ravenite)']  #these are the uncommon ancestries
anc_r = ['harengon', 'fairy', 'reborn', 'hexblood', 'dhampir', 'aasimar', \
         'custom lineage', 'gith (githzerai)', 'gith (githyanki)', 'satyr', 'minotaur', \
         'leonin', 'centaur', 'vedalken', 'simic hybrid', 'loxodon', 'warforged', \
         'shifter', 'kalashtar', 'changeling', 'dragonborn (draconblood)', 'genasi (water)', \
         'genasi (fire)', 'genasi (earth)', 'genasi (air)', 'aarakocra', 'merfolk', \
         'verdan']  #these are the rarest ancestires

def pick_one(chosen_list):  #this program will iterate within a given list and pick a random one
    y = randint(1,len(chosen_list))
    return chosen_list[y-1]  #return the item at index y-1 in the list

def choose_ancestry(char):  #will take a dictionary, return an 'ancestry': _BLANK_ pairing
    x = randint(1,100)  #set x which determines the rarity of the race
    if x <= 35:  #if x is in the 1-35 range
        char["ancestry"] = pick_one(anc_h) #use the above function, but will return human
    elif x <= 70:  #if x is in the 36-70 range
        char["ancestry"] = pick_one(anc_c)
    elif x <= 90:  #if x is in the 71-90 range
        char["ancestry"] = pick_one(anc_uc)
    else:  #for all other situations, which is 91-100 range
        char["ancestry"] = pick_one(anc_r)
    return char

###
#okay, this last bit will be the part to build out an NPC using the other lists
def choose_pronouns(char):  #2021 UCLA Williams Inst. study found approx. 1.2 million nonbinary Americans, majority under 29 and white = 0.36% US pop
    x = randint(1,100)
    if x <= 50:  #assuming greater proportion of women than men
        char["pronoun"] = "she"
    elif x <= 99:  #bumping non-binary pronoun use to 1%, can revisit later
        char["pronoun"] = "he"
    else:
        char["pronoun"] = "they"
    return char


def build_npc(char):  #assume char is an empty dictionary
    choose_ancestry(char)
    choose_pronouns(char)
    char["apperance"] = pick_one(apper)
    char["physical trait"] = pick_one(phys_trait)
    char["personality"] = pick_one(perso)
    char["job, city"] = pick_one(job_city)
    char["job, rural"] = pick_one(job_rural)
    
def initiate_build():
    npc = {}
    build_npc(npc)
    return npc

#okay, let's add the vowel-checker to make the first line of into_plaintext() below look good, and could/should I add a gender poriton while at it?
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

def into_plaintext(char):  #this program will print out a nice sheet for the NPC, taking the directory built above as its argument
    if char["apperance"][0] in vowels:
        print("This npc is an %s %s with %s." % (char["apperance"], char["ancestry"], char["physical trait"]))
    else:
        print("This npc is a %s %s with %s." % (char["apperance"], char["ancestry"], char["physical trait"]))
    if char["pronoun"] == 'they':
        print("Personality-wise, they are %s." % (char["personality"]))
    else:
        print("Personality-wise, %s is %s." % (char["pronoun"], char["personality"]))
    if char['pronoun'] == 'they':
        print("If they are encountered in a city, they are a %s.  \nOtherwise, they are a %s." % (char["job, city"], char["job, rural"]))
    else:
        print("If %s is encountered in a city, %s is a %s.  \nOtherwise, %s is a %s." % \
              (char["pronoun"], char["pronoun"], char["job, city"], char["pronoun"], char["job, rural"]))
    print("")

#quickly testing by building 3 NPCs
for i in range(3):
    npc = initiate_build()
    into_plaintext(npc)
