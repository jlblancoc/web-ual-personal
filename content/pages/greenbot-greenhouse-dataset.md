Title: GREENBOT Dataset: LiDAR SLAM in a Mediterranean greenhouse
h1: Multimodal mobile robotic dataset for a typical Mediterranean greenhouse: the GREENBOT dataset
crumb: GREENBOT Greenhouse Dataset
Date: 2024-01-31
Modified: 2026-11-02
URL: datasets/greenbot-greenhouse-dataset/
save_as: datasets/greenbot-greenhouse-dataset/index.html
nomenu: true
myorder: 90
parent: datasets
template: dataset
dataset: greenhouse
canonical: https://arm.ual.es/arm-group/dataset-greenhouse-2024/
image: imgs/datasets/greenhouse/header.jpg
Summary: GREENBOT: multimodal mobile robot dataset in a tomato greenhouse with Velodyne and Ouster LiDARs, stereo camera and GNSS/IMU, as ROS bags and MRPT rawlogs.

<div class="mirror-note" markdown="1">
This page is a copy of the dataset page of the [ARM research group](https://arm.ual.es/) at the University of Almería.
The **original and canonical source** is
[arm.ual.es/arm-group/dataset-greenhouse-2024](https://arm.ual.es/arm-group/dataset-greenhouse-2024/).
</div>

<figure>
<img class="fig-full" src="{static}/imgs/datasets/greenhouse/header.jpg" alt="GREENBOT dataset: colored LiDAR point cloud of a greenhouse" width="882" height="385">
</figure>

This dataset is an innovative resource for challenging natural agricultural settings, such as a greenhouse, where precise
localization is crucial but **GNSS accuracy may be compromised** by the construction elements and the crop.
It was collected with a mobile platform equipped with sensors typically used in mobile robots, moved through all the corridors of a
typical Mediterranean greenhouse with **tomato crops**. It is a unique opportunity for building detailed 3D models of plants in such
indoor-like spaces, with applications such as robotized spraying. To the authors' knowledge, it is the first dataset suitable
for testing **SLAM** methods in a greenhouse; its suitability is assessed in the paper with state-of-the-art algorithms.

## Description

The sensorised platform was built at the University of Almería. It has a base of 900 x 500 x 700 mm with a load capacity of 180 kg,
four straight wheels and two handles for pushing. The sensors are mounted on a pine wood platform, taking into account the specific
constraints of each one.

<figure>
<img class="fig-full" src="{static}/imgs/datasets/greenhouse/platform.jpg" alt="The GREENBOT sensorised cart with its Velodyne VLP-16, Ouster OS0, Bumblebee stereo camera, NovAtel GNSS and HISTTON computer" width="897" height="839" loading="lazy">
</figure>

* **Bumblebee BB2** stereo camera, model BB2-08S2, FireWire IEEE 1394 (800 Mb/s). Stored resolution of 1032 x 776 pixels. Field of view of 97º horizontal and 66º vertical, within a range of 0.3 m to 20 m. Recorded at 10 Hz (maximum 20 fps). It is placed at the front, so the images are ideal for obstacle identification.
* [**Velodyne VLP-16** LiDAR](https://velodynelidar.com/products/puck/): maximum range of 100 m, 360º horizontal and 30º vertical field of view. Placed at the top, to have the whole field of view available except for the operator. Recorded at 10 Hz.
* [**Ouster OS0** LiDAR](https://ouster.com/products/hardware/os0-lidar-sensor): 32 channels, 360º horizontal and 90º vertical field of view, range from 0.3 m to 50 m, recorded at 10 Hz. It has a reflectivity channel and an IMU to link the complete point cloud to a local source. It is placed 20 cm lower than the Velodyne, which obstructs its view: it only collects data at 275º horizontally.
* **HISTTON PC**: Intel i7-8550U processor, Intel UHD 620 graphics, 32 GB of DDR4 RAM, chosen for its future robot implementation (15 W, operating temperature 0 to 70 ºC, humidity 0 to 85 %). It runs Ubuntu 20.04 with ROS Noetic and Ubuntu 22.04 with ROS 2 Humble, in separate partitions.
* **NovAtel GNSS/INS** [IMU-IGM-A1](https://novatel.com/support/span-gnss-inertial-navigation-systems/span-combined-systems/span-igm-a1) with an [ANTCOM 42G1215](https://novatel.com/products/gps-gnss-antennas/compact-small-gnss-antennas/42g1215a-xt-1) antenna, used to share the same timestamp.

## Videos

The first video shows a complete process simulation of a robot, followed by the result of the post-processing with the MOLA SLAM algorithm.
The point clouds are then shown separately for each LiDAR.

<!-- videos -->

## Download links

The dataset is available for download as **ROS 1 Noetic bags** and as **MRPT rawlogs** (for ROS 2 Humble).
The files are hosted in Google Drive, one folder per sequence.

<!-- sequences -->

The calibration files and the tools needed to run the MOLA SLAM algorithm correctly are linked above.
[MOLA](https://docs.mola-slam.org/) is a modular LiDAR odometry and SLAM framework.

## Copyright

All datasets and benchmarks on this page are copyright by us and published under the
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/) License.
This means that you must attribute the work in the manner specified by the authors, you may not use this work for commercial purposes
and if you alter, transform, or build upon this work, you may distribute the resulting work only under the same license.

## Citation

<!-- cite -->

## Changelog

* **2024-03-15**: The [GreenBot Dataset paper](https://www.mdpi.com/1424-8220/24/6/1874) is available.
* **2024-02-08**: Calibration data problem solved.
* **2024-01-31**: Initial data release.

## Privacy

This dataset is made available for academic use only. However, we take your privacy seriously! If you find yourself or personal belongings
in this dataset and feel unwell about it, please get in touch with us and we will immediately remove the respective data from our server.

<!-- authors -->

## Credits

This work has been partially financed by the 'CyberGreen' Project, PID2021-122560OB-I00, and the 'AgroConnect.es' infrastructure used
to carry out this research, grant EQC2019-006658-P, both funded by MCIN/AEI/10.13039/501100011033 and by ERDF A way to make Europe,
with the support of the Regional Ministry of Economic Transformation, Industry, Knowledge and Universities and the European Regional
Development Fund (FEDER) with the projects UAL2020-TEP-A1991 and PY2020_007-A1991. Also, author Fernando Cañadas-Aránega is supported
by an FPI grant from Spanish Ministery of Science, Innovation and Universities.

## Related datasets

* [Málaga Urban Dataset]({filename}malaga-urban-dataset.md): stereo camera and five laser scanners in real urban traffic.
* [Málaga 2009 Dataset]({filename}malaga-2009-dataset.md): outdoor sequences with centimeter-accuracy 6D ground truth.
