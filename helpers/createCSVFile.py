import sys, csv

sys.path.append('./helpers')
from helpers.message import success, error

def createCSVFile(path_csv, listOfData, headObj):
    
    try:
        columns = ["ID", "NAME", "PATH", "HASH SHA-256", "MATCH", "TEXT", "METADATA"]

        with open(path_csv, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(["Prosecutor Toolkit"])
            writer.writerow([])             # SI FALLA SACAR LOS [] - 9/4/23- 15:31 Hs
            writer.writerow([headObj.user])
            writer.writerow([headObj.case])
            writer.writerow([headObj.time])
            writer.writerow([headObj.target])
            writer.writerow([headObj.mercle])
            writer.writerow([headObj.formats])
            writer.writerow([headObj.terms])
            writer.writerow([headObj.misspellings])
            writer.writerow([])

            writer.writerow(columns)

            for value in listOfData:
                [idF, name, path, hashF, match, text, metadata] = value
        
                data = (str(idF), str(name), path, str(hashF), match, str(text), metadata)
                row = []
                for value in data:
                    row.append(value)
                writer.writerow(row)

        success('CSV WAS CREATED')

        return True

    except:
        error('CSV could not create')
        return False