import sys


def make_chains(corpus):
    """Takes input text as string; returns dictionary of markov chains."""
    # now corpus = input_text which is a whole file that we need to break down
    # line by line

    content = corpus.read().split()
    content = [w.rstrip("\n?.,") for w in content]
    # content = []
    # for line in corpus:
    #     seperate_line_content = line.rstrip().split(" ") # put this on one line chained
    # #words = words.strip("\n") this doesnt work because words is a list and you cant 
    # # 'strip' a list... we may need a for loop! 
    #     seperate_line_content = [w.rstrip("\n.,").lower() for w in seperate_line_content]
    # # we started with the for loop below and then condensed it into list_comprehension above.
    # # for w in words:
    # #     stripped_words.append(w.rstrip())
    #     content.extend(seperate_line_content)
    # # create tuples list of bigrams from list of words
   
    tuples_list = []
    for word in content:
        if word != content[-1]: # so that the word is not the last word
            next_word_idx = content.index(word) + 1
            tuples_list.append((word, content[next_word_idx]))

    print tuples_list

    # can I index the tuple in the original list?
    # for atuple in tuples_list:
    #     print content[content.index(atuple[1])+1] # YES!

    # now create dictionary!!
    
    bigrams_dictionary = {}
    for atuple in tuples_list:
        if atuple[1] != content[-1]:
            next_word_idx = content.index(atuple[1])+1
            bigrams_dictionary.setdefault(key, []).append(value)

    print "This is the dictionary:"
    print bigrams_dictionary


    #key- this will need to be a tuple for the first word in the bigram followed by the second word
    # pseudo code for how to get key 'key = (word in content, word+1 in content)'

    # bigrams_dictionary(key) = ""

    # return {}
    



def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    return "Here's some random text."


# Change this to read input_text from a file, deciding which file should
# be used by examining the `sys.argv` arguments (if neccessary, see the
# Python docs for sys.argv)

input_text = open('./green-eggs.txt')



# Get a Markov chain
make_chains(input_text)
# print input_text
# chain_dict = make_chains(input_text)
# print "This is the dictionary:", chain_dict
# # Produce random text
# random_text = make_text(chain_dict)

# print random_text


    