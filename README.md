# Vacuum-Cold-Spray-Hydroxyapatite
This repository contains C++ code for MD simulations of high-velocity impacts of hydroxyapatite (HA) nanoparticles on a titanium substrate. The code allows you to study the mechanical deformation, stress, and temperature during these fast impacts, providing insights into the bonding mechanisms of HA particles with the substrate.
#Abstract:

Hydroxyapatite [Ca10 (PO4)6 (OH)2] is the primary mineral component of bone and teeth, widely used for implant coatings due to its osteoconductive and bioactive properties, essential for early bone formation. Aerosol deposition (AD), a novel coating method using a cold vacuum spray, offers the opportunity to produce robust, dense, and pore-free coatings with nanoceramic particles like hydroxyapatite (HA). However, the high-velocity impact of HA particles on underlying substrates, such as titanium, is poorly understood.

In this repository, we employ large-scale molecular dynamics simulations to reveal the mechanical deformation, stress, and temperature profiles during the rapid impact of 3 nm HA particles on a titanium surface. We discuss the impact of deposition velocity on deformation and the development of mechanical stresses and temperatures in both the particle and substrate.

Our simulations demonstrate that at ultrahigh strain rates (>1010 s−1), the temperatures of the particle and substrate rapidly rise within picoseconds to ~1100–1253 K, depending on the impact velocity. However, these temperatures remain below the melting points of the materials. The simulations capture the initial elastic deformation, followed by yield and plastic deformation of the particle. We also explore the dependence of particle penetration depth and structural transformation of the top layers of titanium on particle velocity, revealing ultrafast mechanisms of particle–substrate bonding.
# Hydroxyapatite (HA) Nanoparticles on Titanium Substrate Simulation

This repository contains a LAMMPS input script to perform molecular dynamics simulations of high-velocity impacts of hydroxyapatite (HA) nanoparticles on a titanium substrate. The simulations provide insights into the mechanical deformation, stress, and temperature during these impacts, helping to understand the bonding mechanisms of HA particles with the substrate.

## Usage

1. Clone this repository to your local machine.
2. Prepare the necessary data file (data.data) with atomic structures.
3. Set up LAMMPS with the input script (in.lammps) in the same directory.
4. Run the simulation using LAMMPS:
lmp_serial.exe -in in.txt

Replace `lmp_serial.exe` with the appropriate LAMMPS executable on your system. Make sure you have LAMMPS installed and configured to run this simulation.

## Dependencies

- LAMMPS
- C++ Compiler

For more details on the simulation and the choice of potential, please refer to the provided input script.

If you use this code or find it helpful, consider citing the corresponding publication in your work.

## Publication

- Title: Ultrafast Thermomechanical Effects in Aerosol Deposition of Hydroxyapatite Nanoparticles on a Titanium Substrate
- Author:H Jami and A Jabbarzadeh 
- Journal: Surface and Coatings Technology
- Publication date 2019/11


