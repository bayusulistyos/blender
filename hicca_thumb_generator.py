bl_info = {
    "name": "Thumbnail Generator",
    "author": "Bayu Sulistyo S",
    "version": (0.9),
    "blender": (2, 80, 0),
    "location": "View3D > Add > Mesh > New Object",
    "description": "Simple Thumbnail Generator",
    "warning": "",
    "wiki_url": "",
    "category": "Add Mesh",
}




import bpy
import os


def thumbnail():

    filepath = bpy.data.filepath
    directory = os.path.dirname(filepath)
    bpy.context.scene.render.resolution_x = 600
    bpy.context.scene.render.resolution_y = 600
    bpy.context.scene.render.resolution_percentage = 100
    filename = bpy.path.basename(bpy.data.filepath)
    filename = os.path.splitext(filename)[0]

    if filename:
        bpy.context.scene.render.filepath = os.path.join(directory, filename)

    bpy.ops.render.render('INVOKE_DEFAULT', animation=False, write_still=True)


class ThumbPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Thumbnail Generator"
    bl_idname = "TM_PT_thumb"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Hicca Tools"

    #bl_label = "Thumbnail Generator"
    ##bl_idname = "thumb_gen"
    #bl_space_type = 'PROPERTIES'
    #bl_region_type = 'WINDOW'
    #bl_context = "scene"

    #bl_space_type = 'PROPERTIES'
    #bl_region_type = 'WINDOW'
    #bl_context = "scene"


    def draw(self, context):

        layout = self.layout
        obj = context.scene

        row = layout.row()
        row.label(text="Thumbnail Generator")

        row = layout.row()
        row.operator("gen.thumb")


class GenThumb(bpy.types.Operator):
    """Generate Thumbnail"""
    bl_idname = "gen.thumb"
    bl_label = "Generate Thumbnail"


    def execute(self, context):
        thumbnail()
        return {'FINISHED'}

def register():
    bpy.utils.register_class(GenThumb)
    bpy.utils.register_class(ThumbPanel)


def unregister():
    bpy.utils.unregister_class(GenThumb)
    bpy.utils.register_class(GenThumbPanel)



if __name__ == "__main__":
    register()
