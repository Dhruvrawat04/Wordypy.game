import wordy
import PIL 
import pytesseract

def solution(board: PIL.Image) -> str:
    """The student solution to the problem.
    You must write code to query the wordy module and make a guess for the word. You needs to inspect the module to
    understand how to do this, and this function should only return the guess that you are going to make based on the game board state.

    Returns:
        str: The guess that you are going to make.
    """
    
    oc=pytesseract.image_to_string(board)
    
    correct_place=[None]*5
    mismatch=set()
    incorrect=set()
    for line in oc.splitlines():
        if "Correct:" in line:
            for pos,letter in enumerate(line.replace("Correct:","").strip()):
            
                correct_place[pos]=letter
        elif "Misplaced:" in line:
            mismatch.update(line.replace("Misplaced:","").strip())
        elif "Incorrect:"in line:
            incorrect.update(line.replace("Incorrect:","").strip())
    
    potentialguess=[]
    wordlist=wordy.get_word_list()
         
    for word in wordlist:
        value=True
        for i,letter in enumerate(word):
            if letter in incorrect:
                value=False
                break
            if correct_place[i] and word[i]!=correct_place[i]:
                value=False
                break
            if letter in mismatch and word[i]== letter:
                value=False
                break
                
            if value:
                potentialguess.append(word)
        if potentialguess:
            new_guess=potentialguess[0]
        else:
            new_guess=random.choice(wordlist)
    return new_guess



# The autograder for this assignment is easy, it will try and play
# a few rounds of the game and ensure that errors are not thrown. If
# you can make it through five rounds we'll assume you have the right
# solution!
#
# You SHOULD NOT change anything in the wordy module, instead you
# must figure out how to write the solution() function in this notebook
# to make a good guess based on the board state!

for i in range(5):
    try:
        # Get an image of the current board state from wordy.
        # Note that the image contains some number of random guesses (always less than 5 guesses).
        image = wordy.get_board_state()
        # Create a new *good* guess based on the image and rules of wordy
        new_guess = solution(image)  # your code goes in solution()!
        # Send that guess to wordy to make sure it doesn't throw any errors
        wordy.make_guess(new_guess)
    except Exception as e:
        raise e
