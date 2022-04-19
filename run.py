# from subprocess import call

# call(["pytest ", "--alluredir test1 ./SUITES"])

import os 
# os.system('pytest --alluredir test2 ./SUITES')


import datetime
basename = "mylogfile" +"_"
basename_allure = "allure-results"
suffix = datetime.datetime.now().strftime("%y-%m-%d_%H-%M-%S")
filename = "".join([basename, suffix])

print(f'pytest --alluredir {basename_allure} ./SUITES')

os.system(f'pytest --alluredir {basename_allure} ./SUITES')
