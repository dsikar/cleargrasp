# from open3d import *
import open3d as o3d
import matplotlib.pyplot as plt
import numpy as np

#color_raw = o3d.io.read_image("color.png")
#depth_raw = o3d.io.read_image("depth.png")
# this works!
#color_raw = o3d.geometry.Image(np.array(np.asarray(color_raw)[:, :, :3]).astype('uint8'))
#depth_raw = o3d.geometry.Image(np.array(np.asarray(depth_raw)[:, :,1:2]).astype('float32'))
# no joy with expaning dims
#color_raw = o3d.io.read_image("001_color.png")
#depth_raw = o3d.io.read_image("001_depth.png")
with open('../zivid_color_img.npy', 'rb') as f:
        color_raw = np.load(f)       
with open('../zivid_input_depth.npy', 'rb') as f:
        depth_raw = np.load(f) 

color_raw = o3d.geometry.Image(np.array(np.asarray(color_raw)[:, :, :3]).astype('uint8'))
depth_raw = o3d.geometry.Image(np.expand_dims(depth_raw, axis=2))

rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(
        color_raw, depth_raw)


print(rgbd_image)

plt.subplot(1, 2, 1)
plt.title('Redwood grayscale image')
plt.imshow(rgbd_image.color)
plt.subplot(1, 2, 2)
plt.title('Redwood depth image')
plt.imshow(rgbd_image.depth)
plt.show()

print("Type rgbd_image.depth: ", type(rgbd_image.depth))
myarrdepth = np.asarray(rgbd_image.depth)
myarrcolour = np.asarray(rgbd_image.color)

print("Shape rgbd_image.depth: ", myarrdepth.shape)
print("Shape rgbd_image.color: ", myarrcolour.shape)

intrinsic = o3d.camera.PinholeCameraIntrinsic(
            o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault)
# intrinsic = 03d.camera.intrinsic_matrix[[923.93823, 0, 651.2283],[0, 923.2997, 373.53592],[0,0,1]]
rgbd = o3d.geometry.RGBDImage.create_from_color_and_depth(color_raw, depth_raw)
pcd = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd, intrinsic)

# flip the orientation, so it looks upright, not upside-down
# pcd.transform([[1,0,0,0],[0,-1,0,0],[0,0,-1,0],[0,0,0,1]])

# draw_geometries([pcd])    # visualize the point cloud
o3d.visualization.draw_geometries([pcd])
