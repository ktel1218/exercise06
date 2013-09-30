from sys import argv
import operator

script, source = argv


def open_and_write(filename):
    f = open(filename)
    file_text = f.read()
    f.close
    return file_text

def format(file_text):
    file_text = file_text.lower().replace("--", " ")
    list_of_words = file_text.split()
    for i in range(len(list_of_words)):
        list_of_words[i] = list_of_words[i].strip('.,;:?!-`"\'\t\n()_')
    return list_of_words

def main():

    dict_of_words = {}

    list_of_words = format(open_and_write(source))

    for i in list_of_words:
        dict_of_words[i] = dict_of_words.get(i, 0) + 1

    print "\nNot sorted: "
    for key, value in dict_of_words.iteritems():
        print "%s:\t\t%r" % (key, value)

    #for key, value in dict_of_words.iteritems():
    list_of_sorted_values = sorted(dict_of_words.iteritems(), key = operator.itemgetter(1), reverse = True)
    print "\nBy frequency: "
    for duo in list_of_sorted_values:
        print "%s:\t\t%d" % (duo[0], duo[1])

        #for key, value in dict_of_words.iteritems():
    list_of_sorted_keys = sorted(dict_of_words.iteritems())
    print "\nBy word: "
    for duo in list_of_sorted_keys:
        print "%s:\t\t%d" % (duo[0], duo[1])

main()
