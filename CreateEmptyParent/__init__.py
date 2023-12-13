import bpy


class CreateEmptyParentOperator(bpy.types.Operator):
    bl_idname = "object.create_empty_parent"
    bl_label = "Create Empty Parent"
    bl_options = {"UNDO"}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        ao = context.active_object
        so = context.selected_objects
        ac = ao.users_collection[0]

        if len(so) == 0:
            return {'CANCELLED'}

        empty = bpy.data.objects.new("empty", None)
        ac.objects.link(empty)
        empty.empty_display_size = max(0.1, max(ao.dimensions) * 1.1)
        empty.location = ao.location
        empty.parent = ao.parent
        empty.matrix_parent_inverse = ao.matrix_parent_inverse
        empty.name = f"{ao.name}_Parent"

        for s in so:
            s.parent = empty
            s.matrix_parent_inverse = empty.matrix_world.inverted()
            s.location = s.location - empty.location

        return {'FINISHED'}


def register():
    bpy.utils.register_class(CreateEmptyParentOperator)


def unregister():
    bpy.utils.unregister_class(CreateEmptyParentOperator)
