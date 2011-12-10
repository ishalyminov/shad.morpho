#!/usr/bin/env python
# -*- coding: latin-1 -*-

import sys
import pickle

word_form_tags = {}
word_forms = []

if (len(sys.argv) != 2):
  print("%s <train_data_file>") % (sys.argv[0])
  quit()

try:
  with open(sys.argv[1], "r") as train_file:
    for line in train_file:
      line = unicode(line, 'latin-1')
      entry_list = line.strip().split();
      if (3 != len(entry_list)):
        raise RuntimeError("Incorrect data format")
      word_form = entry_list[0]
      word_forms.append(word_form)
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
except IOError as error:
  print "IOError: " + str(error)
except Exception as excp:
  print "Exception: " + str(excp)
