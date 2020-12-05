import os

from sercive.src.main.homeassignmentservice.interfaces.DevRunConf import DevRunConfiguration

# implementation of DevRunConfiguration , the class contain properties for data file creation .
class DevFileProp(DevRunConfiguration):

    #implementaion of loadDevConf , the method load to parameters to OS.
    def loadDevConf(self):
        os.environ['FILE_PATH'] = 'c:\PythonOutFiles'
        os.environ['FILE_NAME'] = 'data.json'