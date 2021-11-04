bl_info = {
    "name": "Pop Drawers",
    "description": "Open Temporary Areas in your Main Screen",
    "author": "Spectral Vectors",
    "version": (0, 4),
    "blender": (3, 00, 0),
    "location": "Text Editor & 3D View",
    "category": "Screen"}

import bpy

#bpy.types.Scene.pop_type = bpy.props.StringProperty(default='INFO')



class InfoDrawerOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "screen.info_drawer"
    bl_label = "Info Drawer Operator"

    pop_type = 'INFO'
    direction = 'HORIZONTAL'
    factor = 0.33

    @staticmethod
    def open_drawer(self, pop_type=pop_type):
        current_type = bpy.context.space_data.type
        scene = bpy.context.scene
        screen = bpy.context.screen
        screenops = bpy.ops.screen

        if scene.drawer_open:
            screen.areas[-1].type = pop_type
            scene.console = False
            scene.properties = False
            scene.outliner = False
            scene.view3d = False
            scene.info = True
            scene.asset = False
            scene.shader = False
            scene.geometry = False
            scene.timeline = False
            scene.file = False
        else:    
            screenops.space_type_set_or_cycle(space_type=pop_type)
            bpy.context.space_data.show_region_header = False
            screenops.area_split(direction=self.direction, 
                                factor=self.factor, 
                                cursor=(0,0))
            screenops.space_type_set_or_cycle(space_type=current_type)
            scene.drawer_open = True
            scene.info = True
    
    @staticmethod    
    def close_drawer():
        scene = bpy.context.scene
        screenops = bpy.ops.screen

        scene.drawer_open = False
        scene.info = False
        
        screenops.area_close({"area": bpy.context.screen.areas[-1]})

        
    def execute(self, context):
        scene = context.scene
        screen = context.screen

        if scene.drawer_open and screen.areas[-1].type == self.pop_type:
            self.close_drawer()
        else:
            self.open_drawer(self)
        
        return {'FINISHED'}


class ConsoleDrawerOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "screen.console_drawer"
    bl_label = "Console Drawer Operator"
        
    pop_type = 'CONSOLE'
    direction = 'HORIZONTAL'
    factor = 0.33

    @staticmethod
    def open_drawer(self, pop_type=pop_type):
        current_type = bpy.context.space_data.type
        scene = bpy.context.scene
        screen = bpy.context.screen
        screenops = bpy.ops.screen

        if scene.drawer_open:
            screen.areas[-1].type = pop_type
            scene.console = True
            scene.properties = False
            scene.outliner = False
            scene.view3d = False
            scene.info = False
            scene.asset = False
            scene.shader = False
            scene.geometry = False
            scene.timeline = False
            scene.file = False
        else:    
            screenops.space_type_set_or_cycle(space_type=pop_type)
            bpy.context.space_data.show_region_header = False
            screenops.area_split(direction=self.direction, 
                                factor=self.factor, 
                                cursor=(0,0))
            screenops.space_type_set_or_cycle(space_type=current_type)
            scene.drawer_open = True
            scene.console = True
    
    @staticmethod    
    def close_drawer():
        scene = bpy.context.scene
        screenops = bpy.ops.screen

        scene.drawer_open = False
        scene.console = False
        
        screenops.area_close({"area": bpy.context.screen.areas[-1]})

        
    def execute(self, context):
        scene = context.scene
        screen = context.screen

        if scene.drawer_open and screen.areas[-1].type == self.pop_type:
            self.close_drawer()
        else:
            self.open_drawer(self)
        
        return {'FINISHED'}


class PropertiesDrawerOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "screen.properties_drawer"
    bl_label = "Properties Drawer Operator"
        
    pop_type = 'PROPERTIES'
    direction = 'VERTICAL'
    factor = 0.33

    @staticmethod
    def open_drawer(self, pop_type=pop_type):
        current_type = bpy.context.space_data.type
        scene = bpy.context.scene
        screen = bpy.context.screen
        screenops = bpy.ops.screen

        if scene.drawer_open:
            screen.areas[-1].type = pop_type
            scene.console = False
            scene.properties = True
            scene.outliner = False
            scene.view3d = False
            scene.info = False
            scene.asset = False
            scene.shader = False
            scene.geometry = False
            scene.timeline = False
            scene.file = False
        else:    
            screenops.space_type_set_or_cycle(space_type=pop_type)
            bpy.context.space_data.show_region_header = False
            screenops.area_split(direction=self.direction, 
                                factor=self.factor, 
                                cursor=(0,0))
            screenops.space_type_set_or_cycle(space_type=current_type)
            scene.drawer_open = True
            scene.properties = True
    
    @staticmethod    
    def close_drawer():
        scene = bpy.context.scene
        screenops = bpy.ops.screen

        scene.drawer_open = False
        scene.properties = False
        
        screenops.area_close({"area": bpy.context.screen.areas[-1]})

        
    def execute(self, context):
        scene = context.scene
        screen = context.screen

        if scene.drawer_open and screen.areas[-1].type == self.pop_type:
            self.close_drawer()
        else:
            self.open_drawer(self)
        
        return {'FINISHED'}


class OutlinerDrawerOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "screen.outliner_drawer"
    bl_label = "Outliner Drawer Operator"
        
    pop_type = 'OUTLINER'
    direction = 'VERTICAL'
    factor = 0.33

    @staticmethod
    def open_drawer(self, pop_type=pop_type):
        current_type = bpy.context.space_data.type
        scene = bpy.context.scene
        screen = bpy.context.screen
        screenops = bpy.ops.screen

        if scene.drawer_open:
            screen.areas[-1].type = pop_type
            scene.console = False
            scene.properties = False
            scene.outliner = True
            scene.view3d = False
            scene.info = False
            scene.asset = False
            scene.shader = False
            scene.geometry = False
            scene.timeline = False
            scene.file = False
        else:    
            screenops.space_type_set_or_cycle(space_type=pop_type)
            bpy.context.space_data.show_region_header = False
            screenops.area_split(direction=self.direction, 
                                factor=self.factor, 
                                cursor=(0,0))
            screenops.space_type_set_or_cycle(space_type=current_type)
            scene.drawer_open = True
            scene.outliner = True
    
    @staticmethod    
    def close_drawer():
        scene = bpy.context.scene
        screenops = bpy.ops.screen

        scene.drawer_open = False
        scene.outliner = False
        
        screenops.area_close({"area": bpy.context.screen.areas[-1]})

        
    def execute(self, context):
        scene = context.scene
        screen = context.screen

        if scene.drawer_open and screen.areas[-1].type == self.pop_type:
            self.close_drawer()
        else:
            self.open_drawer(self)
        
        return {'FINISHED'}


class View3DDrawerOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "screen.view3d_drawer"
    bl_label = "3D View Drawer Operator"
        
    pop_type = 'VIEW_3D'
    direction = 'VERTICAL'
    factor = 0.33

    @staticmethod
    def open_drawer(self, pop_type=pop_type):
        current_type = bpy.context.space_data.type
        scene = bpy.context.scene
        screen = bpy.context.screen
        screenops = bpy.ops.screen

        if scene.drawer_open:
            screen.areas[-1].type = pop_type
            scene.console = False
            scene.properties = False
            scene.outliner = False
            scene.view3d = True
            scene.info = False
            scene.asset = False
            scene.shader = False
            scene.geometry = False
            scene.timeline = False
            scene.file = False
        else:    
            screenops.space_type_set_or_cycle(space_type=pop_type)
            bpy.context.space_data.show_region_header = False
            screenops.area_split(direction=self.direction, 
                                factor=self.factor, 
                                cursor=(0,0))
            screenops.space_type_set_or_cycle(space_type=current_type)
            scene.drawer_open = True
            scene.view3d = True
    
    @staticmethod    
    def close_drawer():
        scene = bpy.context.scene
        screenops = bpy.ops.screen

        scene.drawer_open = False
        scene.view3d = False
        
        screenops.area_close({"area": bpy.context.screen.areas[-1]})

        
    def execute(self, context):
        scene = context.scene
        screen = context.screen

        if scene.drawer_open and screen.areas[-1].type == self.pop_type:
            self.close_drawer()
        else:
            self.open_drawer(self)
        
        return {'FINISHED'}


class PopDrawersTextPanel(bpy.types.Panel):
    """Creates a Panel in the text editor"""
    bl_label = "Pop Drawers"
    bl_idname = "TEXT_PT_PopDrawers"
    bl_space_type = 'TEXT_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Text"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        if scene.info:
            infolabel = 'Close'
            infoicon = 'X'
        else:
            infolabel = 'Info'
            infoicon = 'INFO'

        if scene.console:
            consolelabel = 'Close'
            consoleicon = 'X'
        else:
            consolelabel = 'Console'
            consoleicon = 'CONSOLE'

        if scene.properties:
            propertieslabel = 'Close'
            propertiesicon = 'X'
        else:
            propertieslabel = 'Properties'
            propertiesicon = 'PROPERTIES'

        if scene.outliner:
            outlinerlabel = 'Close'
            outlinericon = 'X'
        else:
            outlinerlabel = 'Outliner'
            outlinericon = 'OUTLINER'
            
        if scene.view3d:
            view3dlabel = 'Close'
            view3dicon = 'X'
        else:
            view3dlabel = '3D View'
            view3dicon = 'VIEW3D'

        column = layout.column(align=True)            
        column.operator(text=infolabel, icon=infoicon, operator="screen.info_drawer")
        column.operator(text=consolelabel, icon=consoleicon, operator="screen.console_drawer")
        column.operator(text=propertieslabel, icon=propertiesicon, operator="screen.properties_drawer")
        column.operator(text=outlinerlabel, icon=outlinericon, operator="screen.outliner_drawer")
        column.operator(text=view3dlabel, icon=view3dicon, operator="screen.view3d_drawer")

class FileDrawerOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "screen.file_drawer"
    bl_label = "File Drawer Operator"

    pop_type = 'FILE_BROWSER'
    direction = 'HORIZONTAL'
    factor = 0.33

    @staticmethod
    def open_drawer(self, pop_type=pop_type):
        current_type = bpy.context.space_data.type
        scene = bpy.context.scene
        screen = bpy.context.screen
        screenops = bpy.ops.screen

        if scene.drawer_open:
            screen.areas[-1].type = pop_type
            screen.areas[-1].ui_type = 'FILES'
            scene.asset = False
            scene.shader = False
            scene.geometry = False
            scene.timeline = False
            scene.file = True
            scene.console = False
            scene.properties = False
            scene.outliner = False
            scene.view3d = False
            scene.info = False
        else:    
            screenops.space_type_set_or_cycle(space_type=pop_type)
            bpy.context.area.ui_type = 'FILES'
            bpy.context.space_data.show_region_header = False
            screenops.area_split(direction=self.direction, 
                                factor=self.factor, 
                                cursor=(0,0))
            screenops.space_type_set_or_cycle(space_type=current_type)
            scene.drawer_open = True
            scene.file = True
    
    @staticmethod    
    def close_drawer():
        scene = bpy.context.scene
        screenops = bpy.ops.screen

        scene.drawer_open = False
        scene.file = False
        
        screenops.area_close({"area": bpy.context.screen.areas[-1]})

        
    def execute(self, context):
        scene = context.scene
        screen = context.screen

        if scene.drawer_open and screen.areas[-1].type == self.pop_type:
            self.close_drawer()
        else:
            self.open_drawer(self)
        
        return {'FINISHED'}


class AssetDrawerOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "screen.asset_drawer"
    bl_label = "Asset Drawer Operator"

    pop_type = 'FILE_BROWSER'
    direction = 'HORIZONTAL'
    factor = 0.33

    @staticmethod
    def open_drawer(self, pop_type=pop_type):
        current_type = bpy.context.space_data.type
        scene = bpy.context.scene
        screen = bpy.context.screen
        screenops = bpy.ops.screen

        if scene.drawer_open:
            screen.areas[-1].type = pop_type
            screen.areas[-1].ui_type = 'ASSETS'
            scene.asset = True
            scene.shader = False
            scene.geometry = False
            scene.timeline = False
            scene.file = False
            scene.console = False
            scene.properties = False
            scene.outliner = False
            scene.view3d = False
            scene.info = False
        else:    
            screenops.space_type_set_or_cycle(space_type=pop_type)
            bpy.context.area.ui_type = 'ASSETS'
            bpy.context.space_data.show_region_header = False
            screenops.area_split(direction=self.direction, 
                                factor=self.factor, 
                                cursor=(0,0))
            screenops.space_type_set_or_cycle(space_type=current_type)
            scene.drawer_open = True
            scene.asset = True
    
    @staticmethod    
    def close_drawer():
        scene = bpy.context.scene
        screenops = bpy.ops.screen

        scene.drawer_open = False
        scene.asset = False
        
        screenops.area_close({"area": bpy.context.screen.areas[-1]})

        
    def execute(self, context):
        scene = context.scene
        screen = context.screen

        if scene.drawer_open and screen.areas[-1].type == self.pop_type:
            self.close_drawer()
        else:
            self.open_drawer(self)
        
        return {'FINISHED'}

class ShaderDrawerOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "screen.shader_drawer"
    bl_label = "Shader Drawer Operator"

    pop_type = 'NODE_EDITOR'
    direction = 'HORIZONTAL'
    factor = 0.33

    @staticmethod
    def open_drawer(self, pop_type=pop_type):
        current_type = bpy.context.space_data.type
        scene = bpy.context.scene
        screen = bpy.context.screen
        screenops = bpy.ops.screen

        if scene.drawer_open:
            screen.areas[-1].type = pop_type
            screen.areas[-1].ui_type = 'ShaderNodeTree'
            scene.asset = False
            scene.shader = True
            scene.geometry = False
            scene.timeline = False
            scene.file = False
            scene.console = False
            scene.properties = False
            scene.outliner = False
            scene.view3d = False
            scene.info = False
        else:    
            screenops.space_type_set_or_cycle(space_type=pop_type)
            bpy.context.area.ui_type = 'ShaderNodeTree'
            bpy.context.space_data.show_region_header = False
            screenops.area_split(direction=self.direction, 
                                factor=self.factor, 
                                cursor=(0,0))
            screenops.space_type_set_or_cycle(space_type=current_type)
            scene.drawer_open = True
            scene.shader = True
    
    @staticmethod    
    def close_drawer():
        scene = bpy.context.scene
        screenops = bpy.ops.screen

        scene.drawer_open = False
        scene.shader = False
        
        screenops.area_close({"area": bpy.context.screen.areas[-1]})

        
    def execute(self, context):
        scene = context.scene
        screen = context.screen

        if scene.drawer_open and screen.areas[-1].type == self.pop_type:
            self.close_drawer()
        else:
            self.open_drawer(self)
        
        return {'FINISHED'}


class GeometryDrawerOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "screen.geometry_drawer"
    bl_label = "Geometry Drawer Operator"

    pop_type = 'NODE_EDITOR'
    direction = 'HORIZONTAL'
    factor = 0.33

    @staticmethod
    def open_drawer(self, pop_type=pop_type):
        current_type = bpy.context.space_data.type
        scene = bpy.context.scene
        screen = bpy.context.screen
        screenops = bpy.ops.screen

        if scene.drawer_open:
            screen.areas[-1].type = pop_type
            screen.areas[-1].ui_type = 'GeometryNodeTree'
            scene.asset = False
            scene.shader = False
            scene.geometry = True
            scene.timeline = False
            scene.file = False
            scene.console = False
            scene.properties = False
            scene.outliner = False
            scene.view3d = False
            scene.info = False
        else:    
            screenops.space_type_set_or_cycle(space_type=pop_type)
            bpy.context.area.ui_type = 'GeometryNodeTree'
            bpy.context.space_data.show_region_header = False
            screenops.area_split(direction=self.direction, 
                                factor=self.factor, 
                                cursor=(0,0))
            screenops.space_type_set_or_cycle(space_type=current_type)
            scene.drawer_open = True
            scene.geometry = True
    
    @staticmethod    
    def close_drawer():
        scene = bpy.context.scene
        screenops = bpy.ops.screen

        scene.drawer_open = False
        scene.geometry = False
        
        screenops.area_close({"area": bpy.context.screen.areas[-1]})

        
    def execute(self, context):
        scene = context.scene
        screen = context.screen

        if scene.drawer_open and screen.areas[-1].type == self.pop_type:
            self.close_drawer()
        else:
            self.open_drawer(self)
        
        return {'FINISHED'}

class TimelineDrawerOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "screen.timeline_drawer"
    bl_label = "Timeline Drawer Operator"

    pop_type = 'DOPESHEET_EDITOR'
    direction = 'HORIZONTAL'
    factor = 0.33

    @staticmethod
    def open_drawer(self, pop_type=pop_type):
        current_type = bpy.context.space_data.type
        scene = bpy.context.scene
        screen = bpy.context.screen
        screenops = bpy.ops.screen

        if scene.drawer_open:
            screen.areas[-1].type = pop_type
            screen.areas[-1].ui_type = 'TIMELINE'
            scene.asset = False
            scene.shader = False
            scene.geometry = False
            scene.timeline = True
            scene.file = False
            scene.console = False
            scene.properties = False
            scene.outliner = False
            scene.view3d = False
            scene.info = False
        else:    
            screenops.space_type_set_or_cycle(space_type=pop_type)
            bpy.context.area.ui_type = 'TIMELINE'
            bpy.context.space_data.show_region_header = False
            screenops.area_split(direction=self.direction, 
                                factor=self.factor, 
                                cursor=(0,0))
            screenops.space_type_set_or_cycle(space_type=current_type)
            scene.drawer_open = True
            scene.timeline = True
    
    @staticmethod    
    def close_drawer():
        scene = bpy.context.scene
        screenops = bpy.ops.screen

        scene.drawer_open = False
        scene.timeline = False
        
        screenops.area_close({"area": bpy.context.screen.areas[-1]})

        
    def execute(self, context):
        scene = context.scene
        screen = context.screen

        if scene.drawer_open and screen.areas[-1].type == self.pop_type:
            self.close_drawer()
        else:
            self.open_drawer(self)
        
        return {'FINISHED'}


class PopDrawersView3DPanel(bpy.types.Panel):
    """Creates a Panel in the text editor"""
    bl_label = "Pop Drawers"
    bl_idname = "VIEW_3D_PT_PopDrawers"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Pop Drawers"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        if scene.file:
            filelabel = 'Close'
            fileicon = 'X'
        else:
            filelabel = 'File Browser'
            fileicon = 'FILEBROWSER'

        if scene.asset:
            assetlabel = 'Close'
            asseticon = 'X'
        else:
            assetlabel = 'Asset Browser'
            asseticon = 'ASSET_MANAGER'

        if scene.geometry:
            geometrylabel = 'Close'
            geometryicon = 'X'
        else:
            geometrylabel = 'Geometry Nodes'
            geometryicon = 'NODETREE'

        if scene.shader:
            shaderlabel = 'Close'
            shadericon = 'X'
        else:
            shaderlabel = 'Shader Nodes'
            shadericon = 'NODE_MATERIAL'
            
        if scene.timeline:
            timelinelabel = 'Close'
            timelineicon = 'X'
        else:
            timelinelabel = 'Timeline'
            timelineicon = 'TIME'

        column = layout.column(align=True)            
        column.operator(text=filelabel, icon=fileicon, operator="screen.file_drawer")
        column.operator(text=assetlabel, icon=asseticon, operator="screen.asset_drawer")
        column.operator(text=geometrylabel, icon=geometryicon, operator="screen.geometry_drawer")
        column.operator(text=shaderlabel, icon=shadericon, operator="screen.shader_drawer")
        column.operator(text=timelinelabel, icon=timelineicon, operator="screen.timeline_drawer")

classes = [
    PopDrawersTextPanel,
    PopDrawersView3DPanel,
    InfoDrawerOperator,
    ConsoleDrawerOperator,
    OutlinerDrawerOperator,
    PropertiesDrawerOperator,
    View3DDrawerOperator,
    FileDrawerOperator,
    AssetDrawerOperator,
    TimelineDrawerOperator,
    ShaderDrawerOperator,
    GeometryDrawerOperator,
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.drawer_open = bpy.props.BoolProperty(default=False)
    bpy.types.Scene.info = bpy.props.BoolProperty(default=False)
    bpy.types.Scene.console = bpy.props.BoolProperty(default=False)
    bpy.types.Scene.properties = bpy.props.BoolProperty(default=False)
    bpy.types.Scene.outliner = bpy.props.BoolProperty(default=False)
    bpy.types.Scene.view3d = bpy.props.BoolProperty(default=False)

    bpy.types.Scene.file = bpy.props.BoolProperty(default=False)
    bpy.types.Scene.asset = bpy.props.BoolProperty(default=False)
    bpy.types.Scene.shader = bpy.props.BoolProperty(default=False)
    bpy.types.Scene.geometry = bpy.props.BoolProperty(default=False)
    bpy.types.Scene.timeline = bpy.props.BoolProperty(default=False)
        


def unregister():
    del(bpy.types.Scene.drawer_open)
    del(bpy.types.Scene.info)
    del(bpy.types.Scene.console)
    del(bpy.types.Scene.properties)
    del(bpy.types.Scene.outliner)
    del(bpy.types.Scene.view3d)

    del(bpy.types.Scene.file)
    del(bpy.types.Scene.asset)
    del(bpy.types.Scene.shader)
    del(bpy.types.Scene.geometry)
    del(bpy.types.Scene.timeline)

    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
