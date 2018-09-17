import libtcodpy as libtcod

from entity import Entity
from input_handlers import handle_keys
from map_objects.game_map import GameMap
from render_function import clear_all, render_all

def main():
    screen_width = 80
    screen_height = 50
    map_width = 80
    map_height = 45

    colors = {
        'dark_wall': libtcod.Color(0, 0, 100),
        'dark_ground': libtcod.Color(50, 50, 150)
    }

    player = Entity(int(screen_width / 2), int(screen_height / 2), '@', libtcod.white)
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), '@', libtcod.yellow)
    # Store created entities in our list
    entities = [npc, player]

    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

    libtcod.console_init_root(screen_width, screen_height, 'The Teacher', False)

    con = libtcod.console_new(screen_width, screen_height)

    game_map = GameMap(map_width, map_height)

    # Hold our keyboard and mouse input
    key = libtcod.Key()
    mouse = libtcod.Mouse()

    # This while loop is our 'game loop', won't end unless we close screen
    while not libtcod.console_is_window_closed():
        # Captures and updates user input of keyboard and mouse
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)
        print("Render")
        render_all(con, entities, game_map, screen_width, screen_height, colors)
        # Presents everything on the screen
        libtcod.console_flush()
        print("Flushed")
        # Replaces old locations of entities with a space
        clear_all(con, entities)
        print("Cleared")
        action = handle_keys(key)

        # Note that handle_keys returns a dictionary 
        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')
        
        if move:
            dx, dy = move
            if not game_map.is_blocked(player.x + dx, player.y + dy):
                player.move(dx, dy)

        if exit:
            return True

        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

if __name__ == '__main__':
    main()
