# Project b3dBarChart

# Import the CSV Reader library and blender python library
import csv
import bpy
import colorsys

# Delete the defauly cube and lamp (we'll use ambient lighting)
#bpy.ops.object.delete(use_global=False)

# Read the CSV file into a csv.reader object
with open('D:/00_Dev/b3dBarChart/sample3dMatrix.csv', newline='') as csvfile:
    chartDataReader = csv.reader(csvfile, delimiter=',', quotechar='"')
    
    # Define my looping variables
    i = 0
    j = 0
    
    # Create a cube for each bar in the chart and scale to the data point value
    for row in chartDataReader:
        for cell in row:

            # Create a new cube at the size and location desired
            bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(i*0.25, j*0.25, 0), rotation=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
            
            # Scale my newly created mesh to fit in the camera's view distance
            bpy.ops.transform.resize(value=(0.1, 0.1, 0.1), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), texture_space=False, release_confirm=False)
            
            #### Now the hard part - we need to select the uppermost face then transform it in edit mode
            # Start by jumping into edit mode, deselecting all nodes, then dropping back to object mode
            bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.select_all(action='TOGGLE')
            bpy.ops.object.editmode_toggle()
            
            # Now in object mode use the data block to select the vertices
            bpy.context.active_object.data.vertices[4].select = True
            bpy.context.active_object.data.vertices[5].select = True
            bpy.context.active_object.data.vertices[6].select = True
            bpy.context.active_object.data.vertices[7].select = True
            
            # Enter edit mode
            bpy.ops.object.editmode_toggle()
            
            # Select the uppermost face (to be moved upwards in forming the chart)
            #bpy.ops.mesh.select_axis(mode='POSITIVE', axis='Z_AXIS')      
            
            # Move the top face upwards to the desired height for the bar
            bpy.ops.transform.translate(value=(0, 0, float(cell)*50), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), texture_space=False, release_confirm=False)
            
            # Swap back to object mode
            bpy.ops.object.editmode_toggle()

            # Create the new material
            myMatName = str(i) + '-' + str(j)
            myMat = bpy.data.materials.new(myMatName)
            
            # Set the new material's colour
            # luminence ranges from 90 (dark) to 180 (light)
            # Hue rolls from 0 to 255 in increments of 255/len(row)
            myHSLColors = (j*(1/len(row)),0.5,(90/255)+((90/255)*(i/len(row))))
            myRGBColors = colorsys.hls_to_rgb(myHSLColors[0], myHSLColors[1], myHSLColors[2])
            myMat.diffuse_color = myRGBColors
            
            # Append the material to the object
            bpy.context.object.data.materials.append(myMat)
            
            # Iterate data point in the loop
            i = i+1
        
        # Iterate to the next y-row and reset x counter    
        j = j+1
        i=0

# Set the render variables (white background, ambient occlusion, environment lighting, indirect lighting
#WorldLighting.use_ambient_occlusion
#WorldLighting.use_environment_light
#WorldLighting.use_indirect_light


# Produce a bunch of renders from different angles



# Generate a 360 orbiting camera view of the chart for embedding in powerpoint