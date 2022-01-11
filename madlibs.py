adjective_count = 1
adjective = [input("Enter an adjective: ") for adj in range(adjective_count)]

exclamation_count = 1
exclamation = [input("Enter an exclamation: ") for exc in range(exclamation_count)]

noun_count = 5
noun = [input("Enter a noun: ") for n in range(noun_count)]

noun_plural_count = 1
noun_plural = [input("Enter a plural noun: ") for ns in range(noun_plural_count)]

verb_ending_in_ing_count = 2
verb_ending_in_ing = [input("Enter a verb ending in -ing: ") for v_ing in range(verb_ending_in_ing_count)]

verb_past_tense_count = 1
verb_past_tense = [input("Enter a past tense verb: ") for v_past in range(verb_past_tense_count)]

madlib = f"\"Put your hands up\" said the {noun[0]}.\n\"You're under arrest for {verb_ending_in_ing[0]} the {noun[1]} \
at the {noun[2]}\".\n\"{exclamation[0]}!\" thought Frank.\nHis hands were {verb_ending_in_ing[1]} like \
{noun_plural[0]} on a {noun[3]}.\nThis wasn't the first time he had {verb_past_tense[0]} a {noun[4]} and he knew \
he was in {adjective[0]} trouble.\n "

print(madlib)
