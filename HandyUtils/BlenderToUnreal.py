import bpy


class BTUS_Setup_Operator(bpy.types.Operator):
    bl_idname = "object.btus_setup"
    bl_label = "Blender to Unreal Setup"
    bl_options = {'REGISTER', 'UNDO'}

    lightmapSurfaceScale: bpy.props.IntProperty(
        name="Surface Scale",
        description="StaticMesh LightMap Surface Scale",
        default=64,
        min=1
    )
    lightmapRoundPowerOfTwo: bpy.props.BoolProperty(
        name="Round to POT",
        description="StaticMesh LightMap Round Power Of Two",
        default=False
    )

    collisionTraceFlag: bpy.props.EnumProperty(
        name="Collision Complexity",
        description="Collision Trace Flag",
        items=[
            ("CTF_UseDefault",
                "Project Default",
                "Create only complex shapes (per poly)." +
                " Use complex shapes for all scene queries" +
                " and collision tests." +
                " Can be used in simulation for" +
                " static shapes only" +
                " (i.e can be collided against but not moved" +
                " through forces or velocity.",
                1),
            ("CTF_UseSimpleAndComplex",
                "Use Simple And Complex",
                "Use project physics settings (DefaultShapeComplexity)",
                2),
            ("CTF_UseSimpleAsComplex",
                "Use Simple as Complex",
                "Create both simple and complex shapes." +
                " Simple shapes are used for regular scene queries" +
                " and collision tests. Complex shape (per poly)" +
                " is used for complex scene queries.",
                3),
            ("CTF_UseComplexAsSimple",
                "Use Complex as Simple",
                "Create only simple shapes." +
                " Use simple shapes for all scene" +
                " queries and collision tests.",
                4)
        ],
        default="CTF_UseDefault"
    )

    @classmethod
    def poll(cls, context):
        return len(context.selected_objects) > 0

    def execute(self, context):
        sos = context.selected_objects
        for so in sos:
            if so.ExportEnum == "dont_export":
                continue

            collection_path = []
            current_collection = so.users_collection[0] if so.users_collection else None
            while current_collection:
                collection_path.insert(0, current_collection.name)
                parent_collection_candids = [col for col in bpy.data.collections if current_collection.name in col.children]
                current_collection = parent_collection_candids[0] if len(parent_collection_candids) > 0 else None

            so.ExportEnum = "export_recursive"
            so.exportFolderName = "/".join(collection_path)

            so.RotateToZeroForExport = True

            so.CollisionTraceFlag = self.collisionTraceFlag
            so.AutoGenerateCollision = True
            so.MaterialSearchLocation = "AllAssets"

            if so.StaticMeshLightMapEnum != "CustomMap":
                so.GenerateLightmapUVs = False
                so.StaticMeshLightMapEnum = "SurfaceArea"
                so.useStaticMeshLightMapWorldScale = True
                so.staticMeshLightMapRoundPowerOfTwo = self.lightmapRoundPowerOfTwo
                so.staticMeshLightMapSurfaceScale = self.lightmapSurfaceScale

            so.exportAxisForward = "-Y"
            so.exportAxisUp = "Z"

        self.report({'INFO'}, "Setup objects")
        return {'FINISHED'}


class BTUS_Export_Operator(bpy.types.Operator):
    bl_idname = "object.btus_export"
    bl_label = "Blender to Unreal Export"

    def execute(self, context):
        ctx = bpy.context
        sos = ctx.selected_objects
        for so in sos:
            so.ExportEnum = "export_recursive"
        self.report({'INFO'}, "Export flag set")
        return {'FINISHED'}


class BTUS_DontExport_Operator(bpy.types.Operator):
    bl_idname = "object.btus_dontexport"
    bl_label = "Blender to Unreal Dont Export"

    def execute(self, context):
        ctx = bpy.context
        sos = ctx.selected_objects
        for so in sos:
            so.ExportEnum = "dont_export"
        self.report({'INFO'}, "Export flag unset")
        return {'FINISHED'}


class BTUS_UpdatePath_Operator(bpy.types.Operator):
    bl_idname = "object.btus_updatepath"
    bl_label = "Blender to Unreal Export"

    def execute(self, context):
        ctx = bpy.context
        sos = ctx.selected_objects
        for so in sos:
            collection_path = []
            current_collection = so.users_collection[0] if so.users_collection else None
            while current_collection:
                collection_path.insert(0, current_collection.name)
                parent_collection_candids = [col for col in bpy.data.collections if current_collection.name in col.children]
                current_collection = parent_collection_candids[0] if len(parent_collection_candids) > 0 else None
            so.exportFolderName = "/".join(collection_path)
        self.report({'INFO'}, "Updated path")
        return {'FINISHED'}
