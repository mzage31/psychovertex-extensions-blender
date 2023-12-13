import bpy
import bmesh
from bmesh.types import BMEdge

PRECISION = 5


def getUnitsInfo():
    scale = bpy.context.scene.unit_settings.scale_length
    unit_system = bpy.context.scene.unit_settings.system
    separate_units = bpy.context.scene.unit_settings.use_separate
    if unit_system == 'METRIC':
        scale_steps = ((1000, 'km', "KILOMETERS"), (1, 'm', "METERS"), (1 / 100, 'cm', "CENTIMETERS"),
                       (1 / 1000, 'mm', "MILIMETERS"), (1 / 1000000, '\u00b5m', "MICROMETERS"))
    elif unit_system == 'IMPERIAL':
        scale_steps = ((5280, 'mi', "MILES"), (1, '\'', "FEET"),
                       (1 / 12, '"', "INCHES"), (1 / 12000, 'thou', "THOU"))
        scale /= 0.3048  # BU to feet
    else:
        scale_steps = ((1, ' BU'),)
        separate_units = False
    return (scale, scale_steps, separate_units)


def convertDistance(val):
    units_info = getUnitsInfo()
    U = bpy.context.scene.unit_settings.length_unit
    scale, scale_steps, separate_units = units_info
    sval = val * scale
    idx = 0
    found = False
    while idx < len(scale_steps) - 1:
        if scale_steps[idx][2] == U:
            fount = True
            break
        idx += 1
    if not found:
        idx = 1

    factor, suffix, id = scale_steps[idx]
    sval /= factor
    if not separate_units or idx == len(scale_steps) - 1:
        dval = str(round(sval, PRECISION)) + suffix
    else:
        ival = int(sval)
        dval = str(round(ival, PRECISION)) + suffix
        fval = sval - ival
        idx += 1
        while idx < len(scale_steps):
            fval *= scale_steps[idx - 1][0] / scale_steps[idx][0]
            if fval >= 1:
                dval += ' ' \
                    + ("%.1f" % fval) \
                    + scale_steps[idx][1]
                break
            idx += 1
    return dval


class GetEdgeLengthOperator(bpy.types.Operator):
    bl_idname = "mesh.get_edge_length"
    bl_label = "Get Edge Length"

    def execute(self, context):
        ao = bpy.context.active_object
        aobm = bmesh.from_edit_mesh(ao.data)
        se = [e for e in aobm.edges if e.select]
        ae = None
        history_count = len(aobm.select_history)
        if history_count > 0:
            last_history = aobm.select_history[history_count - 1]
            print(type(last_history))
            if isinstance(last_history, BMEdge):
                ae = last_history

        selected_length = 0
        for e in se:
            selected_length += e.calc_length()

        acl = ""
        if ae != None:
            acl = f"Active: {convertDistance(ae.calc_length())} | "
        self.report({'INFO'}, f"{acl}Total: {convertDistance(selected_length)}")

        return {'FINISHED'}


def register():
    bpy.utils.register_class(GetEdgeLengthOperator)


def unregister():
    bpy.utils.unregister_class(GetEdgeLengthOperator)
