Time = input("Please enter the time :")
split = Time.split(":")
seconds = int(split[0]) * 3600 + int(split[1]) * 60 + int(split[2])

print("Total seconds" , seconds)