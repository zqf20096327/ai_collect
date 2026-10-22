# PPIprediction

Software used in the paper:

Daberdaku S, Ferrari C. Exploring the potential of 3D Zernike descriptors and SVM for protein–protein interface
prediction. BMC Bioinformatics 19, 35 (2018). https://doi.org/10.1186/s12859-018-2043-3

The surface computation and the 3D Zernike surface descriptors were developed in the PhD thesis: Daberdaku S. Protein
contour modelling and computation for complementarity detection and docking. University of Padova (2016).
http://hdl.handle.net/11577/3421792 (chapter 2 for the surfaces, chapters 3 and 4 for the descriptors).

## Contents
* `train` and `test`: prebuilt executables (Linux x86-64, statically linked). They compute the 3D Zernike descriptors
  of surface patches from a receptor and a ligand PDB file, and write the training and test samples.
* `interface_descriptors_train/` and `interface_descriptors_test/`: the C++ sources and Makefiles of the two executables.
* `CHARMM22`: the atomic radii used during the surface computation.
* Python scripts used in the experiments: SVM hyperparameter search and training, selection of the SVM threshold and of
  the Isolation Forest contamination value, and evaluation on the test set.

## Running the executables
The `CHARMM22` file contains the atomic radii information used during the surface computation process. Users can
append new entries at the end of this file, modify existing ones, or create their own file with the desired radius
assignment for each atom type. The easiest way to run the binaries is to place the binary, the `CHARMM22` file and the
two PDB files in the same directory. The location of the `CHARMM22` file can also be given with the `--atom_radii`
option.

```bash
./train --receptor receptor.pdb --ligand ligand.pdb
./test --receptor receptor.pdb --ligand ligand.pdb
```

Output of `./train -h`:
```
PPI prediction - Training samples generator. Usage:
  -h [ --help ]                         Display this brief help message.
  --receptor arg                        Name of the receptor's PDB file.
  --ligand arg                          Name of the ligand's PDB file.
  --atom_radii arg                      File containing the radius information 
                                        of each atom. If not specified, the 
                                        default CHARMM22 radius values will be 
                                        used for PDB files. It is ignored if 
                                        specified for PQR files.
  --no_hetatm                           Ignore HETATM records in the surface 
                                        computation.
  --no_hydrogen                         Ignore hydrogen atoms in the surface 
                                        computation.
                                        NOTE: X-ray crystallography cannot 
                                        resolve hydrogen atoms in most protein 
                                        crystals, so in most PDB files, 
                                        hydrogen atoms are absent. Sometimes 
                                        hydrogens are added by modeling. 
                                        Hydrogens are always present in PDB 
                                        files resulting from NMR analysis, and 
                                        are usually present in theoretical 
                                        models.
  --surf_description                    Prints a brief description of the 
                                        supported surface types.
  -p [ --probe_radius ] arg (=1.4)      Probe radius (in Å), floating point 
                                        number in (0, 2.0] (default is 1.4Å).
  -R [ --patch_radius ] arg (=6)        Patch radius (in Å), positive floating
                                        point (default is 6.0Å).
  -t [ --patch_threshold ] arg (=0.8)   Threshold value used for the interface 
                                        patch determination (between 0 and 1, 
                                        default is 0.8).
  -i [ --interface_distance ] arg (=4.5)
                                        Threshold distance for the interface 
                                        determination (in Å), positive 
                                        floating point (default is 4.5Å).
  -d [ --nint_patch_dist ] arg (=4.5)   Minimum distance between non-interface 
                                        patch centers (in Å), positive 
                                        floating point (default is 4.5Å).
  -D [ --int_patch_dist ] arg (=1)      Minimum distance between interface 
                                        patch centers (in Å), positive 
                                        floating point (default is 1.0Å).
  -r [ --resolution ] arg (=4)          Resolution factor, positive floating 
                                        point (default is 4.0). This value's 
                                        cube determines the number of voxels 
                                        per Å³.
  -N [ --max_order ] arg (=20)          Maximum Zernike descriptor order 
                                        (default is 20)
  -l [ --license ]                      View license information.
  -v [ --version ]                      Display the version number
```

`./test -h` lists the same options, except that the two patch distances are replaced by one, `-d` / `--patch_dist`
(minimum distance between patch centers, default 1.8 Å).

## Building from source
The executables need g++ with OpenMP support and the Boost libraries `program_options`, `regex`, `system` and
`filesystem`. Tested with GCC 13 and Boost 1.83 on Ubuntu 24.04:

```bash
sudo apt-get install g++ make libboost-program-options-dev libboost-regex-dev \
    libboost-system-dev libboost-filesystem-dev
cd interface_descriptors_train   # or interface_descriptors_test
make all
```

Each Makefile builds one executable into its own `bin/` folder. The Makefiles link statically and compile with
`-march=native`, so the executables run on CPUs like the one they were built on.

## Python scripts
The scripts are written for Python 2.7 and use NumPy, SciPy, scikit-learn, matplotlib, joblib and Biopython. They use
scikit-learn APIs that later releases removed (for example `RandomizedLogisticRegression`), so they need an old
scikit-learn release. The dataset paths are hard-coded and must be changed before running them.

## License
[BSD 3-Clause](LICENSE)
