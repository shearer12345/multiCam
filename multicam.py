'''
sudo add-apt-repository ppa:gijzelaar/opencv2.4
sudo add-apt-repository ppa:kivy-team/kivy-daily 
sudo apt-get update

sudo apt-get install libopencv-core2.4 libopencv-highgui2.4 libopencv-legacy2.4 libopencv-video2.4 libopencv-videostab2.4
sudo apt-get install python-kivy python-opencv
'''

import kivy
kivy.require('1.2.0')
kivy.kivy_options['camera'] = 'opencv'


from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.camera import Camera

class TestApp(App):

    def build(self):

        res = (640,480)
        layout = GridLayout(rows=2, cols=2, padding=0)
	print layout.width
        for i in range(1,5):	
            try:
                layout.add_widget(Camera(index=i, resolution=res))
            except:
                print 'Camera with index ' + str(i) + ' failed to start'
        return layout

if __name__ == '__main__':
    TestApp().run()
