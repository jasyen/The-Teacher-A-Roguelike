import libtcodpy as libtcod

from input_handlers import handle_keys

def main():
    screen_width = 80
    screen_height = 50

    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

    libtcod.console_init_root(screen_width, screen_height, 'The Teacher', False)

    con = libtcod.console_new(screen_width, screen_height)

    # Hold our keyboard and mouse input
    key = libtcod.Key()
    mouse = libtcod.Mouse()

    # This while loop is our 'game loop', won't end unless we close screen
    while not libtcod.console_is_window_closed():
        # Captures and updates user input of keyboard and mouse
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)

        libtcod.console_set_default_foreground(con, libtcod.white)
        libtcod.console_put_char(con, player_x, player_y, '@', libtcod.BKGND_NONE)
        libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)
        # Presents everything on the screen
        libtcod.console_flush()

        # Replaces old location of player with a space
        libtcod.console_put_char(con, player_x, player_y, ' ', libtcod.BKGND_NONE)

        action = handle_keys(key)

        # Note that handle_keys returns a dictionary 
        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')
        
        if move:
            dx, dy = move
            player_x += dx
            player_y += dy

        if exit:
            return True

        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

if __name__ == '__main__':
    main()
