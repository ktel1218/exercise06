from sys import argv
import operator

script, filename = argv

f = open(filename)
file_text = f.read()
f.close

list_of_words = file_text.split()
dict_of_words = {}

for i in list_of_words:
    i = i.lower().strip('.,;:?!"-\'`')
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
