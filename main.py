import arcade
import gameData as gameDt
import pathlib



"""Global Variables"""
image_location = pathlib.Path.cwd() / 'images'

SCREEN_W = 960
SCREEN_H = 800
SCREEN_TITLE = "Duck Tower Defense"
SCREEN_SCALING = 2
SPEED = 3

FRAME_H = 32
FRAME_W = 32


class AracdeWindow(arcade.Window):
        """ Main application class. """

        def __init__(self, width, height, title):
            super().__init__(width, height, title)


            self.map_loction = None
            self.spawn_e = None
            self.start_wave = None

            self.currentGameState = None

            self.fireball_explosion = None
            self.fireball_tower = None
            self.rock_explosion = None
            self.rock_tower = None
            self.ironball_tower = None
            self.ironball_explosion = None
            self.stone_tower = None
            self.stone_explosion = None
            self.fire_spikes = None
            self.traps_list = None

            "Lists for map layers"
            self.map_list = None
            self.river_list = None
            self.wall_list = None
            self.base_list = None

            self.tower_menu = None
            self.select_tower = None
            self.select_tower_type = None
            self.min_tower_menu = None
            self.max_tower_menu = None
            self.buy_rock_tower = None
            self.buy_fireball_tower = None
            self.buy_ironball_tower = None
            self.buy_stone_tower = None
            self.buy_fire_trap = None

            self.base_health = None

            self.wave_timer = None
            self.wave_counter = None
            self.death_num = None
            self.timer = None
            self.curreny = None
            self.buy_status = None
            self.buy_err = None
            self.spawn_num = 0


            self.mouse_x = 0
            self.mouse_y = 0

            self.map_type = None
            self.currentGameState = "Open_Menu"

            self.image_map_1 = None
            self.image_map_2 = None
            self.image_map_3 = None

            self.sound_loction = None
            self.explosion_sound_1 = None
            self.explosion_sound_2 = None
            self.explosion_sound_3 = None
            self.explosion_sound_4 = None

            arcade.set_background_color(arcade.color.AERO_BLUE)


        def setup(self):
            # Set up your game here


            if self.currentGameState == "Open_Menu":
                map_folder = pathlib.Path.cwd()
                self.image_map_1 = arcade.load_texture(str(map_folder) + "/map/map1.png")
                self.image_map_2 = arcade.load_texture(str(map_folder) + "/map/map2.png")
                self.image_map_3 = arcade.load_texture(str(map_folder) + "/map/map3.png")

            elif self.currentGameState == "Play_Game":

                self.base_health = 100

                self.wave_timer = 5
                self.wave_counter = 0
                self.death_num = 0
                self.spawn_num = 0
                self.start_wave = False
                self.curreny = 500
                self.buy_status = True

                #Tilesets from Jetsan on itch.io

                self.map_loction = pathlib.Path.cwd()
                self.map_loction = (str(self.map_loction) + ("/map/map") + str(self.map_type) + (".tmx"))
                game_map = arcade.tilemap.read_tmx(str(self.map_loction))
                self.map_list = arcade.tilemap.process_layer(game_map, "ground", SCREEN_SCALING)
                self.river_list = arcade.tilemap.process_layer(game_map, "river", SCREEN_SCALING)
                self.wall_list = arcade.tilemap.process_layer(game_map, "wall", SCREEN_SCALING)
                self.base_list = arcade.tilemap.process_layer(game_map, "base", SCREEN_SCALING)

                self.min_tower_menu = arcade.load_texture(str(image_location) + "/menu/tower_menu/min_tower.png", 0, 0)
                self.max_tower_menu = arcade.load_texture(str(image_location) + "/menu/tower_menu/max_tower.png")
                self.buy_fireball_tower = arcade.load_texture(str(image_location) + "/fireball_tower/0.png")
                self.buy_rock_tower = arcade.load_texture(str(image_location) + "/rock_tower/0.png" )
                self.buy_ironball_tower = arcade.load_texture(str(image_location) + "/ironball_tower/0.png" )
                self.buy_stone_tower = arcade.load_texture(str(image_location) + "/stone_tower/0.png")
                self.buy_fire_trap = arcade.load_texture(str(image_location) + "/buy_fire-trap.png")
                self.buy_err = arcade.load_texture(str(image_location) + "/buy_error.png")

                self.sound_loction = pathlib.Path.cwd() / 'sounds'
                self.explosion_sound_1 = arcade.load_sound(str(self.sound_loction) + "/explode1.wav")
                self.explosion_sound_2 = arcade.load_sound(str(self.sound_loction) + "/explode2.wav")
                self.explosion_sound_3 = arcade.load_sound(str(self.sound_loction) + "/explode3.wav")
                self.explosion_sound_4 = arcade.load_sound(str(self.sound_loction) + "/explode4.wav")

                self.tower_menu = False
                self.select_tower = False
                self.select_tower_type = 0

                self.sound_loction = pathlib.Path.cwd() / 'sounds'

            else:
                print('Menu Screen')

        def on_key_press(self, key, modifiers):
                pass


        def on_key_release(self, key, modifiers):
               pass

        def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):

           if self.currentGameState == "Open_Menu":
               if button == arcade.MOUSE_BUTTON_LEFT and (x < 385 and x>= 65) and (y < 635 and y >= 365):
                   self.map_type = 1
                   self.currentGameState = "Play_Game"
                   self.setup()
               elif button == arcade.MOUSE_BUTTON_LEFT and (x < 910 and x >= 590) and (y < 635 and y >= 365):
                   self.map_type = 2
                   self.currentGameState = "Play_Game"
                   self.setup()
               elif button == arcade.MOUSE_BUTTON_LEFT and (x < 635 and x >= 315) and (y < 285 and y >= 15):
                    self.map_type = 3
                    self.currentGameState = "Play_Game"
                    self.setup()
           elif self.currentGameState == "Play_Game":
               if button == arcade.MOUSE_BUTTON_LEFT and (x < SCREEN_W and x>= 885) and (y < SCREEN_H and y >= 765):
                    self.tower_menu = True
               elif button == arcade.MOUSE_BUTTON_LEFT and (x < SCREEN_W and x>= 785) and (y < 685 and y >= 635):
                    self.tower_menu = False
               elif button == arcade.MOUSE_BUTTON_LEFT and (x < 210 and x >= 175) and (y < 775 and y >= 720) and self.tower_menu == True:
                   self.select_tower = True
                   self.select_tower_type = 1
               elif button == arcade.MOUSE_BUTTON_LEFT and (x < 350 and x >= 295) and (y < 775 and y >= 720) and self.tower_menu == True:
                    self.select_tower = True
                    self.select_tower_type = 2
               elif button == arcade.MOUSE_BUTTON_LEFT and (x < 500 and x >= 460) and (y < 775 and y >= 720) and self.tower_menu == True:
                   self.select_tower = True
                   self.select_tower_type = 3
               elif button == arcade.MOUSE_BUTTON_LEFT and (x < 750 and x >= 615) and (y < 775 and y >= 720) and self.tower_menu == True:
                   self.select_tower = True
                   self.select_tower_type = 4
               elif button == arcade.MOUSE_BUTTON_LEFT and (x < 825 and x >= 775) and (
                       y < 775 and y >= 720) and self.tower_menu == True:
                   self.select_tower = True
                   self.select_tower_type = 5
               else:
                   if self.select_tower == True:
                       self.place_tower() #will place a given tower if was previously clicked
                   self.tower_menu = False
                   self.select_tower = False
           pass

        def on_mouse_release(self, x: float, y: float, button: int,
                         modifiers: int):
            pass

        def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
                    self.mouse_x = x
                    self.mouse_y = y

        
        def on_draw(self):
            """ Render the screen. """
            arcade.start_render()

            if self.currentGameState == "Open_Menu":
                arcade.draw_text("Select A Map", 500, 700, arcade.color.REDWOOD, 45, anchor_x="center")
                arcade.draw_texture_rectangle(225, 500, 318, 267, self.image_map_1)
                arcade.draw_rectangle_outline(225, 500, 318, 267, arcade.color.BLACK_LEATHER_JACKET,6)
                arcade.draw_texture_rectangle(750, 500, 318, 267, self.image_map_2)
                arcade.draw_rectangle_outline(750, 500, 318, 267, arcade.color.BLACK_LEATHER_JACKET, 6)
                arcade.draw_texture_rectangle(475, 150, 318, 267, self.image_map_3)
                arcade.draw_rectangle_outline(475, 150, 318, 267, arcade.color.BLACK_LEATHER_JACKET, 6)

                pass
            elif self.currentGameState == "Play_Game":
                self.map_list.draw()
                self.river_list.draw()
                self.wall_list.draw()
                self.base_list.draw()

                gameDt.tower_list.draw()
                gameDt.bullet_list.draw()
                gameDt.traps_list.draw()
                gameDt.enemy_list.draw()

                self.draw_tower_menu()

                # Wave Timer
                self.draw_wave_count_down_time()
                self.draw_base_health()
                self.draw_currency()

                gameDt.explosion_list.draw() #current bug in the method
            else:
                pass
            arcade.finish_render()

        def update(self, delta_time):


            if self.currentGameState == "Open_Menu":
                pass
            elif self.currentGameState == "Play_Game":
                self.increment_wave_timer()
                gameDt.enemy_list.update()
                gameDt.enemy_list.update_animation()
                gameDt.tower_list.update()
                gameDt.bullet_list.update()
                gameDt.traps_list.update()

                self.handle_wave()
                self.update_enemy_collisions()
                gameDt.explosion_list.update()
            else:
                pass


        def place_tower(self):
            if self.select_tower_type == 1:
                if self.curreny - 50 >= 0:
                    self.fire_spikes = gameDt.Trap(1, self.mouse_x, self.mouse_y, 5, 41, 32)
                    gameDt.traps_list.append(self.fire_spikes)
                    self.curreny -= 50
                    self.buy_status = True
                else:
                    self.buy_status = False
            elif self.select_tower_type == 2:
                if self.curreny - 450 >= 0:
                    self.fireball_tower = gameDt.Fire_Tower(1, self.mouse_x, self.mouse_y, 1, 8, 100,str(image_location) + "/fireball_tower")
                    gameDt.tower_list.append(self.fireball_tower)
                    self.curreny -= 450
                    self.buy_status = True
                else:
                    self.buy_status = False
            elif self.select_tower_type == 3:
                if self.curreny - 35 >= 0:
                    self.rock_tower = gameDt.Rock_Tower(1, self.mouse_x, self.mouse_y, 1, 8, 45,str(image_location) + "/rock_tower")
                    gameDt.tower_list.append(self.rock_tower)
                    self.curreny -= 35
                    self.buy_status = True
                else:
                    self.buy_status = False
            elif self.select_tower_type == 4:
                if self.curreny - 150 >= 0:
                    self.ironball_tower = gameDt.Iron_Tower(1, self.mouse_x, self.mouse_y, 1, 8, 45,str(image_location) + "/ironball_tower")
                    gameDt.tower_list.append(self.ironball_tower)
                    self.curreny -= 150
                    self.buy_status = True
                else:
                    self.buy_status = False
            elif self.select_tower_type == 5:
                if self.curreny - 50 >= 0:
                    self.stone_tower = gameDt.Stone_Tower(1, self.mouse_x, self.mouse_y, 1, 10, 50,str(image_location) + "/stone_tower")
                    gameDt.tower_list.append(self.stone_tower)
                    self.curreny -= 50
                    self.buy_status = True
                else:
                    self.buy_status = False
            pass



        def update_enemy_collisions(self):
            #Handles enemies colliding with river tiles
            for river_tile in self.river_list:
                enemy_river_tile_collide = arcade.check_for_collision_with_list(river_tile, gameDt.enemy_list)

                for enemy in enemy_river_tile_collide:
                    enemy.move_auto()
                    pass

            # Handles enemies colliding with wall tiles
            for wall_tile in self.wall_list:
                enemy_wall_tile_collide = arcade.check_for_collision_with_list(wall_tile, gameDt.enemy_list)

                for enemy in enemy_wall_tile_collide:
                    enemy.move_auto()

            # Handles enemies colliding into the towers
            for enemy in gameDt.enemy_list:
                enemy_c = self.tower_collision(enemy, gameDt.tower_list)

                if enemy_c == None:
                    pass
                else:
                    enemy_c.move_auto()


            #Handles enemies colliding into the base and reduces health
            for base_tile in self.base_list:
                enemy_base_tile_collide = arcade.check_for_collision_with_list(base_tile, gameDt.enemy_list)

                for enemy in enemy_base_tile_collide:
                    enemy.kill()
                    self.base_health -= 5

            #Handles any bullets that hit the enemy
            for bullet in gameDt.bullet_list:
                enemy_hit_list = arcade.check_for_collision_with_list(bullet, gameDt.enemy_list)

                for hit in enemy_hit_list:
                    bullet.kill()

                    if isinstance(bullet, gameDt.Fireball):
                        arcade.play_sound(self.explosion_sound_1)
                        self.fireball_explosion = gameDt.Explosions(5, hit.center_x, hit.center_y, 5)
                        gameDt.explosion_list.append(self.fireball_explosion)
                        hit.health -= 100
                    elif isinstance(bullet, gameDt.Ironball):
                        arcade.play_sound(self.explosion_sound_2)
                        self.ironball_explosion = gameDt.Ironball_Explosion(1, hit.center_x, hit.center_y, 5)
                        gameDt.explosion_list.append(self.ironball_explosion)
                        hit.health -= 50
                    elif isinstance(bullet, gameDt.Stone):
                        arcade.play_sound(self.explosion_sound_3)
                        self.stone_explosion = gameDt.Stone_Explosion(1, hit.center_x, hit.center_y, 7)
                        gameDt.explosion_list.append(self.stone_explosion)
                        hit.health -= 35
                    elif isinstance(bullet, gameDt.Rock):
                        arcade.play_sound(self.explosion_sound_4)
                        self.rock_explosion = gameDt.Rock_Explosion(1, hit.center_x, hit.center_y, 5)
                        gameDt.explosion_list.append(self.rock_explosion)
                        hit.health -= 20
                    else:
                        print(False)

                    if isinstance(hit, gameDt.BatEnemy) and hit.health <= 0:
                        self.curreny += 25
                        self.death_num +=1
                        hit.kill()
                    elif isinstance(hit, gameDt.HorseEnemy) and hit.health <= 0:
                        self.curreny += 50
                        self.death_num +=1
                        hit.kill()
                    elif isinstance(hit, gameDt.SpiderEnemy) and hit.health <= 0:
                        self.curreny += 100
                        self.death_num +=1
                        hit.kill()
            #print(self.death_num, self.spawn_num)

            #Handles enemy collisions with traps
            for trap in gameDt.traps_list:
                enemy_trap_collision = arcade.check_for_collision_with_list(trap, gameDt.enemy_list)

                for enemy in enemy_trap_collision:


                    if enemy.hit_trap == False:
                        enemy.hit_trap = True
                        enemy.health -= 15
                        trap.reset()
                        if enemy.change_x > 0:
                            enemy.speed = (enemy.speed / 2)
                            enemy.move("right")
                        elif enemy.change_x < 0:
                            enemy.speed = (enemy.speed / 2)
                            enemy.move("left")
                        elif enemy.change_y > 0:
                            enemy.speed = (enemy.speed / 2)
                            enemy.move("up")
                        elif enemy.change_y < 0:
                            enemy.speed = (enemy.speed / 2)
                            enemy.move("down")
                        else:
                            print("error_enemy_trap_collision")

            #Handles enemys staying within the window
            for e in gameDt.enemy_list:
                e.move_boundaries()


        def handle_wave(self):
            if self.start_wave == True:
                if (self.spawn_num < 10 and self.wave_counter % 75==0):
                    self.spawn_enemies(1)
                    self.spawn_num += 1
                elif (self.spawn_num < 20 and self.wave_counter % 75 == 0) and self.death_num >= 8:
                    if self.spawn_num % 5 == 0:
                        self.spawn_enemies(2)
                    else:
                        self.spawn_enemies(1)
                    self.spawn_num += 1
                elif (self.spawn_num < 30 and self.wave_counter % 75 == 0) and self.death_num >= 18:
                    if self.spawn_num % 5 == 0:  # spawns spiders
                        self.spawn_enemies(3)
                    if self.spawn_num % 2 == 0:
                        self.spawn_enemies(2)
                    else:
                        self.spawn_enemies(1)
                    self.spawn_num += 1
                elif (self.spawn_num < 40 and self.wave_counter % 75 == 0) and self.death_num >= 28:
                    if self.spawn_num % 5 == 0: #spawns spiders
                        self.spawn_enemies(3)
                    if self.spawn_num % 2 == 0:
                        self.spawn_enemies(2)
                    else:
                        self.spawn_enemies(1)
                    self.spawn_num += 1
                elif (self.spawn_num < 50 and self.wave_counter % 75 == 0) and self.death_num >= 38:
                    if self.spawn_num % 3 == 0: #spawns spiders
                        self.spawn_enemies(3)
                    if self.spawn_num % 5 == 0:
                        self.spawn_enemies(2)
                    else:
                        self.spawn_enemies(1)
                    self.spawn_num += 1
                elif (self.spawn_num < 55 and self.wave_counter % 75 == 0) and self.death_num >= 40:
                    if self.map_type == 1:
                        if self.wave_counter % 2 == 0:
                            self.map_type = 2
                            self.reset()
                            self.setup()
                        else:
                            self.map_type = 3
                            self.reset()
                            self.setup()
                    elif self.map_type == 2:
                        if self.wave_counter % 2 == 0:
                            self.map_type = 3
                            self.reset()
                            self.setup()
                        else:
                            self.map_type = 1
                            self.reset()
                            self.setup()
                    else:
                        if self.wave_counter % 2 == 0:
                            self.map_type = 1
                            self.reset()
                            self.setup()
                        else:
                            self.map_type = 2
                            self.reset()
                            self.setup()

        def reset(self):
            self.wave_counter = 0
            self.spawn_num = 0
            self.death_num = 0
            self.wave_timer = 5
            gameDt.tower_list = arcade.SpriteList()
            gameDt.enemy_list = arcade.SpriteList()

            
        def increment_wave_timer(self):
            if self.wave_counter % 100 == 0:
                self.wave_timer -= 1
            self.wave_counter += 1

            if self.death_num == 8:
                self.wave_timer = 10
                self.wave_counter = 0
                self.start_wave = False
            elif self.death_num == 18:
                self.wave_timer = 10
                self.wave_counter = 0
                self.start_wave = False
            elif self.death_num == 30:
                self.wave_timer = 10
                self.wave_counter = 0
                self.start_wave = False
            elif self.death_num == 40:
                self.wave_timer = 10
                self.wave_counter = 0
                self.start_wave = False
            elif self.death_num == 50:
                self.wave_timer = 10
                self.wave_counter = 0
                self.start_wave = False


        def draw_tower_menu(self):

            if self.tower_menu == False:
                arcade.draw_texture_rectangle(SCREEN_W/2, SCREEN_H-15, 960, 35, self.min_tower_menu) #35 is height of the image
            elif self.tower_menu == True and self.select_tower == False and self.select_tower_type == 0:
                arcade.draw_texture_rectangle(SCREEN_W/2, SCREEN_H-15, 960, 300, self.max_tower_menu) #35 is height of the image
                arcade.draw_texture_rectangle(SCREEN_W/5, SCREEN_H-50, 41, 32, self.buy_fire_trap)
                arcade.draw_texture_rectangle(SCREEN_W/3, SCREEN_H-50, 57, 61, self.buy_fireball_tower)
                arcade.draw_texture_rectangle((SCREEN_W/3) * 1.5, SCREEN_H-50, 49, 61, self.buy_rock_tower)
                arcade.draw_texture_rectangle((SCREEN_W / 3) * 2, SCREEN_H - 50, 57, 65, self.buy_ironball_tower)
                arcade.draw_texture_rectangle((SCREEN_W / 3) * 2.5, SCREEN_H - 50, 57, 65, self.buy_stone_tower)
                if (self.mouse_x < 210 and self.mouse_y >= 175) and (self.mouse_y < 775 and self.mouse_y >= 720):
                    arcade.draw_text("Fire Trap", SCREEN_W / 3, SCREEN_H - 150, arcade.color.RED_DEVIL, 35,
                                     font_name='arial')
                    arcade.draw_text("D: 15\nRS -5\n$50", 220, 725, arcade.color.BLACK, 16, anchor_y="bottom")
                elif (self.mouse_x < 350 and self.mouse_x >= 295) and (self.mouse_y < 775 and self.mouse_y >= 720):
                    arcade.draw_text("Fire Tower", SCREEN_W/3, SCREEN_H-150, arcade.color.RED_BROWN, 35, font_name='arial')
                    arcade.draw_text("D: 100\nR: 300\n$450", 365, 725, arcade.color.BLACK, 16, anchor_y="bottom")
                elif (self.mouse_x < 500 and self.mouse_x >= 460) and (self.mouse_y < 775 and self.mouse_y >= 720):
                    arcade.draw_text("Rock Tower", SCREEN_W / 3, SCREEN_H - 150, arcade.color.BROWN_NOSE, 35,
                                     font_name='arial')
                    arcade.draw_text("D: 20\nR: 150\n$35", 520, 725, arcade.color.BLACK, 16, anchor_y="bottom")
                elif (self.mouse_x < 750 and self.mouse_x >= 615) and (self.mouse_y < 775 and self.mouse_y >= 720):
                    arcade.draw_text("Iron Tower", SCREEN_W / 3, SCREEN_H - 150, arcade.color.SILVER_LAKE_BLUE, 35,
                                     font_name='arial')
                    arcade.draw_text("D: 50\nR: 100\n$50", 675, 725, arcade.color.BLACK, 16, anchor_y="bottom")
                elif (self.mouse_x < 825 and self.mouse_x >= 775) and (self.mouse_y < 775 and self.mouse_y >= 720):
                    arcade.draw_text("Stone Tower", SCREEN_W / 3, SCREEN_H - 150, arcade.color.GRAY_BLUE, 35,
                                     font_name='arial')
                    arcade.draw_text("D: 35\nR: 300\n$100", 835, 725, arcade.color.BLACK, 16, anchor_y="bottom")
            elif self.tower_menu == True and self.select_tower == True and self.select_tower_type == 1: #selecting firetower
                arcade.draw_texture_rectangle(SCREEN_W / 2, SCREEN_H - 15, 960, 300,
                                              self.max_tower_menu)  # 35 is height of the image
                arcade.draw_texture_rectangle(SCREEN_W/5, SCREEN_H-50, 41, 32, self.buy_fire_trap, alpha=100)
                arcade.draw_texture_rectangle(SCREEN_W / 3, SCREEN_H - 50, 57, 61, self.buy_fireball_tower)
                arcade.draw_texture_rectangle((SCREEN_W / 3) * 1.5, SCREEN_H - 50, 49, 61, self.buy_rock_tower)
                arcade.draw_rectangle_filled(self.mouse_x, self.mouse_y, 50,50, [192, 192, 192, 100])
                arcade.draw_texture_rectangle(self.mouse_x, self.mouse_y, 50, 50, self.buy_fire_trap, alpha=75 )
                arcade.draw_texture_rectangle((SCREEN_W / 3) * 2, SCREEN_H - 50, 57, 65, self.buy_ironball_tower)
                arcade.draw_texture_rectangle((SCREEN_W / 3) * 2.5, SCREEN_H - 50, 57, 65, self.buy_stone_tower)
            elif self.tower_menu == True and self.select_tower == True and self.select_tower_type == 2: #selecting firetower
                arcade.draw_texture_rectangle(SCREEN_W / 2, SCREEN_H - 15, 960, 300,
                                              self.max_tower_menu)  # 35 is height of the image
                arcade.draw_texture_rectangle(SCREEN_W/5, SCREEN_H-50, 41, 32, self.buy_fire_trap)
                arcade.draw_texture_rectangle(SCREEN_W / 3, SCREEN_H - 50, 57, 61, self.buy_fireball_tower, alpha=100)
                arcade.draw_texture_rectangle((SCREEN_W / 3) * 1.5, SCREEN_H - 50, 49, 61, self.buy_rock_tower)
                arcade.draw_circle_filled(self.mouse_x, self.mouse_y, 300, [192, 192, 192, 100])
                arcade.draw_texture_rectangle(self.mouse_x, self.mouse_y, 50, 50, self.buy_fireball_tower, alpha=75 )
                arcade.draw_texture_rectangle((SCREEN_W / 3) * 2, SCREEN_H - 50, 57, 65, self.buy_ironball_tower)
                arcade.draw_texture_rectangle((SCREEN_W / 3) * 2.5, SCREEN_H - 50, 57, 65, self.buy_stone_tower)
            elif self.tower_menu == True and self.select_tower == True and self.select_tower_type == 3:
                arcade.draw_texture_rectangle(SCREEN_W / 2, SCREEN_H - 15, 960, 300,
                                              self.max_tower_menu)  # 35 is height of the image
                arcade.draw_texture_rectangle(SCREEN_W/5, SCREEN_H-50, 41, 32, self.buy_fire_trap)
                arcade.draw_texture_rectangle(SCREEN_W / 3, SCREEN_H - 50, 57, 61, self.buy_fireball_tower)
                arcade.draw_texture_rectangle((SCREEN_W / 3) * 1.5, SCREEN_H - 50, 49, 61, self.buy_rock_tower, alpha=100)
                arcade.draw_circle_filled(self.mouse_x, self.mouse_y, 150, [192, 192, 192, 100])
                arcade.draw_texture_rectangle(self.mouse_x, self.mouse_y, 50, 50, self.buy_rock_tower, alpha=75 )
                arcade.draw_texture_rectangle((SCREEN_W / 3) * 2, SCREEN_H - 50, 57, 65, self.buy_ironball_tower)
                arcade.draw_texture_rectangle((SCREEN_W / 3) * 2.5, SCREEN_H - 50, 57, 65, self.buy_stone_tower)
            elif self.tower_menu == True and self.select_tower == True and self.select_tower_type == 4:
                arcade.draw_texture_rectangle(SCREEN_W / 2, SCREEN_H - 15, 960, 300,
                                              self.max_tower_menu)  # 35 is height of the image
                arcade.draw_texture_rectangle(SCREEN_W/5, SCREEN_H-50, 41, 32, self.buy_fire_trap)
                arcade.draw_texture_rectangle(SCREEN_W / 3, SCREEN_H - 50, 57, 61, self.buy_fireball_tower)
                arcade.draw_texture_rectangle((SCREEN_W / 3) * 1.5, SCREEN_H - 50, 49, 61, self.buy_rock_tower)
                arcade.draw_circle_filled(self.mouse_x, self.mouse_y, 100, [192, 192, 192, 100])
                arcade.draw_texture_rectangle(self.mouse_x, self.mouse_y, 50, 50, self.buy_ironball_tower, alpha=100)
                arcade.draw_texture_rectangle((SCREEN_W / 3) * 2, SCREEN_H - 50, 57, 65, self.buy_ironball_tower, alpha=75)
                arcade.draw_texture_rectangle((SCREEN_W / 3) * 2.5, SCREEN_H - 50, 57, 65, self.buy_stone_tower)
            elif self.tower_menu == True and self.select_tower == True and self.select_tower_type == 5:
                arcade.draw_texture_rectangle(SCREEN_W / 2, SCREEN_H - 15, 960, 300,
                                              self.max_tower_menu)  # 35 is height of the image
                arcade.draw_texture_rectangle(SCREEN_W/5, SCREEN_H-50, 41, 32, self.buy_fire_trap)
                arcade.draw_texture_rectangle(SCREEN_W / 3, SCREEN_H - 50, 57, 61, self.buy_fireball_tower)
                arcade.draw_texture_rectangle((SCREEN_W / 3) * 1.5, SCREEN_H - 50, 49, 61, self.buy_rock_tower)
                arcade.draw_circle_filled(self.mouse_x, self.mouse_y, 300, [192, 192, 192, 100])
                arcade.draw_texture_rectangle(self.mouse_x, self.mouse_y, 50, 50, self.buy_stone_tower, alpha=100)
                arcade.draw_texture_rectangle((SCREEN_W / 3) * 2, SCREEN_H - 50, 57, 65, self.buy_ironball_tower)
                arcade.draw_texture_rectangle((SCREEN_W / 3) * 2.5, SCREEN_H - 50, 57, 65, self.buy_stone_tower, alpha=75)

            else:
                arcade.draw_texture_rectangle(SCREEN_W / 2, SCREEN_H - 15, 960, 300,
                                              self.max_tower_menu)  # 35 is height of the image
                arcade.draw_texture_rectangle(SCREEN_W/5, SCREEN_H-50, 41, 32, self.buy_fire_trap)
                arcade.draw_texture_rectangle(SCREEN_W / 3, SCREEN_H - 50, 57, 61, self.buy_fireball_tower)
                arcade.draw_texture_rectangle((SCREEN_W / 3) * 1.5, SCREEN_H - 50, 49, 61, self.buy_rock_tower)
                arcade.draw_texture_rectangle((SCREEN_W / 3) * 2, SCREEN_H - 50, 57, 65, self.buy_ironball_tower)
                arcade.draw_texture_rectangle((SCREEN_W / 3) * 2.5, SCREEN_H - 50, 57, 65, self.buy_stone_tower)
                if (self.mouse_x < 210 and self.mouse_y >= 175) and (self.mouse_y < 775 and self.mouse_y >= 720):
                    arcade.draw_text("Fire Trap", SCREEN_W / 3, SCREEN_H - 150, arcade.color.RED_DEVIL, 35,
                                     font_name='arial')
                    arcade.draw_text("D: 15\nRS -5\n$50", 220, 725, arcade.color.BLACK, 16, anchor_y="bottom")
                elif (self.mouse_x < 350 and self.mouse_x >= 295) and (self.mouse_y < 775 and self.mouse_y >= 720):
                    arcade.draw_text("Fire Tower", SCREEN_W / 3, SCREEN_H - 150, arcade.color.RED_BROWN, 35,
                                     font_name='arial')
                    arcade.draw_text("D: 100\nR: 300\n$450", 365, 725, arcade.color.BLACK, 16, anchor_y="bottom")
                elif (self.mouse_x < 500 and self.mouse_x >= 460) and (self.mouse_y < 775 and self.mouse_y >= 720):
                    arcade.draw_text("Rock Tower", SCREEN_W / 3, SCREEN_H - 150, arcade.color.BROWN_NOSE, 35,
                                     font_name='arial')
                    arcade.draw_text("D: 20\nR: 150\n$35", 520, 725, arcade.color.BLACK, 16, anchor_y="bottom")
                elif (self.mouse_x < 750 and self.mouse_x >= 615) and (self.mouse_y < 775 and self.mouse_y >= 720):
                    arcade.draw_text("Iron Tower", SCREEN_W / 3, SCREEN_H - 150, arcade.color.SILVER_LAKE_BLUE, 35,
                                     font_name='arial')
                    arcade.draw_text("D: 50\nR: 100\n$50", 675, 725, arcade.color.BLACK, 16, anchor_y="bottom")
                elif (self.mouse_x < 825 and self.mouse_x >= 775) and (self.mouse_y < 775 and self.mouse_y >= 720):
                    arcade.draw_text("Stone Tower", SCREEN_W / 3, SCREEN_H - 150, arcade.color.GRAY_BLUE, 35,
                                     font_name='arial')
                    arcade.draw_text("D: 35\nR: 300\n$100", 835, 725, arcade.color.BLACK, 16, anchor_y="bottom")
        def draw_base_health(self):
            arcade.draw_rectangle_filled(875, 300, self.base_health, 10, arcade.color.RED_DEVIL)
            arcade.draw_rectangle_outline(875, 300, 100, 10, arcade.color.BLACK)
            pass

        def draw_wave_count_down_time(self):
            wave = "Wave Start: " + str(self.wave_timer)
            if self.wave_timer <= 0:
                self.timer = arcade.draw_text(str("Wave Start!"), SCREEN_W, 0, arcade.color.RADICAL_RED, font_size=28, font_name="arial", anchor_y="bottom", anchor_x="right")
                self.start_wave = True
            else:
                self.timer = arcade.draw_text(str(wave), SCREEN_W, 0, arcade.color.BANANA_YELLOW, font_size=25, font_name="arial", anchor_y="bottom", anchor_x="right")

        def spawn_enemies(self, type):
            if type == 1:
                    self.spawn_e = gameDt.BatEnemy(1.25, 0, 65, 2, 32, 32, 100)
                    self.spawn_e.move("right")
                    gameDt.enemy_list.append(self.spawn_e)
            elif type == 2:
                    self.spawn_e = gameDt.HorseEnemy(1, 0, 65, 3, 64, 64, 200)
                    self.spawn_e.move("right")
                    gameDt.enemy_list.append(self.spawn_e)
            elif type == 3:
                    self.spawn_e = gameDt.SpiderEnemy(1, 0, 65, 3.5, 64, 64, 350)
                    self.spawn_e.move("right")
                    gameDt.enemy_list.append(self.spawn_e)
            pass

        def draw_currency(self):
            arcade.draw_text("Sacagaweas: $" + str(self.curreny), SCREEN_W, 25, arcade.color.CHROME_YELLOW, font_size=20, anchor_y="bottom", anchor_x="right")
            if self.buy_status == False:
                arcade.draw_texture_rectangle(SCREEN_W / 2, 20, 300, 50, self.buy_err)




        def tower_collision(self, sprite: arcade.Sprite, list2: arcade.SpriteList):
                for counter in list2:
                    check_bound = ((sprite.center_x - counter.center_x) ** 2) + ((sprite.center_y - counter.center_y )** 2) <=  (50 ** 2)

                    if check_bound == True:
                        return sprite
                return None

def main():
    """Main method"""
    window = AracdeWindow(SCREEN_W, SCREEN_H, SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == '__main__':
    main()