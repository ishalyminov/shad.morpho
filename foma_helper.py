#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import subprocess

command = 'echo "%s" | ./foma_binaries/linux/flookup -x spanish.bin'

def main():
  try:
    with open(sys.argv[1], "r") as test_file, open(sys.argv[2], "w") as res_file:
      common_word_forms = set()
      common_variants = set()

      for line in test_file:
        new_word_form = unicode(line, 'latin-1').strip().split()[0]
        process = subprocess.Popen(command % new_word_form, shell=True, stdout=subprocess.PIPE)
        flookup_output = process.communicate()[0]

        new_variants = set(unicode(flookup_output, 'latin-1').split())

        intersection = common_variants.intersection(new_variants)

        if (0 == len(intersection)):
          for word_form in common_word_forms:
            for variant in common_variants:
              print >> res_file, ("%s\t%s") % (word_form.encode('latin-1'), variant.encode('latin-1'))
              res_file.flush()
          common_variants = new_variants
          common_word_forms.clear()
          common_word_forms.add(new_word_form)
        else:
          common_variants = intersection
          common_word_forms.add(new_word_form)

      if (0 < len(common_word_forms)):
        for word_form in common_word_forms:
          for variant in common_variants:
            print >> res_file, ("%s\t%s") % (word_form.encode('latin-1'), variant.encode('latin-1'))
            res_file.flush()
  except IOError as error:
    print("%s") % (str(error))

if (__name__ == "__main__"):
  if (len(sys.argv) != 3):
    print("%s <test_data_file> <result_file>") % (sys.argv[0])
    quit()

  main()
