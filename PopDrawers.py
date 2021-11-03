bl_info = {
    "name": "Pop Drawers",
    "description": "Open Temporary Areas in your Main Screen",
    "author": "Spectral Vectors",
    "version": (0, 1),
    "blender": (3, 00, 0),
    "location": "Text Editor",
    "category": "Text Editor"}

import bpy

#bpy.types.Scene.popup_type = bpy.props.StringProperty(default='INFO')

class InfoDrawerOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "screen.info_drawer"
    bl_label = "Info Drawer Operator"
    
    
    popup_type = 'INFO'
    direction = 'HORIZONTAL'
    factor = 0.25

    @staticmethod
    def open_drawer(self, popup_type=popup_type):
        current_type = bpy.context.space_data.type
        if bpy.context.scene.opened:
            bpy.context.screen.areas[-1].type = popup_type
        else:    
            bpy.ops.screen.space_type_set_or_cycle(space_type=popup_type)
            bpy.context.space_data.show_region_header = False
            bpy.ops.screen.area_split(direction=self.direction, factor=self.factor, cursor=(0,0))
            bpy.ops.screen.space_type_set_or_cycle(space_type=current_type)
            bpy.context.scene.opened = True
    
    @staticmethod    
    def close_drawer():
        bpy.ops.screen.area_close({"area": bpy.context.screen.areas[-1]})
        bpy.context.scene.opened = False                
        
    def execute(self, context):
        if bpy.context.scene.opened and bpy.context.screen.areas[-1].type == self.popup_type:
            self.close_drawer()
        else:
            self.open_drawer(self)
        
        return {'FINISHED'}


class ConsoleDrawerOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "screen.console_drawer"
    bl_label = "Console Drawer Operator"
    
    
    popup_type = 'CONSOLE'
    direction = 'HORIZONTAL'
    factor = 0.25

    @staticmethod
    def open_drawer(self, popup_type=popup_type):
        current_type = bpy.context.space_data.type
        if bpy.context.scene.opened:
            bpy.context.screen.areas[-1].type = popup_type
        else:    
            bpy.ops.screen.space_type_set_or_cycle(space_type=popup_type)
            bpy.context.space_data.show_region_header = False
            bpy.ops.screen.area_split(direction=self.direction, factor=self.factor, cursor=(0,0))
            bpy.ops.screen.space_type_set_or_cycle(space_type=current_type)
            bpy.context.scene.opened = True
    
    @staticmethod    
    def close_drawer():
        bpy.ops.screen.area_close({"area": bpy.context.screen.areas[-1]})
        bpy.context.scene.opened = False                
        
    def execute(self, context):
        if bpy.context.scene.opened and bpy.context.screen.areas[-1].type == self.popup_type:
            self.close_drawer()
        else:
            self.open_drawer(self)
        
        return {'FINISHED'}


class PropertiesDrawerOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "screen.properties_drawer"
    bl_label = "Properties Drawer Operator"
    
    
    popup_type = 'PROPERTIES'
    direction = 'VERTICAL'
    factor = 0.25

    @staticmethod
    def open_drawer(self, popup_type=popup_type):
        current_type = bpy.context.space_data.type
        if bpy.context.scene.opened:
            bpy.context.screen.areas[-1].type = popup_type
        else:    
            bpy.ops.screen.space_type_set_or_cycle(space_type=popup_type)
            bpy.context.space_data.show_region_header = False
            bpy.ops.screen.area_split(direction=self.direction, factor=self.factor, cursor=(0,0))
            bpy.ops.screen.space_type_set_or_cycle(space_type=current_type)
            bpy.context.scene.opened = True
    
    @staticmethod    
    def close_drawer():
        bpy.ops.screen.area_close({"area": bpy.context.screen.areas[-1]})
        bpy.context.scene.opened = False                
        
    def execute(self, context):
        if bpy.context.scene.opened and bpy.context.screen.areas[-1].type == self.popup_type:
            self.close_drawer()
        else:
            self.open_drawer(self)
        
        return {'FINISHED'}


class OutlinerDrawerOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "screen.outliner_drawer"
    bl_label = "Outliner Drawer Operator"
    
    
    popup_type = 'OUTLINER'
    direction = 'VERTICAL'
    factor = 0.25

    @staticmethod
    def open_drawer(self, popup_type=popup_type):
        current_type = bpy.context.space_data.type
        if bpy.context.scene.opened:
            bpy.context.screen.areas[-1].type = popup_type
        else:    
            bpy.ops.screen.space_type_set_or_cycle(space_type=popup_type)
            bpy.context.space_data.show_region_header = False
            bpy.ops.screen.area_split(direction=self.direction, factor=self.factor, cursor=(0,0))
            bpy.ops.screen.space_type_set_or_cycle(space_type=current_type)
            bpy.context.scene.opened = True
    
    @staticmethod    
    def close_drawer():
        bpy.ops.screen.area_close({"area": bpy.context.screen.areas[-1]})
        bpy.context.scene.opened = False                
        
    def execute(self, context):
        if bpy.context.scene.opened and bpy.context.screen.areas[-1].type == self.popup_type:
            self.close_drawer()
        else:
            self.open_drawer(self)
        
        return {'FINISHED'}


class PopDrawersPanel(bpy.types.Panel):
    """Creates a Panel in the text editor"""
    bl_label = "Pop Drawers"
    bl_idname = "TEXT_PT_PopDrawers"
    bl_space_type = 'TEXT_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Text"

    def draw(self, context):
        layout = self.layout
        
        layout.label(text="Spaces:")
        column = layout.column(align=True)
            
        column.operator(text='Info', operator="screen.info_drawer")
        column.operator(text='Console', operator="screen.console_drawer")
        column.operator(text='Properties', operator="screen.properties_drawer")
        column.operator(text='Outliner', operator="screen.outliner_drawer")


classes = [
    PopDrawersPanel,
    InfoDrawerOperator,
    ConsoleDrawerOperator,
    OutlinerDrawerOperator,
    PropertiesDrawerOperator,
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
