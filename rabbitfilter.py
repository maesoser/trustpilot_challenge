import sys 

def contains(word,letters):
    #if word.find("'")!=-1:
    #    return False
    if set(letters) & set(word):
           for w in letters:
		if word.count(w)>letters.count(w):
			return False
	   return True
    return False

phrase = 'poultryoutwitsants'
abcd = 'abcdefghijklmnopqrstuvwxyz'
nophrase = set(abcd).difference(set(phrase))

try:
	dictfile = sys.argv[1]
except:
	print "Not enough arguments"
	print "\t"+argv[0]+" [wordlist]"

print "Loading wordlist: "+dictfile
fo = open(dictfile,"r")
wordlist = fo.readlines()
fo.close()

print "Importing original wordlist"

list1 = []
for word in wordlist:
        if contains(word,phrase):
            list1.append(word)
for character in nophrase:
	list1 = [ x for x in list1 if character not in x ]

print "list: "+str(len(list1))
print str(len(list1)*len(list1)*len(list1))+" COMBINATIONS"
print str(len(list1)*len(list1)*len(list1)*len(phrase)/1000000000)+" Gbytes"
print " "
print "Writing filtered wordlist"
fi = open("filtered_"+dictfile,"w")
for item in list1:
	fi.write(item)
fi.close()
