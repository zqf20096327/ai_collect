<a href="https://xplorahub.com/methods"><img src="assets/banner.png" alt="Awesome mineral exploration, curated by XploraHub" width="100%"></a>

# Awesome Mineral Exploration

> Open-source software for finding what lies beneath.

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Link check](https://github.com/XploraHub/awesome-mineral-exploration/actions/workflows/links.yml/badge.svg)](https://github.com/XploraHub/awesome-mineral-exploration/actions/workflows/links.yml)
[![Contributors](https://img.shields.io/github/contributors/XploraHub/awesome-mineral-exploration)](https://github.com/XploraHub/awesome-mineral-exploration/graphs/contributors)
[![Last commit](https://img.shields.io/github/last-commit/XploraHub/awesome-mineral-exploration)](https://github.com/XploraHub/awesome-mineral-exploration/commits/main)
[![Licence: CC0](https://img.shields.io/badge/licence-CC0--1.0-green)](LICENSE)

A curated list of open-source software for mineral exploration: geophysics, geological modelling, drillholes, geostatistics, geochemistry, remote sensing, prospectivity mapping and drone surveys, with the open data portals they work from.

Every tool here is open source, has a licence and has been updated in the last 18 months, except those under No longer maintained, at the end. Icons show the main language; the licence follows each description. Curated by [XploraHub](https://xplorahub.com), open ground for exploration & mining technology.

## Contents

- [Geophysics](#geophysics)
- [Geological modelling and structural geology](#geological-modelling-and-structural-geology)
- [Drillholes and logging](#drillholes-and-logging)
- [Geostatistics and resource estimation](#geostatistics-and-resource-estimation)
- [Geochemistry](#geochemistry)
- [Remote sensing](#remote-sensing)
- [Prospectivity mapping and machine learning](#prospectivity-mapping-and-machine-learning)
- [Open data](#open-data)
- [Drones, photogrammetry and point clouds](#drones-photogrammetry-and-point-clouds)
- [GIS and 3D visualisation](#gis-and-3d-visualisation)
- [Related lists](#related-lists)
- [No longer maintained](#no-longer-maintained)

## Geophysics

How the methods work: [magnetics, gravity, ERT, IP, MT and more](https://xplorahub.com/methods).

- [SimPEG](https://github.com/simpeg/simpeg) - <img src="assets/icons/python.svg" alt="Python" height="16"> Forward modelling and inversion for gravity, magnetics, DC resistivity, IP and electromagnetics. MIT.
- [discretize](https://github.com/simpeg/discretize) - <img src="assets/icons/python.svg" alt="Python" height="16"> Meshes and finite-volume tools behind SimPEG. MIT.
- [geoapps](https://github.com/MiraGeoscience/geoapps) - <img src="assets/icons/python.svg" alt="Python" height="16"> Notebook apps for exploration inversion and interpretation, built on SimPEG. MIT.
- [geoh5py](https://github.com/MiraGeoscience/geoh5py) - <img src="assets/icons/python.svg" alt="Python" height="16"> Python API for geoh5, an open file format for geoscience data. LGPL-3.0.
- [Tomofast-x](https://github.com/TOMOFAST/Tomofast-x) - <img src="assets/icons/fortran.svg" alt="Fortran" height="16"> Parallel 3D inversion, including joint gravity and magnetic inversion. MIT.
- [PyGMI](https://github.com/Patrick-Cole/pygmi) - <img src="assets/icons/python.svg" alt="Python" height="16"> Processing, modelling and interpretation of potential-field and radiometric data, aimed at exploration. GPL-3.0.
- [pyGIMLi](https://github.com/gimli-org/pyGIMLi) - <img src="assets/icons/python.svg" alt="Python" height="16"> Modelling and inversion library, widely used for ERT and IP. Apache-2.0.
- [ResIPy](https://gitlab.com/hkex/resipy) - <img src="assets/icons/python.svg" alt="Python" height="16"> Graphical interface and Python API for processing and inverting resistivity and IP surveys. GPL-3.0.
- [Harmonica](https://github.com/fatiando/harmonica) - <img src="assets/icons/python.svg" alt="Python" height="16"> Processing, forward modelling and inversion of gravity and magnetic data. BSD-3-Clause.
- [Verde](https://github.com/fatiando/verde) - <img src="assets/icons/python.svg" alt="Python" height="16"> Gridding and processing of spatial data such as ground and airborne survey lines. BSD-3-Clause.
- [Boule](https://github.com/fatiando/boule) - <img src="assets/icons/python.svg" alt="Python" height="16"> Reference ellipsoids and normal gravity for gravity processing. BSD-3-Clause.
- [Choclo](https://github.com/fatiando/choclo) - <img src="assets/icons/python.svg" alt="Python" height="16"> Forward-modelling kernels for gravity and magnetic sources. BSD-3-Clause.
- [MTpy-v2](https://github.com/MTgeophysics/mtpy-v2) - <img src="assets/icons/python.svg" alt="Python" height="16"> Tools for magnetotelluric transfer functions, built on MTH5. MIT.
- [emg3d](https://github.com/emsig/emg3d) - <img src="assets/icons/python.svg" alt="Python" height="16"> 3D electromagnetic modelling with a multigrid solver. Apache-2.0.
- [empymod](https://github.com/emsig/empymod) - <img src="assets/icons/python.svg" alt="Python" height="16"> Electromagnetic modelling for layered (1D) earth models. Apache-2.0.
- [GA-AEM](https://github.com/GeoscienceAustralia/ga-aem) - <img src="assets/icons/cplusplus.svg" alt="C++" height="16"> Modelling and 1D inversion of airborne electromagnetic data, from Geoscience Australia. GPL-2.0.
- [segyio](https://github.com/equinor/segyio) - <img src="assets/icons/c.svg" alt="C" height="16"> <img src="assets/icons/python.svg" alt="Python" height="16"> Fast reading and writing of SEG-Y seismic files. LGPL-3.0.
- [OpendTect](https://github.com/OpendTect/OpendTect) - <img src="assets/icons/cplusplus.svg" alt="C++" height="16"> Seismic interpretation software. GPL-3.0.
- [SGTool](https://github.com/swaxi/SGTool) - <img src="assets/icons/python.svg" alt="Python" height="16"> QGIS and ArcGIS Pro plugin for potential-field grid processing, built for the WAXI structural geophysics course. MIT.
- [resistics](https://github.com/resistics/resistics) - <img src="assets/icons/python.svg" alt="Python" height="16"> Robust processing of magnetotelluric time series. MIT.
- [razorback](https://github.com/BRGM/razorback) - <img src="assets/icons/python.svg" alt="Python" height="16"> Robust magnetotelluric processing from BRGM. GPL-3.0.
- [MTH5](https://github.com/IAGA-DVI-DataStandards/mth5) - <img src="assets/icons/python.svg" alt="Python" height="16"> Archivable, exchangeable file format for magnetotelluric time series. MIT.
- [FEMTIC](https://github.com/yoshiya-usui/femtic) - <img src="assets/icons/cplusplus.svg" alt="C++" height="16"> 3D magnetotelluric inversion on unstructured meshes. MIT.
- [rjmcmcmt](https://github.com/GeoscienceAustralia/rjmcmcmt) - <img src="assets/icons/cplusplus.svg" alt="C++" height="16"> Reversible-jump Markov chain Monte Carlo inversion of magnetotelluric data, from Geoscience Australia. GPL-3.0.
- [deinterf](https://github.com/dyuu7/deinterf) - <img src="assets/icons/python.svg" alt="Python" height="16"> Removes the aircraft's own magnetic interference from airborne magnetic data (Tolles–Lawson). MIT.
- [invert4geom](https://github.com/mdtanker/invert4geom) - <img src="assets/icons/python.svg" alt="Python" height="16"> 3D geometric gravity inversion, such as depth to basement. MIT.
- [GPRPy](https://github.com/NSGeophysics/GPRPy) - <img src="assets/icons/python.svg" alt="Python" height="16"> Ground-penetrating radar processing and visualisation. MIT.
- [hvsrpy](https://github.com/jpvantassel/hvsrpy) - <img src="assets/icons/python.svg" alt="Python" height="16"> Horizontal-to-vertical spectral ratio (HVSR) processing of passive seismic data, used for depth to bedrock under cover. GPL-3.0.

## Geological modelling and structural geology

How the methods work: [geological modelling](https://xplorahub.com/methods/geological-modelling) and [structural geology](https://xplorahub.com/methods/structural-geology).

- [GemPy](https://github.com/gempy-project/gempy) - <img src="assets/icons/python.svg" alt="Python" height="16"> Implicit 3D structural geological modelling from contacts and orientations, with uncertainty. EUPL-1.2.
- [GemGIS](https://github.com/cgre-aachen/gemgis) - <img src="assets/icons/python.svg" alt="Python" height="16"> Prepares GIS and spatial data for geological modelling with GemPy. LGPL-3.0.
- [LoopStructural](https://github.com/Loop3D/LoopStructural) - <img src="assets/icons/python.svg" alt="Python" height="16"> 3D structural geological modelling library, including folds and faults. MIT.
- [geoML](https://github.com/italo-goncalves/geoML) - <img src="assets/icons/python.svg" alt="Python" height="16"> Gaussian-process spatial modelling, including implicit geological models. GPL-3.0.
- [curlew](https://github.com/samthiele/curlew) - <img src="assets/icons/python.svg" alt="Python" height="16"> 2D and 3D geological models built from neural fields, following the geological history, with synthetic models for testing. MIT.
- [APSG](https://github.com/ondrolexa/apsg) - <img src="assets/icons/python.svg" alt="Python" height="16"> Structural geology and fabric analysis. MIT.
- [mplstereonet](https://github.com/joferkington/mplstereonet) - <img src="assets/icons/python.svg" alt="Python" height="16"> Stereonets for structural data in matplotlib. MIT.
- [BlenderGeoModeller](https://github.com/bsomps/BlenderGeoModeller) - <img src="assets/icons/python.svg" alt="Python" height="16"> Blender add-on that imports drillholes and builds block models and grade shells, with GemPy integration. MIT.
- [fractoolbox](https://github.com/ICWallis/fractoolbox) - <img src="assets/icons/python.svg" alt="Python" height="16"> Structural geology and borehole image analysis of fractures. Apache-2.0.
- [structuralGeology](https://github.com/nfcd/structuralGeology) - <img src="assets/icons/python.svg" alt="Python" height="16"> Jupyter notebooks for structural geology, from a university course. MIT.
- [OpenGeode-Geosciences](https://github.com/Geode-solutions/OpenGeode-Geosciences) - <img src="assets/icons/cplusplus.svg" alt="C++" height="16"> <img src="assets/icons/python.svg" alt="Python" height="16"> Data structures for geological models and geological objects, built on the OpenGeode framework. MIT.
- [OpenGeode-GeosciencesIO](https://github.com/Geode-solutions/OpenGeode-GeosciencesIO) - <img src="assets/icons/cplusplus.svg" alt="C++" height="16"> <img src="assets/icons/python.svg" alt="Python" height="16"> Reads and writes GOCAD (TS, PL, VS, VO, WL, ML, LSO), OMF, GeoTIFF, DEM, GRDECL, shapefiles and well files for OpenGeode models; its sister module [OpenGeode-Inspector](https://github.com/Geode-solutions/OpenGeode-Inspector) checks meshes and models for topology errors, intersections and degenerate elements. MIT.
- [ferreus_rbf](https://github.com/graphic-goose/ferreus_rbf_rs) - <img src="assets/icons/rust.svg" alt="Rust" height="16"> <img src="assets/icons/python.svg" alt="Python" height="16"> Fast global radial basis function interpolation and isosurface extraction for millions of points in 1D, 2D and 3D, with Python bindings. MIT.

## Drillholes and logging

How the methods work: [diamond and RC drilling](https://xplorahub.com/methods/diamond-and-rc-drilling), [core logging](https://xplorahub.com/methods/core-logging-and-scanning) and [downhole geophysics](https://xplorahub.com/methods/downhole-geophysics).

- [GeoStrix](https://github.com/Matt-Mendes-ai/geostrix) - <img src="assets/icons/javascript.svg" alt="JavaScript" height="16"> Lightweight 3D software for drillholes, geochemistry, geophysics, modelling and drill planning. MIT. [XploraHub page](https://xplorahub.com/products/geostrix).
- [lasio](https://github.com/kinverarity1/lasio) - <img src="assets/icons/python.svg" alt="Python" height="16"> Read and write Log ASCII Standard (LAS) files for downhole logs. MIT.
- [omfvista](https://github.com/pyvista/omfvista) - <img src="assets/icons/python.svg" alt="Python" height="16"> Loads Open Mining Format (OMF) files into PyVista for 3D viewing. BSD-3-Clause.
- [GeoSuite](https://github.com/ghoziankarami/geosuite) - <img src="assets/icons/javascript.svg" alt="JavaScript" height="16"> Browser and Windows app that validates and desurveys drillhole data, composites assays and builds a screening block model. GPL-3.0.
- [Baselode](https://github.com/darkmine-oss/baselode) - <img src="assets/icons/python.svg" alt="Python" height="16"> <img src="assets/icons/javascript.svg" alt="JavaScript" height="16"> Python and JavaScript toolkit for loading, desurveying and viewing drillhole data in 1D, 2D and 3D, with potential-field and radiometric processing. GPL-3.0.
- [OpenGeoPlotter](https://github.com/bsomps/OpenGeoPlotter) - <img src="assets/icons/python.svg" alt="Python" height="16"> Desktop app for drillhole cross-sections, strip logs, 3D views and alpha-beta conversion. GPL-3.0.
- [Geoscience for QGIS](https://github.com/rolandhill/geoscience) - <img src="assets/icons/python.svg" alt="Python" height="16"> QGIS plugin that desurveys drillholes and draws them in plan and section. GPL-3.0.
- [corelab](https://github.com/kevinalexandr19/corelab) - <img src="assets/icons/python.svg" alt="Python" height="16"> 2D and 3D plots of drillhole data in Python. MIT.
- [DrillHoles.jl](https://github.com/JuliaEarth/DrillHoles.jl) - <img src="assets/icons/julia.svg" alt="Julia" height="16"> Drillhole desurveying and compositing for the GeoStats.jl framework. MIT.
- [CoreSpecViewer](https://github.com/Russjas/CoreSpecViewer) - <img src="assets/icons/python.svg" alt="Python" height="16"> Desktop app for processing and viewing hyperspectral drill core scans. GPL-3.0.
- [Baselode Viewer](https://github.com/darkmine-oss/baselode-frontend) - <img src="assets/icons/javascript.svg" alt="JavaScript" height="16"> Desktop app for Windows, macOS and Linux that shows drillholes, samples and geophysics on a map, in 3D and as strip logs, built on Baselode. GPL-3.0.
- [Darkmine Data Skills](https://github.com/darkmine-oss/darkmine-data-skills) - <img src="assets/icons/python.svg" alt="Python" height="16"> Skills for AI agents and the command line that work on Baselode drillhole and surface-sample data. GPL-3.0.

## Geostatistics and resource estimation

How the method works: [geostatistics](https://xplorahub.com/methods/geostatistics).

- [GeostatsPy](https://github.com/GeostatsGuy/GeostatsPy) - <img src="assets/icons/python.svg" alt="Python" height="16"> Geostatistics in Python, started as a reimplementation of GSLIB. MIT.
- [GSTools](https://github.com/GeoStat-Framework/GSTools) - <img src="assets/icons/python.svg" alt="Python" height="16"> Variograms, kriging and random field simulation. LGPL-3.0.
- [PyKrige](https://github.com/GeoStat-Framework/PyKrige) - <img src="assets/icons/python.svg" alt="Python" height="16"> Ordinary and universal kriging in 2D and 3D. BSD-3-Clause.
- [scikit-gstat](https://github.com/mmaelicke/scikit-gstat) - <img src="assets/icons/python.svg" alt="Python" height="16"> Variogram estimation and modelling. MIT.
- [GStatSim](https://github.com/GatorGlaciology/GStatSim) - <img src="assets/icons/python.svg" alt="Python" height="16"> Sequential Gaussian simulation and kriging. MIT.
- [pyinterpolate](https://github.com/DataverseLabs/pyinterpolate) - <img src="assets/icons/python.svg" alt="Python" height="16"> Kriging, Poisson kriging and variogram analysis. BSD-3-Clause.
- [GeoStats.jl](https://github.com/JuliaEarth/GeoStats.jl) - <img src="assets/icons/julia.svg" alt="Julia" height="16"> Geostatistical estimation and simulation in Julia, with variography, kriging and geostatistical learning. MIT.

## Geochemistry

How the methods work: [portable XRF](https://xplorahub.com/methods/portable-xrf) and [fire assay](https://xplorahub.com/methods/fire-assay).

- [pyrolite](https://github.com/morganjwilliams/pyrolite) - <img src="assets/icons/python.svg" alt="Python" height="16"> Processing, normalisation and plotting of geochemical data. MIT.
- [Geochemistry QAQC](https://github.com/GeoscienceAustralia/Geochemistry) - <img src="assets/icons/python.svg" alt="Python" height="16"> Geoscience Australia's script for checking standards and duplicates in geochemical data. Apache-2.0.
- [GeoCluster Research Harness](https://github.com/EigenformAI/geocluster-research-harness) - <img src="assets/icons/javascript.svg" alt="JavaScript" height="16"> <img src="assets/icons/python.svg" alt="Python" height="16"> Research agent in a Docker image, with a bundled geological MCP server, that cleans assay tables, clusters geochemistry, ranks anomalies and answers questions from technical reports, using your own model provider. Apache-2.0. [XploraHub page](https://xplorahub.com/products/geocluster-research-harness-eigenform).

## Remote sensing

- [hylite](https://github.com/hifexplo/hylite) - <img src="assets/icons/python.svg" alt="Python" height="16"> Hyperspectral data for geology, including drill-core, outcrop and airborne scans. MIT.
- [EnMAP-Box](https://github.com/EnMAP-Box/enmap-box) - <img src="assets/icons/python.svg" alt="Python" height="16"> QGIS plugin for processing and analysing hyperspectral imagery. GPL-3.0.
- [Spectral Python (SPy)](https://github.com/spectralpython/spectral) - <img src="assets/icons/python.svg" alt="Python" height="16"> Reading, processing and classifying hyperspectral imagery. MIT.

## Prospectivity mapping and machine learning

Background: [AI in mining](https://xplorahub.com/guides/ai-in-mining).

- [EIS Toolkit](https://github.com/GispoCoding/eis_toolkit) - <img src="assets/icons/python.svg" alt="Python" height="16"> Mineral prospectivity mapping library from the EU Exploration Information System project. EUPL-1.2.
- [uncover-ml](https://github.com/GeoscienceAustralia/uncover-ml) - <img src="assets/icons/python.svg" alt="Python" height="16"> Machine learning for geoscience mapping, from Geoscience Australia's UNCOVER programme. Apache-2.0.
- [pulearn](https://github.com/pulearn/pulearn) - <img src="assets/icons/python.svg" alt="Python" height="16"> Positive-unlabelled learning, suited to prospectivity where only known deposits are labelled. BSD-3-Clause.
- [elapid](https://github.com/earth-chris/elapid) - <img src="assets/icons/python.svg" alt="Python" height="16"> MaxEnt and other presence-only models, used for prospectivity as well as species mapping. MIT.
- [GPlates](https://github.com/GPlates/GPlates) - <img src="assets/icons/cplusplus.svg" alt="C++" height="16"> <img src="assets/icons/python.svg" alt="Python" height="16"> Desktop app and Python package (pyGPlates) for plate tectonic reconstructions, the base of spatio-temporal prospectivity models. GPL-2.0.
- [GPlately](https://github.com/GPlates/gplately) - <img src="assets/icons/python.svg" alt="Python" height="16"> Reconstructs points, lines and rasters through deep time and queries plate kinematics, such as subduction rates, on top of pyGPlates. GPL-2.0.
- [STAMP PNG](https://github.com/EarthByte/STAMP_PNG) - <img src="assets/icons/jupyter.svg" alt="Jupyter" height="16"> Spatio-temporal prospectivity modelling of porphyry systems in Papua New Guinea and the Solomon Islands, from EarthByte. Apache-2.0.
- [Porphyry prospectivity, Americas](https://github.com/EarthByte/porphyry-prospectivity-americas) - <img src="assets/icons/jupyter.svg" alt="Jupyter" height="16"> Spatio-temporal copper prospectivity in the American Cordillera, using positive-unlabelled learning on plate-model data, from EarthByte. Apache-2.0.
- [MPM Lachlan Porphyry](https://github.com/EarthByte/MPM_Lachlan_Porphyry) - <img src="assets/icons/jupyter.svg" alt="Jupyter" height="16"> Machine-learning prospectivity for Cu-Au porphyry mineralisation in the Lachlan Orogen, New South Wales, from EarthByte. MIT.

## Open data

Government geoscience portals, where most exploration data starts. For each portal, its licence and what to watch out for, see Geoscience data portals under Related lists below; for datasets in more depth, Awesome Mining Data.

- [Geoscience Australia Portal](https://portal.ga.gov.au) - National geology, geophysics and mineral deposit data for Australia.
- [GSWA Data and Software Centre](https://dasc.dmirs.wa.gov.au) - Western Australian geological maps, geophysics and datasets to download.
- [SARIG](https://map.sarig.sa.gov.au) - South Australian geology, drillholes, geophysics and mineral exploration data.
- [USGS Mineral Resources Data](https://mrdata.usgs.gov) - US mineral deposits, geochemistry and geophysics.
- [Canada Geophysical Data Repository](https://geophysical-data.canada.ca) - Airborne and ground geophysical surveys across Canada.
- [BGS OpenGeoscience](https://www.bgs.ac.uk/geological-data/opengeoscience/) - UK geological maps, boreholes and data from the British Geological Survey.
- [Macrostrat](https://github.com/UW-Macrostrat/macrostrat) - <img src="assets/icons/python.svg" alt="Python" height="16"> Platform for integrating geological maps, stratigraphy and literature. Apache-2.0.

## Drones, photogrammetry and point clouds

- [OpenDroneMap](https://github.com/OpenDroneMap/ODM) - <img src="assets/icons/python.svg" alt="Python" height="16"> Turns drone photos into maps, point clouds and 3D models of outcrops and sites. AGPL-3.0.
- [WebODM](https://github.com/WebODM/WebODM) - <img src="assets/icons/python.svg" alt="Python" height="16"> Browser interface for OpenDroneMap. AGPL-3.0.
- [CloudCompare](https://github.com/CloudCompare/CloudCompare) - <img src="assets/icons/cplusplus.svg" alt="C++" height="16"> Editing and analysis of point clouds and meshes, used for outcrop and lidar work. GPL-2.0.
- [PDAL](https://github.com/PDAL/PDAL) - <img src="assets/icons/cplusplus.svg" alt="C++" height="16"> Scripted processing of lidar and other point-cloud data. BSD-3-Clause.

## GIS and 3D visualisation

- [QGIS](https://github.com/qgis/QGIS) - <img src="assets/icons/cplusplus.svg" alt="C++" height="16"> <img src="assets/icons/python.svg" alt="Python" height="16"> Desktop GIS for maps, tenements and survey data. GPL-2.0.
- [GRASS](https://github.com/OSGeo/grass) - <img src="assets/icons/c.svg" alt="C" height="16"> <img src="assets/icons/python.svg" alt="Python" height="16"> Geospatial processing engine for large rasters and vectors, with 3D voxel tools. GPL-2.0-or-later.
- [GeoPandas](https://github.com/geopandas/geopandas) - <img src="assets/icons/python.svg" alt="Python" height="16"> Vector geospatial data in Python. BSD-3-Clause.
- [Rasterio](https://github.com/rasterio/rasterio) - <img src="assets/icons/python.svg" alt="Python" height="16"> Reading and writing raster data such as grids and imagery. BSD-3-Clause.
- [rioxarray](https://github.com/vylor/rioxarray) - <img src="assets/icons/python.svg" alt="Python" height="16"> Rasterio for xarray, for gridded survey data with coordinates. Apache-2.0.
- [PyGMT](https://github.com/GenericMappingTools/pygmt) - <img src="assets/icons/python.svg" alt="Python" height="16"> Publication-quality maps and figures with the Generic Mapping Tools. BSD-3-Clause.
- [PyVista](https://github.com/pyvista/pyvista) - <img src="assets/icons/python.svg" alt="Python" height="16"> 3D visualisation and mesh analysis, used by several tools above. MIT.
- [RustGIS](https://github.com/opengeos/RustGIS) - <img src="assets/icons/rust.svg" alt="Rust" height="16"> Fast desktop and browser GIS in pure Rust, with over 1,000 terrain, hydrology, lidar and remote sensing tools. Apache-2.0.
- [Vease](https://github.com/Geode-solutions/Vease) - <img src="assets/icons/typescript.svg" alt="TypeScript" height="16"> Desktop and browser viewer for subsurface meshes and geological models, built on OpenGeode and VTK. LGPL-2.1.

## Related lists

- [Awesome Mining](https://github.com/XploraHub/awesome-mining) - Open-source software for working mines, from mine planning and geotechnics to processing, tailings and closure.
- [Geoscience data portals](https://github.com/XploraHub/geoscience-data-portals) - Government geoscience data portals for exploration, with what each holds, its licence, what to watch out for and QGIS connection files.
- [Awesome Open Geoscience](https://github.com/softwareunderground/awesome-open-geoscience) - Open-source geoscience software across every field.
- [Mineral exploration machine learning](https://github.com/RichardScottOZ/mineral-exploration-machine-learning) - Papers, code and data for machine learning in mineral exploration.
- [Awesome Mining Data](https://github.com/Arpeggeo/awesome-mining-data) - Open datasets for the mining industry.
- [Awesome Mining Band Ratio](https://github.com/rodreras/awesome-mining-band-ratio) - Band ratios and mineral spectra for exploration.

## No longer maintained

Good tools that have had no updates for 18 months or more. They may not run on current versions of their dependencies, but the code and methods are still worth reading. Each is filed under the section it came from, and moves back there when it is updated again.

<details>
<summary><b>Geological modelling and structural geology</b> (1)</summary>

- [GeoINR](https://github.com/MichaelHillier/GeoINR) - <img src="assets/icons/python.svg" alt="Python" height="16"> Implicit neural representations for 3D structural geological modelling, from the Geological Survey of Canada and RWTH Aachen. MIT. Last updated 2023.

</details>

<details>
<summary><b>Drillholes and logging</b> (2)</summary>

- [dh2loop](https://github.com/Loop3D/dh2loop) - <img src="assets/icons/python.svg" alt="Python" height="16"> Extracts and standardises drillhole lithology for 3D modelling, from Loop3D. MIT. Last updated 2023.
- [DrillDown](https://github.com/cardinalgeo/drilldown) - <img src="assets/icons/python.svg" alt="Python" height="16"> Interactive 3D views and analysis of drillhole and ore deposit data from a notebook. MIT. Last updated 2024.

</details>

<details>
<summary><b>Geochemistry</b> (1)</summary>

- [geochemical_anomaly_detection](https://github.com/MinersAI/geochemical_anomaly_detection) - <img src="assets/icons/python.svg" alt="Python" height="16"> Notebooks comparing methods for multivariate geochemical outlier detection. MIT. Last updated 2025.

</details>

<details>
<summary><b>Prospectivity mapping and machine learning</b> (4)</summary>

- [3DMPM](https://github.com/ChengYeung1222/3DMPM) - <img src="assets/icons/cplusplus.svg" alt="C++" height="16"> 3D prospectivity from 3D geological models with convolutional neural networks. MIT. Last updated 2023.
- [MPM Gawler](https://github.com/EarthByte/MPM_Gawler) - <img src="assets/icons/jupyter.svg" alt="Jupyter" height="16"> Prospectivity workflow for critical minerals in the Gawler Craton, from EarthByte. GPL-3.0. Last updated 2024.
- [MPM Curnamona REE](https://github.com/EarthByte/MPM_Geochemistry_Curnamona_REE) - <img src="assets/icons/jupyter.svg" alt="Jupyter" height="16"> High-resolution REE prospectivity from geochemical features, from EarthByte. GPL-3.0. Last updated 2024.
- [MPM Lachlan Laterite](https://github.com/EarthByte/MPM_Lachlan_Laterite) - <img src="assets/icons/jupyter.svg" alt="Jupyter" height="16"> Prospectivity workflow for lateritic nickel-cobalt in the Lachlan Orogen, from EarthByte. GPL-3.0. Last updated 2024.

</details>

## Contributing

To add a tool, open a pull request with one line in the right section. Tools listed on XploraHub carry a link to their XploraHub page after the licence. See [CONTRIBUTING.md](CONTRIBUTING.md) for the rules. Everyone taking part agrees to the [code of conduct](CODE_OF_CONDUCT.md).

The list is CC0. The icons, the code of conduct and the XploraHub name and banner have their own terms, set out in [NOTICE.md](NOTICE.md).
