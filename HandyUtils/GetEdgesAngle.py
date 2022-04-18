import bpy
import bmesh
from mathutils import Vector
import math

PRECISION = 5

class GetEdgesAngleOperator(bpy.types.Operator):
    bl_idname = "mesh.get_edges_angle"
    bl_label = "Get Edges Angle"
    
    def execute(self, context):
        ao = bpy.context.active_object
        aobm = bmesh.from_edit_mesh(ao.data)
        se = [e for e in aobm.edges if e.select]
        
        if len(se) != 2:
            self.report({'ERROR'}, "Please only select 2 edges")
            return {'CANCELLED'}
        
        v00 = se[0].verts[0]
        v01 = se[0].verts[1]
        v10 = se[1].verts[0]
        v11 = se[1].verts[1]

        v0 = Vector(v00.co) - Vector(v01.co)
        v1 = Vector(v10.co) - Vector(v11.co)

        angle = v0.angle(v1)
        angle = round(math.degrees(angle), PRECISION)

        if angle >= 360:
            angle = angle - 360
        elif angle >= 180:
            angle = angle - 180
        elif angle > 90 and angle < 180:
            angle = 180 - angle
        
        self.report({'INFO'}, f"Angle: {angle}")
        
        return {'FINISHED'}
