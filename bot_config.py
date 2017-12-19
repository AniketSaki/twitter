consumerKey = 'wwnCMTRhaMlen5PdXzUElmDug'
consumerSecret = 'kYR7Sppx6GrtkMs2yWe6RjRPgXFwpy0ppE5dH2HwZXXq39GiPG'
accessToken = '929721883464835073-YBzh25HobcqNA7a1NmiZOujSDDmF8r9'
accessTokenSecret = '9fgOgo162ItrDmQCP40R4733MDyWnzDMKH2nqz1Y862Jb'
grammar = """
      S -> NP VP
      NP -> Det N
      VP -> V NP
      Det -> 'a' | 'the'
      N -> 'dog' | 'cat' | 'monster' | 'puppy' | 'rodent' | 'megalodon' | 'bunny' | 'jedi' | 'master'
      V -> 'chased' | 'ate' | 'caressed' | 'rode' | 'terrorized' | 'sniffed' | 'dragged' | 'complimented'
    """
pcfg = """
    S    -> NP VP         [1.0]
    VP   -> V NP          [.59]
    VP   -> V             [.40]
    VP   -> VP PP         [.01]
    NP   -> Det N         [.41]
    NP   -> Name          [.28]
    NP   -> NP PP         [.31]
    PP   -> P NP          [1.0]
    V    -> 'attacked'    [.08]
    V    -> 'caught'      [.06]
    V    -> 'dodged'      [.12]
    V    -> 'grabbed'     [.07]
    V    -> 'hid'         [.13]
    V    -> 'met'         [.14]
    V    -> 'ran'         [.09]
    V    -> 'shot'        [.09]
    V    -> 'sniffed'     [.11]
    V    -> 'swung'       [.11]
    N    -> 'rope'        [.18]
    N    -> 'stick'       [.21]
    N    -> 'bludgeon'    [.2]
    N    -> 'sword'       [.22]
    N    -> 'axe'         [.19]
    Name -> 'Amit'        [.13]
    Name -> 'Ben'         [.13]
    Name -> 'Bo'          [.13]
    Name -> 'Devi'        [.12]
    Name -> 'Kamala'      [.12]
    Name -> 'Kartik'      [.12]
    Name -> 'Pavan'       [.13]
    Name -> 'Thor'        [.12]
    P    -> 'against'     [.12]
    P    -> 'between'     [.12]
    P    -> 'near'        [.12]
    P    -> 'past'        [.12]
    P    -> 'towards'     [.13]
    P    -> 'up'          [.13]
    P    -> 'under'       [.13]
    P    -> 'down'        [.13]
    Det  -> 'the'         [.41]
    Det  -> 'a'           [.31]
    Det  -> 'their'       [.28]
    """
