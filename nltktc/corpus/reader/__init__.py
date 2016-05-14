# Natural Language Toolkit: Corpus Readers
#
# Copyright (C) 2001-2016 NLTK Project
# Author: Steven Bird <stevenbird1@gmail.com>
#         Edward Loper <edloper@gmail.com>
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT

"""
NLTK corpus readers.  The modules in this package provide functions
that can be used to read corpus fileids in a variety of formats.  These
functions can be used to read both the corpus fileids that are
distributed in the NLTK corpus package, and corpus fileids that are part
of external corpora.

Corpus Reader Functions
=======================
Each corpus module defines one or more "corpus reader functions",
which can be used to read documents from that corpus.  These functions
take an argument, ``item``, which is used to indicate which document
should be read from the corpus:

- If ``item`` is one of the unique identifiers listed in the corpus
  module's ``items`` variable, then the corresponding document will
  be loaded from the NLTK corpus package.
- If ``item`` is a fileid, then that file will be read.

Additionally, corpus reader functions can be given lists of item
names; in which case, they will return a concatenation of the
corresponding documents.

Corpus reader functions are named based on the type of information
they return.  Some common examples, and their return types, are:

- words(): list of str
- sents(): list of (list of str)
- paras(): list of (list of (list of str))
- tagged_words(): list of (str,str) tuple
- tagged_sents(): list of (list of (str,str))
- tagged_paras(): list of (list of (list of (str,str)))
- chunked_sents(): list of (Tree w/ (str,str) leaves)
- parsed_sents(): list of (Tree with str leaves)
- parsed_paras(): list of (list of (Tree with str leaves))
- xml(): A single xml ElementTree
- raw(): unprocessed corpus contents

For example, to read a list of the words in the Brown Corpus, use
``nltk.corpus.brown.words()``:

    >>> from nltktc.corpus import brown
    >>> print(", ".join(brown.words()))
    The, Fulton, County, Grand, Jury, said, ...

"""

from nltktc.corpus.reader.plaintext import *
from nltktc.corpus.reader.util import *
from nltktc.corpus.reader.api import *
from nltktc.corpus.reader.tagged import *
from nltktc.corpus.reader.cmudict import *
from nltktc.corpus.reader.conll import *
from nltktc.corpus.reader.chunked import *
from nltktc.corpus.reader.wordlist import *
from nltktc.corpus.reader.xmldocs import *
from nltktc.corpus.reader.ppattach import *
from nltktc.corpus.reader.senseval import *
from nltktc.corpus.reader.ieer import *
from nltktc.corpus.reader.sinica_treebank import *
from nltktc.corpus.reader.bracket_parse import *
from nltktc.corpus.reader.indian import *
from nltktc.corpus.reader.toolbox import *
from nltktc.corpus.reader.timit import *
from nltktc.corpus.reader.ycoe import *
from nltktc.corpus.reader.rte import *
from nltktc.corpus.reader.string_category import *
from nltktc.corpus.reader.propbank import *
from nltktc.corpus.reader.verbnet import *
from nltktc.corpus.reader.bnc import *
from nltktc.corpus.reader.nps_chat import *
from nltktc.corpus.reader.wordnet import *
from nltktc.corpus.reader.switchboard import *
from nltktc.corpus.reader.dependency import *
from nltktc.corpus.reader.nombank import *
from nltktc.corpus.reader.ipipan import *
from nltktc.corpus.reader.pl196x import *
from nltktc.corpus.reader.knbc import *
from nltktc.corpus.reader.chasen import *
from nltktc.corpus.reader.childes import *
from nltktc.corpus.reader.aligned import *
from nltktc.corpus.reader.lin import *
from nltktc.corpus.reader.semcor import *
from nltktc.corpus.reader.framenet import *
from nltktc.corpus.reader.udhr import *
from nltktc.corpus.reader.bnc import *
from nltktc.corpus.reader.sentiwordnet import *
from nltktc.corpus.reader.twitter import *
from nltktc.corpus.reader.nkjp import *
from nltktc.corpus.reader.crubadan import *
from nltktc.corpus.reader.mte import *
from nltktc.corpus.reader.reviews import *
from nltktc.corpus.reader.opinion_lexicon import *
from nltktc.corpus.reader.pros_cons import *
from nltktc.corpus.reader.categorized_sents import *
from nltktc.corpus.reader.comparative_sents import *
from nltktc.corpus.reader.panlex_lite import *

# Make sure that nltk.corpus.reader.bracket_parse gives the module, not
# the function bracket_parse() defined in nltk.tree:
from nltktc.corpus.reader import bracket_parse

__all__ = [
    'CorpusReader', 'CategorizedCorpusReader',
    'PlaintextCorpusReader', 'find_corpus_fileids',
    'TaggedCorpusReader', 'CMUDictCorpusReader',
    'ConllChunkCorpusReader', 'WordListCorpusReader',
    'PPAttachmentCorpusReader', 'SensevalCorpusReader',
    'IEERCorpusReader', 'ChunkedCorpusReader',
    'SinicaTreebankCorpusReader', 'BracketParseCorpusReader',
    'IndianCorpusReader', 'ToolboxCorpusReader',
    'TimitCorpusReader', 'YCOECorpusReader',
    'MacMorphoCorpusReader', 'SyntaxCorpusReader',
    'AlpinoCorpusReader', 'RTECorpusReader',
    'StringCategoryCorpusReader','EuroparlCorpusReader',
    'CategorizedBracketParseCorpusReader',
    'CategorizedTaggedCorpusReader',
    'CategorizedPlaintextCorpusReader',
    'PortugueseCategorizedPlaintextCorpusReader',
    'tagged_treebank_para_block_reader',
    'PropbankCorpusReader', 'VerbnetCorpusReader',
    'BNCCorpusReader', 'ConllCorpusReader',
    'XMLCorpusReader', 'NPSChatCorpusReader',
    'SwadeshCorpusReader', 'WordNetCorpusReader',
    'WordNetICCorpusReader', 'SwitchboardCorpusReader',
    'DependencyCorpusReader', 'NombankCorpusReader',
    'IPIPANCorpusReader', 'Pl196xCorpusReader',
    'TEICorpusView', 'KNBCorpusReader', 'ChasenCorpusReader',
    'CHILDESCorpusReader', 'AlignedCorpusReader',
    'TimitTaggedCorpusReader', 'LinThesaurusCorpusReader',
    'SemcorCorpusReader', 'FramenetCorpusReader', 'UdhrCorpusReader',
    'BNCCorpusReader', 'SentiWordNetCorpusReader', 'SentiSynset',
    'TwitterCorpusReader', 'NKJPCorpusReader', 'CrubadanCorpusReader',
    'MTECorpusReader', 'ReviewsCorpusReader', 'OpinionLexiconCorpusReader',
    'ProsConsCorpusReader', 'CategorizedSentencesCorpusReader',
    'ComparativeSentencesCorpusReader', 'PanLexLiteCorpusReader'
]
