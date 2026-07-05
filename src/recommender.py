import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

# --- OOP IMPLEMENTATION (Required for test_recommender.py) ---
class Recommender:
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # Sort songs by our scoring logic in descending order
        scored_songs = sorted(
            self.songs, 
            key=lambda song: self._compute_score(user, song), 
            reverse=True
        )
        return scored_songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        score, reasons = self._compute_score_with_reasons(user, song)
        return f"Score: {score:.2f} | Reasons: {', '.join(reasons)}"

    def _compute_score(self, user: UserProfile, song: Song) -> float:
        score, _ = self._compute_score_with_reasons(user, song)
        return score

    def _compute_score_with_reasons(self, user: UserProfile, song: Song) -> Tuple[float, List[str]]:
        score = 0.0
        reasons = []
        if song.genre.lower() == user.favorite_genre.lower():
            score += 2.0
            reasons.append("Genre match (+2.0)")
        if song.mood.lower() == user.favorite_mood.lower():
            score += 1.0
            reasons.append("Mood match (+1.0)")
        energy_score = 1.0 - abs(user.target_energy - song.energy)
        score += energy_score
        reasons.append(f"Energy proximity (+{energy_score:.2f})")
        return score, reasons


# --- FUNCTIONAL IMPLEMENTATION (Required for src/main.py) ---
def load_songs(csv_path: str) -> List[Dict]:
    songs = []
    print(f"Loading songs from {csv_path}...")
    with open(csv_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert numeric strings to floats
            row['energy'] = float(row.get('energy', 0.0))
            row['tempo_bpm'] = float(row.get('tempo_bpm', 0.0))
            row['valence'] = float(row.get('valence', 0.0))
            row['danceability'] = float(row.get('danceability', 0.0))
            row['acousticness'] = float(row.get('acousticness', 0.0))
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    score = 0.0
    reasons = []

    # 1. Genre Match (+2.0)
    if song.get('genre', '').lower() == user_prefs.get('genre', '').lower():
        score += 2.0
        reasons.append("Genre match (+2.0)")

    # 2. Mood Match (+1.0)
    if song.get('mood', '').lower() == user_prefs.get('mood', '').lower():
        score += 1.0
        reasons.append("Mood match (+1.0)")

    # 3. Energy Proximity (+1.0 max)
    target_energy = user_prefs.get('energy', 0.5)
    energy_score = 1.0 - abs(target_energy - song.get('energy', 0.5))
    score += energy_score
    reasons.append(f"Energy proximity (+{energy_score:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    scored_songs = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        scored_songs.append((song, score, explanation))
        
    # Sort by the score (index 1 in the tuple) descending
    scored_songs.sort(key=lambda x: x[1], reverse=True)
    return scored_songs[:k]