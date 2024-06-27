#radomlly choose a word to guess from the list we made
import random
word_list = ['abruptly', 'absurd', 'abyss', 'affix', 'askew', 'avenue', 'awkward', 'axiom', 'azure', 'bagpipes', 'bandwagon', 'banjo', 'bayou', 'beekeeper', 'bikini', 'blitz', 'blizzard', 
             'boggle', 'bookworm', 'boxcar', 'boxful', 'buckaroo', 'buffalo', 'buffoon', 'buxom', 'buzzard', 'buzzing', 'buzzwords', 'caliph', 'cobweb', 'cockiness', 'croquet', 'crypt', 'curacao', 'cycle', 'daiquiri', 'dirndl', 'disavow', 'dizzying', 'duplex', 'dwarves', 
             'embezzle', 'equip', 'espionage', 'euouae', 'exodus', 'faking', 'fishhook', 'fixable', 
             'fjord', 'flapjack', 'flopping', 'fluffiness', 'flyby', 'foxglove', 'frazzled', 'frizzled', 'fuchsia', 'zoo', 'keyhole', 'khaki', 'kilobyte', 'kiosk', 'kitsch', 
             'kiwifruit', 'klutz', 'knapsack', 'larynx', 'lengths', 'lucky', 'luxury', 'lymph', 'marquis',  'matrix', 'megahertz', 'microwave', 'mnemonic', 'mystify', 'naphtha', 'nightclub', 'nowadays', 
             'numbskull', 'nymph', 'onyx', 'ovary', 'oxidize', 'oxygen', 'pajama', 'peekaboo', 'phlegm', 'pixel', 'pizazz', 'pneumonia', 'polka', 'pshaw', 'psyche', 'puppy', 'puzzling', 'quartz', 'queue', 'quips', 
             'quixotic', 'quiz', 'quizzes', 'tourism', 'walkway', 'waltz', 'wave', 'wavy', 'waxy', 
             'wellspring', 'wheezy', 'whiskey', 'whizzing', 'whomever', 'wimpy', 'witchcraft', 'wizard', 'woozy', 
             'wristwatch', 'wyvern', 'xylophone', 'yachtsman', 'yippee', 'yoked', 'youthful', 'yummy', 'zephyr', 
'zigzag', 'zigzagging', 'zilch', 'zipper', 'zodiac', 'zombie']

chosen_word = random.choice(word_list)
length = len(chosen_word)
#print(chosen_word) #test statement
numOfChars = length
#showing underscores for chosen word
space_of_word_list = ["_"]*length
space_of_word = ' '.join(space_of_word_list)
#initialize of lives variables
wrong_tries = 0
right_tries = 0
remaining_tries = length

#user enter a char
for x in range(1,100):
    print(f"the number of this word characters is {numOfChars}")
    print(space_of_word_list)
    
    users_char = input("Enter the char you guess:").lower()
    
    if users_char in chosen_word:
        print("That's Right")
        right_tries += 1
        
        for i in range (length): #for replace underscores with the char
          if chosen_word[i] == users_char and space_of_word_list[i] == "_":
                space_of_word_list[i] = users_char
        if right_tries == length:
                print(f"you won the word was: {chosen_word}")
                break
         
   
    else:
        print("wrong")
        wrong_tries += 1
        remaining_tries -= 1
        print(f"remaining tries is {remaining_tries}")
        if wrong_tries == length:
            print("you lost\n Game over")
            break
