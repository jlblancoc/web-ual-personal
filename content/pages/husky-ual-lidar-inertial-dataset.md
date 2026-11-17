Title: Husky UAL LiDAR-Inertial Dataset
h1: Husky UAL LiDAR-Inertial Dataset: a mobile robot on a university campus
crumb: Husky UAL LiDAR-Inertial Dataset
Date: 2026-11-17
URL: datasets/husky-ual-lidar-inertial-dataset/
save_as: datasets/husky-ual-lidar-inertial-dataset/index.html
nomenu: true
myorder: 91
parent: datasets
template: dataset
dataset: husky
image: imgs/datasets/husky/cover.jpg
Summary: Clearpath Husky robot on the University of Almería campus: LiDARs, IMUs, wheel odometry and RTK GNSS ground truth as ROS 2 bags. First sequence: wheels + IMUs + GNSS, with a MOLA sensor fusion tutorial.

<figure>
<img class="fig-full" src="{static}/imgs/datasets/husky/2026-11-16-map.jpg" alt="Robot path over an aerial image of the campus: RTK reference, wheel odometry alone diverging hundreds of meters, wheels plus gyroscope, and the MOLA smoother fusion on top of the reference" width="1540" height="572">
<figcaption>Sequence 2026-11-16 over an aerial image of the campus: RTK reference (gray), wheel odometry
alone (green), wheels + gyroscope (orange), and the MOLA smoother fusing wheels, two IMUs and RTK GNSS
with the GNSS removed a third of the time (blue).</figcaption>
</figure>

Sequences recorded with a **Clearpath Husky A200** mobile robot driving around the campus of the
University of Almería (Spain), for benchmarking **LiDAR and LiDAR-inertial odometry**, **SLAM**,
**localization** and **multi-sensor fusion** with GNSS.

The robot carries an **Ouster OS0-32** and a **Velodyne VLP-16** LiDAR, a **Bumblebee2 stereo camera**,
two **IMUs** (a HandsFree 9-axis unit and the Ouster's own), **wheel odometry**, a **u-blox ZED-F9P RTK
GNSS** receiver with NTRIP corrections (centimeter-level ground truth while in RTK fixed) and a low-cost
u-blox 7 receiver. All data is recorded with ROS 2 Jazzy as MCAP bags. The robot PC clock follows the GNSS
time pulse and the Ouster is synchronized by PTP, so all stamps are UTC.

Sequences are released progressively, each with the subset of sensors that is ready. The first one has no
LiDAR data: it is the dataset of the MOLA tutorial on fusing wheel odometry, IMUs and RTK GNSS.

## Sequences

<!-- sequences -->

Each release folder has a README with the topics, sensor poses, timing details and known issues of the
sequence.

## Tutorial: wheels + IMU + RTK GNSS fusion with MOLA

The [MOLA tutorial](https://docs.mola-slam.org/latest/tutorial-wheels-imu-gnss-fusion.html) on the first sequence shows how to fuse
wheel odometry, the gyroscopes of one or two IMUs and RTK GNSS with the
[MOLA state estimation smoother](https://docs.mola-slam.org/), keeping a centimeter-level,
geo-referenced pose while the GNSS is lost for a while. With the GNSS removed 15 s of every 45 s, the
median horizontal error against RTK is 5.5 cm, while wheel odometry alone ends hundreds of meters away:

<figure>
<img class="fig-full" src="{static}/imgs/datasets/husky/2026-11-16-error.jpg" alt="Horizontal error versus time in log scale: wheel odometry alone grows to hundreds of meters, wheels plus gyroscope to about ten meters, and the smoother fusion stays at a few centimeters, also inside the GNSS outages" width="1320" height="506" loading="lazy">
<figcaption>Horizontal error against the RTK fixes. Gray bands: GNSS hidden from the estimator.</figcaption>
</figure>

The tutorial is also available as a short video:

<div class="video-embed">
<iframe src="https://www.youtube-nocookie.com/embed/nocyFJUd1Hc" title="Wheel odometry + IMU + RTK GNSS fusion with MOLA" loading="lazy" allow="encrypted-media; picture-in-picture" allowfullscreen></iframe>
</div>

The tutorial scripts (replay, simulated GNSS outages and evaluation against RTK) are in the release folder.

## License

All sequences are released under the
[Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/) license
(CC BY 4.0): you may share and adapt them for any purpose, including commercially, as long as you give
appropriate credit. The tutorial scripts are BSD 3-Clause, like MOLA.

## Citation

If you use this dataset, please cite it as:

<p class="cite">J.L. Blanco-Claraco. &ldquo;Husky UAL LiDAR-Inertial Dataset&rdquo;. University of Almería, 2026.
https://w3.ual.es/~jlblanco/datasets/husky-ual-lidar-inertial-dataset/</p>

<details class="bibtex">
<summary>BibTeX</summary>
<pre><code>@Misc{blanco2026husky,
  AUTHOR = {Blanco-Claraco, Jose Luis},
  TITLE = {Husky {UAL} {LiDAR}-Inertial Dataset},
  HOWPUBLISHED = {\url{https://w3.ual.es/~jlblanco/datasets/husky-ual-lidar-inertial-dataset/}},
  YEAR = {2026}
}</code></pre>
</details>

## Changelog

* **2026-11-17**: First sequence (2026-11-16 campus loop): wheel odometry, IMUs and GNSS, with the MOLA fusion tutorial.

## Privacy

If you find yourself or personal belongings in this dataset and feel unwell about it, please get in touch
and we will remove the respective data.

## Related datasets

* [Málaga 2009 Dataset]({filename}malaga-2009-dataset.md): outdoor sequences with centimeter-accuracy 6D ground truth.
* [GREENBOT Dataset]({filename}greenbot-greenhouse-dataset.md): LiDAR SLAM in a Mediterranean greenhouse.
