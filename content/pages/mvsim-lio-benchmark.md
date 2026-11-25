Title: MVSim-LIO: simulated LiDAR-inertial odometry benchmark
h1: MVSim-LIO: a simulated LiDAR-inertial odometry benchmark with exact trajectory and map ground truth
crumb: MVSim-LIO Benchmark
Date: 2026-11-26
Modified: 2026-11-26
URL: datasets/mvsim-lio-benchmark/
save_as: datasets/mvsim-lio-benchmark/index.html
nomenu: true
myorder: 92
parent: datasets
template: dataset
dataset: mvsim_lio
image: imgs/datasets/mvsim-lio/cover.jpg
Summary: MVSim-LIO: simulated LiDAR-inertial odometry benchmark with exact ground truth. 15 worlds, 30 trajectories (20.1 km) of five carriers, 9 paired sensor variants up to a realistic LiDAR error model, 25 billion labeled points, on Hugging Face.

<figure>
<video class="fig-full" poster="{static}/imgs/datasets/mvsim-lio/cover.jpg" width="960" height="400" autoplay muted loop playsinline>
<source src="{static}/imgs/datasets/mvsim-lio/maps.mp4" type="video/mp4">
</video>
<figcaption>Exact maps (noise-free sweeps at the true poses) revealed along the ground-truth trajectory of six
of the worlds; inset: the MVSim world.</figcaption>
</figure>

A simulated benchmark for **LiDAR and LiDAR-inertial odometry (LIO)** and **SLAM** whose ground truth is
**exact by construction**: the trajectory is the simulator's input (a C2 spline that can be evaluated at any
time), and the map is the geometry the sensors observe. There is no GNSS/INS, motion capture or laser scanner
registration error in the reference, and no extrinsic calibration or time synchronization error.

* **15 worlds**, from streets, a campus and a tunnel to a forest, an orchard, a greenhouse and multi-level
  buildings with stairs and ramps, rendered with [MVSim](https://github.com/MRPT/mvsim).
* **30 six-degrees-of-freedom trajectories** (20.1 km, 148 minutes) of five carriers: car, ground robot,
  legged robot, quadruped and hand-held rig.
* A ray-traced spinning **LiDAR** with per-point timestamps and semantic labels, a motion-consistent
  **200 Hz IMU** and wheel odometry.
* **9 paired variants** of every trajectory, sharing the motion and the random draws: global or rolling
  shutter, three LiDAR models (OS1-32, OS1-64 and VLP-16 style), and three noise levels, up to a
  **realistic LiDAR error model** (range noise, beam footprint, mixed returns at depth edges, dropouts and
  per-ring calibration errors) with parameter ranges taken from real Ouster sensors.
* **270 rendered sequences**: 798 thousand sweeps, 25.2 billion points, 16 million IMU samples.

<div class="dataset-callout">
<p><strong>&#129303; Download from Hugging Face:</strong>
<a href="https://huggingface.co/datasets/MOLAorg/MVSim-LIO">huggingface.co/datasets/MOLAorg/MVSim-LIO</a>
(pin the release <code>v2.1</code>)</p>
<p><strong><i class="fa-brands fa-github"></i> Worlds, trajectories, generator and evaluation code:</strong>
<a href="https://github.com/MOLAorg/mvsim_lio_benchmark">github.com/MOLAorg/mvsim_lio_benchmark</a></p>
</div>

## Worlds

<figure>
<img class="fig-full" src="{static}/imgs/datasets/mvsim-lio/worlds.jpg" alt="The 15 MVSim worlds of the benchmark: urban street, campus, parking lot, parking garage, tunnel, forest, orchard, open field, rough terrain, greenhouse, warehouse, office, stairwell, stair course and apartment building" width="1600" height="600" loading="lazy">
<figcaption>The 15 worlds of the benchmark.</figcaption>
</figure>

The scenes range from well constrained (streets, campus) to degenerate (a tunnel, an open field with a
handful of objects, the repetitive aisles of a greenhouse and a warehouse), and include stairs for legged robots,
identical floors, ramps between levels and slopes. The
[repository README](https://github.com/MOLAorg/mvsim_lio_benchmark#worlds) describes each world and its
trajectories.

## Data

Each sequence is an MRPT **rawlog** (LiDAR point clouds with fields `x y z t ring label instance`, IMU and
odometry, with the sensor poses on the vehicle), the ground truth in TUM format at the sweep times and at
200 Hz, and, for the realistic variants, the drawn parameters of the error model. The rawlogs can be converted
to **ROS 2 bags** with `rawlog2rosbag` (package `ros-${ROS_DISTRO}-rawlog2rosbag`). A **plain-text copy** of every
sequence, with a reader that needs only Python and NumPy, is also provided. In total, 272 GB of rawlogs and
101 GB of plain text.

Download one variant (realistic errors, OS1-32, rolling shutter) of all 30 sequences, with the 200 Hz ground
truth (26 GB), with the [Hugging Face CLI](https://huggingface.co/docs/huggingface_hub/guides/cli):

```bash
hf download MOLAorg/MVSim-LIO --repo-type dataset --revision v2.1 --local-dir mvsim_lio \
  --include "*/*/os1_32-real-rolling.*" --include "*/*/gt_200hz.tum"
```

The [Hugging Face dataset card](https://huggingface.co/datasets/MOLAorg/MVSim-LIO) and the
[GitHub repository](https://github.com/MOLAorg/mvsim_lio_benchmark) give the file format, frames and
conventions, the sensor models, the full list of sequences and variants, and the known limitations.

## Benchmark

The paper evaluates eight LiDAR-only and LIO configurations ([MOLA](https://docs.mola-slam.org/), KISS-ICP,
FAST-LIO2, DLIO, GLIM, Traj-LO and others) with trajectory and map metrics. The runner, the method
configurations, the metrics and the tuning grid are in the
[`evaluation/`](https://github.com/MOLAorg/mvsim_lio_benchmark/tree/main/evaluation) folder of the repository.
Every sequence can be regenerated bit for bit from the worlds, trajectories and sensor parameters pinned there.

## License

The generated data is released under the
[Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/) license
(CC BY 4.0): commercial use and model training are allowed with attribution. The code, worlds, trajectories
and sensor definitions are BSD 3-Clause.

## Citation

The paper describing the benchmark has been submitted to arXiv. Until its identifier is available, please cite:

<p class="cite">A. Gómez-Espinosa, J.L. Torres-Moreno and J.L. Blanco-Claraco. &ldquo;MVSim-LIO: A Simulated
LiDAR-Inertial Odometry Benchmark with Exact Trajectory and Map Ground Truth&rdquo;. 2026.
https://huggingface.co/datasets/MOLAorg/MVSim-LIO</p>

<details class="bibtex">
<summary>BibTeX</summary>
<pre><code>@Misc{gomez2026mvsimlio,
  AUTHOR = {G\'omez-Espinosa, Ana and Torres-Moreno, Jos\'e Luis and Blanco-Claraco, Jos\'e Luis},
  TITLE = {{MVSim-LIO}: A Simulated {LiDAR}-Inertial Odometry Benchmark with Exact Trajectory and Map Ground Truth},
  HOWPUBLISHED = {\url{https://huggingface.co/datasets/MOLAorg/MVSim-LIO}},
  YEAR = {2026}
}</code></pre>
</details>

## Changelog

* **2026-11-26**: Paper submitted to arXiv.
* **2026-11-23**: Release `v2.1` on Hugging Face: realistic LiDAR error model v2 and a plain-text copy of
  every sequence.

## Related datasets

* [Husky UAL LiDAR-Inertial Dataset]({filename}husky-ual-lidar-inertial-dataset.md): real LiDAR-inertial data of a mobile robot on a campus, with RTK GNSS ground truth.
* [GREENBOT Dataset]({filename}greenbot-greenhouse-dataset.md): LiDAR SLAM in a real Mediterranean greenhouse.
