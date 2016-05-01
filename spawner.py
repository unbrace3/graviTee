# Python Cocos2d Game Development
# Part 1: Getting Started

# Tutorial: http://jpwright.net/writing/python-cocos2d-game-1/
# Github: http://github.com/jpwright/cocos2d-python-tutorials

# Jason Wright (jpwright0@gmail.com)


# Imports

from random import randint

import pyglet
from pyglet.window import key

import cocos
from cocos import actions, layer, sprite, scene
from cocos.director import director


# Player class

class Me(actions.Move):
  
  # step() is called every frame.
  # dt is the number of seconds elapsed since the last call.
  totaltime=0.0
  def step(self, dt):
    
    super(Me, self).step(dt) # Run step function on the parent class.
    
    you = sprite.Sprite('ball.jpg')
    player_layer.add(you)
  
    # Set initial position and velocity.
    you.position = (0, randint(0,600))
    you.velocity = (randint(500,2000), randint(-300,300))
    you.do(You())
    
# Main class
class You(actions.Move):
    def step(self, dt):
    
        super(You, self).step(dt) # Run step function on the parent class.
    
    # Determine velocity based on keyboard inputs.
        #velocity_x = randint(0,1000)
        #velocity_y = randint(-150,150)
    
    # Set the object's velocity.
        #self.target.velocity = (velocity_x, velocity_y)
    
def main():
  global keyboard # Declare this as global so it can be accessed within class methods.
  # Initialize the window.
  director.init(width=1000, height=600, do_not_scale=True, resizable=True)
  
  # Create a layer and add a sprite to it.
  global player_layer
  player_layer = layer.Layer()
  me = sprite.Sprite('ball.jpg')
  player_layer.add(me)
  
  # Set initial position and velocity.
  me.position = (0, randint(0,600))
  me.velocity = (0, 0)
  me.visible=False
  # Set the sprite's movement class.
  me.do(Me())

  # Create a scene and set its initial layer.
  main_scene = scene.Scene(player_layer)

  # Attach a KeyStateHandler to the keyboard object.
  keyboard = key.KeyStateHandler()
  director.window.push_handlers(keyboard)

  # Play the scene in the window.
  director.run(main_scene)

if __name__ == '__main__':
    main()