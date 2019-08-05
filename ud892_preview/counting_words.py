'''
Created on 08/05/2018

@author: jruiz
'''
"""Count words."""

def count_words(text):
    """Count how many times each unique word occurs in text."""
    word_list = dict()

    new_word = ''
    for c in text:
        if c in ' ,.;:!?*/-+_"()[]`' or c == '\r' or c== '\n':
            if new_word:
                if new_word in word_list.keys():
                    word_list[new_word] += 1
                else:
                    word_list[new_word] = 1
                new_word = ''
        else:
            new_word += c.lower()
    
    if new_word:
        if new_word in word_list.keys():
            word_list[new_word] += 1
        else:
            word_list[new_word] = 1
    #print(word_list)
    return word_list


def test_run():
    with open("zen_of_python.txt", "r") as f:
        text = f.read()
        counts = count_words(text)
        #print(counts.items())
        def get_values_from_items(each_tuple):
            return each_tuple[1]


        sorted_counts = sorted(counts.items(), key=get_values_from_items)
        
        print("10 most common words:\nWord\tCount")
        most_common = sorted_counts[-10:]
        most_common.reverse()
        for word, count in most_common:
            print("{}\t{}".format(word, count))
        
        print("\n10 least common words:\nWord\tCount")
        for word, count in sorted_counts[:10]:
            print("{}\t{}".format(word, count))


if __name__ == "__main__":
    test_run()
    # with open("C:\Users\jruiz\Conti\RBS_MSM_D_20.20.135R1_V1\Macro1.asc") as f:
    #     for line in f:
    #         print(line)
        
