# from open3d import *
import open3d as o3d
# import matplotlib.pyplot as plt
import numpy as np
import argparse
import cv2

def generate_point_cloud(rgb, depth, camera, depth_type):
    """
    Generate a point cloud from RGB and Depth acquisitions
    Inputs
        rgb: path to RGB file
        depth: path to depth file
        camera: camera model
        depth_type: depth file type
    Outputs:
        none
    Example:
    generate_point_cloud('../zivid_color_img.npy', '../zivid_input_depth.npy', 'zivid', 'acquired')
    """
    #with open('../zivid_color_img.npy', 'rb') as f:
    #        color_raw = np.load(f)       
    #with open('../zivid_input_depth.npy', 'rb') as f:
    #        depth_raw = np.load(f) 
    
    with open(rgb, 'rb') as f:
        color_raw = np.load(f)       
    with open(depth, 'rb') as f:
        depth_raw = np.load(f) 
        
    # For predicted depth, resize image to match predicted depth size        
    if(depth_type == "predicted") :
        #print("Shape before resizing ", color_img.shape)
        color_raw = cv2.resize(color_raw, (256, 144))
        #print("Shape after resizing ", resized_image.shape)
        #print("type(resized_image) ", type(resized_image))
    
    # from config.yaml
    #  xres: 256  # Image Output Width
    #  yres: 144  # Image Output Height
    #  fx: 185  # Focal length in pixels along width
    #  fy: 185  # Focal length in pixels along height
    #  cx: 128  # Center of image in pixels along width
    #  cy: 72   # Center of image in pixels along height
    
    # TODO
    # If depth_type == 'predicted':
    # 1. resized array to 144 (H) x 256 (D)
    # 2. set camera intrinsics to 185, 185, 128, 72
    
    color_raw = o3d.geometry.Image(np.array(np.asarray(color_raw)[:, :, :3]).astype('uint8'))
    depth_raw = o3d.geometry.Image(np.expand_dims(depth_raw, axis=2))
    
    #rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(
    #        color_raw, depth_raw, convert_rgb_to_intensity=False)
    
    
    #print(rgbd_image)
    
    #plt.subplot(1, 2, 1)
    #plt.title('Grayscale image')
    #plt.imshow(rgbd_image.color)
    #plt.subplot(1, 2, 2)
    #plt.title('Depth image')
    #plt.imshow(rgbd_image.depth)
    #plt.show()
    
    #print("Type rgbd_image.depth: ", type(rgbd_image.depth))
    #myarrdepth = np.asarray(rgbd_image.depth)
    #myarrcolour = np.asarray(rgbd_image.color)
    
    #print("Shape rgbd_image.depth: ", myarrdepth.shape)
    #print("Shape rgbd_image.color: ", myarrcolour.shape)
    
    if(camera == 'zivid') :
        # Zivid camera intrinsics
        fx, fy, cx, cy = 2763.10400390625, 2763.77685546875, 963.131469726562, 595.361694335938
        
    elif(camera == 'd415') :
        # d415 camera intrinsics
        fx, fy, cx, cy = 923.93823, 923.2997, 651.2283, 373.53592
    else :
        raise NameError('Unknown camera: {}'.format(camera))
    
    # for predicted depth camera intrinsics are assumed the same in both cases
    if(depth_type == 'predicted') :
        fx, fy, cx, cy = 185, 185, 128, 72
        
    
    #  fx: 185  # Focal length in pixels along width
    #  fy: 185  # Focal length in pixels along height
    #  cx: 128  # Center of image in pixels along width
    #  cy: 72   # Center of image in pixels along height
        
    #    realsense_fx = 2763.10400390625 # 923.93823 # camera_intrinsics[0, 0]
    #    realsense_fy = 2763.77685546875 # 923.2997 # camera_intrinsics[1, 1]
    #    realsense_cx = 963.131469726562 # 651.2283 # camera_intrinsics[0, 2]
    #    realsense_cy = 595.361694335938 # 373.53592 # camera_intrinsics[1, 2]
        
    #intrinsic = o3d.camera.PinholeCameraIntrinsic(
    #            o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault)
    
    intrinsic = o3d.camera.PinholeCameraIntrinsic(int(cx*2), int(cy*2), fx, fy, cx, cy)
    
    # intrinsic = 03d.camera.intrinsic_matrix[[923.93823, 0, 651.2283],[0, 923.2997, 373.53592],[0,0,1]]
    rgbd = o3d.geometry.RGBDImage.create_from_color_and_depth(color_raw, depth_raw, depth_scale=1.0, depth_trunc=10.0, convert_rgb_to_intensity=False)
    pcd = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd, intrinsic)
    
    
#    if(camera == 'zivid') :
        # flip the orientation, so it looks upright, not upside-down
    pcd.transform([[1,0,0,0],[0,-1,0,0],[0,0,-1,0],[0,0,0,1]])
    
    # draw_geometries([pcd])    # visualize the point cloud
    o3d.visualization.draw_geometries([pcd])



if __name__ == "__main__":
    """
    Point Cloud 0pen 3D Generator
    Example:
    python create-point-cloud.py --rgb=../zivid_color_img.npy --depth=../zivid_input_depth.npy --camera=zivid --depth_type=acquired
    """
    # '../zivid_color_img.npy', '../zivid_input_depth.npy', 'zivid', 'acquired'
    parser = argparse.ArgumentParser(description='Point Cloud  O3D Generator')
    parser.add_argument('--rgb', type=str, help='RGB filename')
    parser.add_argument('--depth', type=str, help='Depth filename')
    parser.add_argument('--camera', type=str, default='zivid', help = 'Camera model: d415 / zivid')
    parser.add_argument('--depth_type', type=str, default='acquired', help='acquired / predicted depth')

    args = parser.parse_args()

    generate_point_cloud(args.rgb, args.depth, args.camera, args.depth_type)
    

