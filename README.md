# PsychoVertexMaster
Handy menus and tools to work easier in blender!

## Handy menu
This menu can be accessed with 'D' key in the 3d view.

### Object mode
![163819780-4f36e33e-708e-42d5-a28d-2b14cfe4851c](https://user-images.githubusercontent.com/13370906/163830785-afdd2435-04c8-4a55-b28f-7e276dcdda60.png)

<table>
    <thead>
        <tr>
            <th>Section</th>
            <th>Option</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=3>Object</td>
            <td>Display As</td>
            <td>Change object's display type to Textured, Solid, Wire or Bounds</td>
        </tr>
        <tr>
            <td>Auto Smooth</td>
            <td>Toggle object's auto smoothing</td>
        </tr>
        <tr>
            <td>Create Empty Parent</td>
            <td>Create an empty object at active object's origin and assigns it as parent for selected objects</td>
        </tr>
        <tr>
            <td rowspan=2>Copy From Active</td>
            <td>Copy Modifiers</td>
            <td>Copy modifiers from active object to selected objects</td>
        </tr>
        <tr>
            <td>Copy Materials</td>
            <td>Copy materials from active object to selected objects</td>
        </tr>
        <tr>
            <td rowspan=3>Display Overlays</td>
            <td>Show Overlays</td>
            <td>Toggle overlays in current space</td>
        </tr>
        <tr>
            <td>Wireframe</td>
            <td>Toggle wireframe overlay in current space</td>
        </tr>
        <tr>
            <td>Face Orientation</td>
            <td>Toggle face orientation overlay in current space</td>
        </tr>
        <tr>
            <td rowspan=2>Import/Export</td>
            <td>Import FBX</td>
            <td>Import fbx file</td>
        </tr>
        <tr>
            <td>Export FBX</td>
            <td>Export fbx file</td>
        </tr>
    </tbody>
</table>


### Edit mode

| Vertex Mode | Edge Mode | Face Mode |
| --- | --- | --- |
| ![image](https://user-images.githubusercontent.com/13370906/163831194-04f018ce-cb80-4b7a-8004-2e658a0eab80.png) | ![image](https://user-images.githubusercontent.com/13370906/163832179-8580cd65-ad70-4ff7-b4b4-410af2dce623.png) | ![image](https://user-images.githubusercontent.com/13370906/163832282-9a2d06a3-f0cf-47e7-ba23-f4369421c497.png) |


<table>
   <thead>
      <tr>
         <th>Section</th>
         <th>Option</th>
         <th>Description</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td rowspan=5>UV</td>
         <td>Mark Seam</td>
		 <td>Self explanatory</td>
      </tr>
      <tr>
         <td>Clear Seam</td>
		 <td>Self explanatory</td>
      </tr>
      <tr>
         <td>Unwrap</td>
		 <td>Self explanatory</td>
      </tr>
      <tr>
         <td>View Project</td>
		 <td>Self explanatory</td>
      </tr>
      <tr>
         <td>Reset</td>
		 <td>Self explanatory</td>
      </tr>
      <tr>
         <td rowspan=3>Mesh</td>
         <td>Set Flow</td>
         <td>This option is only enabled in edge mode if <a href="https://github.com/BenjaminSauder/EdgeFlow">Edge Flow addon</a> is present</td>
      </tr>
      <tr>
         <td>Mark Sharp</td>
		 <td>Self explanatory</td>
      </tr>
      <tr>
         <td>Clear Sharp</td>
		 <td>Self explanatory</td>
      </tr>
      <tr>
         <td rowspan=4>Normals</td>
         <td>Flip</td>
		 <td>Self explanatory</td>
      </tr>
      <tr>
         <td>Recalculate</td>
		 <td>Self explanatory</td>
      </tr>
      <tr>
         <td>Rotate</td>
		 <td>Self explanatory</td>
      </tr>
      <tr>
         <td>Reset</td>
		 <td>Self explanatory</td>
      </tr>
      <tr>
         <td rowspan=7>Selection</td>
         <td>Select Rings</td>
		 <td>Self explanatory</td>
      </tr>
      <tr>
         <td>Select Loops</td>
		 <td>Self explanatory</td>
      </tr>
      <tr>
         <td>Select Boundary</td>
		 <td>Self explanatory</td>
      </tr>
      <tr>
         <td>Select Inside</td>
		 <td>Self explanatory</td>
      </tr>
      <tr>
         <td>Checker Deselect</td>
		 <td>Self explanatory</td>
      </tr>
      <tr>
         <td>Select Coplanar</td>
		 <td>Self explanatory</td>
      </tr>
      <tr>
         <td>Overlapping Vertices</td>
         <td>Find overlapping vertices before removing them using "Merge By Distance"</td>
      </tr>
      <tr>
         <td rowspan=4>Utils</td>
         <td>Set Origin to Selection</td>
         <td>Set origin of the active object to selected vertices</td>
      </tr>
      <tr>
         <td>Get Edge Length</td>
         <td>Show active edge's length and total length of selected edges</td>
      </tr>
      <tr>
         <td>Get Edges Angle</td>
         <td>Show angle in between selected edges</td>
      </tr>
      <tr>
         <td>Snap Vertices To Surface</td>
         <td>Snap selected vertices along global axis to additionaly selected object in edit mode.<br/>(Works like knife project)</td>
      </tr>
   </tbody>
</table>

## Modifiers Menu
This menu can be accessed with 'W' key in the 3d view.
Works both in object and edit mode.

![image](https://user-images.githubusercontent.com/13370906/163840002-6f001558-15e0-41c4-bf0e-d5f9f89b73df.png)

<table>
   <thead>
      <tr>
         <th>Modifier</th>
         <th>Sub Menu</th>
         <th>Description</th>
      </tr>
   </thead>
   <tbody>
      <tr>
        <td>Mirror</td>
        <td><img src="https://user-images.githubusercontent.com/13370906/163844147-1a875874-9115-4cd7-be22-783dca9cc1dd.png"/></td>
        <td>Adds mirror modifier to selected objects in selected axis with clipping and edge enabled at 0.0001m</td>
      </tr>
      <tr>
        <td>Array</td>
        <td><img src="https://user-images.githubusercontent.com/13370906/163845319-4317ee8c-b4b8-42f4-863f-42c597fb7c98.png"/></td>
        <td>
          Adds array modifier to:<br/>
          <b>By Count:</b> <em>Selected objects</em> and sets fit type to "Fixed Count".<br/>
          <b>Fit Length:</b> <em>Selected objects</em> and sets fit type to "Fit Length" with length as 2m.<br/>
          <b>Fit Curve:</b> <em>Active object</em> and sets fit type to "Fit Curve" and assigns target if curve selected.<br/>
          <b>Object Offset:</b> <em>Active object</em> and sets fit type to "Fixed Count" and assigns target if another object is selected.<br/>
        </td>
      </tr>
      <tr>
        <td>Boolean</td>
        <td><img src="https://user-images.githubusercontent.com/13370906/163847347-1c1843ef-3317-4b00-b467-964407669f0d.png"/></td>
        <td>
          <b>Use Selected</b>: Uses selected objects as boolean targets for the active object.<br/>
          <b>Just Add Boolean</b>: Adds boolean with empty targets to all selected objects.<br/>
        </td>
      </tr>
      <tr>
        <td>Bevel</td>
        <td>Doesn't have submenu</td>
        <td>Adds bevel modifier to selected objects.</td>
      </tr>
      <tr>
        <td>Solidify</td>
        <td>Doesn't have submenu</td>
        <td>Adds solidify modifier to selected objects.</td>
      </tr>
      <tr>
        <td>Skin</td>
        <td>Doesn't have submenu</td>
        <td>Adds skin modifier to selected objects.</td>
      </tr>
      <tr>
        <td>Shrinkwrap</td>
        <td><img src="https://user-images.githubusercontent.com/13370906/163847466-610b251a-eb80-49fc-84b7-01e99d0d9b1a.png"/></td>
        <td>
          <b>Use Selected</b>: Adds shrinkwrap to all selected objects except the active object, with active object as target.<br/>
          <b>Just Add Shrinkwrap</b>: Adds shrinkwrap with empty targets to all selected objects.<br/>
        </td>
      </tr>
      <tr>
        <td>Curve</td>
        <td><img src="https://user-images.githubusercontent.com/13370906/163847518-7e02e3c5-6294-4b7b-a33b-f0175e16498a.png"/></td>
        <td>
          <b>Use Selected</b>: Adds curve modifier to active object and uses selected curve as target only if a curve is selected.<br/>
          <b>Use Selected And Set Position</b>: Moves active object to selected curve's location and adds curve modifier to it with the curve as target only if a curve is selected.<br/>
          <b>Just Add Curve</b>: Adds curve with empty targets to all selected objects.<br/>
        </td>
      </tr>
      <tr>
        <td>ExpandAll</td>
        <td>Doesn't have submenu</td>
        <td>Expands all items in modifiers menu for selected objects.</td>
      </tr>
      <tr>
        <td>CollapseAll</td>
        <td>Doesn't have submenu</td>
        <td>Collapses all items in modifiers menu for selected objects.</td>
      </tr>
      <tr>
        <td>ApplyAll</td>
        <td>Doesn't have submenu</td>
        <td>Applies all modifiers on selected objects.</td>
      </tr>
      <tr>
        <td>RemoveAll</td>
        <td>Doesn't have submenu</td>
        <td>Removes all modifiers from selected objects.</td>
      </tr>
   </tbody>
</table>

