import os
import subprocess
# out_bytes = subprocess.Popen(['netstat','-a'])
#redirect output
out = open("tmp.txt","w")

# cmds = "cd ~/eclipse-workspace/Proj3_Library_Vector_SOLUTION ./Debug/Proj3_Library_Vector_SOLUTION;pwd"
cmds = "cd ~/eclipse-workspace/Proj3_Library_Vector_SOLUTION;./Debug/Proj3_Library_Vector_SOLUTION  test"

process = subprocess.Popen(cmds, shell=True, stdout=out, stderr=out)
process.wait()

process = subprocess.Popen(cmds, shell=True, stdout=out, stderr=out)
process.wait()

# process1 = subprocess.Popen(cmds, shell=True, stdout=out, stderr=out)
