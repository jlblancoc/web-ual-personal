Title: Málaga Urban Dataset: stereo camera, LiDAR and GPS for SLAM
h1: The Málaga Stereo and Laser Urban Data Set
crumb: Málaga Urban Dataset
Date: 2013-10-09
Modified: 2026-11-02
URL: datasets/malaga-urban-dataset/
save_as: datasets/malaga-urban-dataset/index.html
nomenu: true
myorder: 90
parent: datasets
template: dataset
dataset: urban
image: imgs/datasets/urban/cover.jpg
Summary: Málaga Urban Dataset: 36.8 km of 20 fps stereo images, five laser scanners, IMU and GPS in real urban traffic. Download 15 extracts or the entire dataset.

The **Málaga Urban Dataset** was gathered entirely in urban scenarios with a car equipped with
one stereo camera (Bumblebee 2) and five laser scanners, among other sensors. Its distinctive
feature is the existence of **high-resolution stereo images grabbed at a high rate (20 fps) during a
36.8 km trajectory**, which turns it into a suitable benchmark for a variety of computer vision
techniques, such as visual odometry, visual SLAM, loop closure and place recognition. Both plain
text and binary files are provided, as well as open source tools for working with the binary versions.

<figure>
<img class="fig-full" src="{static}/imgs/datasets/urban/cover.jpg" alt="Málaga Urban Dataset: stereo image from the car, GPS path over a city map and laser point cloud" width="960" height="540">
</figure>

## Citation and license

Please cite this paper if you use the dataset:

<!-- cite -->

This dataset is copyright by us and published under the
[Creative Commons Attribution CC BY 4.0 License](https://creativecommons.org/licenses/by/4.0/).

## Downloads

* **Selected extracts**: 15 short sections of the dataset, much easier to work with than the entire data. See below.
* **Entire dataset**: plain text, binary and image packages. See further below.
* **Alternative location**: the entire dataset is also available in [Google Drive](https://drive.google.com/open?id=0B5HPWlmxIrvFOGFfUkIxVkhyWEE), in case the main server is unavailable.

### Selected extracts

All packages include raw and rectified stereo images, and all data in plain text files and in binary
([.rawlog](https://www.mrpt.org/Rawlog_Format)) format. The format is described in the
[extracts readme](https://ingmec.ual.es/~jlblanco/malaga-urban-dataset/extracts/README_extracts.txt).
The path of each extract is drawn from its GPS data, with start (green) and end (black) points.

<!-- extracts -->

### Entire dataset

<!-- entire -->

Calibration parameters of the cameras:
[raw images](https://ingmec.ual.es/~jlblanco/malaga-urban-dataset/calibration/camera_params_raw_1024x768.txt),
[rectified 1024x768](https://ingmec.ual.es/~jlblanco/malaga-urban-dataset/calibration/camera_params_rectified_a=0_1024x768.txt) and
[rectified 800x600](https://ingmec.ual.es/~jlblanco/malaga-urban-dataset/calibration/camera_params_rectified_a=0_800x600.txt).
Also available: the [calibration and data sheet of the MTi IMU](https://drive.google.com/open?id=0B5HPWlmxIrvFZ0tUZDk5ck9sMGs).

### Other files

<!-- extra-files -->

All `.rawlog` files can be opened with the program *RawLogViewer*, part of
[MRPT](https://www.mrpt.org/). In Ubuntu, install the package `mrpt-apps`.
Raw (not undistorted) images are **not** included in the rawlogs: download them separately and put
them in a directory named `Images` for the software to find them.

## Sensors

The vehicle is a Citroën C4 with all the sensors installed in a modified roof rack, so it can drive
among the city traffic without restrictions.

| Sensor | Description | Rate |
|---|---|---|
| Stereo camera | Point Grey Bumblebee 2, color, 1024x768 | 20 Hz |
| Laser scanners (3) | Hokuyo UTM-30LX: front (tilted down), left and right (vertical) | 40 Hz |
| Laser scanners (2) | SICK LMS-200: front and rear (horizontal) | about 75 Hz |
| IMU | Xsens MTi | 100 Hz |
| GPS | One receiver, used for the paths shown here | about 2 Hz |

Overall, the dataset has 113,082 stereo frames over 5,655 seconds (about 1.5 hours) and 2.15 million sensor observations.
The sensor labels in the logs are `CAMERA1`, `GPS_DELUO`, `HOKUYO1`, `HOKUYO2`, `HOKUYO3`, `LASER1`, `LASER2` and `XSensMTi`.

<div class="dataset-figures">
<figure>
<a href="{static}/imgs/datasets/urban/car.jpg"><img src="{static}/imgs/datasets/urban/car.jpg" alt="The car used to record the Málaga Urban Dataset, after installing the sensors" width="1200" height="831" loading="lazy"></a>
<figcaption>The car after installing the sensors.</figcaption>
</figure>
<figure>
<a href="{static}/imgs/datasets/urban/sensors.jpg"><img src="{static}/imgs/datasets/urban/sensors.jpg" alt="Sensors of the Málaga Urban Dataset before mounting them on the car" width="1200" height="900" loading="lazy"></a>
<figcaption>Sensors before mounting on the car.</figcaption>
</figure>
</div>

## Overview of the entire dataset

### Path

The path obtained from the GPS sensor during the whole dataset run, about 36 km through different urban areas of Málaga
([KML file](https://ingmec.ual.es/~jlblanco/malaga-urban-dataset/KMLs/malaga-urban-dataset_CAM%2BGPS.kml) for Google Earth).

<figure>
<img class="fig-full" src="{static}/imgs/datasets/urban/paths/full.svg" alt="GPS path of the entire Málaga Urban Dataset, about 36 km" width="800" height="520" loading="lazy">
</figure>

### Video

This composition shows: the raw images from the left stereo camera (top-left), the GPS position over a map of the city (bottom-left)
and a 3D reconstruction of the environment by simple interpolation of GPS points, using two of the five lasers (right).
The exact timestamp is displayed, which is useful to skip to an interesting part for your application.

<!-- overview-video -->

The video can also be downloaded for offline usage: see *Video: dataset preview (FLV)* in the table above.

## Parsing the logs from C++

Apart from plain text files, binary [.rawlog](https://www.mrpt.org/Rawlog_Format) files are an efficient and convenient
way of parsing vision and robotic datasets from C++ code. The following example program is a starting point to write your own:
[parse-dataset-example](https://github.com/MRPT/mrpt/tree/master/doc/parse-dataset-example).
Example of usage:

    ./parse_dataset_example malaga-urban-dataset-extract-01/malaga-urban-dataset-extract-01_rectified_800x600.rawlog

## Analysis of the rawlog file

Output of `rawlog-edit --info -i malaga-urban-dataset_all-sensors.rawlog` for the entire dataset:

    Physical file size                : 1.41 GB
    Uncompressed file size            : 4.79 GB
    Overall number of objects         : 2153717
    All sensor labels                 : CAMERA1, GPS_DELUO, HOKUYO1, HOKUYO2, HOKUYO3, LASER1, LASER2, XSensMTi
    Sensor (Label/Occurs/Rate/Durat.) :         CAMERA1 / 113082 /19.998 /5654.574
    Sensor (Label/Occurs/Rate/Durat.) :       GPS_DELUO /  11244 /1.989 /5653.000
    Sensor (Label/Occurs/Rate/Durat.) :         HOKUYO1 / 225416 /39.864 /5654.617
    Sensor (Label/Occurs/Rate/Durat.) :         HOKUYO2 / 225631 /39.902 /5654.624
    Sensor (Label/Occurs/Rate/Durat.) :         HOKUYO3 / 225510 /39.880 /5654.621
    Sensor (Label/Occurs/Rate/Durat.) :          LASER1 / 398531 /74.974 /5315.578
    Sensor (Label/Occurs/Rate/Durat.) :          LASER2 / 404487 /73.568 /5498.109
    Sensor (Label/Occurs/Rate/Durat.) :        XSensMTi / 549816 /100.000 /5498.150

## Changelog

* **2026-11-02**: New home of the dataset page (previously at mrpt.org/MalagaUrbanDataset).
* **2019-01-29**: The downloads server had technical problems. An alternative location in Google Drive was added.
* **2018-09-13**: Fix typo in the "z" coordinate of the front stereo camera: it should be 57 mm, not 273 mm. Table 2 in the [draft PDF](https://ingmec.ual.es/~jlblanco/papers/blanco2013malaga_urban_dataset_IJRR_draft.pdf) has been updated accordingly.
* **2017-05-10**: Add the calibration and data sheet of the MTi IMU.
* **2014-05-15**: All images have been rectified again such that both stereo image centers coincide. This simplifies the number of parameters needed to perform stereo SLAM or visual odometry. Calibration files of rectified images have been updated.
* **2013-10-09**: First version online.

## Related datasets

* [Málaga 2009 Dataset]({filename}malaga-2009-dataset.md): six outdoor sequences with centimeter-accuracy 6D ground truth.
* [GREENBOT Dataset]({filename}greenbot-greenhouse-dataset.md): mobile robot SLAM in a greenhouse.
