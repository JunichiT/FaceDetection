import commands

os.system('mkdir ~/Desktop/smile_tmp')


score = commands.getoutput("python face_value.py ~/Desktop/smile_tmp/face_detection.png")

if score:
  print score
