from sys import stdin, stdout, argv
import re

def get_lemma(in_tokens):
    if len(in_tokens) >= 2 and len(in_tokens[1]) > 3:
        return in_tokens[1][3:]
    return '?'

def get_pos_tag(in_tokens):
    if len(in_tokens) >= 3 and len(in_tokens[2]) > 3:
        return in_tokens[2][3:]
    return '?'

def main(in_examples_file, in_results_file):
    for ex_line in in_examples_file:
        res_line = in_results_file.readline()
        res_forms = []
        while len(res_line) > 1:
            tokens = re.split('\s+', unicode(res_line, 'latin-1').strip())
            converted_form = get_lemma(tokens) + '+' + get_pos_tag(tokens)
            res_forms.append(converted_form.encode('latin-1'))
            res_line = in_results_file.readline()
        print ex_line.strip() + '\t' + ' '.join(res_forms)

if __name__ == '__main__':
    if len(argv) < 3:
        print 'Usage: convert.py <examples file> <result file>'
        exit(0)
    main(open(argv[1]), open(argv[2]))
