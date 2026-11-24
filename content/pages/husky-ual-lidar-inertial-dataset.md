Title: Husky UAL LiDAR-Inertial Dataset
h1: Husky UAL LiDAR-Inertial Dataset: a mobile robot on a university campus
crumb: Husky UAL LiDAR-Inertial Dataset
Date: 2026-11-17
Modified: 2026-11-24
URL: datasets/husky-ual-lidar-inertial-dataset/
save_as: datasets/husky-ual-lidar-inertial-dataset/index.html
nomenu: true
myorder: 91
parent: datasets
template: dataset
dataset: husky
image: imgs/datasets/husky/cover.jpg
Summary: Clearpath Husky robot on the University of Almería campus: six sequences, 5.8 km, with LiDARs, stereo, IMUs, wheel odometry and RTK GNSS ground truth as ROS 2 bags, on Hugging Face. Includes TPS-A* autonomous navigation and a MOLA sensor fusion tutorial.

<figure>
<img class="fig-full" src="{static}/imgs/datasets/husky/2026-11-16-map.jpg" alt="Robot path over an aerial image of the campus: RTK reference, wheel odometry alone diverging hundreds of meters, wheels plus gyroscope, and the MOLA smoother fusion on top of the reference" width="1540" height="572">
<figcaption>Sequence 2026-11-16 over an aerial image of the campus: RTK reference (gray), wheel odometry
alone (green), wheels + gyroscope (orange), and the MOLA smoother fusing wheels, two IMUs and RTK GNSS
with the GNSS removed a third of the time (blue).</figcaption>
</figure>

Six sequences (**5.8 km, 138 min**) recorded with a **Clearpath Husky A200** mobile robot driving around
the campus of the University of Almería (Spain), through parks, plazas, parking lots and passages between
buildings, among pedestrians and vehicles. For benchmarking **LiDAR and LiDAR-inertial odometry**,
**SLAM**, **localization** and **multi-sensor fusion** with GNSS.

<div class="dataset-callout">
<p><strong>&#129303; Download from Hugging Face:</strong>
<a href="https://huggingface.co/datasets/jlblancoc/ual-husky-campus">huggingface.co/datasets/jlblancoc/ual-husky-campus</a></p>
<p>All six sequences with all the sensors, the RTK ground truth, the calibration and an evaluation
script. The dataset card there has the full details of topics, ground truth and known issues.</p>
</div>

The robot carries an **Ouster OS0-32** LiDAR (plus a **Velodyne VLP-16** in the first two sequences), a
**Bumblebee2 stereo camera**, two **IMUs** (a HandsFree 9-axis unit and the Ouster's own), **wheel
odometry**, a **u-blox ZED-F9P RTK GNSS** receiver with NTRIP corrections and a low-cost u-blox 7 receiver.
All data is recorded with ROS 2 Jazzy as MCAP bags with native messages. The robot PC clock follows the
GNSS time pulse, so stamps are UTC; the Ouster is also synchronized by PTP since sequence 03.

* **00 and 01** were recorded in the same park: the robot first drove around it to build a map with MOLA,
  and then navigated autonomously in it with the TPS-A\* planner among people walking by
  ([details below](#tps-astar-navigation)).
* **02 to 05** cover most of the campus. Sequence 03 is also the dataset of the
  [MOLA tutorial](#tutorial) on fusing wheel odometry, IMUs and RTK GNSS.

## Sequences

Each sequence on Hugging Face has two bags that share the time base and can be played together
(`ros2 bag play sensors stereo`): `sensors/`, with every topic except the 15 Hz stereo images (it includes
1 Hz images of both cameras, enough for LiDAR, inertial and GNSS work), and `stereo/`, with the 15 Hz
left and right images. Download one sequence with the
[Hugging Face CLI](https://huggingface.co/docs/huggingface_hub/guides/cli):

```bash
hf download jlblancoc/ual-husky-campus --repo-type dataset \
  --include "ual_husky_campus_03/*" "calibration.yaml" "eval_rtk.py" --local-dir ual_husky_campus
```

<!-- sequences -->

Some sequences are also on this server as first released: the original single bag of 00 and 01 (01 with
the localization, planner and follower outputs recorded on the robot), the map used in 01, and the
wheels + IMUs + GNSS subset of 03 with the tutorial scripts. Each of those folders has a README.

## Ground truth

The ground truth is the position of the **F9P antenna**, from its RTK carrier-phase fixed solutions at
1 Hz, kept only where they are reliable: reported horizontal accuracy under 5 cm, away from the instants
the fix is acquired or lost, and with every pair of consecutive fixed segments checked for a wrong
ambiguity fix against an independent LiDAR-inertial odometry or the integrated GNSS Doppler velocity.
It is given as TUM and CSV files in a local ENU frame shared by all the sequences, with the exact
transformation from `base_link` to the antenna in `calibration.yaml`. There is no ground truth where the
receiver has no fixed solution (under trees, between buildings), so its coverage varies from 19 % to 92 %
of the time moving.

The script `eval_rtk.py` (numpy only) evaluates a `base_link` trajectory in TUM format against it,
converting it to antenna positions first:

```bash
python3 eval_rtk.py my_estimate.tum ual_husky_campus_03/ground_truth/ground_truth_antenna.tum
```

## TPS-A\* navigation experiment {#tps-astar-navigation}

In the 2026-11-02 18:05 sequence the Husky navigates with
[TPS-A\*](https://github.com/MRPT/mrpt_path_planning), a lattice A\* planner in the TP-Space of a set of
parameterized trajectory generators (PTGs), run by its ROS 2 node in
[mrpt_navigation](https://github.com/mrpt-ros-pkg/mrpt_navigation), and localizes with
[MOLA](https://docs.mola-slam.org/) on the map built from the 17:50 sequence. An operator gave 15 goals one
after another; the robot reached 8 of them, about 210 m of autonomous driving, replanning when people
blocked its path. The bag contains, besides the raw sensors, everything the navigation stack published
on the robot (localization, planned paths, follower status and logs). This is the real-robot experiment
of the paper that presents TPS-A\* (under review): its results can be checked and reproduced from this bag.

## Tutorial: wheels + IMU + RTK GNSS fusion with MOLA {#tutorial}

The [MOLA tutorial](https://docs.mola-slam.org/latest/tutorial-wheels-imu-gnss-fusion.html) on sequence 03 (2026-11-16) shows how to fuse
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

The tutorial scripts (replay, simulated GNSS outages and evaluation against RTK) are in the folder of
the wheels + IMUs + GNSS subset of sequence 03 on this server.

## License

All sequences are released under the
[Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/) license
(CC BY 4.0): you may share and adapt them for any purpose, including commercially, as long as you give
appropriate credit. The tutorial scripts are BSD 3-Clause, like MOLA.

## Citation

A technical report describing the dataset is on its way to arXiv. Until then, if you use this dataset,
please cite it as:

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

* **2026-11-24**: Full release on [Hugging Face](https://huggingface.co/datasets/jlblancoc/ual-husky-campus):
  six sequences (three of them new) with all the sensors, faces and license plates blurred, a validated
  RTK ground truth of the antenna, the calibration and an evaluation script.
* **2026-11-18**: Sequences 2026-11-02 17:50 (CIDU park mapping, with its map) and 2026-11-02 18:05
  (CIDU park TPS-A\* navigation), with all the sensors and the faces blurred.
* **2026-11-17**: First sequence (2026-11-16 campus loop): wheel odometry, IMUs and GNSS, with the MOLA fusion tutorial.

## Privacy

Faces and license plates in the camera images are blurred with
[mcap_anonymizer](https://github.com/MOLAorg/mcap_anonymizer), an open-source tool that changes only the
pixels inside the blurred regions and keeps the rest of the bags bit-exact. The result was reviewed by
hand. The original bags on this server, released before, have only the faces blurred. If you still find yourself or personal belongings in this dataset and feel unwell about it, please
get in touch and we will remove the respective data.

## Related datasets

* [Málaga 2009 Dataset]({filename}malaga-2009-dataset.md): outdoor sequences with centimeter-accuracy 6D ground truth.
* [GREENBOT Dataset]({filename}greenbot-greenhouse-dataset.md): LiDAR SLAM in a Mediterranean greenhouse.
