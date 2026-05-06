
class Animation:
    def __init__(self, frame_list, speed_ani, is_looping):
        self.frame_list = frame_list
        self.current_frame = 0
        self.tickAni = 0
        self.speed_ani = speed_ani
        self.is_looping = is_looping
        self.is_finished = False

    def update(self):

        if self.is_finished:
            return
        self.tickAni += 1
        if self.tickAni > self.speed_ani:
            self.tickAni = 0
            self.current_frame += 1

            if self.current_frame >= len(self.frame_list):
                if self.is_looping:
                    self.current_frame = 0
                else:
                    self.current_frame = len(self.frame_list) - 1
                    self.is_finished = True

    def get_current_frame(self):
        return self.frame_list[self.current_frame]

    def reset(self):
        self.current_frame = 0
        self.tickAni = 0
        self.is_finished = False
