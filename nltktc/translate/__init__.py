# -*- coding: utf-8 -*-
# Natural Language Toolkit: Machine Translation
#
# Copyright (C) 2001-2016 NLTK Project
# Author: Steven Bird <stevenbird1@gmail.com>, Tah Wei Hoon <hoon.tw@gmail.com>
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT

"""
Experimental features for machine translation.
These interfaces are prone to change.
"""

from nltktc.translate.api import AlignedSent, Alignment, PhraseTable
from nltktc.translate.ibm_model import IBMModel
from nltktc.translate.ibm1 import IBMModel1
from nltktc.translate.ibm2 import IBMModel2
from nltktc.translate.ibm3 import IBMModel3
from nltktc.translate.ibm4 import IBMModel4
from nltktc.translate.ibm5 import IBMModel5
from nltktc.translate.bleu_score import sentence_bleu as bleu
from nltktc.translate.ribes_score import sentence_ribes as ribes
from nltktc.translate.metrics import alignment_error_rate
from nltktc.translate.stack_decoder import StackDecoder
