#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pickle
from bisect import bisect


def LargestCommonPrefix(left_word, right_word):
  largest_prefix = ''

  i = 1
  while (i <= len(right_word)):
    prefix = right_word[:i]
    if (False is left_word.startswith(prefix)):
      break
    largest_prefix = prefix
    i += 1
  return largest_prefix


def LargestCommonSuffix(left_word, right_word):
  largest_suffix = ''
  i = len(right_word) - 1
  while (i >= 0):
    suffix = right_word[i:]
    if (False is left_word.endswith(suffix)):
      break
    largest_suffix = suffix
    i -= 1
  return largest_suffix


def CountCommonTailLetters(left_word, right_word):
  return len(LargestCommonSuffix(left_word, right_word))


def DeriveLemmaFirst(target_word_form, closest_word_form, closest_lemma):
  suffix = LargestCommonSuffix(target_word_form, closest_word_form);

  target_begin = target_word_form.rfind(suffix)
  closest_begin = closest_word_form.rfind(suffix)

  end = closest_lemma[closest_begin:]
  begin = target_word_form[:target_begin]
  return begin + end


def DeriveLemmaSecond(target_word_form, closest_word_form, closest_lemma):
  closest_prefix = LargestCommonPrefix(closest_lemma, closest_word_form);
  common_suffix = LargestCommonSuffix(target_word_form, closest_word_form);

  target_suffix_begin = target_word_form.rfind(common_suffix)
  begin = target_word_form[:target_suffix_begin]
  if (len(closest_prefix) == 0):
    raise RuntimeError("Zero lenght closes prefix")
  end = closest_lemma[len(closest_prefix)-1:]
  return begin + end


def ClosestKnownWordForm(word_form, reversed_word_forms):
  reversed_word_form = word_form[::-1]

  index = bisect(reversed_word_forms, reversed_word_form)

  form_scores = []

  if (index - 1 >= 0):
    form = reversed_word_forms[index-1][::-1]
    form_scores.append((form, CountCommonTailLetters(word_form, form)))

  if (index >= 0 and index < len(reversed_word_forms)):
    form = reversed_word_forms[index][::-1]
    form_scores.append((form, CountCommonTailLetters(word_form, form)))

  if (index + 1 < len(reversed_word_forms)):
    form = reversed_word_forms[index+1][::-1]
    form_scores.append((form, CountCommonTailLetters(word_form, form)))

  max_score = 0
  closest_form = ''

  for form_score in form_scores:
    score = form_score[1]
    if (score > max_score):
      max_score = score 
      closest_form = form_score[0]

  return closest_form


def main():
  try:
    with open('word_form_tags.pickle', 'rb') as tags_file:
      word_form_tags = pickle.load(tags_file)

    with open('reversed_forms.pickle', 'rb') as reversed_forms_file:
      reversed_word_forms = pickle.load(reversed_forms_file)
  except IOError as error:
    print "IOError: " + str(error)
  except Exception as excp:
    print "Exception: " + str(excp)

  try:
    with open(sys.argv[1], 'r') as test_file, open(sys.argv[2], 'w') as res_file:
      for line in test_file:
        word_form = unicode(line, 'latin-1').strip()

        closest_form = ClosestKnownWordForm(word_form, reversed_word_forms)
        if (0 < len(closest_form)):
          pos = word_form_tags[closest_form][1]
          lemma = DeriveLemmaFirst(word_form, closest_form, word_form_tags[closest_form][0])
        else:
          pos = "N"
          lemma = word_form

        print >> res_file, ("%s\t%s+%s") % (word_form.encode('latin-1'), lemma.encode('latin-1'), pos.encode('latin-1'))
        res_file.flush()
  except IOError as error:
    print "IOError: " + str(error)
  except Exception as excp:
    print "Exception: " + str(excp)

if (__name__ == "__main__"):
  if (len(sys.argv) != 3):
    print("%s <test_data_file> <result_file>") % (sys.argv[0])
    quit()

  main()
