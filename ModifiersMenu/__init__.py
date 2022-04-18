import bpy

class MZageModifiersControl(bpy.types.Operator):
    bl_idname = "object.mzage_modifiers_control"
    bl_label = "Control"
    bl_options = {'UNDO'}
    operation: bpy.props.StringProperty(name="Operation", default="EXPANDALL")
    def execute(self, context):
        ao = bpy.context.active_object
        so = bpy.context.selected_objects
        if self.operation == "EXPANDALL":
            for s in so:
                for mod in s.modifiers:
                    mod.show_expanded = True
        elif self.operation == "COLLAPSEALL":
            for s in so:
                for mod in s.modifiers:
                    mod.show_expanded = False
        elif self.operation == "APPLYALL":
            for s in so:
                bpy.context.view_layer.objects.active = s
                for mod in s.modifiers:
                    bpy.ops.object.modifier_apply(modifier=mod.name)
            bpy.context.view_layer.objects.active = ao
        elif self.operation == "REMOVEALL":
            for s in so:
                for mod in s.modifiers:
                    s.modifiers.remove(mod)
        return {'FINISHED'}


class MZageModifiersArray(bpy.types.Operator):
    bl_idname = "object.mzage_modifiers_array"
    bl_label = "Array"
    bl_options = {'UNDO'}
    type: bpy.props.StringProperty(name="Type", default="COUNT")
    def execute(self, context):
        ao = bpy.context.active_object
        so = bpy.context.selected_objects
        if self.type == "COUNT":
            for s in so:
                mod = s.modifiers.new("Array", "ARRAY")
                mod.fit_type = "FIXED_COUNT"
        elif self.type == "LENGTH":
            for s in so:
                mod = s.modifiers.new("Array", "ARRAY")
                mod.fit_type = "FIT_LENGTH"
                mod.fit_length = 2
        elif self.type == "CURVE":
            so = [s for s in so if s.type == "CURVE"]
            if ao in so:
                so.remove(ao)
            s = so[0] if len(so) > 0 else None
            if ao:
                mod = ao.modifiers.new("Array", "ARRAY")
                mod.fit_type = "FIT_CURVE"
                if s:
                    mod.curve = s
        elif self.type == "OBJECT":
            if ao in so:
                so.remove(ao)
            s = so[0] if len(so) > 0 else None
            if ao:
                mod = ao.modifiers.new("Array", "ARRAY")
                mod.fit_type = "FIXED_COUNT"
                mod.use_relative_offset = False
                mod.use_object_offset = True
                mod.offset_object = s
        return {'FINISHED'}


class MZageModifiersBevel(bpy.types.Operator):
    bl_idname = "object.mzage_modifiers_bevel"
    bl_label = "Bevel"
    bl_options = {'UNDO'}
    def execute(self, context):
        so = bpy.context.selected_objects
        for s in so:
            mod = s.modifiers.new("Bevel", "BEVEL")
        return {'FINISHED'}


class MZageModifiersBoolean(bpy.types.Operator):
    bl_idname = "object.mzage_modifiers_boolean"
    bl_label = "Boolean"
    bl_options = {'UNDO'}
    type: bpy.props.StringProperty(name="Type", default="JUSTADD")
    def execute(self, context):
        ao = bpy.context.active_object
        so = bpy.context.selected_objects
        if self.type == "JUSTADD":
            for s in so:
                mod = s.modifiers.new("Boolean", "BOOLEAN")
        elif self.type == "USESELECTED":
            if ao in so:
                so.remove(ao)
            if ao:
                if len(so) > 0:
                    for s in so:
                        mod = ao.modifiers.new("Boolean", "BOOLEAN")
                        mod.object = s
                        s.display_type = "WIRE"
                else:
                    mod = ao.modifiers.new("Boolean", "BOOLEAN")
        return {'FINISHED'}

class MZageModifiersCurve(bpy.types.Operator):
    bl_idname = "object.mzage_modifiers_curve"
    bl_label = "Curve"
    bl_options = {'UNDO'}
    type: bpy.props.StringProperty(name="Type", default="JUSTADD")
    position: bpy.props.BoolProperty(name="SetPosition", default=False)
    def execute(self, context):
        ao = bpy.context.active_object
        so = bpy.context.selected_objects
        if self.type == "JUSTADD":
            for s in so:
                mod = s.modifiers.new("Curve", "CURVE")
        elif self.type == "USESELECTED":
            so = [s for s in so if s.type == "CURVE"]
            if ao in so:
                so.remove(ao)
            s = so[0] if len(so) > 0 else None
            if ao and s:
                mod = ao.modifiers.new("Curve", "CURVE")
                mod.object = s
                if self.position:
                    ao.location = s.location
        return {'FINISHED'}

class MZageModifiersMirror(bpy.types.Operator):
    bl_idname = "object.mzage_modifiers_mirror"
    bl_label = "Mirror"
    bl_options = {'UNDO'}
    axis: bpy.props.StringProperty(name="Axis", default="X")
    def execute(self, context):
        so = bpy.context.selected_objects
        for s in so:
            mod = s.modifiers.new("Mirror", "MIRROR")
            mod.use_axis = ["X" in self.axis, "Y" in self.axis, "Z" in self.axis]
            mod.use_clip = True
            mod.merge_threshold = 0.0001
        return {'FINISHED'}

class MZageModifiersShrinkwrap(bpy.types.Operator):
    bl_idname = "object.mzage_modifiers_shrinkwrap"
    bl_label = "Shrinkwrap"
    bl_options = {'UNDO'}
    type: bpy.props.StringProperty(name="Type", default="JUSTADD")
    def execute(self, context):
        ao = bpy.context.active_object
        so = bpy.context.selected_objects
        if self.type == "JUSTADD":
            for s in so:
                mod = s.modifiers.new("Shrinkwrap", "SHRINKWRAP")
        elif self.type == "USESELECTED":
            if ao in so:
                so.remove(ao)
            if ao:
                for s in so:
                    mod = s.modifiers.new("Shrinkwrap", "SHRINKWRAP")
                    mod.target = ao
        return {'FINISHED'}

class MZageModifiersSolidify(bpy.types.Operator):
    bl_idname = "object.mzage_modifiers_solidify"
    bl_label = "Solidify"
    bl_options = {'UNDO'}
    def execute(self, context):
        so = bpy.context.selected_objects
        for s in so:
            mod = s.modifiers.new("Solidify", "SOLIDIFY")
        return {'FINISHED'}

class MZageModifiersSkin(bpy.types.Operator):
    bl_idname = "object.mzage_modifiers_skin"
    bl_label = "Skin"
    bl_options = {'UNDO'}
    def execute(self, context):
        so = bpy.context.selected_objects
        for s in so:
            mod = s.modifiers.new("Skin", "SKIN")
        return {'FINISHED'}





class MZageMenuOpener(bpy.types.Operator):
    bl_label = "Menu Opener"
    bl_idname = "wm.mzage_menu_opener"
    menu: bpy.props.StringProperty(name="Menu")
    def execute(self, context):
        bpy.ops.wm.call_menu(name=self.menu)
        return {'FINISHED'}

class MZageModifiersMirrorMenu(bpy.types.Menu):
    bl_label = "Mirror Menu"
    bl_idname = "OBJECT_MT_mzage_modifiers_mirror_menu"
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        col = row.column()
        col.operator("object.mzage_modifiers_mirror", text="X").axis = "X"
        col.operator("object.mzage_modifiers_mirror", text="Y").axis = "Y"
        col.operator("object.mzage_modifiers_mirror", text="Z").axis = "Z"
        col = row.column()
        col.operator("object.mzage_modifiers_mirror", text="XY").axis = "XY"
        col.operator("object.mzage_modifiers_mirror", text="YZ").axis = "YZ"
        col.operator("object.mzage_modifiers_mirror", text="XZ").axis = "XZ"
        col = row.column()
        col.operator("object.mzage_modifiers_mirror", text="XYZ").axis = "XYZ"


class MZageModifiersArrayMenu(bpy.types.Menu):
    bl_label = "Array Menu"
    bl_idname = "OBJECT_MT_mzage_modifiers_array_menu"
    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.operator("object.mzage_modifiers_array", text="By Count", icon="MOD_ARRAY").type = "COUNT"
        col.operator("object.mzage_modifiers_array", text="Fit Length", icon="ARROW_LEFTRIGHT").type = "LENGTH"
        col.operator("object.mzage_modifiers_array", text="Fit Curve", icon="OUTLINER_OB_CURVE").type = "CURVE"
        col.operator("object.mzage_modifiers_array", text="Object Offset", icon="OBJECT_DATA").type = "OBJECT"


class MZageModifiersBooleanMenu(bpy.types.Menu):
    bl_label = "Boolean Menu"
    bl_idname = "OBJECT_MT_mzage_modifiers_boolean_menu"
    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.operator("object.mzage_modifiers_boolean", text="Use Selected", icon="MOD_BOOLEAN").type = "USESELECTED"
        col.operator("object.mzage_modifiers_boolean", text="Just Add Boolean", icon="MODIFIER_ON").type = "JUSTADD"

class MZageModifiersShrinkwrapMenu(bpy.types.Menu):
    bl_label = "Shrinkwrap Menu"
    bl_idname = "OBJECT_MT_mzage_modifiers_shrinkwrap_menu"
    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.operator("object.mzage_modifiers_shrinkwrap", text="Use Selected", icon="MOD_SHRINKWRAP").type = "USESELECTED"
        col.operator("object.mzage_modifiers_shrinkwrap", text="Just Add Shrinkwrap", icon="MODIFIER_ON").type = "JUSTADD"

class MZageModifiersCurveMenu(bpy.types.Menu):
    bl_label = "Curve Menu"
    bl_idname = "OBJECT_MT_mzage_modifiers_curve_menu"
    def draw(self, context):
        layout = self.layout
        col = layout.column()
        op = col.operator("object.mzage_modifiers_curve", text="Use Selected", icon="MOD_CURVE")
        op.type = "USESELECTED"
        op.position = False
        op = col.operator("object.mzage_modifiers_curve", text="Use Selected And Set Position", icon="OUTLINER_OB_CURVE")
        op.type = "USESELECTED"
        op.position = True
        col.operator("object.mzage_modifiers_curve", text="Just Add Curve", icon="MODIFIER_ON").type = "JUSTADD"

class MZageModifiersMenu(bpy.types.Menu):
    bl_label = "Modifiers Menu"
    bl_idname = "OBJECT_MT_mzage_modifiers_menu"
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        col = row.column()
        col.operator("wm.mzage_menu_opener", text="Mirror", icon="MOD_MIRROR").menu = MZageModifiersMirrorMenu.bl_idname
        col.operator("wm.mzage_menu_opener", text="Array", icon="MOD_ARRAY").menu = MZageModifiersArrayMenu.bl_idname
        col.operator("wm.mzage_menu_opener", text="Boolean", icon="MOD_BOOLEAN").menu = MZageModifiersBooleanMenu.bl_idname
        col.operator("object.mzage_modifiers_bevel", text="Bevel", icon="MOD_BEVEL")
        col.separator()
        col.operator("object.mzage_modifiers_solidify", text="Solidify", icon="MOD_SOLIDIFY")
        col.operator("object.mzage_modifiers_skin", text="Skin", icon="MOD_SKIN")
        col.operator("wm.mzage_menu_opener", text="Shrinkwrap", icon="MOD_SHRINKWRAP").menu = MZageModifiersShrinkwrapMenu.bl_idname
        col.operator("wm.mzage_menu_opener", text="Curve", icon="MOD_CURVE").menu = MZageModifiersCurveMenu.bl_idname
        
        col = row.column()
        col.operator("object.mzage_modifiers_control", text="ExpandAll", icon="COLLAPSEMENU").operation = "EXPANDALL"
        col.operator("object.mzage_modifiers_control", text="CollapseAll", icon="COLLAPSEMENU").operation = "COLLAPSEALL"
        col.separator()
        col.operator("object.mzage_modifiers_control", text="ApplyAll", icon="IMPORT").operation = "APPLYALL"
        col.operator("object.mzage_modifiers_control", text="RemoveAll", icon="X").operation = "REMOVEALL"

