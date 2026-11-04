<p align="center">
  <a href="https://github.com/loumalouomega/meshioplusplus"><img alt="meshio++" src="https://raw.githubusercontent.com/loumalouomega/meshioplusplus/master/doc/logo/logo-with-text.svg" width="60%"></a>
  <p align="center">I/O for mesh files.</p>
</p>


[![PyPi Version](https://img.shields.io/pypi/v/meshioplusplus.svg?style=flat-square)](https://pypi.org/project/meshioplusplus/) [![npm Version](https://img.shields.io/npm/v/%40meshioplusplus%2Fwasm.svg?style=flat-square)](https://www.npmjs.com/package/@meshioplusplus/wasm) [![PyPI pyversions](https://img.shields.io/pypi/pyversions/meshioplusplus.svg?style=flat-square)](https://pypi.org/project/meshioplusplus/) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21629061.svg?style=flat-square)](https://doi.org/10.5281/zenodo.21629061)

[![C++][c++-image]][c++standard] [![Python](https://img.shields.io/badge/Python-3.10%2B-3776ab.svg?style=flat-square&logo=python&logoColor=white)](https://pypi.org/project/meshioplusplus/) [![C](https://img.shields.io/badge/C-99-a8b9cc.svg?style=flat-square&logo=c&logoColor=white)](doc/c_api.md) [![Fortran](https://img.shields.io/badge/Fortran-2008-734f96.svg?style=flat-square&logo=fortran&logoColor=white)](doc/fortran.md) [![Julia](https://img.shields.io/badge/Julia-1.9%2B-9558b2.svg?style=flat-square&logo=julia&logoColor=white)](doc/julia.md) [![R](https://img.shields.io/badge/R-4.0%2B-276dc3.svg?style=flat-square&logo=r&logoColor=white)](doc/r.md) [![Octave](https://img.shields.io/badge/Octave%20%2F%20MATLAB-MEX-0076a8.svg?style=flat-square&logo=octave&logoColor=white)](doc/octave.md) [![WebAssembly](https://img.shields.io/badge/WebAssembly-npm-654ff0.svg?style=flat-square&logo=webassembly&logoColor=white)](https://www.npmjs.com/package/@meshioplusplus/wasm) [![TypeScript](https://img.shields.io/badge/TypeScript-viewer-3178c6.svg?style=flat-square&logo=typescript&logoColor=white)](src/viewer/) [![Spack](https://img.shields.io/badge/spack-meshioplusplus-1f79c2.svg?style=flat-square)](https://packages.spack.io/package.html?name=meshioplusplus) [![Blender](https://img.shields.io/badge/Blender-4.2%2B-ea7600.svg?style=flat-square&logo=blender&logoColor=white)](doc/blender.md)

[![GitHub stars](https://img.shields.io/github/stars/loumalouomega/meshioplusplus.svg?style=flat-square&logo=github&label=Stars&logoColor=white)](https://github.com/loumalouomega/meshioplusplus) [![PyPi downloads](https://img.shields.io/pypi/dm/meshioplusplus.svg?style=flat-square)](https://pypistats.org/packages/meshioplusplus)
[![GitHub release date](https://img.shields.io/github/release-date/loumalouomega/meshioplusplus?style=flat-square&label=release)](https://github.com/loumalouomega/meshioplusplus/releases/latest) [![Commits since latest release](https://img.shields.io/github/commits-since/loumalouomega/meshioplusplus/latest?style=flat-square&label=commits%20since)](https://github.com/loumalouomega/meshioplusplus/compare/v16.22.0...master) [![GitHub last commit](https://img.shields.io/github/last-commit/loumalouomega/meshioplusplus?style=flat-square&label=latest%20commit)](https://github.com/loumalouomega/meshioplusplus/commit/master)

[![gh-actions](https://img.shields.io/github/actions/workflow/status/loumalouomega/meshioplusplus/ci.yml?branch=master&style=flat-square)](https://github.com/loumalouomega/meshioplusplus/actions?query=workflow%3Aci) [![codecov](https://img.shields.io/codecov/c/github/loumalouomega/meshioplusplus.svg?style=flat-square)](https://app.codecov.io/gh/loumalouomega/meshioplusplus) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)

[c++-image]: https://img.shields.io/badge/C++-20-blue.svg?style=flat&logo=c%2B%2B
[c++standard]: https://isocpp.org/std/the-standard

There are various mesh formats available for representing unstructured meshes. meshio++ can read and write all of the following and smoothly converts between them:

Native parity additions: XDMF2/3 and absolute DataItem references; Netgen name/periodic tables, two-line edges and zlib-enabled `.vol.gz`; PCD compressed writes via `MIO_CODEC_LZF` / `codec="lzf"`; and parameterized glTF export in C, Fortran, Julia, R and WASM. See [formats](doc/formats.md), [C API](doc/c_api.md) and [WASM](doc/wasm.md) for options and indexing conventions.

Region-backed point/cell sets now convert to and from scalar integer data in the native core, C/Fortran/Julia/R/WASM bindings and native CLI `convert -s/-d`. Python's mutating `Mesh` methods preserve their ordering and metadata contract; pipelines expose `SetsToData` / `DataToSets`, and MCP exposes `sets_data`. See [sets/data conversions](doc/data_manage.md#sets--integer-data).

Native C/Fortran/Julia/R pipelines also expose owning structured JSON reports (`steps` and `warnings`), without replacing their existing status-only entry points; see [pipeline reports](doc/pipeline.md#structured-reports-on-the-flat-abi).

Exodus writers now preserve node/side sets and expose fixed-grid time-series writers across Python, C++, C, Fortran, Julia, R and WASM; sequence fan-in can write one Exodus file. Pipeline schema Version 2 adds file-backed `Merge`/`Interpolate`/`UndoGreen` and terminal `Split`/`Partition` with `Output.Pattern`. Version 1 remains unchanged. See [Exodus](doc/formats/exodus.md#stateful-series-writing) and [pipeline v2](doc/pipeline.md#version-2-spatial-multi-mesh-steps).

XDMF time-series writers preserve fixed point, cell and side regions alongside the shared topology. Python's array-based writer accepts `regions=` and its series reader exposes `reader.regions`; native writers use the regions already on the mesh. See [XDMF time series](doc/xdmf_time_series.md).

Serial VTK XML readers (`.vtu`, `.vtp`, `.vts`, `.vtr`, `.vti`) accept multiple pieces and appended raw/base64 arrays in both the native core and Python reference, with UInt32/UInt64 headers and either byte order. Pieces concatenate without welding; VTP/VTS/VTR/VTI writers remain inline. Native legacy `.vtk` reads also support structured points, structured grids and rectilinear grids in ASCII and big-endian binary; see the [format documentation](doc/formats.md).

> [Abaqus](https://help.3ds.com/2024/english/dssimulia_established/SIMACAEMODRefMap/simamod-c-inputsyntax.htm) (`.inp`),
> [Abaqus results file](https://ceae-server.colorado.edu/v2016/books/usb/pt02ch05s01afi01.html) (`.fil`, ASCII and binary; every increment is a step, nodal and element results by output location; written too, the model and an increment per step),
> [ANSYS Fluent](https://www.ansys.com/products/fluids/ansys-fluent) mesh (`.msh`; cells rebuilt from faces, written face-based as Fluent reads it, zones as named regions),
> [Ansys MAPDL](https://www.ansys.com) coded database (`.cdb`, `.inp`; degenerate shapes resolved, components as named regions) and results (`.rst`, `.rth`; nodal solution, reactions and element nodal stresses, strains and forces, every result set is a step; distributed solves merged, the full rotor of a static cyclic model),
> [AVS-UCD](https://lanl.github.io/LaGriT/pages/docs/read_avs.html) (`.avs`),
> [CAE sample layout](https://docs.nvidia.com/physicsnemo/) (`.npz`, what PhysicsNeMo's DoMINO/Transolver datapipes read),
> [CGNS](https://cgns.github.io/) (`.cgns`),
> [DOLFIN XML](https://manpages.ubuntu.com/manpages/jammy/en/man1/dolfin-convert.1.html) (`.xml`),
> [DOLFINx VTX](https://docs.fenicsproject.org/dolfinx/main/python/generated/dolfinx.io.html) (`.bp`, an ADIOS2 directory, read and written; each step a mesh, with an optional ADIOS2 build or the `adios2` package),
> [COMSOL](https://www.comsol.com) mesh (`.mphtxt` text and `.mphbin` binary; Selections as named regions, COMSOL's own node order),
> [Exodus](https://nschloe.github.io/meshio/exodus.pdf) (`.e`, `.exo`),
> [Elmer](https://www.elmerfem.org) mesh directory (`mesh.header`/`.nodes`/`.elements`/`.boundary`/`.names`, text or ElmerGrid's binary; bodies and boundaries as named regions, ElmerGrid partitions merged, `partition:part` written as `partitioning.N`, recognised by content),
> [EnSight Gold](https://vis.lbl.gov/archive/NERSC/Software/ensight/doc/OnlineHelp/UM-C11.pdf) (geometry, `.case`/`.geo`; C and Fortran binary),
> [FEBio](https://febio.org) input (`.feb`, spec 2.5/3.0/4.0 read, 4.0 written; sets and surfaces as named regions, MeshData read and written) and plot files (`.xplt`; every state is a step, remeshed runs included, surface variables on facet blocks),
> [Femap](https://www.sw.siemens.com/en-US/simcenter/femap/) neutral file (`.neu`, 4.41 to 2020.1 read, 8.2 mesh written; properties and groups as named regions, every output set is a step, a series written as one output set per step),
> [FLAC3D](https://www.itascacg.com/software/flac3d) (`.f3grid`, named cell groups),
> [FLUX](https://www.altair.com/flux/) (mesh `.pf3`, field `.dex`),
> [FreeFem++](https://freefem.org/) (`.msh`),
> [GiD postprocess](https://www.gidsimulation.com/) (`.post.msh`/`.post.res`, `.post.bin`, `.post.h5`; writing via a vendored gidpost, reading is meshio++'s own code),
> [H5M](https://www.mcs.anl.gov/~fathom/moab-docs/h5mmain.html) (`.h5m`),
> [Code_Aster](https://code-aster.org) native mesh (`.mail`; `GROUP_MA`/`GROUP_NO` as named regions, Code_Aster's own node order),
> [CalculiX](http://www.dhondt.de/) results (`.frd`, ASCII or binary written too; every increment is a step, tensors keep the file order, opt-in von Mises and principal values),
> [HMF](https://loumalouomega.github.io/meshioplusplus/formats/hmf) (`.hmf`, experimental, meshio++-specific),
> [IGES](https://loumalouomega.github.io/meshioplusplus/formats/iges) (`.igs`, `.iges`, read-only, through OpenCASCADE; triangulated, with its NURBS B-rep),
> [I-deas Universal / UNV](https://www.ceas3.uc.edu/sdrluff/) (`.unv`, `.uff`),
> [ANSYS Fluent interpolation](https://github.com/victorsndvg/FEconv) (`.ip`),
> [Kratos/MDPA](https://github.com/KratosMultiphysics/Kratos/wiki/Input-data) (`.mdpa`; tables, geometries, `Mesh` blocks and `Constraints`, including nested sub-model-part geometry/constraint membership, kept in a side channel on every surface; the Kratos IGA geometry beside a deck loaded with it),
> [Kratos CAD JSON](https://loumalouomega.github.io/meshioplusplus/formats/cad_json) (`.cad.json`; trimmed NURBS faces, trimming loops and coupling edges for Kratos IGA, sampled as Lagrange cells and kept exactly in a side channel on every surface, and the `ImportNurbsSbmModeler` dialect),
> [libMesh](https://libmesh.github.io/) (`.xda`, `.xdr`, also gzip/bzip2; active cells of refined meshes, subdomains, side, edge, shell-face and node sets as named regions, written back in the 1.8.0 layout),
> [LS-DYNA](https://lsdyna.ansys.com/manuals-download/) (keyword input `.k`, `.key`, `.dyn`; `*PART` and `*SET_*` as named regions, `*INCLUDE` followed),
> [LS-DYNA d3plot](https://loumalouomega.github.io/meshioplusplus/formats/lsdyna_d3plot) (the binary state database, `d3plot` and its `d3plot01`... family, read and write; every state is a step, parts are regions, deletion flags a mask; SPH, airbag particles, rigid bodies and roads),
> [LS-DYNA binout](https://loumalouomega.github.io/meshioplusplus/formats/lsdyna_binout) (the LSDA binary output; `nodout` outputs are steps, the other databases field data; written too, a `nodout` cloud per step with each database on its own cadence),
> [Medit](https://people.sc.fsu.edu/~jburkardt/data/medit/medit.html) (`.mesh`, `.meshb`) and its solutions (`.sol`, `.solb`; size maps and metrics for MMG, vertex and element fields attached to their mesh),
> [MFEM](https://mfem.org) mesh (`.mesh`, recognised by content; order-2 curved meshes in MFEM's own numbering, attribute sets as named regions, NURBS meshes with their patches kept and written back) and grid functions (`.gf`),
> [MED/Salome](https://docs.salome-platform.org/latest/dev/MEDCoupling/developer/med-file.html) (`.med`; native named multi-mesh access and nodal/element profile expansion),
> [Modulef](https://github.com/victorsndvg/FEconv) (mesh `.mfm`, field `.mff`),
> [Nastran](https://help.autodesk.com/view/NSTRN/2019/ENU/?guid=GUID-42B54ACB-FBE3-47CA-B8FE-475E7AD91A00) and [Altair OptiStruct](https://help.altair.com/hwsolvers/os/index.htm) (bulk data, `.bdf`, `.fem`, `.nas`; HyperMesh components and OptiStruct `SET`s as named regions),
> [MSC Nastran HDF5](https://simulatemore.mscsoftware.com/hdf5-a-useful-enhancement-for-msc-nastran-and-patran/) results (`.h5`; every subcase, mode, time or frequency is a step; coordinate systems applied; corner, ply, station and grid point force values; written too, with nodal results and the centre stress and strain of shells, solids and rods, one step per call or a series),
> [Nastran OP2](https://loumalouomega.github.io/meshioplusplus/formats/nastran_op2) results (`.op2`, MSC and NX, 32- and 64-bit; every subcase, mode, time or frequency is a step; coordinate systems applied; corner, ply, station and grid point force values),
> [Netgen](https://github.com/ngsolve/netgen) (`.vol`, `.vol.gz`),
> [Neuroglancer precomputed format](https://github.com/google/neuroglancer/tree/master/src/datasource/precomputed#mesh-representation-of-segmented-object-surfaces),
> [Gmsh](https://gmsh.info/doc/texinfo/gmsh.html#File-formats) (format versions 2.2, 4.0, and 4.1, `.msh`; native periodic reads across language bindings via format metadata, periodic writes in 2.2/4.1),
> [glTF 2.0](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html) (read as a general glTF 2.0 reader; written as the surface with per-vertex normals, fields as `_NAME` attributes, `color_by` into `COLOR_0`) (`.glb`, `.gltf`),
> [OBJ](https://en.wikipedia.org/wiki/Wavefront_.obj_file) (`.obj`),
> [OFF](https://segeval.cs.princeton.edu/public/off_format.html) (`.off`),
> [OpenFOAM polyMesh](https://www.openfoam.com/) (`.foam`),
> [OpenUSD](https://openusd.org/) (`.usd`, `.usda`, `.usdc`),
> [OpenRadioss](https://openradioss.org/) starter deck (`_0000.rad`; parts, subsets, groups, boxes and surfaces as named regions, units applied, `#include` followed; written with optional placeholder materials and properties), animation files (`<run>A001`…; one state per file, a run's files a transient sequence) and time-history files (`<run>T01`; each output a step of field data; written too, from the `radioss_th:*` field data),
> [MSC Marc](https://hexagon.com/products/marc) input deck (`.dat`, written by name) and formatted post file (`.t19`; `DEFINE` sets as named regions, every increment is a step),
> [MSC Patran 2 neutral file](https://hexagon.com/products/patran) (`.pat`, `.out`; named components as regions),
> [PCD](https://pointclouds.org/documentation/tutorials/pcd_file_format.html) (Point Cloud Library point clouds, `ascii`/`binary`/`binary_compressed`) (`.pcd`),
> [PERMAS](https://www.intes.de) (`.post`, `.post.gz`, `.dato`, `.dato.gz`),
> [PhysicsNeMo mesh](https://developer.nvidia.com/physicsnemo) (`.pmsh`, memory-mapped),
> [PLY](<https://en.wikipedia.org/wiki/PLY_(file_format)>) (`.ply`),
> [PVD](https://docs.vtk.org/en/latest/vtk_file_formats/vtkxml_file_format.html) (`.pvd`; a time-indexed collection of serial or parallel VTK XML files, read by ParaView),
> [PVTP](https://docs.vtk.org/en/latest/vtk_file_formats/vtkxml_file_format.html) (`.pvtp`; a parallel index over per-piece `.vtp` files) and
> [PVTU](https://docs.vtk.org/en/latest/vtk_file_formats/vtkxml_file_format.html) (`.pvtu`; a parallel index over per-piece `.vtu` files, ghost cells and `partition` output included),
> [STEP](https://en.wikipedia.org/wiki/ISO_10303-21) (a closed surface written as an AP214 solid that CAD tools open, one face per plane, cylinder, cone, sphere or torus; read through OpenCASCADE as a triangulation plus its NURBS B-rep, healed and sewn on request with `heal=True`) (`.step`, `.stp`),
> [STL](<https://en.wikipedia.org/wiki/STL_(file_format)>) (`.stl`),
> [Tecplot](http://paulbourke.net/dataformats/tp/) (`.dat`, `.tec`, and binary `.plt`; FE, ordered, polygonal and polyhedral zones; `.szplt` through a TecIO you supply),
> [TetGen .node/.ele](https://wias-berlin.de/software/tetgen/fformats.html),
> [Triangle .node/.ele/.poly](https://www.cs.cmu.edu/~quake/triangle.html),
> [SVG](https://www.w3.org/TR/SVG/) (2D drawing: 2D direct, 3D via skin projection; reads back only what meshio++ wrote, as planar) (`.svg`),
> [TikZ](https://tikz.dev/) (LaTeX 2D drawing: 2D direct, 3D via skin projection; reads back only what meshio++ wrote, as planar) (`.tikz`),
> [SU2](https://su2code.github.io/docs_v7/Mesh-File/) (`.su2`),
> [UGRID](https://www.simcenter.msstate.edu/software/documentation/ug_io/3d_grid_file_type_ugrid.html) (`.ugrid`),
> [VTI](https://docs.vtk.org/en/latest/vtk_file_formats/vtkxml_file_format.html) (VTK XML ImageData; a regular lattice) (`.vti`),
> [VTK](https://vtk.org/wp-content/uploads/2015/04/file-formats.pdf) (`.vtk`),
> [VTKHDF](https://docs.vtk.org/en/latest/vtk_file_formats/vtkhdf_file_format/index.html) (`.vtkhdf`; Kitware's HDF5-based VTK format: time, partitions and fields in one file, read by ParaView),
> [VTM](https://docs.vtk.org/en/latest/vtk_file_formats/vtkxml_file_format.html) (`.vtm`; a VTK XML multiblock index, one piece per cell block),
> [VTP](https://docs.vtk.org/en/latest/vtk_file_formats/vtkxml_file_format.html) (`.vtp`),
> [VTR](https://docs.vtk.org/en/latest/vtk_file_formats/vtkxml_file_format.html) (`.vtr`, VTK XML RectilinearGrid),
> [VTS](https://docs.vtk.org/en/latest/vtk_file_formats/vtkxml_file_format.html) (`.vts`, VTK XML StructuredGrid),
> [VTU](https://vtk.org/Wiki/VTK_XML_Formats) (`.vtu`; `appended=True`/`--appended` writes raw appended binary, VTK's own default layout, about a quarter smaller than inline binary with no base64),
> [WKT](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) ([TIN](https://en.wikipedia.org/wiki/Triangulated_irregular_network)) (`.wkt`),
> [XDMF](https://xdmf.org/index.php/XDMF_Model_and_Format) (`.xdmf`, `.xmf`),
> XYZ point clouds (headerless ASCII: `.xyz`, `.xyzn`, `.xyzrgb`, `.asc`, `.pts`, `.txt`),
> [Z88](https://z88.de/) (`z88i1.txt`, recognised by its file name, with its `z88o2.txt` displacements and `z88o3.txt` stresses),
> [Zarr](https://zarr.dev/) (`.zarr`, the PhysicsNeMo mesh layout).

Files only their vendor's software can read — Abaqus `.odb`, MSC Marc `.t16`, Femap `.modfem`, and Ansys results beyond the native `.rst` reader — have [vendor-runtime routes](https://loumalouomega.github.io/meshioplusplus/vendor_routes): scripts under [`contrib/`](contrib/) that run in the vendor's own Python and write a series meshio++ reads.

<p align="center">
  <img alt="" src="https://raw.githubusercontent.com/loumalouomega/meshioplusplus/master/doc/logo/logo-icon-square.png" width="64">
</p>

<p align="center">
  <a href="https://loumalouomega.github.io/meshioplusplus/architecture"><img alt="meshio++ architecture: one C++ core holding the format registry, the operations layer and one of three mesh backends; the Python, C, Fortran, Julia, R, WebAssembly and C++ surfaces over it; and the CLIs, viewers, MCP server, Blender add-on, ParaView plugin and PhysicsNeMo adapter built on those" src="https://raw.githubusercontent.com/loumalouomega/meshioplusplus/master/doc/public/diagrams/architecture.svg" width="100%"></a>
</p>

One C++ core, six language surfaces, and the tools built on them; the [architecture page](https://loumalouomega.github.io/meshioplusplus/architecture) is the map, with every box linked to the page that owns it.

Release v16.32.0 closes the performance roadmap: the browser viewer renders from typed arrays instead of a VTP file, more readers and operations read through shared cursors and reuse scratch, `import meshioplusplus` loads formats lazily, and `transform` works on ragged meshes. C++ ABI 23 is a bump (`DistanceQuery` layout); see the [changelog](CHANGELOG.md) for details.

meshio++ ships a **C++20 core** (built with pybind11 + scikit-build-core) that reads and writes most formats with zero-copy numpy at the I/O boundary, plus optional HDF5/netCDF acceleration and a **selectable parallel backend** (`AUTO` by default — prefers OpenMP, then STL+TBB, then sequential; override with `-DMESHIOPLUSPLUS_PARALLEL_BACKEND=...`, including a bring-your-own [Kokkos](https://kokkos.org) host backend). Every format has a pure-Python fallback, so behaviour and file compatibility are identical whether or not the native libraries are present. For a standalone C++ build use `build/configure.sh` (Linux/macOS) or `build/configure.bat` (Windows). Full docs (install, data model, per-format options, CLI) live at [the documentation site](https://loumalouomega.github.io/meshioplusplus/) (sources under [`doc/`](https://github.com/loumalouomega/meshioplusplus/tree/master/doc)).

Install with

```
pip install meshioplusplus[all]
```

(`[all]` adds the h5py and netCDF4 runtime extras and the polyscope desktop viewer; `[addons]` adds the three LGPL add-on wheels described below. By default, meshio++ uses numpy and rich.) The base wheel is MIT and carries no copyleft code. OpenCASCADE, which STEP/IGES reading and the OpenCASCADE backend of CAD output (`fit_cad`, `to-cad`) need, is the separate `meshioplusplus-occt` wheel: `pip install "meshioplusplus[occt]"`. That wheel is licensed `MIT AND (LGPL-2.1-only WITH OCCT-exception-1.0)`, because that kernel is LGPL-2.1 with the OCCT exception; without it `fit_cad` uses its native backend. See [`LICENSE-BINARIES.md`](LICENSE-BINARIES.md) and [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md). You can then use the command-line tool

<!--pytest-codeblocks:skip-->

```sh
meshioplusplus convert    input.msh output.vtk   # convert between two formats

meshioplusplus info       input.xdmf             # show some info about the mesh

meshioplusplus compress   input.vtu              # compress the mesh file
meshioplusplus decompress input.vtu              # decompress the mesh file

meshioplusplus binary     input.msh              # convert to binary format
meshioplusplus ascii      input.msh              # convert to ASCII format

meshioplusplus merge      a.vtu b.vtu out.vtu    # merge meshes (optional --weld)

meshioplusplus transform  in.vtu out.vtu --translate 1,2,3   # affine transform
meshioplusplus mirror     half.vtu whole.vtu --keep-original  # reflect, cells right side out
meshioplusplus find-intersections skin.stl flags.vtu --segments cuts.vtu  # self-intersections
meshioplusplus thickness  shell.stl measured.vtu --min 1.5   # wall thickness per facet
meshioplusplus extrude    profile.vtu slab.vtu --num-layers 4  # sweep a surface into a volume
meshioplusplus clean      in.vtu out.vtu --weld              # weld / prune / de-dup
meshioplusplus crop       in.vtu out.vtu --bbox 0,0,0,1,1,1  # subset by region
meshioplusplus crop       in.vtu out.vtu --where "d<0"       # ... or by a data predicate
meshioplusplus select     in.vtu out.vtu --name inlet --kind side --seed 0,0,-1  # a named BC patch
meshioplusplus split      in.vtu 'out_{key}.vtu' --by type   # split by criterion
meshioplusplus stats      mesh.vtu                           # geometric statistics
meshioplusplus convert-cells in.msh out.vtu --mode simplexify  # hexes -> tetra
meshioplusplus subdivide  in.vtu out.vtu                      # polyhedral refinement, any 3D cell
meshioplusplus refine     in.vtu out.vtu --levels 2          # uniform subdivision
meshioplusplus refine     in.vtu out.vtu --where "q<0.3"     # adaptive, closed conformingly
meshioplusplus partition  in.vtu 'out_{part}.vtu' --nparts 4 # N balanced parts
meshioplusplus remesh-volume in.vtu out.vtu --cell-size 0.5  # retetrahedralize (isosurface stuffing)
meshioplusplus optimize-volume in.vtu out.vtu               # ODT-remesh a tet mesh (relocate + flips)
meshioplusplus smooth     in.vtu out.vtu --iterations 20     # relax node positions
meshioplusplus smooth     in.vtu out.vtu --method odt        # ODT smoothing, tet-only
meshioplusplus interpolate src.vtu tgt.vtu out.vtu           # transfer fields across meshes
meshioplusplus slice      in.vtu out.vtu --normal 0,0,1      # planar cross-section
meshioplusplus curvature  in.vtu out.vtu                     # per-vertex mean/Gaussian curvature
meshioplusplus normals    in.vtu out.vtu --split-angle 30    # point/cell normals, split at creases
meshioplusplus feature-edges in.stl edges.vtp --angle 45   # sharp/open/non-manifold edges as lines
meshioplusplus segment    in.stl patches.vtu --method primitive  # one patch per plane/cylinder/... as regions
meshioplusplus fit-primitives patches.vtu fits.vtu --json  # plane/sphere/cylinder/cone/torus per patch
meshioplusplus to-cad part.stl part.step                 # one STEP face per surface (any build; OpenCASCADE trims and checks)
meshioplusplus convert    in.stl part.step               # a closed skin as a CAD solid, coplanar facets merged
meshioplusplus convert    part.step part.cad.json        # a CAD model as Kratos IGA geometry (through OpenCASCADE)
meshioplusplus hausdorff  a.stl b.stl --max 1e-3             # worst-case distance; nonzero exit above it
meshioplusplus check      part.vtu -r "scaled_jacobian >= 0.2"  # quality gate: exit 1 on failure, 2 if unchecked
meshioplusplus regions    in.msh out.msh --union inlet=in_a,in_b --rename "Surface 3=Outlet"  # region algebra
meshioplusplus periodic   in.msh --slave inlet --master outlet --translate 2,0,0  # periodic node pairs
meshioplusplus graph      in.vtu part.graph --kind cell     # dual graph as a METIS file (or .grf: Scotch)
meshioplusplus geodesic   skin.stl dist.vtu --source 0     # surface distance from a point (heat method)
meshioplusplus parameterize bunny.stl bunny.obj             # a UV atlas, written as texture coordinates
meshioplusplus eigenmodes skin.stl modes.vtu -k 16         # lowest Laplace-Beltrami eigenpairs
meshioplusplus morph      duct.vtu moved.vtu --array d     # move the boundary, carry it into the mesh
meshioplusplus untangle   deformed.vtu fixed.vtu          # repair inverted tetrahedra and hexahedra
meshioplusplus metric     flow.vtu sized.vtu --arrays m_p,m_T --target-vertices 20000  # combine metrics
meshioplusplus coordinates rotor.vtu cyl.vtu --arrays U     # vectors/tensors in cylindrical components
meshioplusplus hull       scan.xyz hull.stl                 # convex hull of a point cloud (--dimension 2: outline)
meshioplusplus point-normals scan.ply scan.pcd             # normals of a point cloud (plane fits, oriented)
meshioplusplus reconstruct scan.ply surface.stl            # a triangle surface through an oriented point cloud
meshioplusplus register   scan.ply design.stl --method point_to_plane --output aligned.vtu  # ICP
meshioplusplus delaunay   survey.pcd terrain.vtu            # Delaunay triangulation in x, y (z kept)
meshioplusplus completion bash > ~/.local/share/bash-completion/completions/meshioplusplus  # also zsh, fish
meshioplusplus convert    case.msh.gz case.vtu            # compressed input (.gz .bz2 .xz .zst .zip) read transparently
meshioplusplus convert    s3://bucket/run/out.vtu out.msh # remote input through fsspec (Python CLI, [remote] extra)
meshioplusplus repair     in.vtu out.vtu                     # orientation, holes, bowties
meshioplusplus shrinkwrap in.vtu scan.stl out.vtu           # project onto a target surface
meshioplusplus sobolev-deform in.vtu out.vtu --array d --length-scale 0.5  # filter a displacement
meshioplusplus isosurface in.vtu out.vtu --array T --values 350  # level set of a field
meshioplusplus sdf        skin.stl field.vti --resolution 128,128,128  # signed distance field
meshioplusplus data gradient in.vtu out.vtu --array T           # grad / div / curl of a field
meshioplusplus data hessian  in.vtu out.vtu --array T           # second derivative, gradient's companion
meshioplusplus data estimate-error in.vtu out.vtu --array T --marking dorfler --marking-value 0.6  # ZZ error indicator + marking
meshioplusplus data integrate in.vtu --array density            # total / mean, per region

meshioplusplus data info  mesh.vtu                           # summarize data arrays
meshioplusplus data calc  in.vtu out.vtu --point "s = norm(v)"   # derive a field
meshioplusplus data to-cell  in.vtu out.vtu --keys T         # point -> cell average
meshioplusplus data normalize in.vtu out.vtu --cell damage --to 0,1

meshioplusplus pipeline   settings.json                      # run a whole declarative
                                                             # read -> ops -> write chain
```

with any of the supported formats.

The same verbs are available as a **standalone C++ binary** that needs no Python: grab a ready-to-run, statically-linked build for Linux/macOS/Windows from the [GitHub Releases](https://github.com/loumalouomega/meshioplusplus/releases) page, or build it yourself with `build/configure.sh --cli --build` (or `-DMESHIOPLUSPLUS_BUILD_CLI=ON`). It links only the C++ core. Named [regions](https://loumalouomega.github.io/meshioplusplus/regions) — and so point/cell *sets* — are carried there since v8.1.0, so `info` lists them and `diff` compares them; `convert -s/-d` is still Python-only.

A whole *chain* of operations can be described declaratively in one `settings.json` (`Input` → `Operations` → `Output`) and run with `meshioplusplus pipeline settings.json` — or `meshioplusplus.run_pipeline(...)` from Python, and the same engine from C/Fortran/Julia/R/WASM. `meshioplusplus.apply_operations(mesh, operations)` applies the same steps to a mesh in memory and returns `(mesh, report)`. See [the settings pipeline](https://loumalouomega.github.io/meshioplusplus/pipeline).

In Python, simply do

<!--pytest-codeblocks:skip-->

```python
import meshioplusplus

mesh = meshioplusplus.read(
    filename,  # string, os.PathLike, or a buffer/open file
    # file_format="stl",  # optional if filename is a path; inferred from extension
    # see meshioplusplus convert --help for all possible formats
)
# mesh.points, mesh.cells, mesh.cells_dict, ...

# mesh.vtk.read() is also possible
```

to read a mesh. To write, do

```python
import meshioplusplus

# two triangles and one quad
points = [
    [0.0, 0.0],
    [1.0, 0.0],
    [0.0, 1.0],
    [1.0, 1.0],
    [2.0, 0.0],
    [2.0, 1.0],
]
cells = [
    ("triangle", [[0, 1, 2], [1, 3, 2]]),
    ("quad", [[1, 4, 5, 3]]),
]

mesh = meshioplusplus.Mesh(
    points,
    cells,
    # Optionally provide extra data on points, cells, etc.
    point_data={"T": [0.3, -1.2, 0.5, 0.7, 0.0, -3.0]},
    # Each item in cell data must match the cells array
    cell_data={"a": [[0.1, 0.2], [0.4]]},
)
mesh.write(
    "foo.vtk",  # str, os.PathLike, or buffer/open file
    # file_format="vtk",  # optional if first argument is a path; inferred from extension
)

# Alternative with the same options
meshioplusplus.write_points_cells("foo.vtk", points, cells)
```

For both input and output, you can optionally specify the exact `file_format` (in case you would like to enforce ASCII over binary VTK, for example).

<details>
<summary><b>Mesh and data operations</b> — skin/surface extraction, quality, reorder, diff, merge, transform/clean/crop/split/stats, select (named regions), cell conversion, tessellation, subdivide/agglomerate, tet_to_poly/poly_to_tet, refine, undo-green, decimate, partition, remesh, MMG adaptation, smoothing, interpolation, slice, isosurface, derivatives, Hessian, error estimation, field integration, data ops (click to expand)</summary>

#### Skin extraction

`meshioplusplus.extract_skin` derives the boundary surface of a 3D volume mesh (the [Kratos `SkinDetectionProcess`](https://github.com/KratosMultiphysics/Kratos) face-hashing algorithm — faces occurring exactly once are boundary; points are compacted, `point_data` follows):

<!--pytest-codeblocks:skip-->

```python
vol = meshioplusplus.read("part.msh")     # tetra/hexa/wedge/pyramid mesh
skin = meshioplusplus.extract_skin(vol)   # triangle/quad/... surface mesh
```

The **STL and PLY writers do this automatically** for volume meshes (pass `skin=False` for the legacy drop-volume-cells behavior), and the **SVG/TikZ writers render 3D meshes** by projecting the skin through an orthographic camera (`azimuth`/`elevation`/`roll` in degrees, default the classic CAD isometric view) with painter's-algorithm depth ordering — that is exactly how the Stanford-bunny logo above is drawn.

#### Publication-quality vector figures

The SVG and TikZ writers can colour each face by a data array, turning them into figures you can drop straight into a paper — resolution-independent, and with **no extra dependency**: the colormaps are built into the core.

<!--pytest-codeblocks:skip-->

```python
annotated = meshioplusplus.attach_quality(mesh)
meshioplusplus.write(
    "quality.svg", annotated,
    color_by="quality:scaled_jacobian",   # or any point_data / cell_data name
    cmap="viridis",                       # viridis / coolwarm / turbo / magma / … (and *_r)
    colorbar=True,
)
```

<img alt="a bracket coloured by scaled Jacobian" src="https://raw.githubusercontent.com/loumalouomega/meshioplusplus/master/doc/public/images/color_by_quality.svg" width="85%">

*The bundled bracket coloured by element quality — the same figure `tools/gen_doc_images.py` regenerates.*

**Point data** colours a face by the mean of its corner values, **cell data** by its owning cell's value — for a volume mesh, tracked through the extracted skin's parent-cell provenance, so a per-cell material or metric lands on the right facet. Multi-component arrays reduce to a `component` or to their magnitude; `vmin`/`vmax` set the range (default: the drawn faces' finite range), and non-finite values take `nan_color`. From the command line:

<!--pytest-codeblocks:skip-->

```sh
meshioplusplus convert mesh.vtu figure.svg --color-by temperature --colorbar
```

Colouring is available from Python, from C++ directly, and from both CLIs; the flat C/Fortran/WebAssembly bindings reach these writers through the shared registry and always emit the default styling.

#### glTF export

`meshioplusplus.write("model.glb", mesh)` writes the surface of a mesh as [glTF 2.0](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html), which three.js, Blender and every web dashboard load directly: the skin of volume cells, 2-D cells, lines and point clouds, one named node per cell region, with normals split at creases and every point field exported raw as an `_NAME` attribute. `color_by` also bakes a field through a colormap into `COLOR_0` with an unlit material. The output is Y-up and `float32`; the axis change, unit scale and recentring offset live on the root node rather than in the coordinates. See [glTF](https://loumalouomega.github.io/meshioplusplus/formats/gltf.html).

<!--pytest-codeblocks:skip-->

```python
meshioplusplus.write("model.glb", mesh)                                  # defaults
meshioplusplus.write("result.glb", mesh, color_by="temperature", cmap="turbo", scale=0.001)
```

<!--pytest-codeblocks:skip-->

```sh
meshioplusplus convert result.vtu result.glb --color-by temperature --split-angle 45
```

#### Surface extraction

`meshioplusplus.extract_surface` is the general form of skin extraction: it picks the dimension automatically (a volume mesh → boundary faces, a 2D surface mesh → boundary edges) and can record each facet's parent cell id (`record_parent_ids=True`). See the [surface extraction docs](https://meshioplusplus.readthedocs.io) (`doc/extract_surface.md`).

<!--pytest-codeblocks:skip-->

```python
surf = meshioplusplus.extract_surface(vol)                  # faces (or edges for a 2D mesh)
edges = meshioplusplus.extract_surface(sheet, record_parent_ids=True)
```

#### Mesh quality

`meshioplusplus.compute_quality` scores every cell on a set of geometric quality metrics (area/volume, scaled Jacobian, aspect ratio, skewness, interior/dihedral angles, warpage) and flags inverted/degenerate cells; `attach_quality` writes them back as `cell_data`. See `doc/mesh_quality.md`.

<!--pytest-codeblocks:skip-->

```python
report = meshioplusplus.compute_quality(mesh)
print(report["num_inverted"], "inverted cells")
annotated = meshioplusplus.attach_quality(mesh)   # metrics as cell_data
```

`meshioplusplus.check_quality(mesh, "scaled_jacobian >= 0.2; aspect_ratio <= 5 @ 1%")` turns the metrics into a pass/fail gate tested per cell, and the `check` CLI verb exits 1 when it fails and 2 when it could not run — what a CI job over meshes scripts; every report verb of both CLIs also takes `--json` with one shared, strictly valid shape. See `doc/mesh_quality.md` and `doc/cli.md`.

`meshioplusplus.check_conformity(mesh)` reports the hanging nodes, T-junctions and partly overlapping or unwelded facets of a mesh, flags the hanging points in `conformity:hanging`, and says which `find_interface` mode suits it; the `check-conformity` CLI verb exits 1 when the mesh is not conforming. See `doc/check_conformity.md`.

`meshioplusplus.find_intersections(mesh)` finds where a surface intersects itself, or with a second surface where two parts interpenetrate, by exact triangle–triangle tests: the cell pairs, the crossing segments as a line mesh and `intersections:count` per cell; the `find-intersections` CLI verb exits 1 when anything intersects. `meshioplusplus.thickness(mesh)` measures the wall thickness (or, outward, the clearance to the same or a second part) at every facet by a ray along its normal, into `thickness:distance`. See `doc/find_intersections.md` and `doc/thickness.md`.

#### Reordering / renumbering

`meshioplusplus.reorder` renumbers nodes and elements to reduce sparse-matrix bandwidth (Reverse Cuthill–McKee) or improve cache locality (Morton / Hilbert space-filling curves). It is a pure permutation — geometry and all data preserved — and returns the applied node/cell permutations so external arrays can be remapped. `compute_bandwidth` measures the before/after connectivity bandwidth. See `doc/reorder.md`.

<!--pytest-codeblocks:skip-->

```python
out = meshioplusplus.reorder(mesh, method="rcm")            # "morton" / "hilbert" too
out, node_perm, cell_perms = meshioplusplus.reorder(mesh, return_permutation=True)
print(meshioplusplus.compute_bandwidth(mesh), "->", meshioplusplus.compute_bandwidth(out))
```

#### Comparison (diff)

`meshioplusplus.diff` compares two meshes and reports whether they are equivalent within a tolerance (`abs_err <= atol + rtol*|expected|`), with a structured breakdown (points, cells, data, named sets) and an overall verdict (`identical` / `equal within tolerance` / `different`); `meshes_equal` is the boolean wrapper for test suites. An optional `unordered=True` mode matches nodes by spatial proximity, so a shuffled node order still compares equal. See `doc/diff.md`.

<!--pytest-codeblocks:skip-->

```python
assert meshioplusplus.meshes_equal(a, b, atol=1e-8)         # ideal in a regression test
report = meshioplusplus.diff(a, b, unordered=True)          # tolerant to shuffled node order
print(report["verdict"])
```

The `meshioplusplus diff a.vtu b.vtu` CLI verb sets a nonzero exit code when meshes differ, for direct use in CI / Makefiles.

#### Hausdorff distance, feature edges, region algebra and periodic pairs

Four analysis and editing operations (v16.23.0), each on every surface — Python, C++, C, Fortran, Julia, R, WASM, both CLIs and MCP. **`meshioplusplus.hausdorff_distance(a, b)`** is how far apart two surfaces are at their worst, the scalar a remeshing or format round trip is asserted on (`--max D` turns the CLI verb into a CI gate) — `doc/hausdorff.md`. **`meshioplusplus.feature_edges(mesh)`** writes the sharp, open, non-manifold and inconsistently wound edges as a line mesh; it is the one crease test `decimate` and `smooth` pin nodes with — `doc/feature_edges.md`. **`meshioplusplus.edit_regions(mesh, edits)`** unions, intersects, subtracts, renames, retags and deletes named regions — `doc/regions.md`. **`meshioplusplus.match_periodic_nodes(mesh, slave, master, translate=...)`** pairs the nodes two boundary regions share under a translation or rotation, the input of a periodic boundary condition — `doc/periodic.md`.

<!--pytest-codeblocks:skip-->

```python
d = meshioplusplus.hausdorff_distance(before, after, face_samples=4)["distance"]
edges = meshioplusplus.feature_edges(mesh, feature_angle=45)
mesh = meshioplusplus.edit_regions(mesh, [{"op": "union", "inputs": ["a", "b"], "output": "inlet"}])
pairs = meshioplusplus.match_periodic_nodes(mesh, "inlet", "outlet", translate=(2, 0, 0))
```

#### Skin to CAD: segment, fit primitives, STEP, CAD faces

The mesh-side half of reverse engineering a triangle skin into a CAD model, with no CAD kernel in the loop, on every surface — Python, C++, C, Fortran, Julia, R, WASM, both CLIs, MCP and the pipeline. **`meshioplusplus.segment(mesh)`** splits a surface into smooth patches by region growing, bounded by its feature edges, with a curvature test that separates a fillet from the planes it is tangent to, or, with `method="primitive"`, one patch per plane, cylinder, cone, sphere or torus its facets lie on; the patches come back as `segment:patch` cell data, a patch-adjacency table and one cell region each. **`meshioplusplus.fit_primitives(mesh)`** fits a plane, sphere, cylinder, cone or torus to each patch, deterministically, and keeps the simplest within tolerance — a fit outside it is reported as `none` with its residual, never rounded to a neat primitive. The **`step`** writer hands a closed skin to CAD as an AP214 B-rep solid with no CAD kernel, validated against OpenCASCADE: each fitted patch one analytic face (plane, cylinder, cone, sphere, torus) bounded by lines and circles, each flat region one planar face with its holes, not one face per triangle (`faces="facet"` keeps that layout). **`meshioplusplus.fit_cad(mesh, path)`** runs the chain on a raw skin and builds the solid: without a CAD kernel through its native backend (the analytic faces above), and with OpenCASCADE (included in the PyPI wheels and the release binaries, on by default from source; LGPL-2.1 with the OCCT exception) doing the whole CAD half: each fitted patch becomes an analytic face trimmed by its boundary, a rolling-ball fillet (of one radius or a radius varying along it, also between freeform faces) or a helical thread face (straight or rounded, with or without a cylinder beside it) its own face, and any other patch no primitive explains a freeform B-spline face (split first into pieces a plane or an unrolled cylinder parametrises), sewn into a checked solid and written as STEP a CAD tool can edit (or as Kratos CAD JSON), with anything the kernel cannot build demoted to facets, never silently wrong; since v17.2.0 a chamfer, a conic blend, a tapered or variable-pitch thread and a corner where blends meet (a vertex blend) get their own faces too (every surface, WASM through its full artifact; `to-cad` in both CLIs). Since v17.11.0 the loop is iterative and tolerance-driven, each stage off by default: **`meshioplusplus.refine_patches(mesh)`** (or `fit_cad(refine_segmentation=True)`) refines a segmentation by variational shape approximation, splitting by seeded RANSAC, merging and absorbing until the patches stop moving; `freeform_general=True` fits a patch the height-field B-spline cannot hold over a conformal disc parametrisation with parameter correction and knot insertion; and `snap_junctions`, `extend_surfaces`, `sew_tolerance` and `face_deviation` tighten the edges and measure each face's two-sided distance to the skin. `freeform_mode="adaptive"` (unreleased) turns what no primitive or feature explains into B-spline faces even without a CAD kernel, cutting non-discs along their topology, climbing a refine/re-parametrise/split ladder and giving every face it still demotes a reason, with the share of the skin left as facets in the report; `freeform_mode="network"` lays such a region out in quads and fits them as B-spline patches that share their edge curves exactly, G1 across them, in both backends (a topology-optimised hook keeps well under one per cent of its area as facets, from a quarter), and the native solid comes back as trimmed NURBS for Kratos CAD JSON too; `local_refine="thb"` (experimental) refines with truncated hierarchical B-splines; `constrain_primitives=True` (unreleased) fits related primitives together in both backends, so a turned part's cylinders, cones, tori and dome share one axis exactly, its shoulders are exactly perpendicular to it and nearly equal radii are one radius. See [skin to CAD](https://loumalouomega.github.io/meshioplusplus/cad_fit) and [fit CAD](https://loumalouomega.github.io/meshioplusplus/fit_cad).

<!--pytest-codeblocks:skip-->

```python
seg = meshioplusplus.segment(skin, curvature_tolerance=1.0, min_patch_cells=20)
fit, report = meshioplusplus.fit_primitives(seg, tolerance=2e-3, return_report=True)
fit.field_data["fit:patch_params"]   # per patch: point, axis, radii, half-angle
meshioplusplus.write("part.step", fit)                      # analytic faces, no CAD kernel
solid = meshioplusplus.fit_cad(fit, "part_cad.step")         # trimmed and checked (OpenCASCADE)
meshioplusplus.fit_cad(meshioplusplus.read("bracket.stl"), "bracket.step")  # raw skin, one face per surface
```

#### Isogeometric layer: evaluate, refine, sample NURBS models

The NURBS model a reader keeps beside its mesh (`mesh.info["nurbs"]` for MFEM NURBS meshes, `mesh.info["brep"]` for Kratos CAD JSON, STEP and IGES) can be acted on directly, on every surface (Python, C++, C, Fortran, Julia, R, WASM, both CLIs, MCP): **`iga_refine`** inserts knots and elevates degrees exactly, with the geometry, the NURBS fields and a trimmed face's trimming loops unchanged; **`iga_evaluate`** returns points, first derivatives, normals and the trimming test at parametric coordinates; **`iga_sample`** samples a model into Lagrange cells again. A refined MFEM model writes back as an `MFEM NURBS mesh`. See [isogeometric layer](doc/iga.md).

<!--pytest-codeblocks:skip-->

```python
mesh = meshioplusplus.read("pipe-nurbs.mesh", file_format="mfem")
fine = meshioplusplus.iga_refine(mesh, subdivisions=2, elevate=1)   # exact: same geometry
meshioplusplus.write("fine.mesh", fine, file_format="mfem")         # patches intact
ev = meshioplusplus.iga_evaluate(fine, [[0.3, 0.7, 0.4]], derivatives=1)
```

#### Named regions from geometry (select)

**`meshioplusplus.select(mesh, name, kind)`** writes one named point, cell or side region chosen by a box, half-space or ball, a `cell_data`/`point_data` or quality threshold, a node-connected component, or a smooth patch grown from a seed point across the edges `feature_edges` would not draw — the boundary-condition patch or contact surface a solver deck names, reproducible from a script. Everything else is left bit-identical. See [`doc/select.md`](doc/select.md).

<!--pytest-codeblocks:skip-->

```python
mesh = meshioplusplus.select(mesh, "inlet", "side", seed=(0.0, 0.0, -1.0))
mesh = meshioplusplus.select(mesh, "slivers", quality=("min_dihedral", "<", 10))
```

#### Interfaces and contact

`meshioplusplus.region_adjacency(mesh, regions=None)` extracts conforming facets shared by Cell regions (or by cell blocks when fewer than two Cell regions exist). `find_interface` matches two parts by shared node ids or geometric proximity, `contact_pairs` projects a Point region onto master facets, and `split_interface` duplicates point fans along a Side region with optional cohesive elements. The API and tolerances are documented in [`doc/region_adjacency.md`](doc/region_adjacency.md).

```python
facets, report = meshioplusplus.find_interface(mesh, "part_a", "part_b", return_report=True)
contacts = meshioplusplus.contact_pairs(slave_mesh, "slave_nodes", "master_boundary")
split = meshioplusplus.split_interface(mesh, report["side_a"], add_cohesive=True)
```

The Python CLI provides `region-adjacency`, `find-interface`, `contact-pairs`, and `split-interface`; the native CLI provides `region-adjacency`.

#### Merge / combine

`meshioplusplus.merge` combines two or more meshes into one: it concatenates points (offsetting connectivity so indices stay valid), merges cell blocks by type, concatenates data (per a configurable `data_policy`), and tags each cell's origin. With `weld=True` it fuses coincident nodes across inputs within `atol` using a spatial hash (never O(N²)) — the standard way to stitch adjacent blocks into a watertight mesh. Overlapping set / field-data names are namespaced by source id. See `doc/merge.md`.

<!--pytest-codeblocks:skip-->

```python
combined = meshioplusplus.merge([a, b, c])                 # concatenate
welded = meshioplusplus.merge([left, right], weld=True, atol=1e-8)  # fuse the shared interface
```

#### Editing (transform / clean / crop / split) and statistics

A bundle of dependency-free mesh-editing utilities:

- **`meshioplusplus.transform`** — apply an affine transform (translate / scale / rotate / 4×4 matrix / unit-scale) to the points; connectivity and data are carried through. See `doc/transform.md`.
- **`meshioplusplus.mirror`** — reflect across a plane with every cell right side out (a reflecting `transform` leaves them inverted); `keep_original=True` makes a whole model from a half, the points on the plane shared. See `doc/mirror.md`.
- **`meshioplusplus.clean`** — weld coincident points (spatial hash), drop degenerate and duplicate cells, and remove orphaned points, in one toggleable pass. See `doc/clean.md`.
- **`meshioplusplus.crop`** — extract the part of a mesh inside a bounding box or half-space, pruning unused points (`mode="all"`/`"any"`). See `doc/crop.md`.
- **`meshioplusplus.split`** — partition a mesh into several by cell type, connected component (flood-fill), region (`cell_sets` / integer tag), or one piece per named Cell region (`by="regions"`, cross-binding, not a partition — overlapping regions overlap). See `doc/split.md`. `meshioplusplus regions` (CLI) / `read_metadata(...)["regions"]` lists a mesh's regions cheaply, without a full read where possible.
- **`meshioplusplus.compute_stats`** — geometric statistics (bounding box, centroid, per-type counts, area, signed/unsigned volume, inverted cells) — the geometric complement to `info`. See `doc/stats.md`.

<!--pytest-codeblocks:skip-->

```python
out = meshioplusplus.transform(mesh, rotate=("z", 90))
out = meshioplusplus.clean(mesh, weld=True, atol=1e-8)
sub = meshioplusplus.crop(mesh, bbox=[0, 0, 0, 1, 1, 1])
pieces = meshioplusplus.split(mesh, by="type")             # {"triangle": ..., ...}
s = meshioplusplus.compute_stats(mesh)                     # dict of measures
```

#### Cell conversion (linearize / simplexify / elevate)

**`meshioplusplus.convert_cells`** converts a mesh's *element representation* — which cell types it is built from — while leaving the object it describes intact. See `doc/convert_cells.md`.

- **`mode="linearize"`** — every higher-order cell becomes its linear base (`tetra10` → `tetra`, `hexahedron27` → `hexahedron`), keeping the corner connectivity verbatim and pruning the nodes that become unreferenced.
- **`mode="simplexify"`** — every cell is decomposed into simplices of the same topological dimension (`quad` → 2 `triangle`, `hexahedron` → 6 `tetra`, `wedge` → 3, `pyramid` → 2, an n-gon into an (n−2)-triangle fan). No points are added, each parent's `cell_data` is replicated to its children, and every emitted simplex is positively oriented with volume conserved.
- **`mode="elevate"`** — every linear cell is promoted to its serendipity quadratic counterpart (`triangle` → `triangle6`, `hexahedron` → `hexahedron20`), adding one node per unique edge at the edge midpoint with `point_data` set to the endpoint mean.

<!--pytest-codeblocks:skip-->

```python
linear = meshioplusplus.convert_cells(mesh, mode="linearize")
tets = meshioplusplus.convert_cells(mesh, mode="simplexify")   # hexes -> tetra
quadratic = meshioplusplus.convert_cells(mesh, mode="elevate")
```

Each mode is idempotent on cells it does not apply to, so it is safe on a mixed-order mesh, and output is byte-identical across mesh backends and thread counts.

#### Curved tessellation

**`meshioplusplus.tessellate`** isoparametrically subdivides the five higher-order cell types (`triangle6`/`quad8`/`quad9`/`tetra10`/`hexahedron27`, deliberately excluding `hexahedron20` — see `doc/tessellation.md`) onto a refinement lattice, using each cell's own shape functions so a curved boundary tessellates onto the curve rather than being chopped straight. Unlike `convert_cells(mode="simplexify")`, it records a full provenance map (`Tessellation.source_point`/`source_cell`) from every synthetic point and tessellated cell back to the higher-order cell it was carved out of, so a prediction made on a tetrahedron is written onto the hexahedron it was carved out of via `Tessellation.gather`/`.scatter`/`.aggregate`. `fields=True` (default) interpolates the input's own `point_data`/`cell_data` onto the tessellated mesh. The kernel is in the C++ core, so the native CLI, every flat binding (C, Fortran, Julia, R, WASM) and the pipeline's `Tessellate` step run it too. See `doc/tessellation.md`.

<!--pytest-codeblocks:skip-->

```python
tess = meshioplusplus.tessellate(mesh, levels=2)
mp.write("curved_bracket_tessellated.vtu", tess.mesh)
```

#### Polyhedral refinement (subdivide)

**`meshioplusplus.subdivide`** splits every eligible 3D cell into one polyhedral child per face, connected to a new interior point. `refine` and `decimate` both raise by name on a polyhedron, pointing at `convert_cells(mode="simplexify")` — both are built on fixed same-type subdivision templates, and an arbitrary polyhedron has none. `subdivide` needs no per-type table at all: tabulated types (reduced to corners for a quadratic variant) and existing polyhedron blocks are handled uniformly, so the same code covers every 3D cell type the mesh already supports. Automatically conforming (no closure, no hanging nodes), unlike `refine`. See `doc/subdivide.md`.

<!--pytest-codeblocks:skip-->

```python
out = meshioplusplus.subdivide(mesh, record_parent_ids=True)
```

#### Polyhedral coarsening (agglomerate)

**`meshioplusplus.agglomerate`** merges groups of cells into single larger polyhedral cells — the many-to-one counterpart to `subdivide`. `decimate` raises by name on a polyhedron, pointing at `convert_cells(mode="simplexify")` — its fixed-template QEM edge collapse has no analogue for merging arbitrary polyhedral cells. `agglomerate` is a genuinely different algorithm: greedy seed-and-grow over the mesh's shared-face dual, absorbing face-adjacent neighbours by accumulated shared-face area until a target group size; each group emits one polyhedron whose faces are exactly its external boundary, conserving volume exactly. Non-volume blocks pass through unchanged; points are never pruned or renumbered (`clean(mesh, remove_orphans=True)` is the follow-up for a minimal point set). See `doc/agglomerate.md`.

<!--pytest-codeblocks:skip-->

```python
coarse = meshioplusplus.agglomerate(mesh, target_group_size=8)
# fuse coplanar faces and keep groups compact
coarse, report = meshioplusplus.agglomerate(
    mesh, merge_coplanar_faces=True, min_sphericity=0.7, return_report=True
)
```

#### Tetrahedral ⇄ polyhedral conversion

**`meshioplusplus.tet_to_poly`** converts a tetrahedral mesh into its polyhedral (median) dual — the tet-to-poly conversion CFD meshers perform: one polyhedron per vertex, bounded by the ring of tetrahedron and triangle centroids around each edge and, on the boundary, by the boundary triangles' pieces, fused while their normals agree within `feature_angle` so feature edges and corners survive. A vertex on an interface between `tetra` blocks gets one cell per block. **`meshioplusplus.poly_to_tet`** goes back: `convert_cells(mode="simplexify")`, except that a polyhedron that already is a tetrahedron becomes that one `tetra`. See `doc/tet_poly.md`.

<!--pytest-codeblocks:skip-->

```python
poly, report = meshioplusplus.tet_to_poly(tets, return_report=True)
tets_again = meshioplusplus.poly_to_tet(poly)  # valid and volume-conserving, not the original
```

#### Refinement

**`meshioplusplus.refine`** subdivides cells into congruent children of the *same* cell type, increasing a mesh's resolution: `line` → 2, `triangle` → 4, `quad` → 4, `tetra` → 8, `wedge` → 8, `hexahedron` → 8, with `levels=n` applying the templates `n` times. Given a **selection** — a cell list, a region name, or a `cell_data` threshold — it refines only those cells and resolves the resulting hanging nodes, so the output is still conforming. See `doc/refine.md`.

New nodes sit at the midpoints of the parent's edges, quad faces and (hexahedron only) body, and carry the mean of that entity's corner values for every `point_data` array — so a linear field is interpolated exactly. Mid-edge and quad-face-centre nodes are **shared** between every cell touching the entity, so the refined mesh has no hanging nodes; each parent's `cell_data` row is replicated to its children.

`record_hierarchy=True` attaches two persistent `cell_data` arrays, `refine:cell_id`/`refine:parent_id`: a stable identity that survives across separate `refine` calls — **a link between two meshes, not a tree inside one**, resolved by a multigrid caller against the sequence of meshes it keeps.

<!--pytest-codeblocks:skip-->

```python
fine = meshioplusplus.refine(mesh)                      # one level
finer = meshioplusplus.refine(mesh, levels=2)           # 64x the cells in 3D
tagged = meshioplusplus.refine(mesh, record_parent_ids=True)

# adaptive: refine the worst cells and close up conformingly around them
graded = meshioplusplus.refine(
    meshioplusplus.attach_quality(mesh),
    where="quality:scaled_jacobian < 0.3",
    record_levels=True,                                 # colour by refine:level
)

# multigrid: keep the coarse mesh, resolve the fine mesh's parent ids against it
fine = meshioplusplus.refine(coarse, cells=[4, 8], record_hierarchy=True)
```

Children inherit the parent's orientation (zero newly-inverted cells for a well-oriented input), and volume is conserved — exactly for `tetra` always, and for `wedge`/`hexahedron` when the parent is affine. Higher-order cells, `pyramid`, and ragged blocks have no same-type subdivision and raise by name.

#### Green-element undo

**`meshioplusplus.undo_green(coarse, fine)`** restores `refine`'s transitional ("green") cells back to their original parent — the standard rule for selective refinement: before a new pass touches a region a prior pass already closed up, restore the transitional cell to its parent and re-split from scratch, rather than refining the transitional children directly (which degrades element quality without bound over repeated passes). It is a **two-mesh** operation, like `interpolate`: `coarse` is the mesh a prior `refine(coarse, ..., record_hierarchy=True, record_levels=True)` call was run on, `fine` is that call's output. Since `refine`'s point map is always the identity, a green parent's exact connectivity and cell_data are already sitting, byte-for-byte, in `coarse` — so this is a lookup and substitution, not a reconstruction. See `doc/undo_green.md`.

<!--pytest-codeblocks:skip-->

```python
fine = meshioplusplus.refine(coarse, cells=[4, 8], record_hierarchy=True, record_levels=True)
# ... later, decide to refine a different region ...
undone = meshioplusplus.undo_green(coarse, fine)
redone = meshioplusplus.refine(undone, cells=[12, 19], record_hierarchy=True, record_levels=True)
```

#### Decimation

**`meshioplusplus.decimate`** is `refine`'s inverse: it *reduces* a surface mesh's face count by greedy quadric-error-metric (Garland–Heckbert) edge collapse, preserving shape, boundaries and features. Exactly one stopping criterion is given — `ratio` (fraction of faces to keep), `target_faces`, or `max_error` — and the output is all-triangle (`quad`/`polygon` blocks are triangulated first, block structure kept 1:1). See `doc/decimate.md`.

<p align="center">
<img alt="a refined sphere before and after decimation to 25% of its faces" src="https://raw.githubusercontent.com/loumalouomega/meshioplusplus/master/doc/public/images/decimate_before_after.png" width="85%">
</p>

<!--pytest-codeblocks:skip-->

```python
coarse = meshioplusplus.decimate(mesh, ratio=0.25)            # keep 25% of the faces
coarse = meshioplusplus.decimate(mesh, target_faces=5000)     # absolute face budget
coarse, report = meshioplusplus.decimate(mesh, max_error=1e-6, return_report=True)
```

Boundary vertices (once-used-edge test) and feature vertices (the endpoints of [feature edges](https://loumalouomega.github.io/meshioplusplus/feature_edges): an edge whose two faces' normals differ by more than `feature_angle`, default 30°) are pinned by default, so an open patch keeps its outline exactly and a cube keeps its corners; the link condition and a normal-flip guard reject any collapse that would change topology, create a non-manifold edge, or fold the surface. Float `point_data` blends along the collapsed edge; integer arrays keep the survivor's value. Volume meshes raise by name — run `extract_surface` first, then decimate the skin.

#### Volume decimation

**`meshioplusplus.decimate_volume`** is `decimate`'s volume-mesh sibling — a separate operation, not a mode on it — reducing a **tetrahedral** mesh's cell count by greedy quadric-error-metric **tet**-edge collapse. Unlike `decimate`, boundary vertices *participate* by default (`preserve_boundary=False`): every vertex accumulates a quadric from its incident boundary-triangle planes only, so a purely interior vertex's quadric is exactly zero and interior-only edges are scored by squared length instead, always ranking behind boundary-touching collapses. See `doc/decimate_volume.md`.

<!--pytest-codeblocks:skip-->

```python
coarse = meshioplusplus.decimate_volume(mesh, ratio=0.25)             # keep 25% of the tets
coarse = meshioplusplus.decimate_volume(mesh, target_cells=5000)      # absolute tet budget
coarse, report = meshioplusplus.decimate_volume(mesh, max_error=1e-6, return_report=True)
```

Validity is guarded by an exact vertex-link set-equality condition, a duplicate-tet check, and a tet-inversion guard, plus — for boundary-touching collapses — `decimate`'s own ring/shared-face link condition and normal-flip check reused over the mesh's own outer skin. Tet-only: any non-tetra 3D block raises by name pointing at `convert_cells(mode="simplexify")`.

#### Partitioning

**`meshioplusplus.partition`** decomposes a mesh into exactly N balanced pieces for domain decomposition — the count-driven complement to the criterion-driven `split`. See `doc/partition.md`.

- **SFC** (the default fallback, always available, dependency-free): cells are cut into contiguous ranges along a Hilbert space-filling curve of their centroids — equal-weight part sizes differ by at most one cell, `weights=<cell_data>` balances a per-cell cost instead, and the assignment is deterministic and byte-identical across mesh backends and thread counts.
- **KaHIP** (the optional quality path): the shared-face dual graph goes through [KaHIP](https://github.com/KaHIP/KaHIP)'s serial `kaffpa()`, which actively minimizes the edge cut. Configure `imbalance` (default 3%), `mode` (`fast`/`eco`/`strong`, default `eco` — eco/strong carry the quality) and `seed`. **KaHIP is MIT-licensed like meshio++ itself, so enabling it changes nothing about licensing**; it is bring-your-own (`-DMESHIOPLUSPLUS_WITH_KAHIP=ON` + `KAHIP_ROOT`, Conan `with_kahip`, vcpkg feature `kahip` — next to the HDF5/zstd-style optional deps), links only the serial interface (no MPI), and `pip install meshioplusplus[kahip]` gives pure-Python installs the same quality path via the MIT `kahip` wheel. Requesting it where absent fails by name — never a silent downgrade.

<!--pytest-codeblocks:skip-->

```python
pieces = meshioplusplus.partition(mesh, 4)                    # list of 4 meshes
labels = meshioplusplus.partition_labels(mesh, 4)             # per-block Int64 part ids
quality = meshioplusplus.partition(mesh, 16, method="kahip", mode="strong")
```

Pieces keep the input's block structure 1:1, so they recombine into the input: every cell lands in exactly one piece. `ghost_layers=N` instead grows each piece by N shared-node layers of its neighbours' cells (an MPI-style halo), tagged `partition:ghost`.

#### Geodesic distance (heat method)

**`meshioplusplus.geodesic_distance(mesh, sources)`** measures the distance along a triangle surface from source points (ids, or a region's points) to every point, as `geodesic:distance` point data, by Crane et al.'s heat method over the surface's own cotangent operators: a heat step, its normalised gradient, a Poisson solve. Deterministic, about 1% accurate on a sphere at `h = 0.04`, on every surface — Python, C++, C, Fortran, Julia, R, WASM, both CLIs (`geodesic`), the pipeline (`GeodesicDistance`) and MCP. See `doc/geodesic.md`.

<!--pytest-codeblocks:skip-->

```python
out = meshioplusplus.geodesic_distance(skin, "inlet")   # the points of a region
d = out.point_data["geodesic:distance"]
```

#### UV parameterization

**`meshioplusplus.parameterize(mesh)`** gives a triangle surface a UV atlas: it cuts the surface into charts, flattens each without flipping a triangle (least-squares conformal maps, else mean-value coordinates, the kernels `fit_cad` uses), halves a chart that stretches too much, and shelf-packs the charts into the unit square. The result is split at its seams and carries `uv` point data, which the OBJ (`vt`), glTF (`TEXCOORD_0`) and USD (`primvars:st`) writers turn into texture coordinates, and their readers turn back. On every surface — Python, C++, C, Fortran, Julia, R, WASM, both CLIs (`parameterize`), the pipeline (`Parameterize`) and MCP. See `doc/parameterize.md`.

<!--pytest-codeblocks:skip-->

```python
out, report = meshioplusplus.parameterize(bunny, return_report=True)
meshioplusplus.write("bunny.glb", out)   # TEXCOORD_0 from out.point_data["uv"]
```

#### Metric toolbox

**`meshioplusplus.prepare_metric(mesh, arrays)`** intersects the anisotropic metrics of several fields (so one mesh resolves them all), normalises the result to a target vertex count (continuous-mesh L^p), clamps its sizes and grades it, with no MMG needed: the input `adapt` takes. See [metric toolbox](doc/metric.md).

<!--pytest-codeblocks:skip-->

```python
m = meshioplusplus.prepare_metric(mesh, ["m_p", "m_T"], target_vertices=20000, gradation=1.5)
```

#### Untangling

**`meshioplusplus.untangle(mesh)`** repairs inverted tetrahedra and hexahedra by moving nodes until every corner has a positive signed volume (Escobar et al.'s untangling functional), keeping the connectivity and, by default, the boundary, and moving only the nodes near the tangles. See [untangling](doc/untangle.md).

<!--pytest-codeblocks:skip-->

```python
fixed = meshioplusplus.untangle(meshioplusplus.read("deformed.vtu"))
```

#### Mesh morphing

**`meshioplusplus.morph(mesh, displacement)`** moves the boundary (or chosen points) by a prescribed displacement and carries it into the rest of the mesh by a harmonic extension with Jacobian-based stiffening, in increments for large motions, refusing a result with inverted cells: shape optimisation and fluid–structure mesh motion. See [morphing](doc/morph.md).

<!--pytest-codeblocks:skip-->

```python
moved = meshioplusplus.morph(fluid, "wall_motion", steps=4)
```

#### Laplacian eigenmodes

**`meshioplusplus.laplacian_eigenmodes(surface, num_modes)`** computes the lowest eigenpairs of a triangle surface's Laplace–Beltrami operator (cotangent stiffness against lumped mass) as `laplacian:modes` point data and `laplacian:eigenvalues` field data: spectral positional encodings for graph networks, and shape descriptors. Repeated eigenvalues come out whole (a sphere's `l (l + 1)`, `2 l + 1` times). See [eigenmodes](doc/eigenmodes.md).

<!--pytest-codeblocks:skip-->

```python
out = meshioplusplus.laplacian_eigenmodes(skin, 16)
encoding = out.point_data["laplacian:modes"]   # (n, 16)
```

#### Cylindrical and spherical coordinates

**`meshioplusplus.convert_coordinates(mesh, system, axis=..., arrays=[...])`** records each point's `(r, θ, z)` or `(r, θ, φ)` about an axis as point data and rewrites the named vector and tensor fields in the local basis of each point (a cell's at its centroid), the components rotating machinery and pressure vessels are read in; `inverse=True` turns them back. The points do not move. See [coordinates](doc/coordinates.md).

<!--pytest-codeblocks:skip-->

```python
out = meshioplusplus.convert_coordinates(rotor, "cylindrical", arrays=["U"])
u_r, u_theta, u_z = out.point_data["U"].T
```

#### Rigid registration (ICP)

**`meshioplusplus.register_rigid(source, target)`** finds the rotation and translation laying a scan onto its design (or one run's mesh onto another's) by iterative closest points, point-to-point or point-to-plane, and returns the 4 × 4 matrix `transform` applies. See [rigid registration](doc/registration.md).

<!--pytest-codeblocks:skip-->

```python
matrix, report = meshioplusplus.register_rigid(scan, design, method="point_to_plane")
aligned = meshioplusplus.transform(scan, matrix=matrix)
```

#### Point-cloud normals

**`meshioplusplus.estimate_normals(points, k=16)`** gives every point of a scan a normal from its `k` nearest neighbours' plane fit, oriented consistently (a spanning tree over the neighbour graph, then outward) or towards a viewpoint, as the `normals` array the PCD and XYZ writers emit. See [point-cloud normals](doc/point_normals.md).

<!--pytest-codeblocks:skip-->

```python
scan = meshioplusplus.estimate_normals(meshioplusplus.read("scan.ply"), k=24)
meshioplusplus.write("scan.pcd", scan)   # with normal_x normal_y normal_z
```

#### Surface reconstruction

**`meshioplusplus.reconstruct_surface(cloud)`** turns an oriented point cloud into a triangle surface: the zero level set of the signed distance to the samples' tangent planes (Hoppe et al. 1992), cut by marching tetrahedra on a band of lattice cells about the samples. Normals come from the cloud's `normals` array or are estimated; an open scan stays open. See [surface reconstruction](doc/reconstruct_surface.md).

<!--pytest-codeblocks:skip-->

```python
surface = meshioplusplus.reconstruct_surface(meshioplusplus.read("scan.ply"))
meshioplusplus.write("scan.stl", surface)
```

#### Convex hull and planar Delaunay

**`meshioplusplus.convex_hull(points)`** is the closed hull of scattered points (a `triangle` surface, or with `dimension=2` the `x, y` outline as a `line` loop), its vertices the extreme points alone with `hull:point_id`; **`meshioplusplus.delaunay_2d(points)`** triangulates the points' `x, y` coordinates, every point keeping its `z` and data, so survey scatter becomes a terrain. Every decision is an exact predicate: coplanar and cocircular points need no tolerance. See [hull](doc/hull.md).

<!--pytest-codeblocks:skip-->

```python
hull = meshioplusplus.convex_hull(meshioplusplus.read("scan.xyz"))
terrain = meshioplusplus.delaunay_2d(meshioplusplus.read("survey.pcd"))
```

#### Adjacency graphs (CSR) and METIS / Scotch files

**`meshioplusplus.adjacency(mesh, kind)`** returns the mesh's graph in compressed-sparse-row form, `(indptr, indices)`: `"node"` (nodes joined by a cell edge), `"clique"` (nodes sharing a cell: the sparsity pattern of an assembled FEM matrix) or `"cell"` (cells sharing a facet: the dual graph partitioners cut), sorted, symmetric and byte-identical on every backend. **`write_graph`** writes it as a METIS `.graph` or a Scotch `.grf` file for an external partitioner. Both are on every surface — Python, C++, C, Fortran, Julia, R, WASM, both CLIs (`graph`) and MCP. See `doc/adjacency.md`.

<!--pytest-codeblocks:skip-->

```python
indptr, indices = meshioplusplus.adjacency(mesh, "clique")   # FEM preallocation pattern
meshioplusplus.write_graph("mesh.graph", mesh, "cell")        # gpmetis mesh.graph 16
```

#### Surface remeshing (ACVD clustering)

**`meshioplusplus.remesh`** replaces a **surface** mesh's own triangulation with a new, near-uniformly-sized, well-shaped one at a caller-chosen vertex count, by approximated centroidal Voronoi diagram (ACVD) clustering — the one resolution-changing operation that does not inherit the input's element shapes, so it can *raise* quality at every target count rather than only remove elements. See `doc/remesh.md`.

<!--pytest-codeblocks:skip-->

```python
out = meshioplusplus.remesh(mesh, num_clusters=5000)
out = meshioplusplus.remesh(mesh, num_clusters=5000, metric="quadric")       # preserves sharp edges/corners
out = meshioplusplus.remesh(mesh, num_clusters=5000, metric="anisotropic", max_anisotropy=4.0)
```

`metric="isotropic"` (default) is fast and rounds sharp features; `"quadric"` (Garland-Heckbert error) pins clusters onto edges/corners instead; `"anisotropic"` shapes clusters with a local curvature tensor, elongating elements along low-curvature directions. The output has entirely **new** points and connectivity — no point/cell map — so `point_data`/`cell_data`/named regions are dropped and `field_data` carries through; transfer a field onto the result with `interpolate`/`conservative_interpolate`.

#### Adaptation with MMG (optional backend)

**`meshioplusplus.adapt`** remeshes a simplicial mesh to a constant size, a size field or an anisotropic metric through [MMG](https://www.mmgtools.org/): `mmg3d` for tetrahedra, `mmg2d` for planar triangles, `mmgs` for surfaces. Cell and side regions come back under their names, required points and regions survive exactly, and `metric_from_hessian` turns a `hessian` into the metric. **`discretize_levelset`** embeds a level set's isovalue conformally between an `inside` and an `outside` region, and **`mesh_domain`** triangulates the planar domain a line mesh bounds, holes left out by a point inside each, and **`move`** moves a mesh by a displacement of part of its boundary with MMG's Lagrangian mode (an MMG built with ELAS, GPL-3.0). MMG is LGPL-3.0 and bring-your-own (`-DMESHIOPLUSPLUS_WITH_MMG=ON`, `build/build-mmg.sh`), so the published wheels do not carry it. See `doc/mmg.md`.

#### Volumetric remeshing (isosurface stuffing)

**`meshioplusplus.remesh_volume`** is `remesh`'s volumetric sibling — the tet-mesh counterpart `decimate_volume` needed but could not itself provide, since QEM edge collapse can only remove elements. It retetrahedralizes a **volume** mesh (or a closed surface, unlike `remesh`) at a caller-chosen resolution by isosurface stuffing over a body-centered cubic (BCC) lattice, generating an entirely new mesh rather than working on the input's own cells. See `doc/remesh_volume.md`.

<!--pytest-codeblocks:skip-->

```python
out = meshioplusplus.remesh_volume(mesh, cell_size=0.5)
out = meshioplusplus.remesh_volume(mesh, resolution=(64, 64, 64))
out, report = meshioplusplus.remesh_volume(mesh, cell_size=0.5, return_report=True)
print(report["num_tets"], report["num_non_manifold_edges"])
```

Every uncut lattice tet has a dihedral angle from a small, mesh-size-independent fixed set. `warp_fraction` (default `0.35`) moves lattice vertices near the surface onto it, trading a small, *measured* chance of non-manifold boundary edges (reported in `num_non_manifold_edges`) for substantially better boundary tet quality; `0` disables warping and gives an exactly watertight but lower-quality boundary. Implemented from the published description of Labelle & Shewchuk's isosurface stuffing (SIGGRAPH 2007) only — no predicate library needed, unlike literal Delaunay/CVD tetrahedralization.

#### Volume meshes on an octree (graded tetrahedra fitted to a skin)

**`meshioplusplus.octree_mesh`** meshes the inside of any skin (STL, OBJ, a volume mesh's boundary; holes and self-intersections are tolerated through the fast winding number) on a 2:1-balanced octree whose leaves follow a size field (curvature, sharp features, thin gaps, a user array). The default output is a conforming graded tetrahedral mesh: a graded BCC lattice cut to the skin by isosurface stuffing, sharp corners and edges snapped, then optimised under a guard that never worsens the extreme dihedral angles; `skin_grading="uniform"` gives Labelle and Shewchuk's 10.7°–164.8° bound. `output="castellated"` gives the inside leaves as hexahedra with the `surrogate_boundary` side region and `sdf:distance`/`sdf:closest_point`, for embedded and Shifted Boundary Method solvers. `output="hex"` gives hexahedra only, on one grid at the skin's size, or with `hex_grading="graded"` the all-hexahedral dual of the graded octree, conforming through the transition schemes of Livesu, Pitzalis and Cherchi (ported from CinoLib). The same operation is in C++, C, Fortran, Julia, R, WASM, both CLIs (`octree-mesh`), the pipeline (`OctreeMesh`) and MCP. See `doc/octree_mesh.md`.

<!--pytest-codeblocks:skip-->

```python
tets, report = meshioplusplus.octree_mesh(skin, min_size=0.02, max_size=0.2, return_report=True)
print(report["num_tetrahedra"], report["min_dihedral"], report["warnings"])
cells = meshioplusplus.octree_mesh(skin, output="castellated", min_size=0.02)
```

#### Surface meshes from CAD (conforming triangulation of a B-rep)

**`meshioplusplus.mesh_cad_surface`** triangulates the faces of a CAD model (a Kratos CAD JSON read, or STEP and IGES through OpenCASCADE) into one conforming surface mesh at a target edge size, with no CAD kernel: every B-rep edge is sampled once and shared by the faces that use it, so a closed solid comes out watertight, and each face is a constrained Delaunay triangulation of its parameters on Shewchuk's exact predicates, lifted onto the surface. A face that cannot be meshed is reported by index and reason, never meshed wrong, and the output is identical across backends and thread counts. `min_angle` refines each face by Delaunay refinement until its triangles' smallest angles on the surface reach the bound (guaranteed to 20.7 degrees away from small input angles and poles, which are reported), and `smooth_iterations` smooths the inside under a guard that never lowers a star's smallest angle. `order=2` or `3` writes curved `triangle6` or `triangle10` elements whose nodes lie on the exact surfaces and edges, each proved valid everywhere inside by a Bézier bound on its Jacobian or kept straight-sided and reported. `curvature_deviation` and `cells_across_gaps` size the mesh by the model's curvature and its thin parts through one gradation-limited field (`grading`), `pole_rings` grades the triangles around a pole, and a triangle that would lift folded is refined away. Sizes can be given per face (`face_sizes`), per edge (`edge_sizes`) or by a `background` mesh, with the report naming the edges that hold a face finer than asked; `virtual_edges` skips the slivers of edges a model splits its rims into, and `metric="varying"` meshes each face in its surface's own metric, so stretched faces and the sphere's poles meet `min_angle` too. A face whose parameters are unusable (a side collapsed onto a point, a pole) can be meshed in a flattening of its own coarse mesh (`reparam_condition_number`), a sliver face with the neighbour it meets tangentially (`virtual_faces`), and the gaps a STEP or IGES model declares edge by edge are accepted with `model_tolerances`; `lop_corners` lops acute corners (Pav and Walkington 2005) and states, on planar faces, the angle bound that proves; `metric_background` sizes the triangles by an anisotropic metric from a field's Hessian (`R |Λ| Rᵀ / (8 metric_error)`, Loseille and Alauzet 2011), so they stretch along a layer. `untangle` moves the nodes of folded curved elements on the surface and along the CAD edges to keep them curved and valid (Toulorge et al. 2013), and `quads="dominant"` recombines triangle pairs into quads by a maximum-weight matching (Remacle et al. 2012; `quad_pairs="greedy"` pairs best first) while `quads="all"` leaves no triangle at all, curved `quad9` at `order=2` and `quad16` at `order=3`, sized by the same sources; curved meshes work on flattened and merged faces too, and `metric_array` takes a field itself, its Hessian computed on the background. `triangulate_polygon_2d` exposes the planar triangulator, with the same `min_angle`. A settings pipeline carries the model a CAD read returns to a `MeshCadSurface` step, Gmsh 4.1 output gives every CAD face its own physical surface, and `octree_mesh` fills a closed result with tetrahedra whose dihedral angles keep inside the isosurface-stuffing bound, or `tetrahedralize` in one call (its octree backend, or Netgen keeping the triangles). The same operation is in C++, C, Fortran, Julia, R, WASM, both CLIs (`mesh-cad-surface`) and MCP, and a scheduled job measures it on real STEP models beside Gmsh's own meshes (`tools/cad_corpus.py`). See `doc/mesh_cad.md`.

<!--pytest-codeblocks:skip-->

```python
surface, report = meshioplusplus.mesh_cad_surface(meshioplusplus.read("part.cad.json"), 0.1, return_report=True)
print(report["num_failed"], report["num_open_edges"], report["min_angle_deg"])
```

**`meshioplusplus.project_to_cad`** moves a mesh's points back onto the CAD model it was made from, by the `cad:face` and `cad:edge` cell data `mesh_cad_surface` writes, so a smoothing or an adaptation that knows no CAD can be put back on the model; points that land outside their face's trims are reported, never clamped. See `doc/project_to_cad.md`.

**`meshioplusplus.boundary_layer`** grows prismatic layers from a triangle and quad surface: `num_layers` layers of wedges and hexahedra along the most normal normals (Aubry and Löhner 2009), the first `first_height` thick and growing by `growth`, stopped short of the surface across a gap and where the last layer's front would cross itself or the surface (`front_check`), and halved, then collapsed into pyramids and tetrahedra (or, with `collapse="layers"`, grown fewer layers) where a cell would fold. See `doc/boundary_layer.md`.

**`meshioplusplus.extrude`** and **`meshioplusplus.revolve`** sweep a surface into a volume, or a curve into a surface, along a vector (graded layers) or around an axis (the cells on the axis collapsing into pyramids, tetrahedra and wedges): the swept cells only, with `bottom`/`top` (`start`/`end`) and `side` regions, the input's regions and data carried; extruding `rectangle` gives `box` exactly. See `doc/extrude.md`.

**`meshioplusplus.tetrahedralize`** fills a closed triangle surface (a `mesh_cad_surface` result, a boundary layer's cap) with tetrahedra, nested shells becoming regions and `cad:face` side regions: through its native octree backend in every build (isosurface stuffing, the boundary fitted within a reported distance), or through Netgen's nglib, an optional backend that keeps the surface's triangles exactly (LGPL-2.1, linked dynamically when built with `-DMESHIOPLUSPLUS_WITH_NETGEN=ON`; `backend="auto"` takes it when present), or through an installed TetGen or Gmsh program run as a separate process (`backend="tetgen"`, `"gmsh"`), the surface kept too. See `doc/tetrahedralize.md`. **`meshioplusplus.remesh_quads`** remeshes a triangle surface into field-aligned quads through an installed QuadriFlow or Instant Meshes, also run as a separate process: a sphere comes out all quads with a mean scaled Jacobian of 0.99 and its worst quad at 0.25 to 0.58 (by seed) where recombining a mesher's triangles leaves 0.12 at its poles. See `doc/remesh_quads.md`.

**`meshioplusplus.cut_level_set`** returns the part of a mesh that one or several level sets select (`point_data` arrays or planes, combined by an expression such as `"wall < 0 and hole > 0"`): the pieces of every cell family they cross, on one side or on the interface, the uncut cells inside, point data interpolated and cell data and regions carried; **`cut_quadrature`** gives quadrature rules on that part, the cut-cell quadrature of unfitted finite elements, quadratic level sets included on `triangle6`/`tetra10`. Both run [CutCells](https://github.com/sclaus2/CutCells) (MIT), an optional dependency (`-DMESHIOPLUSPLUS_WITH_CUTCELLS=ON`, `build/build-cutcells.sh`) the Linux and macOS wheels link. See `doc/cut.md`.

**`meshioplusplus.error_size`** turns `estimate_error`'s per-cell indicator into a per-point size by Zienkiewicz and Zhu's adaptive procedure, a `background` for `mesh_cad_surface`, so an adaptation re-meshes from the CAD model. See `doc/error_size.md`.

<!--pytest-codeblocks:skip-->

```python
layers, report = meshioplusplus.boundary_layer(surface, 1e-3, num_layers=8, growth=1.25, return_report=True)
slab = meshioplusplus.extrude(meshioplusplus.rectangle(dims=(8, 4)), (0.0, 0.0, 0.5), num_layers=6, ratio=1.2)
body = meshioplusplus.revolve(meshioplusplus.rectangle(dims=(4, 8)), angle=270.0, num_layers=12)
back = meshioplusplus.project_to_cad(meshioplusplus.smooth(surface, iterations=10), meshioplusplus.read("part.cad.json"))
volume, report = meshioplusplus.tetrahedralize(surface, max_size=0.1, return_report=True)  # Netgen if built, else octree
```

#### ODT remeshing (relocate + flip connectivity)

**`meshioplusplus.optimize_volume`** raises a tetrahedral mesh's worst element quality by *ODT remeshing* — relocating vertices AND changing connectivity. It is the genuine "ODT remeshing" and the third member of a trio whose other two each do half the job: `smooth(method="odt")` moves points on *fixed* connectivity, `remesh_volume` discards the input's tets for a fresh lattice mesh. It alternates the ODT vertex relocation with quality-improving topological **flips** (2-3 and 3-2), **predicate-free** — a flip is applied only when a pure signed-volume test finds the local configuration convex and the minimum scaled Jacobian strictly improves (no in-sphere/Delaunay predicate). See `doc/optimize_volume.md`.

<!--pytest-codeblocks:skip-->

```python
out = meshioplusplus.optimize_volume(mesh)                       # a tetrahedral mesh
out, report = meshioplusplus.optimize_volume(mesh, return_report=True)
print(report["min_dihedral_before"], report["min_dihedral_after"])  # never lower, by default
```

By default (`objective="worst"`) it raises the least dihedral angle and never lowers it — guarded relocation, 2-3 flips, edge removal, multi-face removal and worst-cell smoothing (Freitag and Ollivier-Gooch 1997; Klingner and Shewchuk 2007), taking Netgen's optimised sphere from 17.4 to 32.4 degrees; `objective="energy"` is the ODT energy with scaled-Jacobian flips it ran alone up to v18.0.0. See [`doc/optimize_volume.md`](doc/optimize_volume.md).

The flips touch only interior faces/edges, so the boundary surface is preserved exactly (watertight in ⇒ watertight out); the point set is invariant, so `point_data`/`field_data` and named Point regions carry through while `cell_data`/Cell/Side regions are dropped. Tet-only, and (like `remesh_volume`) C++-core only.

#### Smoothing

**`meshioplusplus.smooth`** relaxes point coordinates to improve element shape, leaving topology and every data value alone: **only the points move**. See `doc/smooth.md`.

Three methods. **Laplacian** (`x <- x + lambda*L(x)`, the edge-neighbour centroid displacement) smooths strongly per pass but shrinks — over 40 iterations on a jittered 8×8 quad grid it contracts the bounding box by 57%. **Taubin** (the default) follows each `+lambda` pass with a larger-magnitude `-mu` pass that deliberately un-shrinks, leaving the same grid 3.6% smaller. **ODT** (optimal-Delaunay-triangulation smoothing, **tet-only**) instead moves each free interior vertex to the closed-form volume-weighted average of its incident tets' circumcenters — the "ODT" half of the volumetric-remeshing roadmap item, closed as *smoothing on existing connectivity* rather than remeshing. Neighbours for Laplacian/Taubin are the nodes joined by an actual cell *edge*, not the element clique, so a structured hex block is a fixed point rather than being bevelled toward a sphere. Boundary nodes, feature nodes (the endpoints of [feature edges](https://loumalouomega.github.io/meshioplusplus/feature_edges) — on a surface mesh its own creases as well as the corners of its boundary), an optional `frozen` mask, and the nodes of blocks whose edge topology is unknown are all pinned by default, and the inversion guard rejects any move that would turn a valid cell inverted.

<!--pytest-codeblocks:skip-->

```python
relaxed = meshioplusplus.smooth(mesh)                          # 10 Taubin iterations
harder = meshioplusplus.smooth(mesh, iterations=40)            # shrink-free even so
lap = meshioplusplus.smooth(mesh, method="laplacian", lambda_=0.4)  # note the underscore
odt = meshioplusplus.smooth(tet_mesh, method="odt", iterations=10)  # tet-only, C++-core only
out, report = meshioplusplus.smooth(mesh, return_report=True)  # nodes moved, max displacement
```

`lambda_` carries a trailing underscore because `lambda` is a Python keyword, and a negative value means "this method's own default" (0.5 Laplacian, 0.33 Taubin). Point and cell counts, connectivity, `cell_data`, `field_data`, `point_data` values and the points array's dtype all come through unchanged, and output is byte-identical across mesh backends and thread counts.

#### Field transfer (interpolation)

**`meshioplusplus.interpolate`** samples a **source** mesh's data arrays onto a **target** mesh — the first cross-mesh operation that transfers data (diff compares, merge concatenates). The result is a copy of the target, its own geometry/data/sets preserved exactly, with the requested source arrays sampled on: source `point_data` at the target's points, source `cell_data` by nearest source-cell centroid. `method="nearest"` (default) copies the nearest source point's value bit-for-bit; `method="barycentric"` simplexifies the source first and interpolates linearly — exact on a linear field — with `default_value`/`extrapolate` deciding what happens outside the source domain. Both search grids are bucket-grid spatial hashes (never O(N²)), and output is byte-identical across backends, thread counts and the C++/numpy boundary. See `doc/interpolate.md`.

<!--pytest-codeblocks:skip-->

```python
coarse = meshioplusplus.read("solution.vtu")   # carries point_data "T"
fine = meshioplusplus.read("remeshed.vtu")
mapped = meshioplusplus.interpolate(coarse, fine, method="barycentric")
meshioplusplus.write("mapped.vtu", mapped)
```

**`meshioplusplus.conservative_interpolate`** is a separate, mass-preserving sibling: over the region the two meshes share, `sum(target value * target measure)` equals `sum(source value * source measure)`, a property `interpolate`'s pointwise sampling does not have. Both meshes are simplexified first (accepting ragged/polyhedron blocks for free), overlapping simplex pairs are measured with an exact geometric clip (Sutherland-Hodgman in 2D, a bounded tetrahedron-tetrahedron clip in 3D), and a target cell's value is the overlap-measure-weighted mean of every source cell it intersects. Unlike `interpolate`, an unset `arrays` transfers every source `point_data` **and** `cell_data` array. `point_data` is transferred by composition (`point_data_to_cell_data` → the same clip algorithm → `cell_data_to_point_data`), a layered approximation rather than exact nodal conservation. C++-core only, with no pure-Python fallback (the 3D clip's discrete branches could disagree near a degenerate overlap). See `doc/conservative_interpolate.md`.

#### Slicing / cross-sections

**`meshioplusplus.slice`** computes the planar cross-section of a mesh — the actual intersection of the mesh with a plane, one topological dimension below the cut cells: a 3D volume mesh yields a `triangle`/`quad` surface, a 2D surface mesh a `line` mesh. Unlike `crop` (plane mode), which keeps whole cells on one side, `slice` computes the intersection and lowers the dimension. It uses robust marching tetrahedra (the input is simplexified first, so each cell's cross-section is a well-defined convex primitive), deduping crossing points on shared edges into single nodes so the section is watertight, and winding every face consistently toward the `+normal` side. Each section cell inherits its parent's `cell_data`; `record_parent_ids=True` attaches `slice:parent_cell`, and `point_data` is interpolated at the cut. Output is byte-identical across backends, thread counts and the C++/numpy boundary. See `doc/slice.md`.

<!--pytest-codeblocks:skip-->

```python
vol = meshioplusplus.read("part.vtu")                          # a tetra/hex/wedge mesh
section = meshioplusplus.slice(vol, origin=(0, 0, 0.5), normal=(0, 0, 1))
meshioplusplus.write("section.vtu", section)                  # a triangle/quad surface at z=0.5
```

(`slice` shadows the Python built-in only as a module attribute — `meshioplusplus.slice` is intended.)

#### Isosurfaces / contours

**`meshioplusplus.isosurface`** computes the level set of a scalar field — the locus where a `point_data` array equals a given isovalue, as a mesh one topological dimension below the cut cells: a 3D volume mesh yields a `triangle`/`quad` surface, a 2D surface mesh a `line` contour. It is the data-driven sibling of `slice` (which cuts where the distance to a plane is zero) and shares its marching-tetrahedra cutter, so contours are watertight in the same way. The field must be `point_data` — `cell_data` is piecewise constant and has no level set, so naming one raises and points at `cell_data_to_point_data`. Several isovalues land in one mesh, cut in ascending order and tagged per cell with a Float64 `iso:value` and an Int64 `iso:index` (the ordinal — the integer tag `split(by="region", tag=…)` needs). The contoured field reads back as **exactly** the isovalue on the cut points, faces are wound toward increasing field, and an out-of-range isovalue is an empty contour rather than an error. Output is byte-identical across backends, thread counts and the C++/numpy boundary. See `doc/isosurface.md`.

<!--pytest-codeblocks:skip-->

```python
vol = meshioplusplus.read("part.vtu")                          # carrying point_data["T"]
shells = meshioplusplus.isosurface(vol, "T", [300.0, 350.0, 400.0])
meshioplusplus.write("shells.vtu", shells)                     # three tagged contour surfaces
```

#### Field derivatives (gradient / divergence / curl)

**`meshioplusplus.gradient`** differentiates a `point_data` field: its gradient, divergence or curl. meshio++ could already transform, transfer, summarize and contour a field — this is what lets it *differentiate* one, which is the missing input for contouring a derived quantity (`|∇T|`, vorticity) and for the gradient-based error indicators that drive the selective `refine`. Two methods: **Green-Gauss** (the default) applies the divergence theorem over the cell, fanning each face into triangles about its corner average, which is **exact for a linear field on any cell** — planar faces or not, because the fan surface is closed; **least-squares** fits over the cells sharing a node and falls back to Green-Gauss (counted, never silently wrong) on a degenerate neighbourhood. An `nc`-component input yields `3·nc` gradient components laid out `[component][derivative]`, so a scalar gives `(n, 3)` and a 3-vector `(n, 9)`; divergence gives 1 and curl 3. Output is `Float64`, named `<input>:gradient` / `:divergence` / `:curl`, at either the cell (default) or point location. A `cell_data` input raises by name — a piecewise-constant field has no derivative — and cells that cannot be differentiated yield NaN and are counted rather than approximated. Geometry, regions and existing data pass through bit-identically; output is byte-identical across backends, thread counts and the C++/numpy boundary. See `doc/gradient.md`.

<!--pytest-codeblocks:skip-->

```python
import numpy as np

vol = meshioplusplus.read("solution.vtu")                      # carrying point_data["T"]
g = meshioplusplus.gradient(vol, "T", location="point")        # point_data["T:gradient"], (n, 3)

grad = np.asarray(g.point_data["T:gradient"])
g.point_data["gradT"] = np.sqrt((grad**2).sum(axis=1))
shells = meshioplusplus.isosurface(g, "gradT", [2.0])          # contour where T changes fastest
```

These operations are exposed across every binding surface (Python, C API, Fortran, WASM) and as the CLI verbs `meshioplusplus quality`, `meshioplusplus extract-surface`, `meshioplusplus reorder`, `meshioplusplus diff`, `meshioplusplus merge`, `meshioplusplus transform`, `meshioplusplus clean`, `meshioplusplus crop`, `meshioplusplus slice`, `meshioplusplus split`, `meshioplusplus stats`, `meshioplusplus convert-cells`, `meshioplusplus tessellate`, `meshioplusplus subdivide`, `meshioplusplus agglomerate`, `meshioplusplus refine`, `meshioplusplus undo-green`, `meshioplusplus partition`, `meshioplusplus remesh`, `meshioplusplus remesh-volume`, `meshioplusplus optimize-volume`, `meshioplusplus smooth`, `meshioplusplus interpolate`, `meshioplusplus conservative-interpolate`, `meshioplusplus isosurface`, `meshioplusplus curvature`, `meshioplusplus normals`, `meshioplusplus repair`, `meshioplusplus shrinkwrap` and `meshioplusplus sobolev-deform` (plus `meshioplusplus data gradient`, `meshioplusplus data hessian`, `meshioplusplus data estimate-error` and `meshioplusplus data integrate`, mesh operations grouped under `data` because that is where a user looks for them).

#### Second derivatives (Hessian)

**`meshioplusplus.hessian`** computes the Hessian (second derivative) of a **scalar** `point_data` field — `gradient`'s companion one order further, for curvature-based adaptive refinement. A **composition** of two `gradient` calls, not a new numerical kernel: the field is differentiated once (point location), then that `(n, 3)` gradient is differentiated again with the default gradient operator, producing `(n, 9)` — the flattened row-major 3x3 Hessian. `method` forwards to both internal passes. A field that is at most linear has an exactly zero Hessian everywhere — the one mesh-shape-independent guarantee; a genuinely quadratic field's composition is exact on a structured/symmetric mesh away from its own boundary and a good, standard, but genuinely approximate curvature estimate on an irregular mesh. Input must have exactly one component. A curvature-driven refinement indicator needs no new code: `data_calc`'s `norm(...)` on the 9-component output is exactly its Frobenius norm, ready for `refine`'s `where` selector. See `doc/hessian.md`.

```python
h = meshioplusplus.hessian(vol, "T")                            # cell_data["T:hessian"], (n, 9)
curv = meshioplusplus.data_calc(h, "norm(`T:hessian`)", location="cell", output="curv")
adapted = meshioplusplus.refine(curv, where="curv > 3.0")       # refine where curvature is largest
```

#### Error estimation (Zienkiewicz-Zhu recovery + marking)

**`meshioplusplus.estimate_error`** estimates the per-cell recovered-gradient error of a `point_data` field, and can mark cells for refinement — the piece that closes the adaptive loop: `gradient` differentiates and selective `refine`'s `--where` consumes any scalar `cell_data` predicate; this produces one, so estimate → mark → refine is three verbs and no new numerical code. It is a **composition**, not a new kernel: `gradient` (Green-Gauss, cell location) → the measure-weighted point↔cell averaging round trip recovers a smoothed gradient, and `eta_K = sqrt(|measure| · sum((recovered − raw)²))` per cell is the standard ZZ indicator. `marking` turns it into a boolean `error:marked` array: `"absolute"` (threshold), `"fraction"` (top N by indicator), or `"dorfler"` (the smallest indicator-descending prefix covering a bulk fraction of the total — the usual AMR criterion). Cells that cannot be evaluated read NaN in the indicator and 0 (never NaN) in the marking array, counted and excluded from the global error. See `doc/error.md`.

```python
out, report = meshioplusplus.estimate_error(
    vol, "T", marking="dorfler", marking_value=0.6, return_report=True,
)
print(report["global_error"], report["num_marked"])
adapted = meshioplusplus.refine(out, where="error:marked > 0.5")
```

#### Field integration (total / mean, per-region)

**`meshioplusplus.data_integrate`** computes a cell-measure-weighted total and mean of one or more `cell_data` arrays — `gradient`'s integration counterpart (`gradient` differentiates a field, this integrates one), for a density field's total mass, a heat-flux field's total power, or an occupied volume. Every sum is weighted by `|measure(cell)|` (the cell's own length/area/volume); a cell whose measure is not computable, or a component whose value is non-finite, is excluded from that component's numerator **and** denominator — never given a fallback weight of 1, unlike `cell_data_to_point_data`'s own measure weighting, since a silent unit-weight substitution would corrupt a physical total. Reported for the whole mesh and independently for every named `Cell` region — regions are **not a partition**, so a cell in two regions contributes fully to both. A `point_data`-only name raises by name, pointing at `point_data_to_cell_data`. The mesh is never modified; this is a read-only report, like `data_info` and `compute_stats`. See `doc/field_integration.md`.

```python
report = meshioplusplus.data_integrate(mesh, arrays=["density"])
report[0]["domain"]["total_per_component"]   # sum(value * |measure|) -- total mass
report[0]["regions"]                         # the same, independently, per named Cell region
```

#### Geometry helpers (curvature, normals, repair, shrinkwrap, Sobolev deformation, grids and SDF)

Six operations built for the physics-ML surface, each with its own CLI verb, MCP tool, and Python-API and doc page: **`meshioplusplus.compute_curvature`** (per-vertex mean/Gaussian curvature by the angle defect and cotangent Laplace-Beltrami operator — `doc/curvature.md`), **`meshioplusplus.compute_normals`** (point/cell normals with an optional crease split — `doc/normals.md`), **`meshioplusplus.repair`** (fixes a surface's orientation, holes and pinched vertices, the defects `clean` does not touch — `doc/repair.md`), **`meshioplusplus.shrinkwrap`** (projects a mesh's points onto a target surface in one pass — `doc/shrinkwrap