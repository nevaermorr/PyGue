"""
key values for all actions
"""

#key map for hero actions
hero_ = {
    #quit button
    'Q': ['quit'],
    #movement keys
    '1': ['move', 'SW'],
    '2': ['move', 'S'],
    '3': ['move', 'SE'],
    '4': ['move', 'W'],
    '5': ['wait'],
    '6': ['move', 'E'],
    '7': ['move', 'NW'],
    '8': ['move', 'N'],
    '9': ['move', 'NE'],
    #equipment management
    '+': ['collect'],
    '-': ['drop'],
    'i': ['showInventory'],
}

#key map for list navigation
displayableList_ = {
    'quit' : 'q',
    'next' : '+',
    'prev' : '-',
}