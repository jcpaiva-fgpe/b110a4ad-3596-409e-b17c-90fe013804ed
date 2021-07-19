def reset():
    global points
    points = 0

def increment():
    global points
    points +=1

reset(); increment(); increment(); print(points)
reset(); print(points)
