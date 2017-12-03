# coding: utf-8

import scene
import motion


class MyScene (scene.Scene):
    def setup(self):
        self.label_node = scene.LabelNode('', ('Arial', 12), position=self.size*0.5, parent=self)
        motion.start_updates()
        self.orientation = '?'


    def update(self):
        x, y, z = motion.get_gravity()
        if abs(x) > abs(y):
            if x > 0:
                self.label_node.text = 'LANDSCAPE, RIGHT'
            else:
                self.label_node.text = 'LANDSCAPE, LEFT'
        else:
            if y < 0:
                self.label_node.text = 'PORTRAIT'

    def did_change_size(self):
        self.label_node.position = self.size*0.5

    def stop(self):
        motion.stop_updates()

scene.run(MyScene())