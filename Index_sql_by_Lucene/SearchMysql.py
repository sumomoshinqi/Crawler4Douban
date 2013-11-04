#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys, os, lucene

from java.io import File
from org.apache.lucene.queryparser.classic import MultiFieldQueryParser
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.index import DirectoryReader
from org.apache.lucene.queryparser.classic import QueryParser
from org.apache.lucene.store import SimpleFSDirectory
from org.apache.lucene.search import IndexSearcher
from org.apache.lucene.util import Version

from sqlConstants import *

#what need to do 
#step 1. change config below
#step 2. ok

#------step 1------
#---start config---
#the dir to store the index file
INDEX_DIR = "/home/rio/workspace/lucene_index"
#the field name you want to search
FIELD = 'summary'
#---end config---



def run(searcher, analyzer):
    while True:
        print
        print "Hit enter with no input to quit."
        command = raw_input("Query:")
        if command == '':
            return

        print
        print "Searching for:", command

        #query = MultiFieldQueryParser(Version.LUCENE_CURRENT,['subject_id','summary'],analyzer).parse(command); 
        #query = MultiFieldQueryParser.parse(command,['subject_id','summary'],analyzer); 

        parser = MultiFieldQueryParser(Version.LUCENE_CURRENT, ['subject_id','summary'],analyzer)
        query = MultiFieldQueryParser.parse(parser, command)
        #在title和content中找word
      	'''I think there's a bug with the method binding.  MultiFieldQueryParser has several static parse
		methods, plus the inherited regular method from QueryParser.  It looks like all of them are
		being resolved as if they were static.  As a workaround, you can call it like this:

		parser = lucene.MultiFieldQueryParser(lucene.Version.LUCENE_CURRENT, ["payload","subject"],
		analyzer)
		lucene.MultiFieldQueryParser.parse(parser, command)
		'''


        #query = QueryParser(Version.LUCENE_CURRENT, FIELD,analyzer).parse(command)
        scoreDocs = searcher.search(query, 50).scoreDocs
        print "%s total matching documents." % len(scoreDocs)

        for scoreDoc in scoreDocs:
            doc = searcher.doc(scoreDoc.doc)
            print 'subject_id', doc.get('subject_id')
            #print 'path:', doc.get("path"), 'name:', doc.get("name")


if __name__ == '__main__':
    lucene.initVM(vmargs=['-Djava.awt.headless=true'])
    print 'lucene', lucene.VERSION
    base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    directory = SimpleFSDirectory(File(os.path.join(base_dir, INDEX_DIR)))
    searcher = IndexSearcher(DirectoryReader.open(directory))
    analyzer = StandardAnalyzer(Version.LUCENE_CURRENT)
    run(searcher, analyzer)
    del searcher