import bpy

class BTUS_Setup_Operator(bpy.types.Operator):
    bl_idname = "object.btus_setup"
    bl_label = "Blender to Unreal Setup"
    
    def execute(self, context):
        ctx = bpy.context
        sos = ctx.selected_objects
        for so in sos:
            if so.ExportEnum == "dont_export":
                continue
            so.ExportEnum = "export_recursive"
            so.exportFolderName = so.users_collection[0].name
            
            so.RotateToZeroForExport = True
            
            so.CollisionTraceFlag = "CTF_UseComplexAsSimple"
            so.AutoGenerateCollision = True
            so.MaterialSearchLocation = "AllAssets"
            
            if so.StaticMeshLightMapEnum != "CustomMap":
                so.GenerateLightmapUVs = False
                so.StaticMeshLightMapEnum = "SurfaceArea"
                so.useStaticMeshLightMapWorldScale = True
                so.staticMeshLightMapRoundPowerOfTwo = False
                so.staticMeshLightMapSurfaceScale = 96
            
            so.exportAxisForward = "-Y"
            so.exportAxisUp = "Z"
        
        self.report({'INFO'}, f"Setup objects")
        return {'FINISHED'}


class BTUS_Export_Operator(bpy.types.Operator):
    bl_idname = "object.btus_export"
    bl_label = "Blender to Unreal Export"
    
    def execute(self, context):
        ctx = bpy.context
        sos = ctx.selected_objects
        for so in sos:
            so.ExportEnum = "export_recursive"
        self.report({'INFO'}, f"Export flag set")
        return {'FINISHED'}


class BTUS_DontExport_Operator(bpy.types.Operator):
    bl_idname = "object.btus_dontexport"
    bl_label = "Blender to Unreal Dont Export"
    
    def execute(self, context):
        ctx = bpy.context
        sos = ctx.selected_objects
        for so in sos:
            so.ExportEnum = "dont_export"
        self.report({'INFO'}, f"Export flag unset")
        return {'FINISHED'}
