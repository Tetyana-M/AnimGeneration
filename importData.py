import numpy as np
import re

scenePath = cmds.file(q=True, exn=True)
scenePath = re.sub('[^\/]+$', '', scenePath)
dataPath = f'{scenePath}predictions.csv'

predictions = []

with open(dataPath, newline='') as file:
    reader = csv.reader(file)
    predictions = list(reader)

names = predictions[0]

for t in range(1, len(predictions)):
    time = numFrames + t
    cmds.currentTime(time)
    for i in range(0, len(predictions[0])):
        print(i)
        print(names[i])
        x = float(predictions[t][i])
        cmds.setAttr(names[i], x)
        cmds.setKeyframe(names[i])
        