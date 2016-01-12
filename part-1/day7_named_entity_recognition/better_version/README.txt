INPUT: a file in text format ( the review)

DEPENDENCY FILES: 
new_pos_complete_tokenized_with_stopwords-removed_and_stemming_done.txt,
new_neg_complete_tokenized_with_stopwords-removed_and_stemming_done.txt

EXECUTABLE FILE: jumbo_code.py

OUTPUT:
The output file will be like:

score: 1;    scaled score: 5.0
score: 0;    scaled score: 0.0
...
...
...

TOTAL SCORE 11; scaled score:3.63636363636

Here, score and scaled score represent that of individual line corresponding to their line number.
TOTAL SCORE, scaled score represent the review rating of the overall review.

HOW TO RUN??
Instructions
1>
place your input file in the same diirectory of jumbo_code.py, new_pos_complete_tokenized_with_stopwords-removed_and_stemming_done.txt,
new_neg_complete_tokenized_with_stopwords-removed_and_stemming_done.txt
2>
Open the jumbo_code.py file, replace "input_whole_review_test2.txt" of line number 002 with your own file name.
Run jumbo_code.py
3>
The ouput file is:-
output_scaled_analyzed_reviews_without_dict.txt


P.S. This is better than any of the codes sent before. Here only the adverbs, adjectives are filtered out at first. We are analysing based on these adjectives and adverbs, Thus nouns, pronouns creating noise before are eliminated to a large extent.