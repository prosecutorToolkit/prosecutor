import os
from os import walk

def routeFiles(formatsListInObj, targetPath):
    numallfiles = 0
    filesRouteList = []
    ignoredFilesList = []

    ram = []
    ram.append(targetPath)
    while ram:
        for route in ram:
            try:
                listafiles = next(walk(route))[2]
                for file in listafiles:
                    ext = os.path.splitext(file)[1].lower()
                    if ext in formatsListInObj.list:
                        fileRoute = os.path.join(route, file)
                        filesRouteList.append(fileRoute)
                        numallfiles += 1
                    else:
                        ignoredFilesList.append((file, ext, route))
            except: pass
            ram.remove(route)
            try:
                subdirs = next(walk(route))[1]
                for subdir in subdirs:
                    route1 = os.path.join(route, subdir)
                    ram.append(route1)
            except: pass

    return filesRouteList, ignoredFilesList