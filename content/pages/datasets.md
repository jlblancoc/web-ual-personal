Title: Datasets
h1: Robotics datasets for SLAM, visual odometry and localization
Date: 2013-10-09
Modified: 2026-11-02
myorder: 4.5
URL: datasets/
save_as: datasets/index.html
template: dataset
dataset: hub
image: imgs/datasets/urban/cover.jpg
Summary: Free robotics datasets by Jose Luis Blanco-Claraco: Málaga Urban (stereo, LiDAR, GPS), Málaga 2009 with RTK ground truth, and GREENBOT greenhouse SLAM.

Public datasets recorded with instrumented vehicles and mobile robots, released to benchmark
**SLAM**, **visual odometry**, **loop closure**, **place recognition**, **localization** and
**mapping** algorithms. All of them are free to download. If you use them in your work,
please cite the corresponding paper.

<!-- hub -->

## How to cite

Every dataset page includes the paper reference and a BibTeX entry:

* [Málaga Urban Dataset]({filename}malaga-urban-dataset.md): Blanco-Claraco, Moreno-Dueñas and González-Jiménez, *The International Journal of Robotics Research*, 2014, DOI [10.1177/0278364913507326](https://doi.org/10.1177/0278364913507326).
* [Málaga 2009 Dataset]({filename}malaga-2009-dataset.md): Blanco, Moreno and González, *Autonomous Robots*, 2009, DOI [10.1007/s10514-009-9138-7](https://doi.org/10.1007/s10514-009-9138-7).
* [GREENBOT Dataset]({filename}greenbot-greenhouse-dataset.md): Cañadas-Aránega, Blanco-Claraco, Moreno and Rodriguez-Diaz, *Sensors*, 2024, DOI [10.3390/s24061874](https://doi.org/10.3390/s24061874).

## Tools to work with the data

* The **rawlog** binary files of these datasets are part of the [Mobile Robot Programming Toolkit (MRPT)](https://www.mrpt.org/). They can be inspected with [RawLogViewer](https://www.mrpt.org/list-of-mrpt-apps/rawlogviewer/) and processed from C++ code. See the [rawlog format](https://www.mrpt.org/Rawlog_Format).
* [MOLA](https://docs.mola-slam.org/) is a modular framework for LiDAR odometry, SLAM and localization, able to read these datasets.

## Looking for the old pages?

The datasets were previously described in the MRPT web site at *mrpt.org/MalagaUrbanDataset* and
*mrpt.org/malaga_dataset_2009*. These pages are their new home.
