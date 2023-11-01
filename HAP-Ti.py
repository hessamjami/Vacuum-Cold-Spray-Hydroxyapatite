from lammps import lammps

# Initialize LAMMPS
lmp = lammps()
lmp.command("echo both")
lmp.command("units real")
lmp.command("boundary p p p")
lmp.command("atom_style full")

# Atom Definition
lmp.command("read_data data.data")
lmp.command("lattice custom 3.01 a1 1.0 0.0 0.0 a2 0.0 1.41421356 0.0 a3 0.0 0.0 1.41421356 basis 0.0 0.0 0.0 basis 0.0 0.5 0.5")
lmp.command("region Substrate block -49 49 -49 49 -89 -40 units box")
lmp.command("create_atoms 5 region Substrate")
lmp.command("group substrate type 5")
lmp.command("group HAP type 1 2 3 4")

# Dreiding potential information
lmp.command("bond_style harmonic")
lmp.command("bond_coeff 1 350 0.98")
lmp.command("bond_coeff 2 350 0.98")
lmp.command("bond_coeff 3 350 0.98")
lmp.command("bond_coeff 4 350 0.98")
lmp.command("bond_coeff 5 350 1.54")
lmp.command("pair_style hybrid lj/cut 2.5 eam/fs")
lmp.command("pair_coeff * * eam/fs Ti.eam.fs NULL NULL NULL NULL Ti")
lmp.command("pair_coeff 1 1 lj/cut 0.012 3.472")
lmp.command("pair_coeff 2 2 lj/cut 0.002 3.2")
lmp.command("pair_coeff 3 3 lj/cut 0.104 3.71")
lmp.command("pair_coeff 4 4 lj/cut 0.054 4.295")
lmp.command("pair_coeff 1 2 lj/cut 0.005 3.333")
lmp.command("pair_coeff 1 3 lj/cut 0.035 3.589")
lmp.command("pair_coeff 1 4 lj/cut 0.025 3.862")
lmp.command("pair_coeff 2 3 lj/cut 0.014 3.446")
lmp.command("pair_coeff 2 4 lj/cut 0.010 3.707")
lmp.command("pair_coeff 3 4 lj/cut 0.075 3.992")
lmp.command("pair_coeff 1 5 lj/cut 0.012 3.472")
lmp.command("pair_coeff 2 5 lj/cut 0.005 3.333")
lmp.command("pair_coeff 3 5 lj/cut 0.035 3.589")
lmp.command("pair_coeff 4 5 lj/cut 0.025 3.862")

# Equilibration (Langevin dynamics at 300 K)
lmp.command("velocity all create 300 12345 rot yes mom yes dist uniform")
lmp.command("fix 1 all nve/limit 0.05")
lmp.command("fix 2 all langevin 300.0 300.0 1.0 904297")
lmp.command("fix 3 HAP setforce NULL NULL NULL")
lmp.command("thermo_style custom step temp pe")
lmp.command("thermo_modify lost ignore")
lmp.command("thermo_modify lost/bond ignore")
lmp.command("thermo 10")
lmp.command("timestep 0.1")
lmp.command("run 3000")

# Run Minimization
lmp.command("reset_timestep 0")
lmp.command("thermo 10")
lmp.command("thermo_style custom step temp pe")
lmp.command("min_style cg")
lmp.command("minimize 1e-20 1e-20 1000 1000")

lmp.command("unfix 1")
lmp.command("unfix 3")
lmp.command("velocity substrate create 300 12345 mom yes rot yes dist uniform")
lmp.command("velocity HAP set 0 0 -9")
lmp.command("fix 1 all nve")

# Compute Local Temp
lmp.command("thermo_modify lost ignore")
lmp.command("thermo_modify lost/bond ignore")
lmp.command("run 30000000")

# Close LAMMPS
lmp.close()
