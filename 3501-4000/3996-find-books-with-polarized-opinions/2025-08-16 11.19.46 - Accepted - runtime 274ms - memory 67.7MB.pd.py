import pandas as pd

def find_polarized_books(books: pd.DataFrame, reading_sessions: pd.DataFrame) -> pd.DataFrame:
    fixed_round = lambda x: round(x + 0.00001, 2)

    book_ratings = defaultdict(list)
    for book_id, rating in zip(reading_sessions['book_id'], reading_sessions['session_rating']):
        book_ratings[book_id].append(rating)
    
    polarized_books = []
    for book_id, ratings in book_ratings.items():
        if len(ratings) < 5: continue
            
        high_ratings = sum(1 for r in ratings if r >= 4)
        low_ratings = sum(1 for r in ratings if r <= 2)
        
        if high_ratings == 0 or low_ratings == 0: continue
            
        polarization_score = (high_ratings + low_ratings) / len(ratings)
        
        if polarization_score < 0.6: continue
            
        rating_spread = max(ratings) - min(ratings)
        
        # Get book information
        book_info = books.loc[book_id-1]
        
        # Add to results
        polarized_books.append({
            'book_id': book_id,
            'title': book_info['title'],
            'author': book_info['author'],
            'genre': book_info['genre'],
            'pages': book_info['pages'],
            'rating_spread': rating_spread,
            'polarization_score': fixed_round(polarization_score)
        })
    
    result_df = pd.DataFrame(polarized_books)
    
    # Sort by polarization score descending, then by title descending
    result_df = result_df.sort_values(['polarization_score', 'title'], ascending=[False, False])
    

    return result_df