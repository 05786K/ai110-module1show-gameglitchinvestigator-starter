# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
        The game looked alright in terms of its UI Design. However, it was not responssive to screen size. 

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
        
        1: Difficulty level is confusing. 'Easy' Level seems more harder than 'Hard' level. 
        2: There is not input validation for input numbers
        3: After a game has been played, the 'Submit Guess' button does NOT work when a new game is initiated
        4: Hints are totally misleading
        5: In a normal dificulty game, the initial game allows 7 attempts, but when you ask for a new game, it allows  8 attempts.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|   20  | "Go Higher" hint      Go Lower           Hints were backwards
|   60  | "Go Lower"            Go Higher          Hints were backwards
|   45  |  Go Higher            NO HINTS           No Hints were given
|   55  | Correct Guess         Correct            Correct/Game won
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
    I used Claude

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
    When a user clicked on 'New Game', the app ignored the difficulty level. Thats what claude suggested to fix. I verified it by running the app and observing its behaviour. 

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  Claude wanted to remove the debug panel because it was revealing the secret number. I denied the fix because that debug panel is there on purpose. 
 
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
    I run the application manually and tested each feature. In addition to that, I run pytest. 

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

    1. TestInputValidation — Verifies that parse_guess correctly handles empty, non-numeric, valid, decimal, and out-of-range inputs. A key test that run in pytest submitted 21 as a guess number in Easy mode (range 1–20) and it confirmed the guess was rejected, ensuring validation was respected given the selected difficulty limits.

    2. TestAccurateHints — I manually tested check_guess to verify that it returned the correct result for a win, a guess that was too high and a guess that was too low. It behaved correctly. 

- Did AI help you design or understand any tests? How?
    Yes. Claude helped me understand the purpose of one of my tests, TestCorrectAttempts. It explained that the test verifies the game's scoring system by ensuring the score is calculated correctly based on the number of guesses taken. The explanation clarified that the attempt counter is not just displayed to the player but is also used to determine the final score, with fewer attempts resulting in a higher score.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

    Reruns:
    Every time a user interacts with the app (clicks a button, enters text, or changes a setting), Streamlit reruns the entire script from top to bottom to update the interface.

    Session State:
    Session state acts as the app's memory. It stores values that persist across reruns, allowing things like scores, game progress, and user settings to be remembered.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
    - I want to continue writing tests after fixing bugs to verify that the fixes actually work.
- What is one thing you would do differently next time you work with AI on a coding task?
    - I will thoroughly inspect and berify the AI-generated code step by step instead of accepting large code changes at once.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
    - This project showed me that AI is a good coding assistant and can speed up development, but its code still needs careful testing and review.
