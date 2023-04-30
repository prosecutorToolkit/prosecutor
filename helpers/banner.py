import random, sys

sys.path.append('../helpers')
from helpers.message import blue

def banner():
    n1 = '''
                                                                                        ,d
                                                                                        88
8b,dPPYba,   8b,dPPYba,   ,adPPYba,   ,adPPYba,   ,adPPYba,   ,adPPYba,  88       88  MM88MMM   ,adPPYba,   8b,dPPYba,
88P'    "8a  88P'   "Y8  a8"     "8a  I8[    ""  a8P_____88  a8"     ""  88       88    88     a8"     "8a  88P'   "Y8
88       d8  88          8b       d8   `"Y8ba,   8PP"""""""  8b          88       88    88     8b       d8  88
88b,   ,a8"  88          "8a,   ,a8"  aa    ]8I  "8b,   ,aa  "8a,   ,aa  "8a,   ,a88    88,    "8a,   ,a8"  88
88`YbbdP"'   88           `"YbbdP"'   `"YbbdP"'   `"Ybbd8"'   `"Ybbd8"'   `"YbbdP'Y8    "Y888   `"YbbdP"'   88
88
88
        '''
    n2 = '''
                                                  o
                                                  8
.oPYo. oPYo. .oPYo. .oPYo. .oPYo. .oPYo. o    o  o8P .oPYo. oPYo.
8    8 8  `' 8    8 Yb..   8oooo8 8    ' 8    8   8  8    8 8  `'
8    8 8     8    8   'Yb. 8.     8    . 8    8   8  8    8 8
8YooP' 8     `YooP' `YooP' `Yooo' `YooP' `YooP'   8  `YooP' 8
8 ....:..:::::.....::.....::.....::.....::.....:::..::.....:..::::
8 ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
..::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    '''
    n3 = '''
 .S_sSSs     .S_sSSs      sSSs_sSSs      sSSs    sSSs    sSSs   .S       S.   sdSS_SSSSSSbs    sSSs_sSSs     .S_sSSs
.SS~YS$sb   .SS~YS$sb    d$sSP~YS$sb    d%SSP   d%SSP   d$sSP  .SS       SS.  YSSS~S%SSSSSP   d$sSP~YS$sb   .SS~YS$sb
S%S   `S%B  S%S   `S%B  d%S'     `S%B  d%S'    d%S'    d%S'    S%S       S%S       S%S       d%S'     `S%B  S%S   `S%B
S%S    S%S  S%S    S%S  S%S       S%S  S%|     S%S     S%S     S%S       S%S       S%S       S%S       S%S  S%S    S%S
S%S    d*S  S%S    d*S  S&S       S&S  S&S     S&S     S&S     S&S       S&S       S&S       S&S       S&S  S%S    d*S
S&S   .S*S  S&S   .S*S  S&S       S&S  Y&Ss    S&S_Ss  S&S     S&S       S&S       S&S       S&S       S&S  S&S   .S*S
S&S_sdSSS   S&S_sdSSS   S&S       S&S  `S&&S   S&S~SP  S&S     S&S       S&S       S&S       S&S       S&S  S&S_sdSSS
S&S~YSSY    S&S~YSY%B   S&S       S&S    `S*S  S&S     S&S     S&S       S&S       S&S       S&S       S&S  S&S~YSY%B
S*S         S*S   `S%B  S*b       d*S     l*S  S*b     S*b     S*b       d*S       S*S       S*b       d*S  S*S   `S%B
S*S         S*S    S%S  S*S.     .S*S    .S*P  S*S.    S*S.    S*S.     .S*S       S*S       S*S.     .S*S  S*S    S%S
S*S         S*S    S&S   SSSbs_sdSSS   sSS*S    SSSbs   SSSbs   SSSbs_sdSSS        S*S        SSSbs_sdSSS   S*S    S&S
S*S         S*S    SSS    YSSP~YSSY    YSS'      YSSP    YSSP    YSSP~YSSY         S*S         YSSP~YSSY    S*S    SSS
    '''
    n4 = '''

 #######  #######  #######  #######  #######  #######  ##   ## ########  #######  #######
      ##       ##       ##                             ##   ##    ##          ##       ##
 #######  #######  ##   ##  #######  ####     ##       ##   ##    ##     ##   ##  #######
 ##       ##  ##   ##   ##       ##  ##       ##       ##   ##    ##     ##   ##  ##  ##
 ##       ##   ##  #######  #######  #######  #######  #######    ##     #######  ##   ##
    '''
    devData = '''
                                        P R O S E C U T O R   T O O L K I T
                                                   Version 1.0
    '''

    onesAndCeros = '''
1                               1                       1           1             1                                 1
0 1       1       1             0           0   1       0       0   1   0         0   1       1       1         1   0
0 0   0   0   0   0     1       0   1       1   0       1   0   1   1   1     1   1   0   0   0   0   0     1   1   0
1 0   1   1 1 0   1     0   1   1   0   1   1   0   0   1   1   0   0   0 1   1   0   0   1   1   0   1     0   1   1
1 1 0 1 1 0 1 1 0 1   0 1 0 1 0 1 0 1   0 1 0 0 1   0 1 1 0 1   1 0 0   1 0 0 1 0 1   1 0 1 1 0   1 0 1   0 1 0 1 0 1
0 1 0 1 0 1 0 0 1 0 1 0 1 0 0 1 0 1 0 1 0 0 1 0 1 0 1 0 0 1 0 1 0 1 0 0 1 0 1 0 1 1 0 1 0 1 0 1 0 0 1 0 1 0 1 0 0 1 0
    '''

    # colorama.init()
    # ramdomNumber = random.randint(1, 4)
    # ramdomColor = random.randint(1, 4)
    # if ramdomColor == 1: color = colorama.Fore.RED
    # elif ramdomColor == 2: color = colorama.Fore.BLUE
    # elif ramdomColor == 3: color = colorama.Fore.YELLOW
    # else: color = colorama.Fore.GREEN
    # if ramdomNumber == 1: print(color + n1 + onesAndCeros + '\n\n' + devData + '\n\n')
    # elif ramdomNumber == 2: print(color + n2 + onesAndCeros + '\n\n' + devData + '\n\n')
    # elif ramdomNumber == 3: print(color + n3 + onesAndCeros + '\n\n' + devData + '\n\n')
    # else: print(color + n4 + onesAndCeros + '\n\n' + devData + '\n\n')
    blue(n1 + onesAndCeros + '\n\n' + devData + '\n\n')