import maya.cmds as cmds
import numpy as np
import csv
import datetime
import re



np.set_printoptions(precision=6)
np.set_printoptions(suppress=True)

numFrames = 13000
step = 1

# Make sure the joints you want to export are selected.
joints = cmds.ls( selection=True )


names = [[f'{x}.rotateX' , f'{x}.rotateY', f'{x}.rotateZ'] for x in joints]
names = [x for x in joints  for x in [f'{x}.rotateX' , f'{x}.rotateY', f'{x}.rotateZ'] ]
names = ['time', 'Hips.translateX', 'Hips.translateY', 'Hips.translateZ'] + names

# Remove rotations that are not needed.
names.remove('RightLeg.rotateY')
names.remove('RightLeg.rotateZ')
names.remove('LeftLeg.rotateY')
names.remove('LeftLeg.rotateZ')
names.remove('RightToeBase.rotateY')
names.remove('RightToeBase.rotateZ')
names.remove('LeftToeBase.rotateY')
names.remove('LeftToeBase.rotateZ')
#names.remove('RightForeArm.rotateY')
#names.remove('RightForeArm.rotateZ')
#names.remove('LeftForeArm.rotateY')
#names.remove('LeftForeArm.rotateZ')

numFeatures = len(names)

data = []
data.append(names)
dt = datetime.datetime(2003,8,1,12)

for t in range(step, numFrames, step):
    values = []
    dt += datetime.timedelta(days=1)
    values.append(str(dt))
    for i in range(1, len(names)):
       value = str(round(cmds.getAttr(names[i],time=t), 6))
       values.append(value)
    data.append(values)

scenePath = cmds.file(q=True, exn=True)
scenePath = re.sub('[^\/]+$', '', scenePath)
dataPath = f'{scenePath}data.csv'

# Write data to CSV file
with open(dataPath, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

print(f'CSV file exported successfully to {file_path}')

#-----------------------------------------------------------------------------#
