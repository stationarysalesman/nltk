# Natural Language Toolkit: Stemmers
#
# Copyright (C) 2001-2016 NLTK Project
# Author: Trevor Cohn <tacohn@cs.mu.oz.au>
#         Edward Loper <edloper@gmail.com>
#         Steven Bird <stevenbird1@gmail.com>
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT

"""
NLTK Stemmers

Interfaces used to remove morphological affixes from words, leaving
only the word stem.  Stemming algorithms aim to remove those affixes
required for eg. grammatical role, tense, derivational morphology
leaving only the stem of the word.  This is a difficult problem due to
irregular words (eg. common verbs in English), complicated
morphological rules, and part-of-speech and sense ambiguities
(eg. ``ceil-`` is not the stem of ``ceiling``).

StemmerI defines a standard interface for stemmers.
"""

from nltktc.stem.api import StemmerI
from nltktc.stem.regexp import RegexpStemmer
from nltktc.stem.lancaster import LancasterStemmer
from nltktc.stem.isri import ISRIStemmer
from nltktc.stem.porter import PorterStemmer
from nltktc.stem.snowball import SnowballStemmer
from nltktc.stem.wordnet import WordNetLemmatizer
from nltktc.stem.rslp import RSLPStemmer


