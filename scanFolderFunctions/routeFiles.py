import sys, os
from os import walk
from shutil import rmtree

def routeFiles(formatsListInObj, targetPath):
    numallfiles = 0
    filesRouteList = []
    allFilesRouteList = []

    ram = []
    ram.append(targetPath)
    while ram:
        for route in ram:
            try:
                listafiles = next(walk(route))[2]
                for file in listafiles:
                    recognizedFormat = False 
                    for final in formatsListInObj.list:
                        if file.endswith(final) == True:
                            fileRoute = os.path.join(route, file)
                            filesRouteList.append(fileRoute)
                            numallfiles += 1
                            recognizedFormat = True
                    if recognizedFormat == False:
                        fileRoute = os.path.join(route, file)
                        allFilesRouteList.append(fileRoute)
            except: pass
            ram.remove(route)
            try:
                subdirs = next(walk(route))[1]
                for subdir in subdirs:
                    route1 = os.path.join(route, subdir)
                    ram.append(route1)
            except: pass

    return allFilesRouteList, filesRouteList