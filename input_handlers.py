import libtcodpy as libtcod

def handle_keys(key):
    # Movement keys
    if key.vk == libtcod.KEY_CHAR:
        if key.c == ord('w'):
            return {'move': (0, -1)}
        elif key.c == ord('s'):
            return {'move': (0, 1)}
        elif key.c == ord('a'):
            return {'move': (-1, 0)}
        elif key.c == ord('d'):
            return {'move': (1, 0)}
    
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggles full screen
        return {'fullscreen': True}

    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the game
        return {'exit': True}
    
    # No key was pressed
    return {}