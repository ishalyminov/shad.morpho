#!/usr/bin/env python

import sys
import pickle

try:
  with open('word_form_tags.pickle', 'rb') as tags_file:
    word_form_tags = pickle.load(tags_file)

  with open('word_forms.pickle', 'rb') as forms_file:
    word_forms = pickle.load(forms_file)
except IOError as error:
  print "IOError: " + str(error)
except Exception as excp:
  print "Exception: " + str(excp)


for form in word_forms:
  print form
