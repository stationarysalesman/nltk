# Natural Language Toolkit: Metrics
#
# Copyright (C) 2001-2016 NLTK Project
# Author: Steven Bird <stevenbird1@gmail.com>
#         Edward Loper <edloper@gmail.com>
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT
#

"""
NLTK Metrics

Classes and methods for scoring processing modules.
"""

from nltktc.metrics.scores import          (accuracy, precision, recall, f_measure,
                                            log_likelihood, approxrand)
from nltktc.metrics.confusionmatrix import ConfusionMatrix
from nltktc.metrics.distance        import (edit_distance, binary_distance,
                                            jaccard_distance, masi_distance,
                                            interval_distance, custom_distance,
                                            presence, fractional_presence)
from nltktc.metrics.paice           import Paice
from nltktc.metrics.segmentation    import windowdiff, ghd, pk
from nltktc.metrics.agreement       import AnnotationTask
from nltktc.metrics.association     import (NgramAssocMeasures, BigramAssocMeasures,
                                            TrigramAssocMeasures, ContingencyMeasures)
from nltktc.metrics.spearman        import (spearman_correlation, ranks_from_sequence,
                                            ranks_from_scores)
