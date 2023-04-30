import sys

sys.path.append('./helpers')
from helpers.message import title, error, blue
from helpers.yesNo import yesNo


def formatFile():
    title('FORMAT FILE')
    while True:
        getPDF = False; getTXT = False; getPNG = False; getICO = False; getJPG = False; getJPEG = False; getTIFF = False; getBMP = False; getGIF = False; getXLS = False; getXLSX = False; getCSV = False
        shownString = ''

        try:
            blue('Set the format flags:') 
            flags = str(input('''\n  - a (get all: images, pdf, xlsx, txt)
                        \n  > i (images)
                        \n      - j (jpg)
                        \n      - e (jpeg)
                        \n      - f (tiff)
                        \n      - b (bmp)
                        \n      - g (gif)
                        \n      - n (png)
                        \n      - o (ico)
                        \n  > p (PDFs)
                        \n  > t (txt)
                        \n  > d (data)
                        \n      - x (xls)
                        \n      - l (xlsx)
                        \n      - c (csv)
                        \n  > '''))
            if len(flags) == 0:
                error("Must select al least one format to get")
                continue
            flags = list(flags.lower())

            if 'a' in flags:
                getJPG = True; getJPEG = True; getTIFF = True; getBMP = True; getGIF = True; getPNG = True; getICO = True
                getTXT = True
                getPDF = True
                shownString = '''  > i (images)
                                \n      - j (jpg)
                                \n      - e (jpeg)
                                \n      - f (tiff)
                                \n      - b (bmp)
                                \n      - g (gif)
                                \n      - n (png)
                                \n      - o (ico)
                                \n  > t (text)
                                \n  > p (pdf)
                                \n  > d (data)
                                \n      - x (xls)
                                \n      - l (xlsx)
                                \n      - c (csv)'''
            else:
                if 'i' in flags:
                    getJPG = True; getJPEG = True; getTIFF = True; getBMP = True; getGIF = True; getPNG = True; getICO = True
                    shownString += '''\n  > i (images)
                                        \n      - j (jpg)
                                        \n      - e (jpeg)
                                        \n      - f (tiff)
                                        \n      - b (bmp)
                                        \n      - g (gif)
                                        \n      - n (png)
                                        \n      - o (ico)'''
                else:
                    if 'j' in flags:
                        getJPG = True
                        shownString += '\n  > jpg'

                    if 'e' in flags:
                        getJPEG = True
                        shownString += '\n  > jpeg'

                    if 'f' in flags:
                        getTIFF = True
                        shownString += '\n  > tiff'
                        
                    if 'b' in flags:
                        getBMP = True
                        shownString += '\n  > bmp'

                    if 'g' in flags:
                        getGIF = True
                        shownString += '\n  > gif'

                    if 'n' in flags:
                        getPNG = True
                        shownString += '\n  > png'

                    if 'o' in flags:
                        getICO = True
                        shownString += '\n  > ico'

                if 'p' in flags:
                    getPDF = True
                    shownString += '\n  > pdf'
                
                if 't' in flags:
                    getTXT = True
                    shownString += '\n  > txt'
                
                if 'd' in flags:
                    getXLS = True; getXLSX = True; getCSV = True
                    shownString += '''\n  > Data
                                        \n      - x (xls)
                                        \n      - l (xlsx)
                                        \n      - c (csv)'''
                else:
                    if 'x' in flags:
                        getXLS = True
                        shownString += '\n  > xls'

                    if 'l' in flags:
                        getXLSX = True
                        shownString += '\n  > xlsx'

                    if 'c' in flags:
                        getCSV = True
                        shownString += '\n  > csv'

            if not getPDF and not getTXT and not getJPG and not getJPEG and not getTIFF and not getBMP and not getGIF and not getXLS and not getXLSX and not getCSV and not getPNG and not getICO:
                error('Invalid configuration')
                continue
            
            fList = []
            if getPDF: fList.append('pdf')
            if getTXT: fList.append('txt')
            if getJPG: fList.append('jpg')
            if getJPEG: fList.append('jpeg')
            if getTIFF: fList.append('tiff')
            if getBMP: fList.append('bmp')
            if getGIF: fList.append('gif')
            if getXLS: fList.append('xls')
            if getXLSX: fList.append('xlsx')
            if getCSV: fList.append('csv')
            if getPNG: fList.append('png')
            if getICO: fList.append('ico')

            answer = yesNo('Selected files:\n{}\nAre you sure that you want to get this? (y/n)\n > '.format(shownString))
            if answer == False: continue

            formatStr = shownString.replace('\n', ' ')
            while '  ' in formatStr: formatStr = formatStr.replace('  ', ' ')

            def createFormatClass():
                class Format:
                    def __init__(self):
                        self.string = shownString
                        self.strInLine = formatStr
                        self.list = fList
                return Format
            getFormat = createFormatClass()
        except: error("Unknown error. ID=S4")
        break
    return getFormat()