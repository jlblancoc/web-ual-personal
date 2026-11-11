Title: Software
Date: 2026-01-27
Modified: 2026-11-11
myorder: 4
Summary: Tensora.app, free online structural analysis in the browser, and open-source frameworks and tools for robotics (MOLA, MRPT, MVSim), multibody dynamics, and data acquisition.

## Profiles
* **GitHub**: [@jlblancoc](https://github.com/jlblancoc)
* **Packages**: [Debian/Ubuntu Developer Profile](https://qa.debian.org/developer.php?login=joseluisblancoc%40gmail.com)

---

## Online Engineering Tools

### Tensora.app: structural analysis in your browser
<a href="https://tensora.app/" title="Tensora.app: free online structural analysis"><img class="tensora-logo" alt="Tensora.app: free online structural analysis and mechanics of materials tools" src="{static}/imgs/tensora-logo.png" width="600" height="149"></a>

<figure class="video-preview">
<a href="https://www.youtube.com/shorts/0tKTx6MyMIY" title="Tensora.app preview on YouTube"><img src="{static}/imgs/tensora-short-preview.jpg" alt="Tensora.app solving a portal frame: bending moment diagram and deflected shape" width="540" height="540" loading="lazy"></a>
<figcaption><i class="fa-brands fa-youtube"></i> <a href="https://www.youtube.com/shorts/0tKTx6MyMIY">1-minute preview</a>: bending moments and deflected shapes</figcaption>
</figure>

**[Tensora.app](https://tensora.app/)** is a free web application for **structural analysis and mechanics of materials**, for students and engineers in civil, mechanical and industrial engineering. Define nodes, beams, loads and supports, and it solves **2D beams, trusses and frames** with the finite element method and draws the **axial force, shear force and bending moment diagrams** and the **deflected shape** as you edit the model. It runs entirely in the browser, with no installation or sign-up: its solver is my C++ structural analysis library, OpenBeam, compiled to WebAssembly.

* **Structural analysis**: beams, continuous beams, trusses and frames, with a gallery of classic cases (cantilevers, fixed-fixed beams, Warren truss, portal and three-hinged frames) ready to modify and solve.
* **Mohr's circle**: interactive 2D Mohr circle of a plane stress state, with shareable links and PNG export.
* **3D stress tensor**: traction vectors on the sphere of normals, principal stresses and directions, and the three Mohr circles.
* **Languages**: English, Spanish, French and Chinese.
* **Website**: [tensora.app](https://tensora.app/)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebApplication",
  "name": "Tensora.app",
  "url": "https://tensora.app/",
  "description": "Free online structural analysis and mechanics of materials tools: 2D beams, trusses and frames with axial, shear and bending moment diagrams and deflected shapes, Mohr circles and 3D stress tensors. Runs in the browser.",
  "applicationCategory": "EducationalApplication",
  "applicationSubCategory": "Structural analysis",
  "operatingSystem": "Any (web browser)",
  "inLanguage": ["en", "es", "fr", "zh"],
  "isAccessibleForFree": true,
  "offers": { "@type": "Offer", "price": "0", "priceCurrency": "EUR" },
  "image": "https://tensora.app/og-image.png",
  "author": {
    "@type": "Person",
    "name": "Jose Luis Blanco Claraco",
    "url": "https://w3.ual.es/~jlblanco/"
  },
  "video": {
    "@type": "VideoObject",
    "name": "tensora.app: online structural analysis (bending moments, deflected shapes)",
    "description": "Tensora.app solving 2D frames in the browser: bending moment diagrams and deflected shapes.",
    "thumbnailUrl": "https://i.ytimg.com/vi/0tKTx6MyMIY/maxresdefault.jpg",
    "uploadDate": "2026-11-10T17:05:47+00:00",
    "contentUrl": "https://www.youtube.com/shorts/0tKTx6MyMIY",
    "embedUrl": "https://www.youtube.com/embed/0tKTx6MyMIY"
  }
}
</script>

---

## Core Robotics Frameworks

### MOLA: Modular Optimization and Localization Abstraction
<a href="https://docs.mola-slam.org/"><img class="sw-logo" alt="MOLA" src="{static}/imgs/mola-slam-logo.png"></a>

The successor to the SLAM foundations of MRPT, **MOLA** is a modular, high-performance C++ framework designed for lifelong SLAM, localization, and mapping. It is built to be highly extensible through a plugin-based architecture, and includes a state-of-the-art LiDAR odometry and the `mp2p_icp` point cloud registration library.

* **Status**: Active / Most Relevant
* **Documentation**: [docs.mola-slam.org](https://docs.mola-slam.org/)
* **Repository**: [github.com/MOLAorg](https://github.com/MOLAorg)

### MRPT: Mobile Robot Programming Toolkit
<a href="https://www.mrpt.org/"><img class="sw-logo" alt="MRPT" src="{static}/imgs/Mrpt_logo_vertical.png"></a>

A mature, cross-platform C++ library (2005-present) providing developers with a vast collection of algorithms for robotics: SLAM, computer vision, and motion planning.

* **Highlights**: Extensive support for 2D/3D range sensors, probabilistic motion models, and real-time visualization.
* **Website**: [www.mrpt.org](https://www.mrpt.org/)
* **Repository**: [github.com/MRPT](https://github.com/MRPT)

### MVSim: Multi-Vehicle Simulator
A lightweight, realistic 2.5D dynamics simulator for wheeled robots and multi-agent research, with simulated LiDARs, cameras and other sensors. Worlds are fully configured via XML files, and it runs standalone, as a ROS 2 node, or embedded in C++/Python applications, including a headless mode for CI pipelines.

* **Documentation**: [mvsimulator.readthedocs.io](https://mvsimulator.readthedocs.io/)
* **Repository**: [github.com/MRPT/mvsim](https://github.com/MRPT/mvsim)

### nanoflann
A header-only C++ library for building KD-trees and running fast nearest neighbor searches on point clouds and other datasets, widely used in robotics, computer graphics, and machine learning.

* **Repository**: [github.com/jlblancoc/nanoflann](https://github.com/jlblancoc/nanoflann)

---

## ROS Ecosystem
<img class="sw-logo" alt="ROS" src="{static}/imgs/ros-300x70.png">

I maintain a wide variety of ROS 2 integrations to bridge high-performance C++ backends with the ROS middleware.

* **MRPT ROS Packages**: The official bridge between MRPT and ROS 2, including [`mrpt_navigation`](https://docs.ros.org/en/rolling/p/mrpt_navigation/), [`mrpt_slam`](https://docs.ros.org/en/rolling/p/mrpt_slam/) and [`mrpt_sensors`](https://github.com/mrpt-ros-pkg/mrpt_sensors).
* **MOLA and MVSim**: Both are available as binary ROS 2 packages.
* **UAL ARM ROS**: Packages specifically for robotic arm control and integration.
* **GitHub Orgs**: [github.com/mrpt-ros-pkg](https://github.com/mrpt-ros-pkg) | [github.com/ual-arm-ros-pkg](https://github.com/ual-arm-ros-pkg)

---

## Specialized Engineering Organizations

### Multibody Dynamics & Simulation (MBDS)
Tools and libraries focused on the simulation of complex mechanical systems and multibody dynamics.

* **Repository**: [github.com/MBDS](https://github.com/MBDS)

### LibreDAQ: Open Data Acquisition
A collection of projects dedicated to open-source hardware and software interfaces for data acquisition.

* **Repository**: [github.com/LibreDAQ](https://github.com/LibreDAQ)

### Mechanical Design & Structural Analysis
<a href="https://github.com/jlblancoc/mechplot"><img class="sw-logo" alt="Mechplot" src="{static}/imgs/mechplot_icon.png"></a>

* **Open-Beam**: Specialized tools for structural and beam analysis. ([github.com/open-beam](https://github.com/open-beam)). Its C++ solver powers [Tensora.app, the online structural analysis tool](https://tensora.app/).
* **Mechplot**: A MATLAB library for rendering structures and mechanisms. ([github.com/jlblancoc/mechplot](https://github.com/jlblancoc/mechplot))

---

## Developer Tools & Utilities

* **[SuiteSparse-METIS for Windows](https://github.com/jlblancoc/suitesparse-metis-for-windows)**: A CMake-based build system that enables the use of these powerful sparse matrix libraries in Visual Studio and other CMake-supported IDEs.
* **[RWL (Recursive World Language)](https://code.google.com/archive/p/recursive-world-toolkit)**: A domain-specific language and interpreter for generating vast simulated worlds for SLAM benchmarking.
* **[Eigen](https://libeigen.gitlab.io/)**: Proud (though minor) contributor to this world-class C++ template library for linear algebra.

---

## Didactic & Historical Projects

* **[A tutorial on SE(3) transformation parameterizations and on-manifold optimization](https://github.com/jlblancoc/tutorial-se3-manifold)**: Technical report on Lie groups for 3D pose estimation, with its LaTeX sources.
* **[Robotics teaching notebooks](https://github.com/jlblancoc/robotics-teaching)**: Jupyter notebooks used in Robotics courses at UAL.
* **[Mohr 2D GUI](https://github.com/jlblancoc/mohr-2d-gui)**: Visualizes a 2D stress tensor and its Mohr's circle.
* **[Maxwell-Boltzmann Simulator](https://github.com/jlblancoc/maxwell-boltzmann-simulator)**: A graphical simulator illustrating the kinetic theory of gases and probability distributions.
* **[Denavit-Hartenberg GUI](https://docs.mrpt.org/reference/latest/app_robotic-arm-kinematics.html)**: A visual tool for learning and teaching robotic arm kinematics, distributed with MRPT.
* **[OpenMORA](https://github.com/OpenMORA) (2008-2014)**: A middleware framework based on MOOS and MRPT. This was before ROS took off.
* **[Open-CV Bots](https://github.com/jlblancoc/open-cv-bots)**: Experimental computer vision programs designed to autonomously play web-based games.
* **[Syncpath](https://sourceforge.net/projects/syncpath/)**: A lightweight, cross-platform CLI tool for directory synchronization and backups.
