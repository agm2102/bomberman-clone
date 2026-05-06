from entities.base_classes.BaseEntity import BaseEntity


class Door(BaseEntity):
    def __init__(self, x, y, sprite_manager):
        super().__init__(x, y, sprite_manager)
        self.sprite = sprite_manager.get("map")[9]
        self.visible = False
        self.locked = True

    def is_locked(self):
        return self.locked

    def set_locked(self, locked):
        self.locked =  locked

    def set_visible(self, visible):
        self.visible = visible

    def is_visible(self):
        return self.visible