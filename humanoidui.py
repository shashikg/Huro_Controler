import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Handler:
    def main_window_delete_event_cb(self, *args):
        Gtk.main_quit(*args)

    def main_window_destroy_cb(self, *args):
        Gtk.main_quit(*args)

    def forward_clicked_cb(self, *args):
        print("forward")

    def back_clicked_cb(self, *args):
        print("back")

    def left_clicked_cb(self, *args):
        print("left")

    def right_clicked_cb(self, *args):
        print("right")

    def stop_clicked_cb(self, *args):
        print("stop")

    # def main_window_destroy_cb(self, *args):
    #     Gtk.main_quit(*args)

    def line_follow_switch_state_set_cb(self, switch, gparam):
        if switch.get_active():
            state = "on"
            switchFaceRec.set_active(False)
            switchObjDetect.set_active(False)
        else:
            state = "off"
        print("line follow was turned", state)
        

    def face_rec_switch_state_set_cb(self, switch, gparam):
        if switch.get_active():
            state = "on"
            switchLineFollow.set_active(False)
            switchObjDetect.set_active(False)
        else:
            state = "off"
        print("face rec was turned", state)


    def obj_detect_switch_state_set_cb(self, switch, gparam):
        if switch.get_active():
            state = "on"
            switchFaceRec.set_active(False)
            switchLineFollow.set_active(False)
        else:
            state = "off"
        print("obj detect was turned", state)

builder = Gtk.Builder()
builder.add_from_file("humanoidui.glade")
builder.connect_signals(Handler())

window = builder.get_object("main_window")
switchLineFollow = builder.get_object("line_follow_switch")
switchFaceRec = builder.get_object("face_rec_switch")
switchObjDetect = builder.get_object("obj_detect_switch")
# switch = builder.get_object("_switch")
# switch = builder.get_object("_switch")
window.show_all()

Gtk.main()
