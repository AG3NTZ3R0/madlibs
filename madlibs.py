from random import choice, shuffle


def gather_words(pos, qty=3):
    """
    Store a part of speech within a list to be shuffled and utilized to populate a madlib.\n
    qty: The number of parts of speech a user will be prompted to enter.\n
    :return: A shuffled list of parts of speech entered by the user.
    """
    parts_of_speech = [input(f"Enter a(n) {pos}: ") for word in range(qty)]
    shuffle(parts_of_speech)
    return parts_of_speech


# Populate lists
adjective = gather_words('adjective')
noun = gather_words('noun', qty=5)
noun_plural = gather_words('plural noun')
verb_ending_in_ing = gather_words('veb ending in -ing')

madlib1 = f"A vacation is when you take a trip to some {adjective[0]} place with your {adjective[1]} family.\nUsually \
you go to some place that is near a/an {noun[0]} or up on a/an {noun[1]}.\nA good vacation place is one where you can \
ride {noun_plural[0]} or play corn hole or go hunting for {noun_plural[1]}.\nI like to spend my time \
{verb_ending_in_ing[0]} or relaxing.\nWhen parents go on a vacation, they spend their time eating \
three {noun_plural[2]} a day, and fathers play golf, and mothers sit around {verb_ending_in_ing[1]}.\nLast summer, \
my little brother fell in a/an {noun[2]} and got poison ivy all over his leg.\nMy family is going to go to the \
beach, and I will practice {verb_ending_in_ing[2]}.\nParents need vacations more than kids because parents are always \
very {adjective[2]} and because they have to work 3 hours every day all year making enough money for the vacation."

madlib2 = f"\"Look!\", said my mother.\nI turned my head and saw a(n) {adjective[0]} {noun[0]} jumping \
up and down in a tree.\nHe ran straight through the large tunnel that led to its {adjective[1]} {noun[1]}.\nI got some \
peanuts and passed them through the cage to a gigantic gray {noun[2]} who ate them pleasantly and smiled.\nWhat a day \
it was today."

if __name__ == '__main__':
    # Print a random madlib
    print(choice([madlib1, madlib2]))
