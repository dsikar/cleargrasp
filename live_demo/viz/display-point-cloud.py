# from open3d import *    
import open3d as o3d

def main():
    cloud = o3d.io.read_point_cloud("data/zivid_studio_capture.ply") # Read the point cloud
    cloud.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
    o3d.visualization.draw_geometries([cloud]) # Visualize the point cloud     

if __name__ == "__main__":
    main()
