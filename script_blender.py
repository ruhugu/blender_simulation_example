import bpy
import numpy as np

# Clear previously loaded objects
for obj in bpy.context.scene.objects:
    obj.select_set(obj.type == "MESH")
bpy.ops.object.delete()

# Load array containing the positions of particles
# Structure: 2D array where each row represents the x-positions of 
#            all particles at a specific time step
pos_prtcls_list = np.load(
        "/home/ruben/Proyectos/FPUT_animation/animation_short.npy")

# Count number of particles
nprtcls = pos_prtcls_list.shape[1]
        
# Set particle radius
r_sphere = 0.5

# Create list of sphere objects representing each particle
spheres = list()
for j_sphere in range(nprtcls):
    # Create sphere with radius r_sphere at the origin
    bpy.ops.mesh.primitive_uv_sphere_add(location=(0, 0, 0), radius=r_sphere)  
    bpy.ops.object.shade_smooth() # This makes the sphere smooth
    # Get sphere object and append it to the list
    sphere = bpy.context.object
    spheres.append(sphere) 
    
# Define the particle's position at each frame
for j_frame, pos_prtcls in enumerate(pos_prtcls_list):
    # Set frame number
    bpy.context.scene.frame_set(2*j_frame) # I skip one frame so that blender can interpolate

    # Set the spheres' position in the keyframe
    for sphere, pos in zip(spheres, pos_prtcls):
        sphere.location = (pos, 0, 0)

        # Add to keyframe
        sphere.keyframe_insert(data_path="location", index=-1)
