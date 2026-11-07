Title: Málaga 2009 Robotic Datasets with RTK GPS ground truth
h1: The Málaga 2009 Robotic Dataset Collection
crumb: Málaga 2009 Dataset
Date: 2009-11-01
Modified: 2026-11-07
URL: datasets/malaga-2009-dataset/
save_as: datasets/malaga-2009-dataset/index.html
nomenu: true
myorder: 90
parent: datasets
template: dataset
dataset: 2009
image: imgs/datasets/2009/seq-parking-6l.jpg
Summary: Six outdoor datasets with centimeter-accuracy 6D ground truth from RTK GPS, lasers, cameras and IMU, for visual SLAM and localization. Málaga 2009 collection.

**A Collection of Outdoor Robotic Datasets with centimeter-accuracy Ground Truth.**
Six datasets recorded in November 2008 at the University of Málaga (Spain) with an electric vehicle equipped
with laser scanners, color cameras, an IMU and three RTK GPS receivers. The 6D path of the vehicle, together with its
uncertainty, is estimated from the RTK data, so the collection is a test bed for **visual SLAM**, **2D SLAM**, **visual odometry**
and localization methods. Reference 3D point clouds built from the lasers are provided as well.

<div class="status-note" markdown="1">
**Download status (7 November 2026).** All six sequences are available again, byte-identical to the 2009 release, from a
[Zenodo record](https://doi.org/10.5281/zenodo.24021075) (DOI 10.5281/zenodo.24021075), with a
[Google Drive mirror](https://drive.google.com/drive/folders/1dKNi9SVLriP3ivrS6wPplwN2YOKYotAN?usp=sharing) as backup.
Each sequence is now also available as a **ROS 2 bag** (MCAP), see [below](#ros-2-mcap-files).
</div>

<figure>
<a href="{static}/imgs/datasets/2009/seq-campus-2l-overview.jpg"><img class="fig-full" src="{static}/imgs/datasets/2009/seq-campus-2l.jpg" alt="CAMPUS-2L: 3D point cloud from the vertical laser scanners and the RTK ground-truth path" width="900" height="510" loading="lazy"></a>
<figcaption>CAMPUS-2L: 3D point cloud built from the laser scans, with the ground-truth path in green.</figcaption>
</figure>

## Paper, citation and license

Please cite this paper if you use the datasets:

<!-- cite -->

These datasets are copyright by us and published under the
[Creative Commons Attribution CC BY 4.0 License](https://creativecommons.org/licenses/by/4.0/).

**Abstract.** The lack of publicly accessible datasets with a reliable ground truth has prevented in the past a fair and coherent comparison
of different methods proposed in the mobile robot Simultaneous Localization and Mapping (SLAM) literature. Providing such a ground truth
renders specially challenging in the case of visual SLAM, where the world model is 3-dimensional and the robot path is 6-dimensional.
This work addresses both the practical and theoretical issues found while building a collection of six outdoor datasets. It is discussed how
to estimate the 6-d vehicle path from readings of a set of three Real Time Kinematics (RTK) GPS receivers, as well as the associated
uncertainty bounds that can be employed to evaluate the performance of Visual SLAM methods. The vehicle was also equipped with several
laser scanners, from which reference point clouds are built as a test-bed for other algorithms such as segmentation or surface fitting.
All the datasets, calibration information and associated software tools are available for download.

### Errata (updated March 2012)

* Figure 1(b) shows the IMU mounted upside down, while it was actually mounted right-side up. See the pictures below.
  The yaw, pitch and roll angles given in Table 1 are correct: it was only an issue with the figure.
* Equation (30) in appendix I fails to mention that adding the angles is only a valid approximation for small rotations.

## Dataset downloads

The collection has two locations: the **parking** of the Computer Science School (PARKING-0L, 2L and 6L, with almost planar paths, trees,
cars and loops) and the **campus boulevard** (CAMPUS-0L, 2L and RT, with long straight sections and large loops).
In five of the sequences the suffix is the number of complete loops (0L means zero loops), while in CAMPUS-RT it means *round trip*.
Click on a preview to see the full overview figure of the sequence: 3D point cloud, aerial view of the path, and GPS operation modes.
The suitability tags follow the summary table of the paper.

<!-- sequences -->

### What each package contains

* `<name>.rawlog`: binary log with all the sensor data, in [MRPT rawlog format](https://www.mrpt.org/Rawlog_Format).
* `Images`, `Images_rect`: raw and rectified images of the left and right cameras.
* `GT_path_vehicle.txt`: ground-truth 6D pose of the vehicle at 1 Hz, with its covariance. `GT_path_vehicle_interp.txt`: interpolated at 100 Hz. Also as `GT_path_vehicle.bin.gz` for C++/MRPT, and one file per sensor (`GT_path_<sensor>.txt`).
* `GT_path_vehicle_confidence.txt`: quality measure of the ground truth at each instant. `W_star_cov_matrix.txt`: reference covariance matrix of the estimated path.
* `pointcloud.txt`, `pointcloud.3Dscene`, `pointcloud_img.png`: 3D point cloud from the two vertical SICK scanners and their ground-truth path.
* `malaga_datasets_grabber.ini`: 6D pose of every sensor on the vehicle, camera parameters and other settings.
* `README.html`: full description of the format. Rotations are given as yaw, pitch and roll.

The README of each sequence is also available online from its card above.
Most data are plain text and image files, so they can be read from MATLAB or any other software.

### ROS 2 MCAP files {#ros-2-mcap-files}

Since 2026, each sequence is also provided as a ROS 2 bag in MCAP format (`malaga2009_<name>.mcap`), with all the raw
sensor data of the rawlog and the 100 Hz ground truth. They were created with
[`rawlog2rosbag`](https://github.com/MRPT/mrpt_ros_bridge), play in ROS 2 Humble and newer, and can be opened directly in
[Foxglove](https://foxglove.dev/). The ground truth is also available in TUM format (`GT (TUM)` links above), e.g. for `evo`.

```bash
ros2 bag play malaga2009_parking_0L.mcap --qos-profile-overrides-path tf_static_latched.yaml
```

The file [`tf_static_latched.yaml`](https://zenodo.org/records/24021075/files/tf_static_latched.yaml?download=1) makes
`/tf_static` latched, so tools started after the playback still get the sensor frames.
Main topics: the five laser scanners (`/lms_sick_left/scan`, `/laser_hokuyo_front/scan`, ...), the cameras
(`/camera_left/image_raw/compressed` with the original JPEG images, and `camera_info`), the IMU (`/xsens/imu`), the four
GPS receivers (`/gps_rtk_rear/fix`, ...), `/ground_truth` (`nav_msgs/Odometry`) and `/tf_static` with all the sensor
poses. The ground truth has gaps in some sequences, where the RTK solution was not available.
The full list of topics is in the [README of the Zenodo record](https://zenodo.org/records/24021075/files/README.md?download=1).

The latitude and longitude of the rear RTK receiver (`/gps_rtk_rear/fix`) are shifted by about 150 m with respect to the
other receivers, because it used a different reference. The ground truth corrects this with the offsets given in the
`[OFFSET_GPS_RTK_*]` sections of `/rawlog_comment`. The front RTK receivers and the consumer-grade one are in WGS84.

#### Foxglove layout

The layout [`malaga2009_foxglove_layout.json`]({static}/docs/malaga2009_foxglove_layout.json) ([Google Drive mirror](https://drive.google.com/file/d/18uASwbF_mIuC8d-DLl_nWpE1-VXuiy4o/view?usp=sharing)) shows any of the MCAP files
in [Foxglove](https://foxglove.dev/): the five laser scanners in 3D (the vertical SICK scans are accumulated along the
ground-truth path), both cameras as image panels and also projected in the 3D view on their sensor frames, the GPS receivers
on a map, and the IMU. Import it from the *Layouts* menu (*Import from file...*). It includes a small user script that
republishes `/ground_truth` as the `map` → `base_link` transform.

<figure>
<a href="{static}/imgs/datasets/2009/foxglove-campus-0l.jpg"><img class="fig-full" src="{static}/imgs/datasets/2009/foxglove-campus-0l-thumb.jpg" alt="CAMPUS-0L in Foxglove: lasers accumulated in 3D, projected camera images, camera panels, GPS map and IMU plot" width="960" height="540" loading="lazy"></a>
<figcaption>CAMPUS-0L in Foxglove with this layout.</figcaption>
</figure>

## Vehicle and sensors

* 3 SICK laser scanners (two LMS-221 and one LMS-200) and 2 Hokuyo UTM-30LX.
* 2 FireWire color cameras (1024x768 at 7.5 fps).
* 1 Xsens MTi inertial measurement unit (100 Hz).
* 3 RTK GPS receivers, used to compute the ground truth, and 1 consumer-grade USB GPS receiver.

As an example, PARKING-0L has 1,922 stereo pairs, 256 seconds of data and about 65,000 sensor observations in its rawlog.

<!-- gallery -->

## Software

The following [MRPT](https://www.mrpt.org/) applications were used to elaborate the article:
[rawlog-grabber](https://www.mrpt.org/list-of-mrpt-apps/application-rawlog-grabber/) to record the datasets in the vehicle, and
[RawLogViewer](https://www.mrpt.org/list-of-mrpt-apps/rawlogviewer/) to inspect and filter the raw datasets and to generate the
ground-truth estimates. RawLogViewer can also be used directly with the downloaded datasets. In Ubuntu and Debian, install the package `mrpt-apps`.

## Camera calibration

A set of stereo image pairs of a 5x8 checkerboard with squares of 12x12 cm, which can be used to calibrate the cameras or to rectify the images.
The original file in SourceForge was `malaga2009_imgs_stereo_calib.zip`; this package was rebuilt from the author's archive.

<!-- calibration -->

## Extra material

Selected material from the preparation of the paper, which may have historical value: LaTeX sources and EPS figures of the manuscript,
overview figures of each sequence, pictures of the vehicle and sensors taken in November 2008, sensor pose measurements and notes.

<!-- extras -->

## Related datasets

* [Málaga Urban Dataset]({filename}malaga-urban-dataset.md): the follow-up, with a stereo camera and five laser scanners in real urban traffic.
* [GREENBOT Dataset]({filename}greenbot-greenhouse-dataset.md): mobile robot SLAM in a greenhouse.

## Changelog

* **2026-11-07**: All six sequences are available again (Zenodo, with a Google Drive mirror), byte-identical to the original files, and also as ROS 2 MCAP bags, with a Foxglove layout to visualize them.
* **2026-11-02**: New home of the dataset page (previously at mrpt.org/malaga_dataset_2009). PARKING-0L and the calibration images are available again; the other five sequences are unavailable.
* **2012-03**: Errata added.
* **2009-11**: Paper published and datasets released.
