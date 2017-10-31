'''
    goodies.py

    Definitions for some example goodies
'''

import random

from maze import Goody, UP, DOWN, LEFT, RIGHT, STAY, PING

class StaticGoody(Goody):
    ''' A static goody - does not move from its initial position '''

    def take_turn(self, _obstruction, _ping_response):
        ''' Stay where we are '''
        return STAY

class RandomGoody(Goody):
    ''' A random-walking goody '''

    def take_turn(self, obstruction, _ping_response):
        ''' Ignore any ping information, just choose a random direction to walk in, or ping '''

        possibilities = [direction for direction in [UP, DOWN, LEFT, RIGHT] if not obstruction[direction]] + [PING]
        return random.choice(possibilities)

class TorBenGoody(Goody):
    ''' A random-walking goody '''
    
    def __init__(self):
        self.count = 0
        self.corner = None
        self.middlepoint_x = None
        self.middlepoint_y = None
        self.position_x = 0
        self.position_y = 0
        self.withinmiddlepoint = False

    def take_turn(self, obstruction, _ping_response):
        ''' Ignore any ping information, just choose a random direction to walk in, or ping '''
        
        if self.count==0 and _ping_response == None:
            self.count += 1
            return PING
        elif _ping_response != None:
            self.count += 1
            for player, position in _ping_response.items():
                if isinstance(player, Goody):
                    goody_position = position
                else:
                    baddy_position = position
            
            self.middlepoint_x = goody_position.x/2
            self.middlepoint_y = goody_position.y/2
            
            if goody_position.y/2<baddy_position.y:
                if goody_position.x/2<baddy_position.x:
                    self.corner = 'bottomleft'
                else:
                    self.corner = 'bottomright'
            else:
                if goody_position.x/2<baddy_position.x:
                    self.corner = 'topleft'
                else:
                    self.corner = 'topright'
        
        '''Check whether goody has reached meeting area, if not, proceed there, o/w go to side'''
        if abs(self.middlepoint_x-self.position_x)**2+abs(self.middlepoint_y-self.position_y)**2<2:
            self.withinmiddlepoint = True
        
        
        if self.withinmiddlepoint == False:
            u = random.uniform(0,1)
            if u<0.7:
                u = u/0.7
                if u < abs(self.middlepoint_x-self.position_x)/(abs(self.middlepoint_x-self.position_x)+abs(self.middlepoint_y-self.position_y)):
                    if self.middlepoint_x-self.position_x > 0 and not obstruction[RIGHT]:
                        self.position_x += 1
                        return RIGHT
                    elif not obstruction[LEFT]:
                        self.position_x -= 1
                        return LEFT
                else:
                    if self.middlepoint_y-self.position_y > 0 and not obstruction[UP]:
                        self.position_y += 1
                        return UP
                    elif not obstruction[DOWN]:
                        self.position_y -= 1
                        return DOWN   
                        
        
        if self.withinmiddlepoint == True:           
            if self.corner == 'bottomleft':
                possibilities = [direction for direction in [LEFT, DOWN, UP, DOWN, LEFT, RIGHT] if not obstruction[direction]] 
                return random.choice(possibilities)
            elif self.corner == 'topleft':
                possibilities = [direction for direction in [LEFT, UP, UP, DOWN, LEFT, RIGHT] if not obstruction[direction]] 
                return random.choice(possibilities)
            elif self.corner == 'bottomright':
                possibilities = [direction for direction in [RIGHT, DOWN, UP, DOWN, LEFT, RIGHT] if not obstruction[direction]] 
                return random.choice(possibilities)
            else:
                possibilities = [direction for direction in [RIGHT, UP, UP, DOWN, LEFT, RIGHT] if not obstruction[direction]] 
                return random.choice(possibilities)
        
        
        '''Every now and then we get here and just do a random move'''
        possibilities = [direction for direction in [UP, DOWN, LEFT, RIGHT] if not obstruction[direction]] 
        return random.choice(possibilities)


class TorBenGoody2(Goody):
    ''' A random-walking goody '''
    
    def __init__(self):
        self.count = 0
        self.corner = None
        self.middlepoint_x = None
        self.middlepoint_y = None
        self.position_x = 0
        self.position_y = 0
        self.withinmiddlepoint = False

    def take_turn(self, obstruction, _ping_response):
        ''' Ignore any ping information, just choose a random direction to walk in, or ping '''
        
        if self.count==0 and _ping_response == None:
            self.count += 1
            return PING
        elif _ping_response != None:
            self.count += 1
            for player, position in _ping_response.items():
                if isinstance(player, Goody):
                    goody_position = position
                else:
                    baddy_position = position
            
            self.middlepoint_x = goody_position.x/2
            self.middlepoint_y = goody_position.y/2
            
            if abs(goody_position.x/2-baddy_position.x)>abs(goody_position.y/2-baddy_position.y):
                if goody_position.x/2<baddy_position.x:
                    self.corner = 'left'
                else:
                    self.corner = 'right'
            else:
                if goody_position.y/2<baddy_position.y:
                    self.corner = 'bottom'
                else:
                    self.corner = 'top'
        
        '''Check whether Goody has reached meeting area, if not, go there, o/w go to side'''
        if abs(self.middlepoint_x-self.position_x)**2+abs(self.middlepoint_y-self.position_y)**2<2:
            self.withinmiddlepoint = True
        else:
            self.withinmiddlepoint = False
        
        
        if self.withinmiddlepoint == False:
            u = random.uniform(0,1)
            if u<0.7:
                u = u/0.7
                if u < abs(self.middlepoint_x-self.position_x)/(abs(self.middlepoint_x-self.position_x)+abs(self.middlepoint_y-self.position_y)):
                    if self.middlepoint_x-self.position_x > 0 and not obstruction[RIGHT]:
                        self.position_x += 1
                        return RIGHT
                    elif not obstruction[LEFT]:
                        self.position_x -= 1
                        return LEFT
                else:
                    if self.middlepoint_y-self.position_y > 0 and not obstruction[UP]:
                        self.position_y += 1
                        return UP
                    elif not obstruction[DOWN]:
                        self.position_y -= 1
                        return DOWN   
                        
        
        '''Whenever we are in the meetingarea just do a random move'''
        possibilities = [direction for direction in [UP, DOWN, LEFT, RIGHT] if not obstruction[direction]]
        dir = random.choice(possibilities)
        if dir == UP:
            self.position_y += 1
        elif dir == DOWN:
            self.position_y -= 1
        elif dir == LEFT:
            self.position_x -= 1
        elif dir == RIGHT:
            self.position_x += 1
        return dir