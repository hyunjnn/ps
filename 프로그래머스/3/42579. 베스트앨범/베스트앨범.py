from collections import defaultdict

def solution(genres, plays):
    data = defaultdict(list)
    
    for genre, play, index in zip(genres, plays, range(len(plays))):
        data[genre].append((play, index))
        
    genre_totals = {
        genre: sum(play for play, _ in data[genre]) 
            for genre in data.keys()
    }
    
    sorted_genres = sorted(genre_totals.keys(), key=lambda x: (genre_totals[x]), reverse=True)
    
    answer = []
    
    for genre in sorted_genres:
        top_songs = sorted(data[genre], key=lambda x: (-x[0], x[1]))
        answer.extend(index for _, index in top_songs[:2])
    
    return answer