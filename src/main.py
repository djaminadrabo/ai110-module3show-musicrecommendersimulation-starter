"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Profile 1: High Energy Pop
    profile_1 = {"genre": "pop", "mood": "happy", "energy": 0.9}
    # Profile 2: Chill Lofi
    profile_2 = {"genre": "lofi", "mood": "chill", "energy": 0.3}

    profiles = [("High Energy Pop", profile_1), ("Chill Lofi", profile_2)]

    for profile_name, prefs in profiles:
        print(f"--- Top Recommendations for {profile_name} ---")
        print(f"Preferences: {prefs}")
        
        recommendations = recommend_songs(prefs, songs, k=3) # Top 3 
        
        for rec in recommendations:
            song, score, explanation = rec
            print(f"🎵 {song['title']} by {song['artist']} - Score: {score:.2f}")
            print(f"   Why: {explanation}")
        print("\n")

if __name__ == "__main__":
    main()
