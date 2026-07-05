# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

- The system gives more importance to matching the genre than the song's energy. This means it may recommend a rock song with the wrong mood instead of a pop song that matches the user's preferred energy.

- The recommender doesn't look at the artist, so it could suggest several songs by the same artist, making the recommendations less diverse.

- Since there are only 10 songs in the dataset, users with uncommon music tastes may receive poor or unrelated recommendations because there aren't enough songs to choose from.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

- I tested two user profiles: one that likes high-energy pop music and another that prefers relaxing lofi music.

- The recommender worked well by giving upbeat songs to the pop user and slower, relaxing songs to the lofi user.

-  If a user chooses a genre that isn't in the dataset, such as country, the recommendations become almost random because the system has no matching songs and only compares energy levels.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

- I learned that a recommendation system doesn't actually understand music. It simply compares numbers and features to find the closest match.

- The biggest surprise was seeing how easily bias can be added. By giving genre more weight than energy, I unintentionally made the system focus more on genre labels than on the overall feel or mood of the music.
