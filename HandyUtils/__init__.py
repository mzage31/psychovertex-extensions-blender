import bpy
from .SetOriginToSelection import SetOriginToSelectionOperator
from .GetEdgeLength import GetEdgeLengthOperator
from .SnapVerticesToSurface import SnapVerticesToSurfaceOperator, register as r1, unregister as u1
from .SelectOverlappingVertices import SelectOverlappingVerticesOperator, register as r2, unregister as u2
from .GetEdgesAngle import GetEdgesAngleOperator

def register():
    r1()
    r2()

def unregister():
    u1()
    u2()
    
    