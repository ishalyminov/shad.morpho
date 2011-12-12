#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pickle

reversed_word_forms = []
word_form_tags = {}
word_forms = []

def main():
  try:
    with open(sys.argv[1], "r") as learn_file:
      for line in learn_file:
        line = unicode(line, 'latin-1')
        entry_list = line.strip().split();
        if (3 != len(entry_list)):
          raise RuntimeError("Incorrect data format")
        word_form = entry_list[0]
        word_forms.append(word_form)
        reversed_word_forms.append(word_form[::-1])
        if (word_form in word_form_tags):
          raise RuntimeError("Already in the set")

        lemma = entry_list[1]
        pos = entry_list[2]
        word_form_tags[word_form] = (lemma, pos)
  except IOError as error:
    print "IOError: " + str(error)
  except Exception as excp:
    print "Exception: " + str(excp)

  try:
    with open('word_form_tags.pickle', 'wb') as tags_file:
      pickle.dump(word_form_tags, tags_file)

    word_forms.sort()
    with open('word_forms.pickle', 'wb') as forms_file:
      pickle.dump(word_forms, forms_file)

    reversed_word_forms.sort()
    with open('reversed_forms.pickle', 'wb') as reversed_forms_file:
      pickle.dump(reversed_word_forms, reversed_forms_file)
  except IOError as error:
    print "IOError: " + str(error)
  except Exception as excp:
    print "Exception: " + str(excp)

if (__name__ == "__main__"):
  if (len(sys.argv) != 2):
    print("%s <learn_data_file>") % (sys.argv[0])
    quit()

  main()
