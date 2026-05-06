from entities.base_classes.BaseEntity import BaseEntity

class Item(BaseEntity):
    def __init__(self, x, y, sprite_manager, type_item):
        super().__init__(x, y, sprite_manager)
        self.type = type_item
        self.sprite = sprite_manager.get("item")[type_item]
        self.visible = False
        self.collected = False

    def set_visible(self, visible):
        self.visible = visible

    def is_visible(self):
        return self.visible

    def get_type(self):
        return self.type

    def is_collected(self):
        return self.collected

    def set_collected(self, collected):
        self.collected = collected