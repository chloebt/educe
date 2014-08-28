# -*- coding: utf-8 -*-
#
# Author: Eric Kow
# License: BSD3

import optparse
import pdtb
import pdtb.util.cmd.extract as feat

if __name__ == '__main__':
    usage = "Test de educe\n"
    parser = optparse.OptionParser(usage=usage
            )
    (options, args) = parser.parse_args()
    #reader = pdtb.corpus.Reader('/Users/chloe/data/corpora/englCorpora/PDTB/PdtbRoot_dev/')
    #files     =  reader.files()
    #corpus    = reader.slurp()
    #for k in corpus:
    #    print k, corpus[k].__str__
    '''
    pdtb_docs = []
    for (id, f) in files.items():
        doc = pdtb.parse.parse(f)
        print doc.__repr__(), '\n'
        pdtb_docs.append(doc)
    print feat.read_corpus_inputs('/Users/chloe/data/corpora/englCorpora/PDTB/PdtbRoot_dev/')
    '''
    feat.main(args)
