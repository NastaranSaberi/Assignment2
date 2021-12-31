numbers = int(input(" the number of students : "))
scores = []

for i in range (numbers):
    scores.append(float(input("Please enter the scores : ")))
    Average = sum(scores) / numbers
    Highestscore = max(scores)
    lowestscore = min(scores)

print("Average :" , Average , "\n " , "Highest score :" , Highestscore , "\n " , "lowest score :" , lowestscore)


