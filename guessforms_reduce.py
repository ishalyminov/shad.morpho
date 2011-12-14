from sys import stdin, stdout

def main():
    guess_forms = {}
    for line in stdin:
        tokens = line.strip().split('\t')
        if tokens[0] not in guess_forms:
            guess_forms[tokens[0]] = [tokens[1]]
        else:
            guess_forms[tokens[0]].append(tokens[1])
    
    for wordform in sorted(guess_forms.keys()):
		s = wordform + '\t' + ' '.join(guess_forms[wordform])
		s = unicode(s, 'utf8').encode('latin-1')
		print s
		#stdout.write(wordform + '\t')
		#print ' '.join(guess_forms[wordform])

if __name__ == '__main__':
    main()
