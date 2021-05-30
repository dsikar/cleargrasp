# from open3d import *    
import open3d as o3d
import argparse

def render_point_cloud(filename, transform):
    """
    Render point cloud using Open3D
    Inputs
        filename: string, point cloud file
        transform: string, flag to change point of view
    Outputs
        none
    Example
    python display-point-cloud.py --file RealSenseViewerPointCloudCapture.plyi --transform False
    """
    cloud = o3d.io.read_point_cloud(filename) # Read the point cloud
    if (transform == "True"):
       cloud.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
    o3d.visualization.draw_geometries([cloud]) # Visualize the point cloud     

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Open3D Point Cloud Renderer')
    parser.add_argument('--file', type=str, help='model filename')
    parser.add_argument('--transform', type=str, help='Transform POV flag')
    args = parser.parse_args()
    render_point_cloud(args.file, args.transform)

