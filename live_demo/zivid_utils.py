"""
Zivid utils
"""

import numpy as np
import zivid
import datetime
from zivid import Application, Settings
import cv2


def get_zivid_rgb_depth():
    """
    Get rgb and depth arrays from Zivid capture
    Outputs
        zivid_rgb: numpy.uint8 (720, 1280, 3) array
        zivid_input_depth: numpy.float32 (720, 1280) array
    Example
        zivid_rgb, zivid_input_depth = get_zivid_rgb_depth()
    """
    # init app
    app = zivid.Application()

    # capture frame
    camera = app.connect_camera()
    settings = Settings()
    settings.acquisitions.append(Settings.Acquisition())
    settings.acquisitions[0].aperture = 2.6 # 5.6
    settings.acquisitions[0].exposure_time = datetime.timedelta(microseconds=11500) #8333)
    settings.processing.filters.outlier.removal.enabled = True
    settings.processing.filters.outlier.removal.threshold = 5.0
    frame = camera.capture(settings)

    # get data from file - to debug
    # data_file = "result.zdf"
    # print(f"Reading ZDF frame from file: {data_file}")
    # frame = zivid.Frame(data_file)

    point_cloud = frame.point_cloud()
    # get rgb data
    rgba = point_cloud.copy_data("rgba")
    rgb = rgba[:, :, 0:3]
    zivid_rgb = cv2.resize(rgb, (1280, 720))
    # get depth data
    z = frame.point_cloud().copy_data("z")
    zivid_input_depth = np.asarray(z)
    zivid_input_depth = cv2.resize(zivid_input_depth, (1280, 720))

    # remove nans
    zivid_input_depth = np.nan_to_num(zivid_input_depth)
    sf = 18.368 / np.amax(zivid_input_depth) # approximate maximum observed in D415 depth divided by zivid maximum
    scaled_zivid_input_depth = zivid_input_depth * sf
    # print("type(zivid_input_depth): ", type(zivid_input_depth))
    # print("zivid_input_depth.shape: ", zivid_input_depth.shape)
    # print("type(zivid_input_depth[0, 0]: ", type(zivid_input_depth[0, 0]))

    # print("type(zivid_rgb): ", type(zivid_rgb))
    # print("zivid_rgb.shape: ", zivid_rgb.shape)
    # print("type(zivid_rgb[0, 0]: ", type(zivid_rgb[0, 0, 0]))

    # print(f"Before downsampling: {point_cloud.width * point_cloud.height} point cloud")

    app.release

    return zivid_rgb, scaled_zivid_input_depth


    # _display_pointcloud(xyz, rgba[:, :, 0:3])

    # print("Downsampling point cloud")
    # point_cloud.downsample(zivid.PointCloud.Downsampling.by2x2)
    # xyz_donwsampled = point_cloud.copy_data("xyz")
    # rgba_downsampled = point_cloud.copy_data("rgba")

    # print(f"After downsampling: {point_cloud.width * point_cloud.height} point cloud")

    # _display_pointcloud(xyz_donwsampled, rgba_downsampled[:, :, 0:3])

    # input("Press Enter to close...")


def show_images():
    zivid_rgb, zivid_input_depth = get_zivid_rgb_depth()
    cv2.imshow('image', zivid_rgb)
    cv2.waitKey(0)

if __name__ == "__main__":
    # If running the script from Spyder IDE, first run '%gui qt'
    show_images()

