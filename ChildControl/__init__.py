import bpy
from collections import Counter

def all_children(o):
    children = [o]
    for child in o.children:
        children.extend(all_children(child))
    return children

def parent_collections(collection, parents):
  for parent_collection in bpy.data.collections:
    if collection.name in parent_collection.children.keys():
      parents.append(parent_collection)
      parent_collections(parent_collection, parents)
      return

def hide_select(o):
    collections = [o.users_collection[0]]
    parent_collections(collections[0], collections)
    for col in collections:
        if col.hide_select:
            return True
    return o.hide_select

class ChildToggleOperator(bpy.types.Operator):
    bl_idname = "object.child_control"
    bl_label = "Button"
    bl_options = {"UNDO"}

    type: bpy.props.StringProperty(name="type")
    target: bpy.props.StringProperty(name="target")

    def execute(self, context):
        if self.type == "TOGGLE":
            for object in bpy.data.objects:
                if object.name == self.target:
                    children = all_children(object)
                    showing = len([c for c in children if not c.hide_viewport])
                    hiding = len(children) - showing
                    must_hide = hiding < showing
                    for child in children:
                        child.hide_viewport = must_hide
        elif self.type == "SELECT":
            targetObject = bpy.data.objects[self.target]
            if not targetObject.hide_viewport:
                bpy.ops.object.select_all(action='DESELECT')
                targetObject.select_set(True)
                context.view_layer.objects.active = targetObject
        elif self.type == "RENAME":
            ao = context.active_object
            targetObject = bpy.data.objects[self.target]
            context.view_layer.objects.active = targetObject
            bpy.ops.wm.call_panel(name="TOPBAR_PT_name", keep_open=False)
            context.view_layer.objects.active = ao
        return {'FINISHED'}

class ChildControlPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Child Control"
    bl_idname = "SCENE_PT_childcontrol"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        all = bpy.data.objects
        selected = bpy.context.selected_objects
        
        data = {}
        for s in selected:
            childCount = 0
            for child in s.children:
                if hide_select(child):
                    continue
                childCount+=1
            if childCount > 0:
                groups = {}
                for child in s.children:
                    if hide_select(child):
                        continue
                    group = child.name.split("_")[0]
                    if group in groups:
                        groups[group].append(child)
                    else:
                        groups[group] = [child]
                data[s] = groups
        
        col = layout.column()
        for d in data:
            for group in data[d].copy():
                if len(data[d][group]) > 1:
                    continue
                obj = data[d][group][0]
                if "Other" in groups:
                    groups["Other"].append(obj)
                else:
                    groups["Other"] = [obj]
                data[d].pop(group)
        
        col = layout.column()
        for d in data:
            col.label(text=f"{d.name}'s Children:")
            for group in data[d]:
                box = col.box()
                box.label(text=group + "s" if group[-1] != "s" else group)
                for child in data[d][group]:
                    n = child.name
                    row = box.row(align=True)
                    c = row.column(align=True)
                    c.enabled = False
                    c.prop(child, "hide_viewport", text="")
                    
                    btn = row.operator("object.child_control", text=n)
                    btn.type = "TOGGLE"
                    btn.target = n

                    btn = row.operator("object.child_control", text="", icon="GREASEPENCIL")
                    btn.type = "RENAME"
                    btn.target = n
                    
                    c = row.column(align=True)
                    c.enabled = not bpy.data.objects[n].hide_viewport
                    btn = c.operator("object.child_control", text="", icon="RESTRICT_SELECT_OFF" if c.enabled else "RESTRICT_SELECT_ON")
                    btn.type = "SELECT"
                    btn.target = n
