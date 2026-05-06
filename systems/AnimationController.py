
class AnimationController:

    def __init__(self):
        self.animations = {}
        self.current_animation = None
        self.current_name = None

    def add_animation(self, name, animation):
        self.animations[name] = animation
        if self.current_animation is None:
            self.current_animation = animation
            self.current_name = name

    def change_current_animation(self, nome, force_change):
        if nome == self.current_name and not force_change:
            return
        if nome not in self.animations:
            return

        self.current_name = nome
        self.current_animation = self.animations[nome]
        self.current_animation.reset()

    def update(self):
        self.current_animation.update()

    def get_frame(self):
        if self.current_animation:
            return self.current_animation.get_current_frame()
        return None

    def finished(self):
        return self.current_animation.is_finished if self.current_animation else False

