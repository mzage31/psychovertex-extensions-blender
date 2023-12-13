import bpy
from . import HandyUtils
from . import UvTools
from . import HandyMenu
from . import ChildControl
from . import ModifiersMenu
from . import AddMaterialToSelectedFaces
from . import CreateEmptyParent

bl_info = {
    "name": "PsychoVertex Pipeline Addons",
    "category": "3D View",
    "author": "Mohammad Zamanian",
    "location": "3D View > 'W' and 'D' keymaps",
    "version": (1, 2, 1),
    "blender": (3, 0, 0),
}

keymaps = []


def register():
    HandyUtils.register()
    UvTools.register()
    HandyMenu.register()
    ChildControl.register()
    ModifiersMenu.register()
    AddMaterialToSelectedFaces.register()
    CreateEmptyParent.register()

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')

        kmi = km.keymap_items.new('wm.call_menu', 'D', 'PRESS', ctrl=False, shift=False, alt=False)
        kmi.properties.name = HandyMenu.MZageHandyMenu.bl_idname
        keymaps.append((km, kmi))

        kmi = km.keymap_items.new('wm.call_menu', 'W', 'PRESS', ctrl=False, shift=False, alt=False)
        kmi.properties.name = ModifiersMenu.MZageModifiersMenu.bl_idname
        keymaps.append((km, kmi))


def unregister():
    HandyUtils.unregister()
    UvTools.unregister()
    HandyMenu.unregister()
    ChildControl.unregister()
    ModifiersMenu.unregister()
    AddMaterialToSelectedFaces.unregister()
    CreateEmptyParent.unregister()

    for km, kmi in keymaps:
        km.keymap_items.remove(kmi)
    keymaps.clear()


if __name__ == "__main__":
    register()
