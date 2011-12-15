from sys import stdin, stdout
import re

def get_lemma(in_tokens):
    if len(in_tokens) < 2:
        return ''
    return in_tokens[1][3:]

def get_pos_tag(in_tokens):
    if len(in_tokens) < 3:
        return '?'
    return in_tokens[2][3:]

def main():
    guess_forms = {}
    for line in stdin:
        tokens = re.split('\s+', unicode(line, 'latin-1').strip())
        if tokens == ['']:
            continue
        converted_form = get_lemma(tokens) + '+' + get_pos_tag(tokens)
        if tokens[0] not in guess_forms:
            guess_forms[tokens[0]] = [converted_form]
        else:
            guess_forms[tokens[0]].append(converted_form)
    
    for wordform in sorted(guess_forms.keys()):
		s = wordform + '\t' + ' '.join(guess_forms[wordform])
		s = s.encode('latin-1')
		print s
		#stdout.write(wordform + '\t')
		#print ' '.join(guess_forms[wordform])

if __name__ == '__main__':
    main()
