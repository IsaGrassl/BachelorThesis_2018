
# BachelorThesis_2018

For compiling CreateCSVfile.py following datasets are required (not public):

- econstor_2017-06-01.json : 
This dataset contains abstracts with their content and meta data whereby the row number (indices) refers to the abstract id.

- collections.json : 
This dataset contains ids of samples: collection of document and a candidate document for each type of relation (similar, intermediate, dissimilar).

- keywords.json :
This dataset contains the dictionary that links the ids of a document to the three related lists of keywords for each algorithm (TFIDF, Rake TextRank).


For compiling CreateTask.html you need to be in the environment of the web interface of CrowdFlower due to using its platform-specific Markup Language CML.
