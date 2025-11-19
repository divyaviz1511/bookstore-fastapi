# Author popularity mapping
author_score_map = {
    "JK Rowling": 10,
    "Dan Brown": 8,
    "Stephenie Meyer": 7,
    "Daniel Steel" : 9
}

def return_author_score(author : str) :
    return author_score_map.get(author, 5)
