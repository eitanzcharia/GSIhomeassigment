import json
from flask import jsonify
from sercive.src.main.homeassignmentservice.utils.FileUtils import FileUtils

#Server dictionary class inherit from dict ,The class resposible to add/remove/count objects to/from the server dictionary.
#Data from the server dictionary will be submitted to a json file while commiting .
class MyDictionary(dict):

    #construtor , resposible to initiate dict super class and fileUtils helper to submitt data to file.
    def __init__(self):
        super().__init__()
        self.__fileUtils__=FileUtils(True)

    #add objects to the dict.
    #input , dictionary of keys:value
    def add(self ,toAdd : dict ):
        self.update(toAdd)
        print(str(toAdd.keys()) +str(toAdd.values()) + ' was added')

    #method to remove items from the list .
    #input: list of keys.
    #return:keys which removed/not removed fron the dictionary.
    def remove (self,keys):
        removedKeys=[]
        unRemovedKeys=[]
        for key in keys:
            if key in self:
                del self[key]
                removedKeys.append(key)
            else:unRemovedKeys.append(key)
        return  self.__createRemoveMessage__(removedKeys, unRemovedKeys)

    #Method to return the object count.
    #return the actual dictionary object count
    def count(self):
        print( 'lentgh is' + str(self.__len__()) )
        return self.keys().__len__()

    #the method save the dictionary data to a json file .
    #path and file name are taking from devFileProp.
    def writeToFile(self):
        self.__fileUtils__.fillFile(json.dumps(self))

    #privatr method for building remove message .
    def __createRemoveMessage__(self, removedKeys, unRemovedKeys):
        message = 'Removed:' + str(removedKeys) + ' , Not Removed: ' + str(unRemovedKeys)
        return message

