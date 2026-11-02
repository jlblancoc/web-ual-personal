Title: Málaga 2009 Robotic Datasets with RTK GPS ground truth
h1: The Málaga 2009 Robotic Dataset Collection
crumb: Málaga 2009 Dataset
Date: 2009-11-01
Modified: 2026-11-02
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
**Download status (2 November 2026).** The original files were hosted in SourceForge and are no longer available there.
**PARKING-0L is available again** (restored from the author's archive), together with the stereo calibration images.
The other five sequences (PARKING-2L, PARKING-6L, CAMPUS-0L, CAMPUS-2L and CAMPUS-RT) are currently unavailable. Their
original MD5 sums are listed below, to help verifying any copy you may have downloaded in the past.
If you need one of them, please [contact me](mailto:jlblanco@ual.es).
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

* **2026-11-02**: New home of the dataset page (previously at mrpt.org/malaga_dataset_2009). PARKING-0L and the calibration images are available again; the other five sequences are unavailable.
* **2012-03**: Errata added.
* **2009-11**: Paper published and datasets released.
