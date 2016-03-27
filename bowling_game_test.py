#!/usr/bin/env python

import unittest

from bowling_game import Game

class BowlingGameTest(unittest.TestCase):


  def test_gutter_game(self):
    g = Game()
    for roll in range(0,20):
      g.roll(0)
    self.assertEquals(g.score(),0)

  def test_all_ones(self):
    g = Game()
    for roll in range(0,20):
      g.roll(1)
    self.assertEquals(g.score(),20)

if __name__ == '__main__':
    unittest.main()
