# from subprocess import call
# call(["pytest ", "--alluredir test1 ./SUITES"])
import os 
# os.system('pytest --alluredir test2 ./SUITES')
import datetime
basename = "mylogfile" +"_"
suffix = datetime.datetime.now().strftime("%y-%m-%d_%H-%M-%S")
filename = "".join([basename, suffix])
print(f'pytest --alluredir {filename} ./SUITES')
os.system(f'pytest --alluredir {filename} ./SUITES')
