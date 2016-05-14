# Natural Language Toolkit: Applications package
#
# Copyright (C) 2001-2016 NLTK Project
# Author: Edward Loper <edloper@gmail.com>
#         Steven Bird <stevenbird1@gmail.com>
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT

"""
Interactive NLTK Applications:

chartparser:  Chart Parser
chunkparser:  Regular-Expression Chunk Parser
collocations: Find collocations in text
concordance:  Part-of-speech concordancer
nemo:         Finding (and Replacing) Nemo regular expression tool
rdparser:     Recursive Descent Parser
srparser:     Shift-Reduce Parser
wordnet:      WordNet Browser
"""


# Import Tkinter-based modules if Tkinter is installed
import nltktc.compat
try:
    import tkinter
except ImportError:
    import warnings
    warnings.warn("nltk.app package not loaded "
                  "(please install Tkinter library).")
else:
    from nltktc.app.chartparser_app import app as chartparser
    from nltktc.app.chunkparser_app import app as chunkparser
    from nltktc.app.collocations_app import app as collocations
    from nltktc.app.concordance_app import app as concordance
    from nltktc.app.nemo_app import app as nemo
    from nltktc.app.rdparser_app import app as rdparser
    from nltktc.app.srparser_app import app as srparser
    from nltktc.app.wordnet_app import app as wordnet

    try:
        from matplotlib import pylab
    except ImportError:
        import warnings
        warnings.warn("nltk.app.wordfreq not loaded "
                      "(requires the matplotlib library).")
    else:
        from nltktc.app.wordfreq_app import app as wordfreq

# skip doctests from this package
def setup_module(module):
    from nose import SkipTest
    raise SkipTest("nltk.app examples are not doctests")
