import arcade
import pathlib
import random
import main
import os
import math
from pathfinding import *


"""Global Variables"""
image_location = pathlib.Path.cwd() / 'images'
sound_loction = pathlib.Path.cwd() / 'sounds'

launch_sound_1 = arcade.load_sound(str(sound_loction) + "/launch1.wav")
launch_sound_2 = arcade.load_sound(str(sound_loction) + "/launch2.wav")
launch_sound_3 = arcade.load_sound(str(sound_loction) + "/launch3.wav")
launch_sound_4 = arcade.load_sound(str(sound_loction) + "/launch4.wav")

enemy_list = arcade.SpriteList()
tower_list = arcade.SpriteList()
bullet_list = arcade.SpriteList()
explosion_list = arcade.SpriteList()
traps_list = arcade.SpriteList()

#All Towers, Projectile and Explosinos assests by Chisel Mark
#https://www.dafont.com/chisel-mark.font

class Projectial(arcade.Sprite):
    def __init__(self, scale, x_pos, y_pos, imageFileName, angle):
        super().__init__(scale = scale, center_x=x_pos, center_y=y_pos, filename=imageFileName)
        self.angle = angle
        self.position_adjust = True

class Fireball(Projectial):
    def __init__(self, x_pos, y_pos, angle):
        super().__init__(0.5, x_pos, y_pos, str(image_location) + "/fireball/0.png", angle)

class Ironball(Projectial):
    def __init__(self, x_pos, y_pos, angle):
        super().__init__(0.5, x_pos, y_pos, str(image_location) + "/ironball/0.png", angle)

class Stone(Projectial):
    def __init__(self, x_pos, y_pos, angle):
        super().__init__(0.5, x_pos, y_pos, str(image_location) + "/stone/0.png", angle)

class Rock(Projectial):
    def __init__(self, x_pos, y_pos, angle):
        super().__init__(0.5, x_pos, y_pos, str(image_location) + "/rock/0.png", angle)

class Tower(arcade.Sprite):
    def __init__(self, scale, x_pos, y_pos, frame_delay, firing_speed, firing_delay ,imageFileName):
        super().__init__(scale=scale,center_x=x_pos, center_y=y_pos)
        self.image_location = imageFileName
        self.frame_delay = frame_delay
        self.dest_angle = None
        self.bullet_speed = firing_speed
        self.firing_delay = firing_delay
        self.counter = 0
        self.current_frame = 0
        self.range = 0
        self.attack = 0
        self.textures = None
        self.closest_enemy = None
        self.able_shoot = False
        self.setup()
        self.establish()

    def setup(self):
        textures = []
        files = os.listdir(self.image_location)
        for x in range(len(files)):
            frame = arcade.load_texture(str(self.image_location) + "/" +str(x) + ".png") #.glob function randomly assorts the files
            textures.append(frame)
            if len(textures) == 0:
                self.texture = frame
        self.textures = textures

    def update(self):
        if self.counter % self.frame_delay == 0:
            if self.current_frame < len(self.textures):
                self.set_texture(self.current_frame)
            else:
                self.set_texture(0)
            self.current_frame += 1
        self.counter +=1
        self.position()
        self.shoot()


    def reset(self):
        self.counter = 0
        self.current_frame = 0

    def position(self):
        if len(enemy_list) == 0:
            pass
        else:
            self.check_shoot()

            if self.closest_enemy is None:
                pass
            else:
                enemy_x = self.closest_enemy.center_x
                enemy_y = self.closest_enemy.center_y
                x_offset = enemy_x - self.center_x
                y_offset = enemy_y - self.center_y
                self.dest_angle = math.atan2(y_offset, x_offset)
                self.angle = math.degrees(self.dest_angle) - 90 # 180 is the offset to correctly position the top to the target; different per tower

    def check_shoot(self):
        for x in range(len(enemy_list)):

            check_bound = ((enemy_list[x].center_x - self.center_x) ** 2) + ((enemy_list[x].center_y - self.center_y ) ** 2) <= (self.range)**2
            if check_bound:
                self.closest_enemy = enemy_list[x]
                self.able_shoot = True

    def shoot(self):
        if self.able_shoot and self.counter % self.firing_delay == 0:
            self.able_shoot = False
            self.reset()
            bul_angle = self.angle - 180 # 180 is th offset angle
            bullet = Projectial(0.5, self.center_x, self.center_y, str(image_location) + "/fireball/0.png", bul_angle)
            bullet.change_x = math.cos(self.dest_angle) * self.bullet_speed
            bullet.change_y = math.sin(self.dest_angle) * self.bullet_speed
            bullet_list.append(bullet)



    def establish(self):
        pass

class Fire_Tower(Tower):
    def shoot(self):
        if self.able_shoot and self.counter % self.firing_delay == 0:
            self.able_shoot = False
            self.reset()
            arcade.play_sound(launch_sound_1)
            bul_angle = self.angle - 180 # 180 is th offset angle
            bullet = Fireball(self.center_x, self.center_y, bul_angle)
            bullet.change_x = math.cos(self.dest_angle) * self.bullet_speed
            bullet.change_y = math.sin(self.dest_angle) * self.bullet_speed
            bullet_list.append(bullet)

    def establish(self):
        self.range = 350
        self.attack = 5

class Rock_Tower(Tower):
    def shoot(self):
        if self.able_shoot and self.counter % self.firing_delay == 0:
            self.able_shoot = False
            self.reset()
            arcade.play_sound(launch_sound_2)
            bul_angle = self.angle - 180  # 180 is th offset angle
            bullet = Rock(self.center_x,self.center_y, bul_angle)
            bullet.change_x = math.cos(self.dest_angle) * self.bullet_speed
            bullet.change_y = math.sin(self.dest_angle) * self.bullet_speed
            bullet_list.append(bullet)

    def establish(self):
        self.range = 150
        self.attack = 3

class Iron_Tower(Tower):
    def shoot(self):
        if self.able_shoot and self.counter % self.firing_delay == 0:
            self.able_shoot = False
            self.reset()
            arcade.play_sound(launch_sound_3)
            bul_angle = self.angle - 180  # 180 is th offset angle
            bullet = Ironball(self.center_x, self.center_y, bul_angle)
            bullet.change_x = math.cos(self.dest_angle) * self.bullet_speed
            bullet.change_y = math.sin(self.dest_angle) * self.bullet_speed
            bullet_list.append(bullet)

    def establish(self):
        self.range = 100
        self.attack = 3

class Stone_Tower(Tower):
    def shoot(self):
        if self.able_shoot and self.counter % self.firing_delay == 0:
            self.able_shoot = False
            self.reset()
            arcade.play_sound(launch_sound_4)
            bul_angle = self.angle - 180  # 180 is th offset angle
            bullet = Stone(self.center_x, self.center_y, bul_angle)
            bullet.change_x = math.cos(self.dest_angle) * self.bullet_speed
            bullet.change_y = math.sin(self.dest_angle) * self.bullet_speed
            bullet_list.append(bullet)

    def establish(self):
        self.range = 300
        self.attack = 3

class Explosions(arcade.Sprite):
    def __init__(self, scale, x_pos, y_pos, frame_delay):
        super().__init__(scale=scale, center_x=x_pos, center_y=y_pos)
        self.frame_delay = frame_delay
        self.counter = 0
        self.current_frame = 0
        self.textures = None
        self.i_path = None
        self.setup()


    def setup(self):
        self.i_path = pathlib.Path.cwd() / 'images' / 'fireball'
        textures = []
        pathFiles = pathlib.Path(self.i_path).glob("*.png")
        filesList = [x for x in pathFiles if x.is_file()]
        files = len(filesList)
        for x in range(files):
            frame = arcade.load_texture(str(self.i_path) + "/" +str(x) + ".png") #.glob function randomly assorts the files
            textures.append(frame)
            if len(textures) == 0:
                self.texture = frame
        self.textures = textures

    def update(self):
        if self.counter % self.frame_delay == 0:
            if self.current_frame < len(self.textures):
                self.set_texture(self.current_frame)
            else:
                self.kill()
            self.current_frame += 1
        self.counter +=1

class Rock_Explosion(Explosions):
    def setup(self):
        self.i_path = pathlib.Path.cwd() / 'images' / 'rock'
        textures = []
        pathFiles = pathlib.Path(self.i_path).glob("*.png")
        filesList = [x for x in pathFiles if x.is_file()]
        files = len(filesList)
        for x in range(files):
            frame = arcade.load_texture(
                str(self.i_path) + "/" + str(x) + ".png")  # .glob function randomly assorts the files
            textures.append(frame)
            if len(textures) == 0:
                self.texture = frame
        self.textures = textures

class Ironball_Explosion(Explosions):
    def setup(self):
        self.i_path = pathlib.Path.cwd() / 'images' / 'ironball'
        textures = []
        pathFiles = pathlib.Path(self.i_path).glob("*.png")
        filesList = [x for x in pathFiles if x.is_file()]
        files = len(filesList)
        for x in range(files):
            frame = arcade.load_texture(
                str(self.i_path) + "/" + str(x) + ".png")  # .glob function randomly assorts the files
            textures.append(frame)
            if len(textures) == 0:
                self.texture = frame
        self.textures = textures

class Stone_Explosion(Explosions):
    def setup(self):
        self.i_path = pathlib.Path.cwd() / 'images' / 'stone'
        textures = []
        pathFiles = pathlib.Path(self.i_path).glob("*.png")
        filesList = [x for x in pathFiles if x.is_file()]
        files = len(filesList)
        for x in range(files):
            frame = arcade.load_texture(
                str(self.i_path) + "/" + str(x) + ".png")  # .glob function randomly assorts the files
            textures.append(frame)
            if len(textures) == 0:
                self.texture = frame
        self.textures = textures

#Trap image is from Stealthix from itch.io

class Trap(arcade.AnimatedWalkingSprite):
    def __init__(self, scale, x_pos, y_pos, frame_speed, frameH, frameW):
        super().__init__(scale=scale, center_x=x_pos, center_y=y_pos)
        self.Frame_Height = frameH
        self.Frame_Width = frameW
        self.frame_delay = frame_speed
        self.counter = 0
        self.current_frame = 0
        self.setup()

    def setup(self):
        textures = []
        self.image_location = pathlib.Path.cwd() / 'images' / 'Fire_Trap.png'
        for x in range(14):
            frame = arcade.load_texture(str(self.image_location), self.Frame_Width*x, 0,
                                    height=self.Frame_Height,
                                    width=self.Frame_Width)
            textures.append(frame)
            if x == 0:
                self.texture = frame

        self.textures = textures

    def update(self):
        if self.counter % self.frame_delay == 0:
            if self.current_frame < len(self.textures):
                self.set_texture(self.current_frame)
            else:
                self.set_texture(0)
            self.current_frame += 1
        self.counter +=1


    def reset(self):
        self.counter = 0
        self.current_frame = 0


class Projectial(arcade.Sprite):
    def __init__(self, scale, x_pos, y_pos, imageFileName, angle):
        super().__init__(scale = scale, center_x=x_pos, center_y=y_pos, filename=imageFileName)
        self.angle = angle
        self.position_adjust = True

class Fireball(Projectial):
    def __init__(self, x_pos, y_pos, angle):
        super().__init__(0.5, x_pos, y_pos, str(image_location) + "/fireball/0.png", angle)

class Ironball(Projectial):
    def __init__(self, x_pos, y_pos, angle):
        super().__init__(0.5, x_pos, y_pos, str(image_location) + "/ironball/0.png", angle)

class Stone(Projectial):
    def __init__(self, x_pos, y_pos, angle):
        super().__init__(0.5, x_pos, y_pos, str(image_location) + "/stone/0.png", angle)

class Rock(Projectial):
    def __init__(self, x_pos, y_pos, angle):
        super().__init__(0.5, x_pos, y_pos, str(image_location) + "/rock/0.png", angle)



class Enemy(arcade.AnimatedWalkingSprite):
    def __init__(self, scale, x_pos, y_pos, speed, frameH, frameW, health, map ,end_goal):
        super().__init__(scale=scale, center_x=x_pos, center_y=y_pos)
        self.Frame_Height = frameH
        self.Frame_Width = frameW
        self.speed = speed
        self.health = health
        self.direction = None
        self.hit_trap = False
        self.nav_map = map
        self.path = None
        self.currentPos = (0,0)
        self.end_goal = end_goal
        self.setup()



    def setup(self):
        self.image_location = pathlib.Path.cwd() / 'images' / 'bat_animate.png'
        frame = arcade.load_texture(str(self.image_location), 0, self.Frame_Height * 3, height=self.Frame_Height, width=self.Frame_Height)
        self.stand_left_textures = []
        self.stand_left_textures.append(frame)

        frame = arcade.load_texture(str(self.image_location), 0, self.Frame_Width, height=self.Frame_Height, width=self.Frame_Width)
        self.stand_right_textures = []
        self.stand_right_textures.append(frame)
        self.texture = frame

        self.walk_left_textures = []
        for x in range(4):
            frame = arcade.load_texture(str(self.image_location), x * self.Frame_Width, self.Frame_Height * 3, height=self.Frame_Height,
                                        width=self.Frame_Width)
            self.walk_left_textures.append(frame)

        self.walk_right_textures = []
        for x in range(4):
            frame = arcade.load_texture(str(self.image_location), x * self.Frame_Width, self.Frame_Height * 1, height=self.Frame_Height,
                                        width=self.Frame_Width)
            self.walk_right_textures.append(frame)

        self.walk_up_textures = []
        for x in range(4):
            frame = arcade.load_texture(str(self.image_location), x * self.Frame_Width, self.Frame_Height * 2, height=self.Frame_Height,
                                        width=self.Frame_Width)
            self.walk_up_textures.append(frame)

        self.walk_down_textures = []
        for x in range(4):
            frame = arcade.load_texture(str(self.image_location), x * self.Frame_Width, 0, height=self.Frame_Height,
                                        width=self.Frame_Width)
            self.walk_down_textures.append(frame)

    def move(self, direction):
       self.direction = direction

       if (self.direction == "up"):
         self.change_y = self.speed
         self.change_x = 0
       elif (self.direction == "down"):
         self.change_y = -self.speed
         self.change_x = 0
       elif (self.direction == "right"):
         self.change_x = self.speed
         self.change_y = 0
       elif (self.direction == "left"):
         self.change_x = -self.speed
         self.change_y = 0
       else:
         self.change_x = 0
         self.change_y = 0
         print("error")

    def move_boundaries(self):

        dir = random.randint(0, 9)

        if self.top > main.SCREEN_H:
            if dir % 2 == 0:
                self.top -= 1
                self.move("right")
            else:
                self.top -= 1
                self.move("left")
        elif self.bottom < 0:
            if dir % 2 == 0:
                self.bottom += 1
                self.move("right")
            else:
                self.bottom += 1
                self.move("left")
        elif self.left < 0:
            if dir % 2 == 0:
                self.left += 1
                self.move("up")
            else:
                self.left += 1
                self.move("down")
        elif self.right > main.SCREEN_W:
            if dir % 2 == 0:
                self.right -= 1
                self.move("up")
            else:
                self.right -= 1
                self.move("down")

    def move_auto(self):
        currentPos = (round(self.center_x / 32), round(self.center_y / 40))
        if self.currentPos != currentPos:
            self.currentPos = currentPos
            came_from, cost_so_far = a_star_search(self.nav_map, currentPos, self.end_goal)
            pth = path(came_from, currentPos, self.end_goal)
            nextstep = pth[1]

            if currentPos[0] == nextstep[0]:
                if currentPos[1] < nextstep[1]:
                    self.move("up")
                else:
                    self.move("down")
            elif currentPos[0] > nextstep[0]:
                self.move("left")
            elif currentPos[0] < nextstep[0]:
                self.move("right")
        else:
            pass





        """
        dir = random.randint(0, 9)

        if self.direction == "up":
            if dir % 3 == 0:
                self.top -= 1
                self.move("left")
            elif dir % 2 == 0:
                self.top -= 1
                self.move("down")
            else:
                self.top -= 1
                self.move("right")
        elif self.direction == "down":
            if dir % 3 == 0:
                self.bottom += 1
                self.move("right")
            elif dir % 2 == 0:
                self.bottom += 1
                self.move("left")
            else:
                self.bottom += 1
                self.move("up")
        elif self.direction == "left":
            if dir % 3 == 0:
                self.left += 1
                self.move("down")
            elif dir % 2 == 0:
                self.left += 1
                self.move("right")
            else:
                self.left += 1
                self.move("up")
        elif self.direction == "right":
            if dir % 3 == 0:
                self.right -= 1
                self.move("up")
            elif dir % 2 == 0:
                self.right -= 1
                self.move("down")
            else:
                self.right -= 1
                self.move("left")
        else:
            self.move(None)#doesn't move; error
        """

#Image by bagzie from OpenGameArt.org

class BatEnemy(Enemy):
    def setup(self):
        self.image_location = pathlib.Path.cwd() / 'images' / 'bat_animate.png'
        frame = arcade.load_texture(str(self.image_location), 0, self.Frame_Height * 3, height=self.Frame_Height, width=self.Frame_Height)
        self.stand_left_textures = []
        self.stand_left_textures.append(frame)

        frame = arcade.load_texture(str(self.image_location), 0, self.Frame_Width, height=self.Frame_Height, width=self.Frame_Width)
        self.stand_right_textures = []
        self.stand_right_textures.append(frame)
        self.texture = frame

        self.walk_left_textures = []
        for x in range(4):
            frame = arcade.load_texture(str(self.image_location), x * self.Frame_Width, self.Frame_Height * 3, height=self.Frame_Height,
                                        width=self.Frame_Width)
            self.walk_left_textures.append(frame)

        self.walk_right_textures = []
        for x in range(4):
            frame = arcade.load_texture(str(self.image_location), x * self.Frame_Width, self.Frame_Height * 1, height=self.Frame_Height,
                                        width=self.Frame_Width)
            self.walk_right_textures.append(frame)

        self.walk_up_textures = []
        for x in range(4):
            frame = arcade.load_texture(str(self.image_location), x * self.Frame_Width, self.Frame_Height * 2, height=self.Frame_Height,
                                        width=self.Frame_Width)
            self.walk_up_textures.append(frame)

        self.walk_down_textures = []
        for x in range(4):
            frame = arcade.load_texture(str(self.image_location), x * self.Frame_Width, 0, height=self.Frame_Height,
                                        width=self.Frame_Width)
            self.walk_down_textures.append(frame)

#Image by bluecarrot16 from OpenGameArt.org

class HorseEnemy(Enemy):
    def setup(self):
        self.image_location = pathlib.Path.cwd() / 'images' / 'horse_animate.png'
        frame = arcade.load_texture(str(self.image_location), 0, self.Frame_Height * 3, height=self.Frame_Height, width=self.Frame_Height)
        self.stand_right_textures = []
        self.stand_right_textures.append(frame)
        self.texture = frame

        frame = arcade.load_texture(str(self.image_location), 0, self.Frame_Width, height=self.Frame_Height, width=self.Frame_Width)
        self.stand_left_textures = []
        self.stand_left_textures.append(frame)


        self.walk_right_textures = []
        for x in range(4):
            frame = arcade.load_texture(str(self.image_location), x * self.Frame_Width, self.Frame_Height * 3, height=self.Frame_Height,
                                        width=self.Frame_Width)
            self.walk_right_textures.append(frame)

        self.walk_left_textures = []
        for x in range(4):
            frame = arcade.load_texture(str(self.image_location), x * self.Frame_Width, self.Frame_Height * 1, height=self.Frame_Height,
                                        width=self.Frame_Width)
            self.walk_left_textures.append(frame)

        self.walk_down_textures = []
        for x in range(4):
            frame = arcade.load_texture(str(self.image_location), x * self.Frame_Width, self.Frame_Height * 2, height=self.Frame_Height,
                                        width=self.Frame_Width)
            self.walk_down_textures.append(frame)

        self.walk_up_textures = []
        for x in range(4):
            frame = arcade.load_texture(str(self.image_location), x * self.Frame_Width, 0, height=self.Frame_Height,
                                        width=self.Frame_Width)
            self.walk_up_textures.append(frame)

#Image by William.Thompsonj on OpenGameArt.org

class SpiderEnemy(Enemy):
    def setup(self):
        self.image_location = pathlib.Path.cwd() / 'images' / 'spider.png'
        frame = arcade.load_texture(str(self.image_location), 0, self.Frame_Height * 3, height=self.Frame_Height, width=self.Frame_Height)
        self.stand_right_textures = []
        self.stand_right_textures.append(frame)
        self.texture = frame

        frame = arcade.load_texture(str(self.image_location), 0, self.Frame_Width, height=self.Frame_Height, width=self.Frame_Width)
        self.stand_left_textures = []
        self.stand_left_textures.append(frame)


        self.walk_right_textures = []
        for x in range(10):
            frame = arcade.load_texture(str(self.image_location), x * self.Frame_Width, self.Frame_Height * 3, height=self.Frame_Height,
                                        width=self.Frame_Width)
            self.walk_right_textures.append(frame)

        self.walk_left_textures = []
        for x in range(10):
            frame = arcade.load_texture(str(self.image_location), x * self.Frame_Width, self.Frame_Height * 1, height=self.Frame_Height,
                                        width=self.Frame_Width)
            self.walk_left_textures.append(frame)

        self.walk_down_textures = []
        for x in range(10):
            frame = arcade.load_texture(str(self.image_location), x * self.Frame_Width, self.Frame_Height * 2, height=self.Frame_Height,
                                        width=self.Frame_Width)
            self.walk_down_textures.append(frame)

        self.walk_up_textures = []
        for x in range(10):
            frame = arcade.load_texture(str(self.image_location), x * self.Frame_Width, 0, height=self.Frame_Height,
                                        width=self.Frame_Width)
            self.walk_up_textures.append(frame)