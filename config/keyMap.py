"""
key values for all actions
"""

#key map for hero actions
hero_ = {
    # quit button
    'Q': ['quit'],
    # movement keys
    '1': ['move', [-1, 1]],
    '2': ['move', [0, 1]],
    '3': ['move', [1, 1]],
    '4': ['move', [-1, 0]],
    '5': ['wait'],
    '6': ['move', [1, 0]],
    '7': ['move', [-1, -1]],
    '8': ['move', [0, -1]],
    '9': ['move', [1, -1]],
    # equipment management
    '+': ['collect'],
    '-': ['drop'],
    'i': ['show_inventory'],
    # interaction
    'o': ['manipulate_door'],
    't': ['aim'],
    'T': ['beam'],
}
