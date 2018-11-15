# Jessica Angela Campisi
# 11/14/2018
# Reverse Story
# Description: It'll be a surprise :)

# import just the functions that are needed
from random import choice, seed
from textwrap import fill

# start the random seed generator
seed()


# define the story with formatting from textwrap
def story(story_name, story_weapon, story_town, story_enemy):
    line_1 = fill('There once was a hero named {0} from {2}. They spent all day training with their {1}. Day '
                  'after day there was a montage with fabulous music playing. One day the sun was blotted out of '
                  'the sky by an immense darkness. {0} was crushed. The montage was over. They would miss the '
                  'fabulous music.', 60).format(story_name, story_weapon, story_town, story_enemy)
    line_2 = fill('Looking to the horizon (which was hard to see with it being dark and all) they stood '
                  'tall. {1} in hand they looked to their enemy... the {3}! Rushing to their enemy the hero'
                  ' {0} gave it their all as their mighty weapon the {1} reflected the rays of the sun '
                  '(even though it was hidden). '.format(story_name, story_weapon, story_town, story_enemy), 70)
    line_3 = fill('Finally after days of combat (5 minutes), {0} and {3} stopped. Both were near passing out '
                  'from complete exhaustion. Suddenly the darkness moved away and they could see {2} again. '
                  '{0} looked up only to find they had been fighting their best friend the whole time! '.format(
        story_name, story_weapon, story_town, story_enemy), 70)
    line_4 = fill('"Well... that was fun", said {3}.'.format(story_name, story_weapon, story_town, story_enemy), 70)
    teh_story = line_1 + '\n\n' + line_2 + '\n\n' + line_3 + '\n\n' + line_4

    return teh_story


# Variables needed
name = ['Eric the bored', 'Millie the Goldfish', 'Captain Keureg', 'Sassy June', 'Bob the Clueless']
weapon = ['screaming swordfish', 'burned out taser', 'cast iron skillet', 'very old tapioca pudding', 'smiley face',
          'rubber chainsaw', 'grapes of wrath', 'a horribly written book']
home_town = ['Omaha', 'Denver', 'Narnia', 'Middle Earth', 'Babylon 5', 'Rome', 'Alpha Centauri', 'Under the sea']
enemy = ['terribly short orc', 'exceedingly angry actuary', 'time displaced English gentlemen', 'nerdy gangster',
         'upbeat cardboard cutout', 'silly siren that sang soothing songs', 'captivating space pirate who was afraid'
                                                                            'of water']
# Start the story! Row well and live!
print("\n\nWelcome to the odd story program.")
print("Time to tell the story... it began long ago... yesterday...\n\n")

# send the random choices of each list into the story. Return the complete story into the variable true_story
true_story = story(choice(name), choice(weapon), choice(home_town), choice(enemy))

# reverse the letters in the story. Make life hard.
print(true_story)

# concatenate 2 literal strings, because reversing the escape sequence will stop it from working right.
print("\n\n" + "Teh End"[::-1])
