import math
import cocos
from cocos.actions import *
import cocos.euclid as eu
import cocos.collision_model as cm
import pyglet


class Ball(cocos.sprite.Sprite):
    TURN_SPEED = 5

    def __init__(self, image, position=(0, 0), rotation=0, scale=1, opacity=255, color=(255, 255, 255), anchor=None):
        super(Ball, self).__init__(image, position, rotation, scale, opacity, color, anchor)
        self.speed = 150
        self.position = eu.Vector2(position[0], position[1])
        self.direction = eu.Vector2(0, 1)
        self.radius = 32.0
        self.turn = 0
        self.rotate_action = None

    def move(self, move_by):
        angle = math.atan2(self.direction.x, self.direction.y)
        angle += move_by
        move_y = math.cos(angle)
        move_x = math.sin(angle)
        self.direction = eu.Vector2(move_x, move_y)

    def move_left(self):
        self.turn = -Ball.TURN_SPEED

    def move_right(self):
        self.turn = Ball.TURN_SPEED

    def stop_turn(self):
        self.turn = 0


class BallWorld(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self):
        super(BallWorld, self).__init__()
        self.ball = Ball('ball.png', position=(320.0, 240.0))
        self.add(self.ball)
        other_ball = Ball('ball.png', position=(420, 240))
        self.add(other_ball)

        self.balls = []
        self.balls.append(self.ball)
        self.balls.append(other_ball)

        self.keys_pressed = set()
        self.debug_label = self.build_debug_label()
        self.add(self.debug_label)
        self.schedule(self.run_update)

    def on_key_press(self, key, modifiers):
        if key == pyglet.window.key.LEFT:
            self.ball.move_left()
        elif key == pyglet.window.key.RIGHT:
            self.ball.move_right()

    def on_key_release(self, key, modifiers):
        self.ball.stop_turn()

    def run_update(self, dt):
        if dt == 0:
            return
        for ball in self.balls:
            print ball.direction
            ball.move(ball.turn * dt)
            move = ball.direction * (ball.speed * dt)
            old_pos = ball.position
            ball.position = ball.position + move
            ball.cshape = cm.CircleShape(ball.position, ball.radius)
            if not ball.cshape.fits_in_box((0.0, 640.0, 0.0, 480.0)):
                if (ball.position[0] - ball.radius) <= 0:
                    ball.direction = ball.direction.reflect(eu.Vector2(1, 0))
                if (ball.position[0] + ball.radius) >= 640:
                    ball.direction = ball.direction.reflect(eu.Vector2(1, 0))
                if (ball.position[1] - ball.radius) <= 0:
                    ball.direction = ball.direction.reflect(eu.Vector2(0, 1))
                if (ball.position[1] + ball.radius) >= 480:
                    ball.direction = ball.direction.reflect(eu.Vector2(0, 1))
                ball.position = old_pos

        self.debug_label.element.text = 'FPS: {0}'.format(str(1.0 / dt))

    def build_debug_label(self):
        label = cocos.text.Label('FPS: 0', font_size=14)
        label.position = 0, 0
        return label


if __name__ == "__main__":
    cocos.director.director.init()
    main_layer = BallWorld()
    main_scene = cocos.scene.Scene(main_layer)
    cocos.director.director.run(main_scene)
