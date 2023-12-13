import bpy


def make_active(name):
    uvs = bpy.context.view_layer.objects.active.data.uv_layers
    for uv in uvs:
        if uv.name == name:
            uvs.active = uv
            return
    print("Could not find:", name, "\n(this should never happen)")


def move_to_bottom(index):
    #    uvs = bpy.context.scene.objects.active.data.uv_textures
    uvs = bpy.context.view_layer.objects.active.data.uv_layers
    uvs.active_index = index
    new_name = uvs.active.name

    bpy.ops.mesh.uv_texture_add()

    # delete the "old" one
    make_active(new_name)
    bpy.ops.mesh.uv_texture_remove()

    # set the name of the last one
    uvs.active_index = len(uvs) - 1
    uvs.active.name = new_name


class UvToolsMoveUVMapDownOperator(bpy.types.Operator):
    bl_idname = "uv_tools.move_uvmap_down"
    bl_label = "Move Down"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        uvs = context.view_layer.objects.active.data.uv_layers

        # get the selected UV map
        orig_ind = uvs.active_index
        orig_name = uvs.active.name

        if orig_ind == len(uvs) - 1:
            return {'FINISHED'}

        # use "trick" on the one after it
        move_to_bottom(orig_ind + 1)

        # use the "trick" on the UV map
        move_to_bottom(orig_ind)

        # use the "trick" on the rest that are after where it was
        for _ in range(orig_ind, len(uvs) - 2):
            move_to_bottom(orig_ind)

        make_active(orig_name)

        return {'FINISHED'}


class UvToolsMoveUVMapUpOperator(bpy.types.Operator):
    bl_idname = "uv_tools.move_uvmap_up"
    bl_label = "Move Up"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        uvs = bpy.context.view_layer.objects.active.data.uv_layers

        if uvs.active_index == 0:
            return {'FINISHED'}

        original = uvs.active.name
        uvs.active_index -= 1
        bpy.ops.uv_tools.move_uvmap_down()
        make_active(original)

        return {'FINISHED'}


def getActiveLayer(uvs):
    for uv in uvs:
        if uv.active:
            return uv.name


class UvToolsRenameOperator(bpy.types.Operator):
    bl_idname = "uv_tools.rename"
    bl_label = "Rename In All"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        scene = context.scene
        properties = scene.uvtoolsProperties
        current_uv_name = getActiveLayer(bpy.context.view_layer.objects.active.data.uv_layers)
        for obj in bpy.data.objects:
            if obj.select_get():
                uvs = obj.data.uv_layers
                for uv in uvs:
                    if uv.name == current_uv_name:
                        uv.name = properties.new_name
                        uv.active = True
        return {'FINISHED'}


class UvToolsSelectOperator(bpy.types.Operator):
    bl_idname = "uv_tools.select"
    bl_label = "Select In All"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        # scene = context.scene
        # properties = scene.uvtoolsProperties
        current_uv_name = getActiveLayer(bpy.context.view_layer.objects.active.data.uv_layers)
        for obj in bpy.data.objects:
            if obj.select_get():
                uvs = obj.data.uv_layers
                for uv in uvs:
                    if uv.name == current_uv_name:
                        uv.active = True
        return {'FINISHED'}


class UvToolsAddOperator(bpy.types.Operator):
    bl_idname = "uv_tools.add"
    bl_label = "Add To All"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        scene = context.scene
        properties = scene.uvtoolsProperties
        for obj in bpy.data.objects:
            if obj.select_get():
                uvs = obj.data.uv_layers
                hasuv = False
                for uv in uvs:
                    if uv.name == properties.new_name:
                        hasuv = True
                if not hasuv:
                    uv = uvs.new(name=properties.new_name)
                    uv.active = True
        return {'FINISHED'}


class UvToolsRemoveOperator(bpy.types.Operator):
    bl_idname = "uv_tools.remove"
    bl_label = "Remove From All"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        # scene = context.scene
        # properties = scene.uvtoolsProperties
        current_uv_name = getActiveLayer(bpy.context.view_layer.objects.active.data.uv_layers)
        for obj in bpy.data.objects:
            if obj.select_get():
                uvs = obj.data.uv_layers
                for uv in uvs:
                    if uv.name == current_uv_name:
                        uvs.remove(uv)
        return {'FINISHED'}


class UvToolsProperties(bpy.types.PropertyGroup):
    new_name: bpy.props.StringProperty(
        name="New Name",
        description="UV slot's new name",
        default="New UV",
        maxlen=1024,
    )


def uv_tools_addition(self, context):
    layout = self.layout
    me = context.mesh
    scene = context.scene
    properties = scene.uvtoolsProperties

    row = layout.row()
    col = row.column()

    col.template_list("MESH_UL_uvmaps", "uvmaps", me, "uv_layers", me.uv_layers, "active_index", rows=2)

    side = row.column()
    col = side.column(align=True)
    col.operator("mesh.uv_texture_add", icon='ADD', text="")
    col.operator("mesh.uv_texture_remove", icon='REMOVE', text="")

    col = side.column(align=True)
    col.operator("uv_tools.move_uvmap_up", icon='TRIA_UP', text="")
    col.operator("uv_tools.move_uvmap_down", icon='TRIA_DOWN', text="")

    col = layout.column()
    col.prop(properties, "new_name")

    row = col.row(align=True)
    row.operator("uv_tools.add", icon="ADD")
    row.operator("uv_tools.remove", icon="REMOVE")
    row = col.row(align=True)
    row.operator("uv_tools.select")
    row.operator("uv_tools.rename")


classes = [
    UvToolsMoveUVMapDownOperator,
    UvToolsMoveUVMapUpOperator,
    UvToolsRenameOperator,
    UvToolsSelectOperator,
    UvToolsAddOperator,
    UvToolsRemoveOperator,
    UvToolsProperties,
]

drawfunc = None


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    global drawfunc
    bpy.types.Scene.uvtoolsProperties = bpy.props.PointerProperty(type=UvToolsProperties)
    drawfunc = bpy.types.DATA_PT_uv_texture.draw
    bpy.types.DATA_PT_uv_texture.draw = uv_tools_addition


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.uvtoolsProperties
    bpy.types.DATA_PT_uv_texture.draw = drawfunc
