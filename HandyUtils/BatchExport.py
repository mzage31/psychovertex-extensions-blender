import bpy


class BatchExportSelectionsAsSMOperator(bpy.types.Operator):
    bl_idname = "object.batch_export_selections_as_sm"
    bl_label = "Batch Export Selections as SM_"
    bl_options = {'REGISTER'}
    directory: bpy.props.StringProperty(name="Export Path", description="Where do you want to export?")
    filter_folder: bpy.props.BoolProperty(default=True, options={"HIDDEN"})

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

    def execute(self, context):
        so = context.selected_objects
        for s in so:
            export_path = f"{self.directory}\\SM_{s.name}.fbx"
            bpy.ops.object.select_all(action='DESELECT')
            s.select_set(True)
            bpy.ops.object.location_clear(clear_delta=False)
            bpy.ops.object.rotation_clear(clear_delta=False)
            bpy.ops.export_scene.fbx(filepath=export_path, use_selection=True)

        bpy.ops.ed.undo_push()
        bpy.ops.ed.undo()
        return {'FINISHED'}


def register():
    bpy.utils.register_class(BatchExportSelectionsAsSMOperator)


def unregister():
    bpy.utils.unregister_class(BatchExportSelectionsAsSMOperator)
