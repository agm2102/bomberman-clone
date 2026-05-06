from entities.base_classes.BaseEntity import BaseEntity
from systems.Animation import Animation
class Block(BaseEntity):
    def __init__(self, x, y, sprite, solid, breakable, sprite_manager):
        super().__init__(x, y, sprite_manager)
        self.sprite = sprite
        self.solid = solid
        self.breakable = breakable
        self.is_destroyed = False

        self.destroy = False
        self.door = None

        self.has_item = False
        self.item = None

        self.frames = sprite_manager.get("map")
        self.animation_controller.add_animation("destroying_breakable_block", Animation(self.frames[3:9], 8, False))

    def update(self):

        if self.destroy:
            self.animation_controller.update()
            self.sprite = self.animation_controller.get_frame()

        if self.animation_controller.finished():
            self.is_destroyed = True

    def draw(self, screen):
        screen.blit(self.sprite, (self.x, self.y))

    def is_solid(self):
        return self.solid

    def is_breakable(self):
        return self.breakable

    def set_destroy(self):
        if self.door is not None :
            self.door.set_visible(True)

        if self.item is not None:
            self.item.set_visible(True)

        self.destroy = True

    def get_is_destroyed(self):
        return self.is_destroyed

    def get_door(self):
        return self.door

    def set_door(self, door):
        self.door = door