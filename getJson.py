import sys
from os import path
from os import SEEK_END
path = path.dirname(path.abspath(__file__))
try:
    import tbapy
except:
    from os import system
    system("pip3 install tbapy")
from datetime import datetime
#if __name__ == "__main__":
now = datetime.now()
try:
    if sys.argv[1] != "":
        event_key = sys.argv[1]
except:
    event_key = "2018ohcl"

extraPath = "/" 
    
filename = event_key + ".json"
tba = tbapy.TBA("Hc4ZR47A3dCfAWaWvmVkI3k8aMjfvkL8jds4Jg23xVkk9kT2FdvMx5WQlG1cciIy")
information = tba.event_teams(event_key, simple=True)
fileE = open(path + extraPath + filename, mode='w')
fileE.write("{ \"teams\": [\n")
a = 0
b = len(information)
for info in information:
    if a < b-1:
        fileE.write('{\n"teamNumber": ' + str(info['team_number']) + ',\n"nickname": "' + info['nickname'] + '"\n},\n')
    else:
        fileE.write('{\n"teamNumber": ' + str(info['team_number']) + ',\n"nickname": "' + info['nickname'] + '"\n}\n')
    a+=1
fileE.write("]}")
fileE.close()
print("Information loaded and saved under " + filename)