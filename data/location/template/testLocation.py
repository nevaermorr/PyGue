from machine.tile import MetaTile

#create example grid
tiles_ = [[MetaTile(i, j) for j in range(20)] for i in range(32)]

from machine.wall import *
from machine.door import *
tiles_[4][1].construction = MetaWall()
tiles_[4][2].construction = MetaWall()
tiles_[4][3].construction = MetaWall()
tiles_[4][4].construction = MetaWall()
tiles_[4][5].construction = MetaWall()
tiles_[8][1].construction = MetaWall()
tiles_[8][2].construction = MetaWall()
tiles_[8][3].construction = MetaWall()
tiles_[8][4].construction = MetaWall()
tiles_[8][5].construction = MetaWall()
tiles_[7][5].construction = MetaWall()
tiles_[6][5].construction = MetaWall()
tiles_[5][5].construction = MetaWall()

tiles_[5][1].construction = MetaDoor(True)
tiles_[6][1].construction = MetaWall()
tiles_[7][1].construction = MetaDoor(False)