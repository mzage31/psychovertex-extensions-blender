import bpy

class MZageHandyMenu(bpy.types.Menu):
    bl_label = ""
    bl_idname = "OBJECT_MT_mzage_handy_menu"
    def draw(self, context):
        layout = self.layout        
        layout.operator_context = 'INVOKE_DEFAULT'
        ao = bpy.context.active_object
        if ao:
            mode = ao.mode
            if mode == "EDIT":
                row = layout.row()
                col = row.column()
                col.label(text="UV")
                col.operator("mesh.mark_seam", text="Mark Seam", icon="GREASEPENCIL")
                col.operator("mesh.mark_seam", text="Clear Seam", icon="OUTLINER_DATA_GP_LAYER").clear = True
                col.operator("uv.unwrap", text="Unwrap", icon="MOD_SHRINKWRAP")
                col.operator("uv.project_from_view", text="View Project", icon="PROP_PROJECTED").scale_to_bounds = False
                col.operator("uv.reset", text="Reset", icon="X")
                col.separator()
                col.label(text="Mesh")
                if bpy.context.tool_settings.mesh_select_mode[1]:
                    col.operator("mesh.set_edge_flow", text="Set Flow", icon="SPHERECURVE")
                col.operator("mesh.mark_sharp", text="Mark Sharp", icon="GREASEPENCIL")
                col.operator("mesh.mark_sharp", text="Clear Sharp", icon="OUTLINER_DATA_GP_LAYER").clear = True
                if bpy.context.tool_settings.mesh_select_mode[2]:
                    col.operator("object.add_mat_sel_faces", text="Add Material", icon="MATERIAL")
                col.separator()
                col.label(text="Normals")
                col.operator("mesh.flip_normals", text="Flip", icon="ORIENTATION_NORMAL")
                col.operator("mesh.normals_make_consistent", text="Recalculate", icon="NORMALS_VERTEX_FACE")
                col.operator("transform.rotate_normal", text="Rotate", icon="NORMALS_VERTEX")
                col.operator("mesh.normals_tools", text="Reset", icon="SHADERFX").mode = "RESET"
                
                col = row.column()
                col.label(text="Selection")
                col.operator("mesh.loop_multi_select", text="Select Rings", icon="MESH_CIRCLE").ring = True
                col.operator("mesh.loop_multi_select", text="Select Loops", icon="STROKE").ring = False
                col.operator("mesh.region_to_loop", text="Select Boundary", icon="MOD_LATTICE")
                col.operator("mesh.loop_to_region", text="Select Inside", icon="OUTLINER_OB_LATTICE")
                col.operator("mesh.select_nth", text="Checker Deselect", icon="TEXTURE")
                if bpy.context.tool_settings.mesh_select_mode[2] and not bpy.context.tool_settings.mesh_select_mode[0] and not bpy.context.tool_settings.mesh_select_mode[1]:
                    col.operator("mesh.select_similar", text="Select Coplanar", icon="FACESEL").type = "COPLANAR"
                col.operator("mesh.select_overlapping_vertices", icon="VERTEXSEL")

                col.separator()
                col.label(text="Utils")
                col.operator("mesh.set_origin_to_selection", icon="OBJECT_ORIGIN")
                col.operator("mesh.set_origin_to_selection_and_rotate", icon="OBJECT_ORIGIN")
                col.operator("mesh.get_edge_length", icon="DRIVER_DISTANCE")
                col.operator("mesh.get_edges_angle", icon="DRIVER_ROTATIONAL_DIFFERENCE")
                col.operator("mesh.snap_vertices_to_surface", icon="MOD_SHRINKWRAP")
            elif mode == "OBJECT":
                row = layout.row()
                col = row.column()
                
                col.label(text="Object")
                if ao.type == "MESH":
                    col.prop(ao, "display_type", text="", icon="NODE_MATERIAL")
                    col.prop(ao.data, "use_auto_smooth", icon="MOD_SMOOTH")
                col.operator("object.create_empty_parent", icon="EMPTY_DATA")
                
                col.separator()
                col.label(text="Copy From Active")
                col.operator("object.make_links_data", text="Copy Modifiers", icon="MODIFIER").type = "MODIFIERS"
                col.operator("object.make_links_data", text="Copy Materials", icon="MATERIAL").type = "MATERIAL"

                col.separator()
                col.label(text="Copy To Active")
                col.operator("object.selected_origins_to_active", text="Origins To Active", icon="TRANSFORM_ORIGINS")
                
                
                col = row.column()
                col.label(text="Display Overlays")
                col.prop(context.area.spaces[0].overlay, "show_overlays", icon="OVERLAY")
                col.prop(context.area.spaces[0].overlay, "show_wireframes", icon="SHADING_WIRE")
                col.prop(context.area.spaces[0].overlay, "show_face_orientation", icon="FACESEL")
                col.separator()
                col.label(text="Import/Export")
                col.operator("import_scene.fbx", text="Import FBX", icon="IMPORT")
                col.operator("export_scene.fbx", text="Export FBX", icon="EXPORT")
                col.separator()
                col.label(text="To Unreal")
                col.operator("object.btus_setup", text="Setup for export", icon="SHADERFX")
                col.operator("object.btus_export", text="Set Export", icon="FAKE_USER_ON")
                col.operator("object.btus_dontexport", text="Set Dont Export", icon="FAKE_USER_OFF")
        else:
            if bpy.context.mode == "OBJECT":
                row = layout.row()
                col = row.column()
                col.label(text="Display Overlays")
                col.prop(context.area.spaces[0].overlay, "show_overlays", icon="OVERLAY")
                col.prop(context.area.spaces[0].overlay, "show_wireframes", icon="SHADING_WIRE")
                col.prop(context.area.spaces[0].overlay, "show_face_orientation", icon="FACESEL")
                col.separator()
                col.label(text="Import/Export")
                col.operator("import_scene.fbx", text="Import FBX", icon="IMPORT")
                col.operator("export_scene.fbx", text="Export FBX", icon="EXPORT")
            
            
