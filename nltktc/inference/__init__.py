# Natural Language Toolkit: Inference
#
# Copyright (C) 2001-2016 NLTK Project
# Author: Dan Garrette <dhgarrette@gmail.com>
#         Ewan Klein <ewan@inf.ed.ac.uk>
#
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT

"""
Classes and interfaces for theorem proving and model building.
"""

from nltktc.inference.api import ParallelProverBuilder, ParallelProverBuilderCommand
from nltktc.inference.mace import Mace, MaceCommand
from nltktc.inference.prover9 import Prover9, Prover9Command
from nltktc.inference.resolution import ResolutionProver, ResolutionProverCommand
from nltktc.inference.tableau import TableauProver, TableauProverCommand
from nltktc.inference.discourse import (ReadingCommand, CfgReadingCommand,
                                        DrtGlueReadingCommand, DiscourseTester)
