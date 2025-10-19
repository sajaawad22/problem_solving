
#/*
#Problem 2:
#Write a function pingPongTracker that accepts no arguments and returns an object with the
#following methods:
#- timeSpentPlaying() should return the total amount of time you have played pingpong.
#- playOneGame() should increase the total time you played pingpong by 15 minutes
 # and return a string "Game played"
#- myLevel() should return your experience level based on how much time you have spent playing
  #pingpong. These are the levels:
  #a) Less than 30 minutes - "I need to improve my game"
  #b) 30–100 minutes       - "You need to improve your game"
 # c) More than 100 minutes - "Wow, I have wasted a lot of time"

#Example:
#var myGame = pingPongTracker();
#myGame.playOneGame();         // should return "Game played";
#myGame.playOneGame();         // should return "Game played";
#myGame.timeSpentPlaying();    // should return 30;
#myGame.myLevel();             // should return "You need to improve your game"
#*/

def pingPongTracker():
    total_time=0

    def timeSpentPlaying():
        return total_time
    
    def playOneGame():
        nonlocal total_time
        total_time += 15
        return "Game played"
    
    def myLevel():
        if total_time < 30:
            return "I need to improve my game"
        elif 30 <= total_time <= 100:
            return "You need to improve your game"
        else:
            return "Wow, I have wasted a lot of time"
        
    return {
        "timeSpentPlaying": timeSpentPlaying,
        "playOneGame": playOneGame,
        "myLevel": myLevel
    }

myGame= pingPongTracker()
print(myGame["playOneGame"]())
print(myGame["myLevel"]())
print(myGame["timeSpentPlaying"]())

  