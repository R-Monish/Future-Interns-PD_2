key Features:-

1.Random Number Generation:-The program uses the random.randint(1, 100) function to generate a random number between 1 and 100. This ensures that the number the user has to guess is different every time the game is played, adding an element of unpredictability.

2.User Interaction and Feedback:- The program is interactive, continuously asking the user to guess the number and providing feedback on whether their guess was too low, too high, or correct. This feedback helps guide the user toward the correct answer.

3.Input Validation:-The program includes checks to ensure the user’s guess is within the valid range (1 to 100). If the user enters a number outside this range, the program prompts them to enter a valid number, improving the user experience and preventing invalid inputs from affecting the game.

4. Error Handling:- The program uses a try-except block to handle cases where the user might enter non-numeric input. If the input is not a valid integer, the program catches the ValueError and prompts the user to enter a valid number, preventing the program from crashing.

5.Loop for Continuous Play:- The program uses a while True loop to keep the game running until the correct number is guessed. This loop ensures that the game continues to prompt the user and provide hints until they successfully guess the number, making the game engaging and persistent until the goal is achieved

