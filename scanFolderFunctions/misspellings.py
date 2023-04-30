# AGREGAR FUNCION YA CREADA PARA CREAR NUEVAS MISSPELLINGS

import sys

sys.path.append('./helpers')
from helpers.message import title, error
from helpers.yesNo import yesNo


def misspellings():
    try:
        title("MISPELLINGS (optional)")
        while True:
            flags = str(input('''Set the misspellings flags:
            \n  > n (none: strict query)
            \n  > a (admit all: B/V, G/J, H and U)
            \n  > b (B/V)
            \n  > g (G/J)
            \n  > h (H)
            \n  > u (U)
            \n > '''))
            if len(flags) == 0:
                error("must select at least one option. ID=5")
                continue
            flags = list(flags.lower())
            BV_OrtErr = False
            GJ_OrtErr = False
            H_OrtErr = False
            U_OrtErr = False
            shownString = ''
            if 'a' in flags:
                confirm = yesNo('Are you sure that you want to admit all: uppers/lowers, B/V, G/J, H and U)? (y/n)\n > ')
                if confirm:
                    BV_OrtErr = True
                    GJ_OrtErr = True
                    H_OrtErr = True
                    U_OrtErr = True
                    shownString = '\n  > B/V\n  > G/J\n  > H\n  > U'
                else: continue
            else:
                if 'n' in flags:
                    shownString = 'NONE misspellings (strict query)'
                else:
                    if 'b' in flags: BV_OrtErr = True; shownString +=  '\n  > B/V'
                    if 'g' in flags: GJ_OrtErr = True; shownString +=  '\n  > G/J'
                    if 'h' in flags: H_OrtErr = True; shownString +=  '\n  > H'
                    if 'u' in flags: U_OrtErr = True; shownString +=  '\n  > U'
                confirm = yesNo('Selected items:\n {}\nAre you sure that you want to get these? (y/n)\n > '.format(shownString))
                if not confirm: continue
            break
    except: error('Unknown. ID=S8')

    misspInLine = shownString.replace('\n', ' ')
    while '  ' in misspInLine: misspInLine = misspInLine.replace('  ', ' ')

    def configure():
        class OE:
            def __init__(self):
                self.string = shownString
                self.strInLine = misspInLine
                self.BV = BV_OrtErr
                self.GJ = GJ_OrtErr
                self.H = H_OrtErr
                self.U = U_OrtErr
        return OE
    getConfig = configure()

    return getConfig()