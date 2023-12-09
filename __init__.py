from .HandyUtils.BlenderToUnreal import BTUS_Setup_Operator, BTUS_Export_Operator, BTUS_DontExport_Operator, BTUS_UpdatePath_Operator
from .HandyUtils.BatchExport import BatchExportSelectionsAsSMOperator
from .HandyUtils import (SetOriginToSelectionOperator,
                         SetOriginToSelectionAndRotateOperator,
                         GetEdgeLengthOperator,
                         GetEdgesAngleOperator,
                         SnapVerticesToSurfaceOperator,
                         SelectOverlappingVerticesOperator,
                         SelectedOriginsToActiveOperator,
                         register as utilsregister,
                         unregister as utilsunregister)
from .UvTools import (register as uvtoolsregister, unregister as uvtoolsunregister,
                      UvToolsMoveUVMapDownOperator,
                      UvToolsMoveUVMapUpOperator,
                      UvToolsRenameOperator,
                      UvToolsSelectOperator,
                      UvToolsAddOperator,
                      UvToolsRemoveOperator,
                      UvToolsProperties)
from .HandyMenu import MZageHandyMenu, MZageHandyMenuSelectWeight, MZageHandyMenuSetWeight
from .ChildControl import ChildToggleOperator, ChildControlPanel
from .ModifiersMenu import *
from .AddMaterialToSelectedFaces import AddMaterialToSelectedFacesOperator
from .CreateEmptyParent import CreateEmptyParentOperator
import bpy

bl_info = {
    "name": "PsychoVertex Pipeline Addons",
    "category": "3D View",
    "author": "Mohammad Zamanian",
    "description": "A collection of addons we use in our pipeline at PsychoVertex",
    "location": "3D View > 'W' and 'D' keymaps",
    "version": (1, 2, 1),
    "blender": (3, 0, 0),
}


properties = [
    UvToolsProperties
]
operators = [
    CreateEmptyParentOperator,
    AddMaterialToSelectedFacesOperator,
    ChildToggleOperator,

    MZageModifiersControl,
    MZageModifiersArray,
    MZageModifiersBevel,
    MZageModifiersBoolean,
    MZageModifiersCurve,
    MZageModifiersMirror,
    MZageModifiersShrinkwrap,
    MZageModifiersSolidify,
    MZageModifiersSkin,


    UvToolsMoveUVMapDownOperator,
    UvToolsMoveUVMapUpOperator,
    UvToolsRenameOperator,
    UvToolsSelectOperator,
    UvToolsAddOperator,
    UvToolsRemoveOperator,

    SetOriginToSelectionOperator,
    SetOriginToSelectionAndRotateOperator,
    GetEdgeLengthOperator,
    GetEdgesAngleOperator,
    SnapVerticesToSurfaceOperator,
    SelectOverlappingVerticesOperator,
    SelectedOriginsToActiveOperator,
    BTUS_Setup_Operator,
    BTUS_Export_Operator,
    BTUS_DontExport_Operator,
    BTUS_UpdatePath_Operator,
    BatchExportSelectionsAsSMOperator,

    MZageHandyMenuSelectWeight,
    MZageHandyMenuSetWeight,
]
menus = [
    MZageMenuOpener,
    MZageModifiersMirrorMenu,
    MZageModifiersArrayMenu,
    MZageModifiersBooleanMenu,
    MZageModifiersShrinkwrapMenu,
    MZageModifiersCurveMenu,
    MZageModifiersMenu,

    ChildControlPanel,
    MZageHandyMenu,
]
classes = []
classes.extend(properties)
classes.extend(operators)
classes.extend(menus)
addon_keymaps = []


def register():
    for c in classes:
        bpy.utils.register_class(c)

    uvtoolsregister()
    utilsregister()

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
        kmi = km.keymap_items.new('wm.call_menu', 'D', 'PRESS', ctrl=False, shift=False, alt=False)
        kmi.properties.name = MZageHandyMenu.bl_idname
        addon_keymaps.append((km, kmi))
        kmi = km.keymap_items.new('wm.call_menu', 'W', 'PRESS', ctrl=False, shift=False, alt=False)
        kmi.properties.name = MZageModifiersMenu.bl_idname
        addon_keymaps.append((km, kmi))


def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)

    uvtoolsunregister()
    utilsunregister()

    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()


if __name__ == "__main__":
    register()
