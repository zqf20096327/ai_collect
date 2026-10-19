# Awesome Geospatial   [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

Long list of geospatial analysis tools. Geospatial analysis, or just spatial analysis, is an approach to applying statistical analysis and other analytic techniques to data which has a geographical or spatial aspect.

![427672_2794027726746_176065793_n](https://user-images.githubusercontent.com/7756611/48104109-2f465b80-e219-11e8-81bb-f6066e6a1be8.jpg)

- [Awesome Geospatial   ](#awesome-geospatial---)
  - [Database](#database)
  - [Image Classification \& DIP Software](#image-classification--dip-software)
  - [Geographic Information System](#geographic-information-system)
  - [Web Map Development](#web-map-development)
  - [Web Map Server](#web-map-server)
  - [Radar](#radar)
  - [Lidar](#lidar)
  - [3D Application](#3d-application)
  - [Geographic Data Mining](#geographic-data-mining)
  - [GNSS/INS Post Processing](#gnssins-post-processing)
  - [Atmospheric Correction](#atmospheric-correction)
  - [Agent-based Modeling](#agent-based-modeling)
  - [Landscape Metrics](#landscape-metrics)
  - [Landscape Modelling](#landscape-modelling)
  - [Spatial Optimization](#spatial-optimization)
  - [Libraries](#libraries)
  - [PaaS - Platform as a Service](#paas---platform-as-a-service)
  - [SaaS - Software as a Service](#saas---software-as-a-service)
  - [DaaS - Data as a Service](#daas---data-as-a-service)
  - [Google Earth Engine](#google-earth-engine)
  - [Deep Learning](#deep-learning)
  - [MCP Servers](#mcp-servers)
  - [Agent Skills](#agent-skills)
  - [C](#c)
  - [C++](#c-1)
  - [C Sharp](#c-sharp)
  - [Clojure](#clojure)
  - [Crystal](#crystal)
  - [CSS](#css)
  - [Dart](#dart)
  - [Delphi](#delphi)
  - [Elixir](#elixir)
  - [Fortran](#fortran)
  - [Go](#go)
  - [Groovy](#groovy)
  - [Haskell](#haskell)
  - [IDL](#idl)
  - [Java](#java)
  - [JavaScript](#javascript)
  - [Julia](#julia)
  - [Kotlin](#kotlin)
  - [Lisp](#lisp)
  - [Lua](#lua)
  - [MATLAB](#matlab)
  - [Nim](#nim)
  - [Perl](#perl)
  - [Python](#python)
  - [PHP](#php)
  - [R](#r)
  - [Ruby](#ruby)
  - [Rust](#rust)
  - [Scala](#scala)
  - [Swift](#swift)
  - [Mobile Development](#mobile-development)
  - [Geospatial Big Data](#geospatial-big-data)
  - [Visualization](#visualization)
  - [Tools](#tools)
  - [Cheat sheets](#cheat-sheets)
  - [Data Sources](#data-sources)
  - [Resources](#resources)
    - [Icons](#icons)
    - [Color Advice](#color-advice)
  - [Free and Open Source Books](#free-and-open-source-books)
  - [Conferences](#conferences)
  - [Podcasts](#podcasts)
  - [References and other awesome lists](#references-and-other-awesome-lists)

- - -

## Database

* [3D CityDB](http://www.3dcitydb.org/) - A free 3D geo database to store, represent, and manage virtual 3D city models on top of a standard spatial relational database. The database model contains semantically rich, hierarchically structured, multi-scale urban objects facilitating complex GIS modeling and analysis tasks, far beyond visualization.
* [Atlas4D](https://github.com/crisbez/atlas4d-base) - Open-source 4D spatiotemporal platform with PostGIS, TimescaleDB, pgvector, and H3 hexagonal indexing.
* [Cloudant](https://cloudant.com/) - IBM noSQL database that supports spatial data (GeoJSON).
* [DB2 Spatial Extender](http://www-03.ibm.com/software/products/en/db2spaext) - Spatial Extender allows you to store, manage, and analyze spatial data in DB2.
* [duckdb-raster](https://github.com/ahuarte47/duckdb-raster) - DuckDB Extension for reading and writing raster files using SQL.
* [GeoCouch](https://github.com/couchbase/geocouch) - GeoCouch is a spatial extension for Couchbase and Apache CouchDB.
* [GeoDesk](https://github.com/clarisma/geodesk) - Fast and storage-efficient spatial database engine for OpenStreetMap data
* [Geopackage](https://www.geopackage.org/) - SQLite spatial extension. More powerful than its older brother Spatialite.
* [H2GIS](https://github.com/orbisgis/h2gis) - A spatial extension of the H2 database.
* [Hastings](https://github.com/cloudant-labs/hastings) - GeoSpatial Search for CouchDB 2
* [Informix Spatial](https://www.ibm.com/docs/en/informix-servers/14.10?topic=guide-getting-started-spatial-data) - Informix spatial extension.
* [Microsoft SQL Server](https://docs.microsoft.com/en-us/sql/relational-databases/spatial/spatial-data-sql-server) - Microsoft SQL/SQL Azure spatial features. All the spatial functionality is also available as a .NET library (can be downloaded using nuget)
* [MobilityDB](https://github.com/ULB-CoDE-WIT/MobilityDB) - An extension to the Postgres database which adds support for temporal and spatio-temporal objects
* [MongoDB](https://www.mongodb.com/) - Also supports GeoJSON and spatial indexes.
* [MySql Spatial](https://dev.mysql.com/doc/refman/8.0/en/spatial-analysis-functions.html) - MySql spatial extension.
* [Neo4j Spatial](https://github.com/neo4j-contrib/spatial) - Library of spatial utilities for Neo4j.
* [Oracle Spatial](http://www.oracle.com/us/products/database/options/spatial/overview/index.html) - Oracle database spatial extension.
* [OrientDB](https://github.com/orientechnologies/orientdb) - OrientDB is an Open Source Multi-Model NoSQL DBMS with the support of Native Graphs, Documents Full-Text, Reactivity, Geo-Spatial and Object Oriented concepts.
* [PgRouting](https://pgrouting.org/) - pgRouting extends the PostGIS / PostgreSQL geospatial database to provide geospatial routing functionality.
* [PointCloud](https://github.com/pgpointcloud/pointcloud) - A PostgreSQL extension for storing point cloud (LIDAR) data.
* [PostGEESE](https://duckdb.org/2023/04/28/spatial.html) - A spatial extension for DuckDB.
* [PostGIS Vector Tile Utils](https://github.com/mapbox/postgis-vt-util) - A set of PostgreSQL functions that are useful when creating vector tile sources.
* [PostGIS](http://postgis.net/) - PostgreSql spatial extension.
* [Rasdaman](http://www.rasdaman.org/) - Array database that allows storing and querying massive multi-dimensional arrays, such as sensor, image, simulation, and statistics data appearing in domains like earth, space, and life science.
* [SciDB](http://www.paradigm4.com/) - Array database designed for multidimensional data management and analytics common to scientific, geospatial, financial, and industrial applications.
* [Spatialite](http://www.gaia-gis.it/gaia-sins/) - SQLite spatial extension.
* [Teradata Geospatial Feature](https://docs.teradata.com/r/Teradata-VantageTM-Geospatial-Data-Types/March-2019/Geospatial-Data/Geospatial-Information) - Teradata spatial extension for DW and BI.
* [Tile38](https://github.com/tidwall/tile38) - Tile38 is a geospatial database, spatial index, and realtime geofence.
* [TileDB](https://github.com/TileDB-Inc/TileDB) - TileDB is a powerful engine for storing and accessing dense and sparse multi-dimensional arrays, which can help you model any complex data efficiently.
* [yogrt](https://github.com/Anagraph/yogrt) - A simple templating tool for importing GIS data to PostGIS


## Image Classification & DIP Software

* [ArcMap Raster Edit Suite](https://github.com/haoliangyu/ares) - An ArcMap Addin that enables manual editing of single pixels on raster layer.
* [ContextCapture](https://www.bentley.com/software/contextcapture/) - ContextCapture enables you to automatically generate multi-resolution 3D models at any scale and precision.
* [Correlator3D](https://www.simactive.com/correlator3d-mapping-software-features) - High-end photogrammetry suite.
* [Dinamica EGO](http://csr.ufmg.br/dinamica/) - Dinamica EGO consists of a sophisticated platform for environmental modeling.
* [e-Foto](http://www.efoto.eng.uerj.br/en) - Free and open source digital photogrammetric workstation.
* [eCognition](https://geospatial.trimble.com/products-and-solutions/ecognition) - GEOBIA software.
* [ENVI](https://www.nv5geospatialsoftware.com/Products/ENVI) - Geospatial image processing and classification software.
* [ERDAS](http://www.hexagongeospatial.com/products/producer-suite/erdas-imagine) - Geospatial image processing and classification software.
* [gdal2tilesp](https://github.com/pramsey/gdal2tilesp) - This enhancement to the gdal2tiles.py script includes additional features.
* [Global Mapper](http://www.bluemarblegeo.com/products/global-mapper.php) - Geospatial and remote sensing data analysis.
* [Guidos Toolbox](http://forest.jrc.ec.europa.eu/download/software/guidos/) - Some GDAL functionalities and includes MSPA (Morphological Spatial Pattern Analysis) for connectivity maps.
* [IDL](https://www.nv5geospatialsoftware.com/Products/IDL) - IDL is a programming language used for data analysis and image processing programming.
* [INPHO](https://geospatial.trimble.com/products-and-solutions/trimble-inpho) - INPHO is a Digital Photogrammetry Software.
* [Interimage](https://github.com/nuest/interimage-container) - Open Source GEOBIA software.
* [Matlab](http://www.mathworks.com/products/matlab/) - Multi-paradigm numerical computing environment and fourth-generation programming language.
* [Metashape](https://www.agisoft.com/) - Agisoft Metashape is a stand-alone software product that performs photogrammetric processing of digital images.
* [MultiSpec](https://engineering.purdue.edu/~biehl/MultiSpec/index.html) - A Freeware Multispectral Image Data Analysis System.
* [OSSIM](http://trac.osgeo.org/ossim/) - Suite of geospatial libraries and applications used to process imagery, maps, terrain, and vector data.
* [PCI Geomatica](http://www.pcigeomatics.com/software/geomatica/professional) - Remote sensing software package for image processing
* [RealityCapture](https://www.realitycapture-training.com/) - Photogrammetry software.
* [SNAP](https://step.esa.int/main/download/snap-download/) - SNAP is an open source common architecture for ESA Toolboxes ideal for the exploitation of Earth Observation data.
* [Spring](http://www.dpi.inpe.br/spring/) - GIS and remote sensing image processing system with an object-oriented data model.
* [TerrSet](https://clarklabs.org/terrset/) - TerrSet (formerly IDRISI) is an integrated geographic information system (GIS) and remote sensing software
* [The Sentinel Toolbox](https://step.esa.int/main/toolboxes/) - The Sentinel Toolboxes consists of a collection of processing tools, data product readers and writers and a display and analysis application to process Sentinel data.
* [TIMESAT](http://web.nateko.lu.se/timesat/timesat.asp?cat=0) - TIMESAT is a software package for analysing time-series of satellite sensor data.
* [WebODM](https://www.opendronemap.org/webodm/) - Generate maps, point clouds, DEMs and 3D models from aerial images.


## Geographic Information System

* [Alidade](https://github.com/AysanZ/alidade) - Open-source Web-GIS platform on MapLibre, PostGIS and FastAPI. Vector tiles, COG imagery mosaicking, symbology, 3D terrain and glTF models, and a live asset layer over WebSocket. No API keys.
* [ArcGIS Pro](https://pro.arcgis.com/en/pro-app/) - Fully 64-bit version of ArcGIS with new GUI and 2D/3D integration.
* [ArcGIS](https://www.arcgis.com/features/) - GIS for working with maps and geographic information.
* [AutoCAD Map 3D](http://www.autodesk.com.br/products/autocad-map-3d/overview) - GIS AutoCAD integration.
* [FME Desktop](https://www.safe.com/fme/fme-desktop/) - FME is an integrated collection of Spatial ETL tools for data transformation and data translation.
* [GC2](http://www.mapcentia.com/en/product/) - GC2 is an enterprise platform GIS (open source)
* [GeoDa](http://geodacenter.github.io/) - Spatial data analysis software.
* [Geolibre](https://github.com/opengeos/GeoLibre) - A lightweight, cloud-native GIS platform for visualizing, exploring, and analyzing geospatial data. It runs in the web browser, on the desktop, on mobile, and inside Jupyter notebooks.
* [Geomedia](https://hexagon.com/products/geomedia) - Commercial GIS.
* [GRASS GIS](https://grass.osgeo.org/) - GRASS (Geographic Resources Analysis Support System) is a free and open source GIS.
* [gvSIG](http://www.gvsig.com/en) - Free and open source GIS.
* [ILWIS](http://52north.org/communities/ilwis/ilwis-open) - Integrated Land and Water Information System (ILWIS) is a remote sensing and GIS software.
* [LuciadFusion](http://www.luciad.com/solutions/luciadfusion) - An all-in-one server solution for your data publication workflow and geospatial data management
* [Manifold System](http://www.manifold.net/) - Commercial GIS.
* [Mapbox Studio](https://github.com/mapbox/mapbox-studio-classic) - Desktop application for vector tile driven map design.
* [MapInfo](https://www.geograph.com.br/mapinfo) - Commercial GIS.
* [MapWindow GIS](http://www.mapwindow.org/) - Free and open source desktop geographic information system.
* [MicroImages TNTgis](https://www.microimages.com/) - Commercial GIS.
* [OpenJUMP](http://openjump.org/) - Open source Java GIS.
* [QGIS](http://www.qgis.org/en/site/) - Cross-platform free and open-source desktop geographic information system.
* [SAGA](http://www.saga-gis.org/en/index.html) - SAGA is the abbreviation for System for Automated Geoscientific Analyses.
* [SM Datum](https://smdatum.com/) - Free browser-based GIS toolkit: format conversion (shapefile/KML/GeoJSON/GeoPackage/DXF), vector analysis, CRS reprojection, raster and hydrology tools, survey calculators. No install or signup.
* [Smallworld](https://www.gegridsolutions.com/geospatial/catalog/smallworld_core.htm) - Commercial GIS.
* [TerraMA2](https://github.com/TerraMA2/terrama2) - A free and open source computational platform for early warning systems.
* [Terraview](http://www.obt.inpe.br/OBT/assuntos/projetos/terralib-terraview) - GIS application built using the TerraLib  GIS library.
* [uDig](http://udig.refractions.net/) - A GIS Framework for Eclipse (Java) and also a GIS software.


## Web Map Development

* [angular-azure-maps](https://github.com/Acaisoft/angular-azure-maps) - Angular 6 Azure Maps is a wrapped MS Azure Map on Angular.
* [ArcGIS JS App Generator](https://github.com/odoe/generator-arcgis-js-app) - This is a yeoman generator for ArcGIS API for JavaScript applications.
* [ArcGIS REST JS](https://github.com/Esri/arcgis-rest-js) - Compact, modular JavaScript wrappers for the ArcGIS REST API that run in Node.js and modern browsers.
* [azure-maps-animations](https://github.com/Azure-Samples/azure-maps-animations) - A rich library of animations for use with the Azure Maps Web SDK.
* [azure-maps-fullscreen-control](https://github.com/Azure-Samples/azure-maps-fullscreen-control) - An Azure Maps Web SDK module that provides a control to display the map in fullscreen mode.
* [azure-maps-geolocation-control](https://github.com/Azure-Samples/azure-maps-geolocation-control) - An Azure Maps Web SDK module that provides a control that uses the browser's geolocation API to locate the user on the map.
* [azure-maps-gridded-data-source](https://github.com/Azure-Samples/azure-maps-gridded-data-source) - A module for the Azure Maps Web SDK that provides a data source that clusters data points into cells of a grid area.
* [azure-maps-selection-control](https://github.com/Azure-Samples/azure-maps-selection-control) - An Azure Maps Web SDK module that provides controls for selecting data in a data source using drawing tools or by requesting a route range polygon.
* [azure-maps-services-ui](https://github.com/Azure-Samples/azure-maps-services-ui) - A set of web UI controls that wrap the Azure Maps REST services.
* [azure-maps-swipe-map](https://github.com/Azure-Samples/azure-maps-swipe-map) - A module for the Azure Maps Web SDK that allows swiping between two overlapping maps, ideal for comparing two overlapping data sets.
* [azure-maps-sync-maps](https://github.com/Azure-Samples/azure-maps-sync-maps) - An Azure Maps Web SDK module that synchronizes the cameras of two or more maps.
* [Bertin.js](https://github.com/neocarto/bertin) - A JavaScript library for visualizing geospatial data and make thematic maps for the web.
* [CesiumJS](https://cesium.com/platform/cesiumjs/) - An open-source JavaScript library for world-class 3D globes and maps.
* [CMV - The Configurable Map Viewer](https://github.com/cmv/cmv-app) - CMV is a community-supported open source mapping framework. CMV works with the Esri JavaScript API, ArcGIS Server, ArcGIS Online and more.
* [d3-geo](https://github.com/d3/d3-geo) - A library for creating maps based on D3.js.
* [d3-geo-projection](https://github.com/d3/d3-geo-projection) - Extended geographic projections for d3-geo.
* [d3-geo-voronoi](https://github.com/Fil/d3-geo-voronoi) - Voronoi diagrams and Delaunay triangulation for the sphere.
* [datamaps](https://github.com/markmarkoh/datamaps) - Customizable map visualizations in one file.
* [deck.gl](https://deck.gl) - A WebGL-powered framework for visual exploratory data analysis of large datasets.
* [Flare Cluster Layer](https://github.com/nickcam/FlareClusterLayer) - ArcGIS javascript custom graphics layer. Creates clusters and creates flares for clusters.
* [geojson-vt](https://github.com/mapbox/geojson-vt) - A highly efficient JavaScript library for slicing GeoJSON data into vector tiles on the fly.
* [GeoNode](http://geonode.org/) - A web-based application and platform for developing geospatial information systems (GIS) and for deploying spatial data infrastructures (SDI).
* [globe.gl](https://github.com/vasturiano/globe.gl) - This library is a convenience wrapper around the three-globe plugin, using ThreeJS/WebGL for 3D rendering.
* [Google Maps API Polyline String Decoder](https://github.com/mgd722/decode-google-maps-polyline) - Function that will convert encoded polyline strings (as returned by the Google Maps API) into a list of lat/lon pairs.
* [gridviz](https://github.com/eurostat/gridviz) - A package for visualizing gridded data.
* [HERE maps API](https://developer.here.com/develop/javascript-api) - Build web applications with feature-rich and customizable HERE maps.
* [Honua SDK JS](https://github.com/honua-io/honua-sdk-js) - TypeScript geospatial client for ArcGIS/Esri GeoServices, OGC API, WFS, WMS/WMTS, STAC, OData, and GeoParquet with a MapLibre runtime and an ArcGIS migration codemod. [Example](https://honua-io.github.io/honua-sdk-js/guides/quickstart.html)
* [jVectorMap](https://jvectormap.com/) - jVectorMap is a vector-based, cross-browser and cross-platform component for interactive geography-related data visualization on the web. It provides numerious features like smooth zooming and panning, fully-customizable styling, markers, labels and tooltips.
* [L7](https://github.com/antvis/L7) - Large-scale WebGL-powered Geospatial Data Visualization By Ant Financial
* [Leaflet](http://leafletjs.com/) - Open-Source JavaScript Library for Mobile-Friendly Interactive Maps.
* [Leaflet.MapboxVectorTile](https://github.com/SpatialServer/Leaflet.MapboxVectorTile) - A Leaflet Plugin that renders Mapbox Vector Tiles on HTML5 Canvas.
* [LuciadRIA](http://www.luciad.com/solutions/luciadria) - A JavaScript library for 3D globes and maps, with support for military symbology and desktop-like performance
* [Map Forecast API](https://github.com/windycom/API) - Simple-to-use library based on Leaflet 1.4.x. It allows you to show wind maps.
* [Mapbox GL JS](https://www.mapbox.com/mapbox-gl-js/api/) - Mapbox GL JS is a JavaScript library that uses WebGL to render interactive maps from vector tiles and Mapbox styles.
* [MapLibre GL](https://github.com/maplibre/maplibre-gl-js) - Is a community led fork derived from Mapbox GL JS prior to their switch to a non-OSS license.
* [MapLineDraw](https://github.com/patrsc/MapLineDraw) - An open source web application for drawing smooth curves (splines) on a map, suitable for sketching or measuring railway lines or roads.
* [MapTalks.js](https://github.com/maptalks/maptalks.js) - An open-source JavaScript library for integrated 2D/3D maps.
* [Mapzen Tangram](https://github.com/tangrams/tangram) - JavaScript library for rendering 2D & 3D maps live in a web browser with WebGL, supports MVT, GeoJSON, TopoJSON.
* [Ol-ext](https://viglino.github.io/ol-ext/) - Cool extensions for OpenLayers (ol) - animated clusters, CSS popup, Font Awesome symbol renderer, charts for statistical map (pie/bar), layer switcher, wikipedia layer, animations, canvas filters.
* [OpenGlobus](https://www.openglobus.org/) - A javascript library designed to display interactive 3d maps and planets with map tiles, imagery and vector data, markers and 3d objects. It uses the WebGL technology, open source and completely free.
* [OpenLayers](http://openlayers.org/) - High-performance, feature-packed library for creating interactive maps on the web.
* [Oskari](https://oskari.org/) - Framework for easily building multipurpose web mapping applications utilizing distributed Spatial Data Infrastructures like INSPIRE.
* [Pharos AI](https://conflicts.app) - Open-source real-time intelligence dashboard for geopolitical conflict tracking with interactive geospatial visualization.
* [react-azure-maps](https://github.com/WiredSolutions/react-azure-maps) - React Wrapper for azure-maps-control.
* [react-simple-maps](https://github.com/zcreativelabs/react-simple-maps) - An SVG mapping component library for React, built on top of d3-geo.
* [TerriaJS](https://github.com/TerriaJS/terriajs) - A library for building rich, web-based geospatial data explorers.
* [titiler](https://github.com/developmentseed/titiler) - A dynamic Web Map tile server.
* [v-mapbox](https://github.com/geospoc/v-mapbox) - Vue.js wrapper for `mapbox-gl-js`.
* [VectorAtlas](https://vectoratlas.menelabs.com/) - Free, 80KB SVG world map with one path per country, id-keyed by ISO 3166-1 alpha-2 code, ready for choropleths.
* [vue-azure-maps](https://github.com/rickyruiz/vue-azure-maps) - Integrate Azure Maps in your Vue application.
* [Wrld.js](https://github.com/wrld3d/wrld.js/) - Animated 3D city maps based on Leaflet.

## Web Map Server

* [52North WPS](http://52north.org/communities/geoprocessing/wps/index.html) - The 52°North Web Processing Service (WPS) enables the deployment of geo-processes on the web in a standardized way. It features a pluggable architecture for processes and data encodings. The implementation is based on the current OpenGIS specification: 05-007r7. Its focus was the creation of an extensible framework to provide algorithms for generalization on the web.
* [Baremaps](https://baremaps.apache.org/) - An open source pipeline for producing Mapbox vector tiles from OpenStreetMap with Postgis and Java.
* [Deegree](http://www.deegree.org/) - Open source software for spatial data infrastructures and the geospatial web. Deegree offers components for geospatial data management, including data access, visualization, discovery and security. Open standards are at the heart of Deegree. It supports WMS, WFS for Catalogue Service, WCS, WPS, WMTS.
* [GeoLens](https://github.com/geolens-io/geolens) - Self-hosted geospatial catalog and map builder on PostGIS; upload data, get vector tiles, style and share maps. Implements OGC API - Features/Records, STAC and DCAT.
* [Geoserver](http://geoserver.org/) - WMS written in Java and relies on GeoTools. Allows users to share and edit geospatial data.
* [GeoTrellis Server](https://github.com/geotrellis/geotrellis-server) - Tools for building raster processing and display services. It supports WMS, WCS, WMTS and can use individual rasters, STAC Catalogs (through the STAC API service) and GeoTrellis Layers as input raster sources.
* [MapGuide](https://mapguide.osgeo.org/) - Runs on Linux or Windows, supports Apache and IIS web servers, and has APIs (PHP, .NET, Java, and JavaScript) for application development.
* [MapProxy](http://mapproxy.org/) - An open source tile server proxy for geospatial data (WMS-C, TMS, WMTS, KML SuperOverlays). It caches, accelerates and transforms data from existing map services and serves any desktop or web GIS client.
* [Mapserver](http://mapserver.org/) - WMS written in C.
* [MapTiler Server](https://www.maptiler.com/server/) - Map server for self-hosting. Publish interactive maps to get map services from your own server or laptop.
* [Nanocubes](https://github.com/laurolins/nanocube) - An in-memory data structure for spatiotemporal data cubes.
* [PGRestAPI](https://github.com/spatialdev/PGRestAPI) - Node.js REST API for PostGres Spatial Entities. AKA: SpatialServer.
* [Planisfy](https://github.com/giseity/planisfy) - Open-source geospatial API platform for MapLibre styles, vector tiles, routing, geocoding, API keys, usage tracking, jobs, and map operations.
* [Terracotta](https://github.com/DHI-GRAS/terracotta) - A light-weight, versatile XYZ tile server. MIT-licensed, pure Python, serving Cloud-Optimized GeoTIFF (COG).
* [THREDDS](https://github.com/Unidata/thredds) - The THREDDS Data Server (TDS) is a web server that provides metadata and data access for scientific data sets, using OPeNDAP, OGC WCS, HTTP, and other data access protocols.
* [utilery](https://github.com/tilery/utilery) - Micro vector tile manufacturing from PostGIS.
* [Zoo Project WPS](http://www.zoo-project.org/) - A WPS (Web Processing Service) implementation written in C, Python and JavaScript. It is an open source platform which implements the WPS 1.0.0 and WPS 2.0.0 standards edited by the Open Geospatial Consortium (OGC). It provides a developer-friendly framework for creating and chaining WPS compliant Web Services.


## Radar

* [GAMMA](https://www.gamma-rs.ch/software) - Allows processing of SAR, interferometric SAR (InSAR) and differential interferometric SAR (DInSAR).
* [GMT5SAR](https://topex.ucsd.edu/gmtsar/) - InSAR processing system based on GMT.
* [InSARHub](https://github.com/jldz9/InSARHub) - A modular Python framework for end to end InSAR and time-series processing with GUI support.
* [LiCSBAS](https://github.com/yumorishita/LiCSBAS) - LiCSBAS is an open-source package in Python and bash to carry out InSAR time series analysis using LiCSAR products.
* [NANSAT](https://github.com/nansencenter/nansat) - Nansat is a scientist friendly Python toolbox for processing 2D satellite earth observation data.
* [PolSARpro](https://earth.esa.int/web/polsarpro) - Open source radar image data processing software.
* [PyRate](https://github.com/GeoscienceAustralia/PyRate) - A Python tool for estimating velocity and time-series from Interferometric Synthetic Aperture Radar (InSAR) data.
* [pyroSAR](https://github.com/johntruckenbrodt/pyroSAR) - A Python Framework for Large-Scale SAR Satellite Data Processing.
* [PySAR](https://github.com/insarlab/PySAR) - InSAR time series analysis in Python.
* [SARbian](https://eo-college.org/sarbian/) - Free and open SAR operating system (based on Debian Linux).
* [Sarmap](https://www.sarmap.ch/index.php/software/sarscape/) - Synthetic Aperture Radar processing software.
* [SARPROZ](https://www.sarproz.com/) - Implements a wide range of Synthetic Aperture Radar (SAR), Interferometric SAR (InSAR) and Multi-Temporal InSAR processing techniques.
* [Sentinel Toolboxes](https://step.esa.int/main/toolboxes/) - Free open source toolboxes for the scientific exploitation of the Sentinel missions.


## Lidar

* [CloudCompare](https://www.danielgm.net/cc/) - 3D point cloud processing software.
* [DielmoOpenLidar](http://www.dielmo.com/eng/ficha-tecnologia-software.php?prod=21) - Open source software based in gvSIG for the management of LiDAR data.
* [displaz](https://github.com/c42f/displaz) - A hackable lidar viewer.
* [Entwine](https://github.com/connormanning/entwine) - Point cloud indexing for massive datasets.
* [FullAnalyze](https://code.google.com/archive/p/fullanalyze/) - Handling, visualizing and processing lidar data (3D point clouds and waveforms).
* [Fusion](http://forsys.cfr.washington.edu/fusion/fusionlatest.html) - CLI/GUI Lidar software.
* [Global Mapper Lidar Module](https://www.bluemarblegeo.com/products/global-mapper-lidar.php) - Lidar module for Global Mapper.
* [greyhound](https://github.com/hobu/greyhound) - A point cloud streaming framework for dynamic web services and native applications.
* [Laspy](http://laspy.readthedocs.io/en/latest/) - Laspy is a python library for reading, modifying, and creating .LAS LIDAR files.
* [lasrs-cpp](https://github.com/bloom256/lasrs-cpp) - C++20 and C library for reading and writing LAS, LAZ and COPC with parallel LAZ decoding, built on the Rust crates las-rs and laz-rs.
* [LAStools](https://rapidlasso.de) - A collection of highly-efficient, scriptable tools with multi-core batching that process LAS, compressed LAZ, Terrasolid BIN, .shp, and ASCII.
* [LASzip](https://laszip.org/) - Quickly turns bulky LAS files into compact LAZ files without information loss.
* [libLAS](https://liblas.org/) - libLAS is a C/C++ library for reading and writing the very common LAS LiDAR format.
* [lidar](https://github.com/jblindsay/lidar) - A Crystal language library for reading and writing LiDAR data in LAS format.
* [lidario](https://github.com/jblindsay/lidario) - A small Go library for reading and writing LiDAR (LAS) files.
* [lidR](https://github.com/Jean-Romain/lidR) - R package for airborne LiDAR data manipulation and visualisation for forestry application.
* [MCC-LIDAR](https://sourceforge.net/projects/mcclidar/) - Multiscale Curvature Classification for LIDAR Data.
* [PDAL](https://pdal.io/) - PDAL is a C++ BSD library for translating and manipulating point cloud data.
* [plas.io](https://github.com/verma/plasio) - WebGL point cloud rendering.
* [potree](https://github.com/potree/potree/) - Potree is a free open-source WebGL based point cloud renderer for large point clouds. PotreeConverter provides all files to view your point cloud with only a basic webserver running.
* [pyGEDI](https://github.com/EduinHSERNA/pyGEDI) - pyGEDI provides a high performance, lower cognitive load, and cleaner and more transparent code for data extraction, analysis, processing, and visualization of GEDI's products.
* [PyLAS](https://pypi.python.org/pypi/PyLAS) - A python library for reading and writing LAS files.
* [Quick Terrain Modeler](http://appliedimagery.com/) - Proprietary LiDAR exploitation software by Applied Imagery.
* [rGEDI](https://github.com/carlos-alberto-silva/rGEDI) - An R Package for NASA's Global Ecosystem Dynamics Investigation (GEDI) Data Visualization and Processing.
* [The Point Cloud Library - PCL](https://pointclouds.org/) - Standalone, large scale, open project for 2D/3D image and point cloud processing.
* [TopoDOT](https://new.certainty3d.com/) - Proprietary software for extracting topography, 3D models, GIS Assets, and more from point cloud data.
* [Treetop](https://github.com/carlos-alberto-silva/weblidar-treetop) - A Shiny-based Application for Extracting Forest Information from LiDAR data.


## 3D Application

* [3dcitybuilder](https://github.com/arthurRuf/3dcitybuilder) - QGIS Plugin that generates 3D Models of Urban Areas.
* [3dfier](https://github.com/tudelft3d/3dfier) - The open-source tool for creation of 3D models.
* [ArcGIS Earth](http://www.esri.com/software/arcgis-earth) - Display data, sketch placemarks, measure distances and areas, and add annotations at any part of the world
* [CityEngine](http://www.esri.com/software/cityengine/) - Transform 2D GIS Data into Smart 3D City Models
* [erzberg](https://github.com/sorny/erzberg) - MIT-licensed browser tool that turns GeoTIFFs and DEMs into topographic line art in 41 draw modes, with OpenStreetMap overlays and SVG, STL and PNG export.
* [Google Earth](http://earth.google.com/) - Bringing a earth view for global mapping
* [Lookout](https://github.com/ExtremeAI-Labs/lookout) - Self-hosted 3D situational-awareness console on a CesiumJS globe: live aircraft, ships, satellites, earthquakes and public cameras, MIT licensed.
* [Open3D](http://www.open3d.org/) - Open-source library that supports rapid development of software that deals with 3D data. The Open3D frontend exposes a set of carefully selected data structures and algorithms in both C++ and Python.
* [Planetary Atlas](https://planetatlas.org) - Browser-based 3D globes of 14 worlds built from open NASA, USGS, ESA and JAXA imagery, with the IAU nomenclature and surface mission landing sites
* [Skyline](http://www.skylineglobe.com/SkylineGlobe/corporate/Default.aspx?) - A glimpse into Skyline's cutting-edge 3D geospatial visualization products, and their potential to transform the way your organization makes decisions, shares information and manages its assets
* [World Wind](http://worldwind.arc.nasa.gov/java/) -  Providing features for displaying with geographic data
* [WorldSeed](https://github.com/yz4git/next-gen) - MIT-licensed browser tool that turns open geospatial data into playable, exportable Three.js worlds with terrain-aware roads, GLB, road graphs, spawn points, and versioned JSON Schema.
* [Yapmap](https://yapmap.cc) - Free, voice-controlled 3D globe in the browser: tap to talk and an AI guide flies anywhere, dives into photorealistic 3D terrain, drops pins and narrates each place. Built on MapLibre GL JS and deck.gl.

## Geographic Data Mining

* [GeoDMA](https://sourceforge.net/projects/geodma/) - GeoDMA is a plugin for TerraView software, used for geographical data mining.
* [Weka](http://www.cs.waikato.ac.nz/ml/weka/) - Weka is a collection of machine learning algorithms for data mining tasks written in Java.

## GNSS/INS Post Processing

* [Applanix POSPAC MMS](https://www.applanix.com/products/pospac-mms.htm) - POSPac MMS leverages Global Navigation Satellite Systems (GNSS) and inertial navigation systems (INS) data to generate a source of truth for post-mission trajectories and mapping.
* [Leica Infinity Surveying Software](https://leica-geosystems.com/en-us/products/gnss-systems/software/leica-infinity) - Easily manage and process data from multiple sites and survey teams and from all of your different survey instruments – digital levels, total stations, UAVs, GNSS sensors, and now even scanners.
* [Novatel Waypoint](https://novatel.com/products/waypoint-post-processing-software) - Waypoint software leverages Global Navigation Satellite Systems (GNSS) and inertial navigation systems (INS) data to generate a source of truth for post-mission trajectories and mapping.
* [RTKLIB](https://github.com/tomojitakasu/RTKLIB) - RTKLIB is an open source program package for standard and precise positioning
with GNSS (global navigation satellite system).
* [Trimble Business Center](https://geospatial.trimble.com/en/products/software/trimble-business-center) - Trimble® Business Center (TBC) software enables surveyors to transform field data from GNSS receivers, total stations, laser scanners, mobile mapping systems, drones and more into high-quality, actionable information and client deliverables.


## Atmospheric Correction

* [6S](http://6s.ltdri.org/) - Second Simulation of the Satellite Signal in the Solar Spectrum (6S) open source algorithm.
* [6S_emulator](https://github.com/samsammurphy/6S_emulator) - The 6S emulator is an open-source atmospheric correction tool. It is based on the 6S radiative transfer model but it runs 100x faster with minimal additional error (i.e. < 0.5 %).
* [ACOLITE_MR](https://github.com/acolite/acolite_mr) - Atmospheric correction for aquatic applications of metre-scale satellites.
* [ARCSI](https://github.com/remotesensinginfo/arcsi) - The Atmospheric and Radiometric Correction of Satellite Imagery (ARCSI) software provides a command line tool for the generation of Analysis Ready Data (ARD) optical data including atmospheric correction, cloud masking, topographic correction etc.
* [ATCOR](http://www.atcor.de/) - ERDAS Imagine module.
* [gee-atmcorr-S2](https://github.com/samsammurphy/gee-atmcorr-S2) - Atmospheric correction of Sentinel 2 imagery in Google Earth Engine using Py6S.
* [i.atcorr](https://grass.osgeo.org/grass70/manuals/i.atcorr.html) - GRASS GIS module that performs atmospheric correction using the 6S algorithm.
* [Py6S](https://py6s.readthedocs.io/en/latest/) - Py6S is a interface to the Second Simulation of the Satellite Signal in the Solar Spectrum (6S) atmospheric Radiative Transfer Model through the Python programming language.
* [radiometric_normalization](https://github.com/planetlabs/radiometric_normalization) - Implementation of radiometric normalization workflows.
* [sen2cor](http://step.esa.int/main/third-party-plugins-2/sen2cor/) - is a processor for Sentinel-2 Level 2A product generation and formatting; it performs the atmospheric-, terrain and cirrus correction of Top-Of- Atmosphere Level 1C input data.
* [SIAC](https://github.com/MarcYin/SIAC) - A sensor invariant Atmospheric Correction (SIAC).
* [SIAC_GEE](https://github.com/MarcYin/SIAC_GEE) - SIAC GEE version.


## Agent-based Modeling
* [DMASON](https://github.com/isislab-unisa/dmason) - DMASON is a parallel version of the MASON library for writing and running simulations of Agent based simulation models.
* [MASON](https://cs.gmu.edu/~eclab/projects/mason/) - MASON is a fast discrete-event multiagent simulation library core in Java, designed to be the foundation for large custom-purpose Java simulations, and also to provide more than enough functionality for many lightweight simulation needs. MASON contains both a model library and an optional suite of visualization tools in 2D and 3D.
* [Mesa](https://github.com/projectmesa/mesa) - Mesa is an Apache2 licensed agent-based modeling (or ABM) framework in Python.
* [NetLogo](https://ccl.northwestern.edu/netlogo/) - NetLogo is a multi-agent programmable modeling environment.
* [nlrx](https://github.com/ropensci/nlrx) - Provides tools to setup and execute NetLogo simulations from R.
* [Repast](https://repast.github.io/) - The Repast Suite is a family of advanced, free, and open source agent-based modeling and simulation platforms.
* [SpaDES](https://spades.predictiveecology.org/) - Metapackage for implementing a variety of event-based models, with a focus on spatially explicit models. These include raster-based, event-based, and agent-based models.


## Landscape Metrics
* [Fragstats](https://fragstats.org/) - Spatial Pattern Analysis Program for Categorical Maps.
* [landscapemetrics](https://github.com/r-spatialecology/landscapemetrics) - landscapemetrics is an R package for calculating landscape metrics for categorical landscape patterns in a tidy workflow.
* [LS_METRICS](https://github.com/LEEClab/LS_METRICS) - A tool for calculating landscape connectivity and other ecologically scaled landscape metrics
* [Makurhini](https://github.com/connectscape/Makurhini) - R package for calculating fragmentation and landscape connectivity indices used in conservation planning.
* [nlmpy](https://pypi.org/project/nlmpy/) - A Python package to create neutral landscape models.
* [NLMR](https://github.com/ropensci/NLMR) - R package to simulate neutral landscape models.
* [PyLandStats](https://github.com/martibosch/pylandstats) - An open-source Pythonic library to compute landscape metrics.


## Landscape Modelling
* [GLOBIOM](https://iiasa.ac.at/web/home/research/GLOBIOM/GLOBIOM.html) - Global Biosphere Management Model (GLOBIOM) is used to analyze the competition for land use between agriculture, forestry, and bioenergy, which are the main land-based production sectors.
* [InVEST](https://naturalcapitalproject.stanford.edu/software/invest) - InVEST (Integrated Valuation of Ecosystem Services and Tradeoffs) is a suite of models used to map and value the goods and services from nature that sustain and fulfill human life.


## Spatial Optimization
* [MARXAN](https://marxansolutions.org/) - Marxan is a freely available conservation planning software. It provides decision support to a range of conservation planning problems, including the design of new reserve systems, reporting on the performance of existing reserve systems, and developing multiple-use zoning plans for natural resource management.
* [prioriactions](https://github.com/prioriactions/prioriactions) - The prioriactions R package uses a mixed integer mathematical programming (MIP) approach for building and solving multi-action conservation planning problems, where the goal is to find an optimal combination of management actions that abate threats, in an efficient way while accounting for connectivity.
* [prioritizr](https://github.com/prioritizr/prioritizr) - R package that uses integer linear programming (ILP) techniques to provide a flexible interface for building and solving conservation planning problems.
* [Zonation](http://conservationcorridor.org/corridor-toolbox/programs-and-tools/zonation/) - Zonation produces a hierarchical prioritization of the landscape based on the occurrence levels of biodiversity features in sites (cells) by iteratively removing the least valuable remaining cell while accounting for connectivity and generalized complementarity.


## Libraries

* [GDAL](http://www.gdal.org/) - Geospatial Data Abstraction Library (GDAL) is a translator library for raster and vector geospatial data formats.
* [GEOS](https://trac.osgeo.org/geos/) - Geometry Engine - Open Source, a C++ port of the Java Topology Suite (JTS) that provides spatial predicates and functions, serving as the core engine for libraries like Shapely (Python), sf (R), and spatial databases like PostGIS.
* [GeographicLib](http://geographiclib.sourceforge.net/) - For solving geodesic problems. Implemented in C, C++, Java, Javascript, Fortran, Python and Matlab.
* [Geolib](http://www.geolib.co.uk/) - GeoLib is a fast, efficient, computational geometry library available in C++, C# and Java.
* [H3](https://github.com/uber/h3) - Hexagonal hierarchical geospatial indexing system, written in C with bindings/ports in Python, JavaScript, Java, R, Rust, Go, Swift, and C#.
* [Mapnik](http://mapnik.org/) - C++/Python/Node.js library for map rendering.
* [MDAL](https://github.com/lutraconsulting/MDAL) - Mesh Data Abstraction Library.
* [PDAL](https://pdal.io/) - Point Data Abstraction Library (PDAL) is a C++ library and command-line utility for translating and manipulating point cloud data formats, similar to GDAL for raster/vector data.
* [PROJ](https://proj.org/) - Cartographic Projections library for transforming coordinates between different reference systems, with bindings/ports in almost every language (C, C++, Python, R, Java, JavaScript, Rust, Go).
* [S2 Geometry](https://s2geometry.io/) - Computational geometry and spatial indexing on the sphere, written in C++ with ports/bindings in Go, Java, Python, Rust, and R.
* [Terralib](http://www.terralib.org/) - TerraLib is a GIS classes and functions open source library.


## PaaS - Platform as a Service

* [ArcGIS Platform](https://www.esri.com/en-us/arcgis/products/arcgis-platform/overview) - Esri's PaaS with multiple location services and developer APIs.
* [Google Maps API](https://developers.google.com/maps/) - Google's PaaS (Platform as a Service) for Geocoding or analysis/processing services.
* [Mapbox GL JS](https://www.mapbox.com/mapbox-gl-js/api/) - MapBox WebGL Javascript API.
* [Mapbox.js](https://www.mapbox.com/mapbox.js/api/v2.4.0/) - MapBox Javascript API.
* [Microsoft Bing API](https://www.microsoft.com/en-us/maps) - Microsoft Bing Maps API.
* [OpenStreetMap API](http://wiki.openstreetmap.org/wiki/API_v0.6) - OpenStreetMap API.


## SaaS - Software as a Service

* [Address API](https://gisco-services.ec.europa.eu/addressapi/docs/) - Pan-European address data with geocoding and reverse-geocoding.
* [ArcGIS Online](https://www.arcgis.com/home/) - ArcGIS Online GIS platform for mapping and spatial analysis.
* [ARLAS](https://www.arlas.io/) - ARLAS Exploration is an Open Source software for exploring and analysing Geo BigData.
* [BreezoMeter](https://docs.breezometer.com/api-documentation/introduction/) - Air Quality, Weather, Pollen, and Environmental data.
* [Carto](https://carto.com/) - Cloud computing platform that provides GIS and web mapping tools for display in a web browser.
* [Catastro GPS](https://www.catastrogps.es/) - European cadastral parcel lookup (29 countries plus the Basque and Navarre foral cadastres): reference to GPS, outline, area and land use from official open data, with a free API tier.
* [CoordMap](https://www.coordmap.com/) - Free browser-based geographic toolkit for coordinate lookup, elevation, distance measurement, coordinate conversion, maps, and location data.
* [Country State City API](https://countrystatecity.in/) - Database of city, state, and country data.
* [CSV2GEO](https://csv2geo.com) - Batch geocoder using excel/csv file, text or API as an input and get latitude, longitude and an interactive map as output.
* [Dekart](https://dekart.xyz) - Open-source alternative to CARTO. SQL to interactive map platform that connects BigQuery, Snowflake, and PostGIS. Self-host or cloud.
* [Draw on a Map](https://drawonamap.com/) - Browser-based map annotation and route-planning tool for drawing routes, markers, arrows, and radius circles on OpenStreetMap and sharing them by URL.
* [Fulcrum](http://www.fulcrumapp.com/) - A mobile data collection platform that allows you to build, deploy, & collect field data with your own customizable data collection apps.
* [Geocode.xyz](https://geocode.xyz/) - Reverse geocoding, forward geocoding, and geoparsing API.
* [Geodocs](https://geodocs.io/) - GIS-powered project management platform for construction and infrastructure projects with support for KML, KMZ, Shapefile, and GeoJSON uploads, PostGIS database, MVT vector tiles, dynamic forms, and Mapbox GL JS visualization.
* [GOAT](https://www.plan4better.de/en/goat/) - Open-source WebGIS for spatial analysis in the browser: built-in catalogue of 30,000+ datasets, accessibility analysis (isochrones, public transport quality classes), no-code workflows, dashboards and real-time collaboration. Cloud or self-hosted.
* [GIS Cloud](https://www.giscloud.com/) - Real-time mapping platform for the entire workflow of your organization.
* [GISCO data distribution API](https://gisco-services.ec.europa.eu/distribution/v2/) - European Commission data source for administrative regions and boundaries.
* [GraphHopper Route Optimization API](https://www.graphhopper.com/route-optimization/) - Solves various vehicle routing problems.
* [Honeycomb Maps](https://honeycombmaps.com) - Browser-based enterprise map dashboard software, with real-time filtering and metric calculation.
* [InstaMaps](https://get-instamaps.com) - Location formulas for Google Sheets: geocoding, routing (100-stop Google Maps links), territories and live shareable maps from spreadsheet data.
* [IPGeolocation.io](https://ipgeolocation.io/) - IP geolocation API bundling timezone and currency data in the same response.
* [LatLng](https://www.latlng.work/) - OSM-based geocoding, reverse geocoding, places, static maps, and tile APIs.
* [LYRASENSE](https://lyrasense.com) - Agentic AI platform for satellite data analysis with a notebook environment and Google Earth Engine integration.
* [MapAtlas](https://mapatlas.eu/) - A mapping REST API providing geocoding, directions, route optimization, matrix, isochrone, MVT vector tiles, map matching, and GeoEnrich services using OpenStreetMap and proprietary data.
* [MapBees](https://mapbees.com/) - Browser-based neighborhood analysis on an H3 hex grid, with no GIS install: weighted site-selection scoring, Location Quotient, gap analysis, Getis-Ord Gi* hot spots, Shannon/Simpson diversity, bivariate maps, isochrone territories and Huff market share, built on Overture Maps, OpenStreetMap and national census data. Free tier.
* [Mapbox](https://www.mapbox.com/) - Platform for web map design and manipulation.
* [MapsLinkQuest](https://mapslink.quest/) - Free for up to 25 places per list, no account needed. Converts a shared Google Maps list link into GPX, KML, CSV or GeoJSON waypoints, with no Takeout export. Paid tiers raise the limit.
* [MapTiler Cloud](https://www.maptiler.com/cloud/) - Maps API for web & mobile developers. Customize maps, upload or create own geodata and publish online.
* [Mercator](https://mercator.blue/) - Gridded earth data (weather, ocean, air quality, elevation) as value-encoded Web Mercator tiles, with an open-source MapLibre SDK for colormapped rasters, wind and current streamlines, arrows and contours.
* [Mergin Maps](https://merginmaps.com/) - A mobile data collection open-source platform for field data surveys based on QGIS. Available as service or self-hosted.
* [movebank-api](https://github.com/movebank/movebank-api-doc) - Platform for animal tracking data.
* [MyCarTracks](https://mycartracks.com) - Mainly app-based GPS vehicle tracking and automatic mileage tracking with route history, geofencing, mileage reports, and fleet visibility.
* [NetLoc8](https://netloc8.com) - IP geolocation API with city-level precision and SDKs for Next.js, React, and Go. Free tier included.
* [NMEA Checksum Calculator](https://beomanro.com/tools/net/nmea-checksum/) - Browser-based NMEA 0183 and AIS sentence checksum validator and calculator with batch processing and XOR step visualization.
* [NextGIS](http://nextgis.com/) - A cloud geospatial service that allows you to create web GIS right in the browser.
* [Open Notify](http://open-notify.org/Open-Notify-API/) - ISS location and number of people in space.
* [Open-Meteo](https://open-meteo.com/) - Global weather forecast API.
* [OpenCage Geocoding API](https://geocoder.opencagedata.com/) - An API aggregating multiple open geo datasources (OpenStreetMap and others).
* [OpenMapTiles](https://openmaptiles.com/) - Vector tiles and map services as service, self-hosted or off-line.
* [OpenSky API](https://github.com/openskynetwork/opensky-api) - Retrieve live airspace information.
* [OSM2CDR](https://osm2cdr.com/) - Web service that exports OpenStreetMap data for a drawn area or admin boundary into 62+ vector, CAD, GIS and 3D formats (CDR, DWG, DXF, SVG, Shapefile, GeoJSON, STL, PMTiles), keeping map layers editable.
* [OSRMRoute](https://osrmroute.com) - Hosted routing, distance matrix, isochrones, map-matching and geocoding REST API built on OpenStreetMap/OSRM.
* [Phantom Tide](https://github.com/tg12/phantomtide) - Real-time geospatial intelligence platform for maritime and airspace monitoring, combining vessel tracking, ADS-B flight activity, official notices, environmental context, and satellite detections in a single live map workflow.
* [PixelGust](https://pixelgust.com/) - A web-based geospatial analysis platform providing 30m terrain data, climate risk assessment, NDVI time series, and environmental reports for any location. Free tier and API available.
* [PostalCodes](https://postalcodes.info/api) - Global postal code search, country exports, and address validation data.
* [RainViewer](https://www.rainviewer.com/api.html) - Free weather radar and satellite data API.
* [REST countries](https://restcountries.com/) - Get country information via a RESTful API.
* [SafeStreets](https://safestreets.streetsandcommons.com) - Free address-level walkability and pedestrian-safety analysis, scoring any neighborhood on a 15-minute-city framework using OpenStreetMap and public data.
* [ShowMeOnMap](https://showmeonmap.com) - Natural-language questions to cited interactive maps; live hazard layers, embeds, MCP/WebMCP agent tools.
* [Sunrise and sunset](https://sunrise-sunset.org) - Provides sunset and sunrise times for locations.
* [TomTom](https://developer.tomtom.com/api-explorer-index/documentation/product-information/introduction) - Geocoding, routing, traffic, and more.
* [USGS earthquake data](https://earthquake.usgs.gov/fdsnws/event/1/) - Search earthquake data by various parameters.
* [what3words](https://developer.what3words.com/public-api) - Converts 3-word addresses to coordinates.
* [World Monitor](https://www.worldmonitor.app) - Real-time global intelligence platform aggregating live military flight tracking (ADS-B), AIS vessel monitoring, GPS jamming heatmaps, conflict event overlays, satellite data, and geopolitical risk scores on an interactive 3D globe.

## DaaS - Data as a Service

* [Apple Maps](https://mapsconnect.apple.com/) - Apple map service.
* [AtlasPI](https://atlaspi.it) - Historical geography as a service for AI agents: 1000+ polities with real GeoJSON borders, events, trade routes, succession chains and cited sources, 4500 BCE-2024. Free, no key, Apache-2.0.
* [GeoRank](https://georank.place) - Monthly sunshine, temperature, rainfall and outdoor-comfort hours for 478 world cities with coordinates. Single JSON file, no key, CC BY 4.0, archived at [Zenodo](https://doi.org/10.5281/zenodo.21976372).
* [Google Maps](https://www.google.com.br/maps) - Google map service.
* [Mantle Place](https://mantle.place) - Draw an area on a globe to get elevation, features, and imagery, delivered as multiple file types you own. Free up to 2 km².
* [Microsoft Bing Maps](http://www.bing.com/mapspreview) - Microsoft map service.
* [OpenStreetMap](http://www.openstreetmap.org/) - OpenStreeMap map service.
* [OpenWaterAtlas](https://openwateratlas.com/en/datasets/) - Integrated open dataset joining 2,928 dive/kite/surf/freedive sites with per-spot climate aggregates (Open-Meteo + ERA5), 112,548 OBIS + GBIF marine species observations, and the 34,876-route OpenFlights direct-route airline graph. CSV + Parquet, CC-BY 4.0, DOI 10.5281/zenodo.20668393.
* [Pera Portal](https://portal.geopera.com) - Satellite imagery platform with a free tier: unlimited Sentinel-2 browsing with 45+ spectral indices computed in-browser. Commercial archive search and tasking across 100+ satellites (30 cm to 2 m), per-km² price shown before ordering, public STAC 1.0.0 API.
* [Seamap](https://openwaters.io/charts/seamap) - Nautical chart web-map tiles rendered weekly from OpenStreetMap seamark data: buoys and beacons with IALA colours and topmarks, lights with sector arcs and characteristics, rocks, wrecks, traffic separation schemes, and depth shading from Seascape. Vector tiles and a MapLibre GL style, CC BY 4.0.
* [Seascape](https://openwaters.io/charts/seascape) - Global bathymetry web-map tiles built from 23 global and regional open sources: Terrarium raster DEM and vector depth contours, spot soundings, and drying areas for MapLibre/Mapbox GL, CC BY 4.0.
* [thirdtrail](https://thirdtrail.life) - Sun, moon, twilight, clear-sky irradiance and tide APIs for any point on Earth, with elevation as a first-class input (sunrise at 214 m is ~3 min earlier than at sea level). Tides from the FES2022 global atlas, any past or future date. Free tier, OpenAPI 3.1, Python client, MCP server.
* [Warnely](https://warnely.com/) - Composite travel-safety scores for 180 countries (FCDO + US State + Global Peace Index + WGI + live incident wire). Free REST API, OpenAPI 3.1 spec, CC BY 4.0. Returns per-country lat/lng centroids alongside score and tier.

## Google Earth Engine

* [AREA2](https://area2.readthedocs.io/en/latest/overview.html) - AREA 2 (“area squared” or “area two”), short for Area Estimation & Accuracy Assessment, is a Google Earth Engine application that provides comprehensive support for sampling and estimation in a design-based inference framework.
* [BAP-GEE](https://github.com/saveriofrancini/bap) - Best Available Pixel calculation using Google Earth Engine.
* [earthEngineGrabR](https://github.com/JesJehle/earthEngineGrabR) - The earthEngineGrabR is an interface between R and the Google Earth Engine, which simplifies the acquisition of remote sensing data.
* [EarthEngine.jl](https://github.com/KMarkert/EarthEngine.jl) - Google Earth Engine in Julia.
* [ee-fastapi](https://github.com/csaybar/ee-fastapi) - Flood Detection with Google Earth Engine.
* [ee-goes](https://github.com/jdbcode/ee-goes) - An Earth Engine JavaScript library for visualizing GOES-R time series.
* [ee-rgb-timeseries](https://github.com/jdbcode/ee-rgb-timeseries) - Earth Engine JS module to color time series chart points as stretched 3-band RGB.
* [eemont](https://github.com/davemlz/eemont) - A python package that extends Google Earth Engine.
* [exploreRGEE](https://github.com/joshualerickson/exploreRGEE) - Google Earth Engine (GEE) in the Rstudio IDE.
* [gee_s1_ard](https://github.com/adugnag/gee_s1_ard) - Creates an analysis ready sentinel-1 SAR image collection in Google Earth Engine by applying additional border noise correction, speckle filtering and radiometric terrain normalization.
* [gee-atmcorr-S2](https://github.com/samsammurphy/gee-atmcorr-S2) - Atmospheric correction of Sentinel 2 imagery in Google Earth Engine using Py6S.
* [geemap](https://github.com/giswqs/geemap) - A Python package for interactive mapping with Google Earth Engine, ipyleaflet, and ipywidgets.
* [geeo](https://github.com/leonsnill/geeo) - GEEO is a processing pipeline and collection of algorithms for obtaining Analysis-Ready-Data (ARD) from Landsat and Sentinel-2 using the Google Earth Engine Python API.
* [GEET](https://github.com/sacridini/GEET) - Google Earth Engine Toolbox - Library to write small EE apps or big/complex apps with a lot less code.
* [geeup](https://github.com/samapriya/geeup) - Simple CLI for Earth Engine Uploads.
* [landsat-extract-gee](https://github.com/loicdtx/landsat-extract-gee) - Get Landsat surface reflectance time-series from google earth engine.
* [msslib](https://github.com/gee-community/msslib) - An Earth Engine JavaScript library for working with Landsat MSS image data.
* [OEEex](https://github.com/open-geocomputing/OEEex) - A chrome extension to enhance Google Earth Engine code editor.
* [OpenEarthEngineLibrary](https://github.com/open-geocomputing/OpenEarthEngineLibrary) - Collection of code goodies for Google Earth Engine(GEE).
* [restee](https://kmarkert.github.io/restee/) - Aims to make plugging Earth Engine (EE) computations into downstream Python processing easier.
* [rgee](https://github.com/r-spatial/rgee) - Google Earth Engine for R.
* [sankee](https://github.com/aazuspan/sankee) - Visualize classified time series data with interactive Sankey plots in Google Earth Engine.
* [spectral](https://github.com/awesome-spectral-indices/spectral) - Awesome Spectral Indices for the Google Earth Engine JavaScript API (Code Editor).
* [wxee](https://github.com/aazuspan/wxee) - A Python interface between Earth Engine and xarray for processing weather and climate data.


## Deep Learning

* [AI Agent by TerraLab](https://github.com/TerraLabAI/QGIS_AI-Agent) - QGIS plugin: an AI agent that runs a plain-language GIS task end to end, from finding the data to building the map, with one-click undo.
* [AI Edit by TerraLab](https://github.com/TerraLabAI/QGIS_AI-Edit) - QGIS plugin for editing aerial and satellite imagery from a text prompt: land cover, building extraction, object removal, flood simulation. Georeferenced output.
* [AI Segmentation by TerraLab](https://github.com/TerraLabAI/QGIS_AI-Segmentation) - QGIS plugin for point-and-click segmentation of buildings, trees and any object in satellite and drone imagery into vector polygons, with a free CPU-only local mode.
* [AIDE](https://github.com/microsoft/aerial_wildlife_detection) - Annotation Interface for Data-driven Ecology: Tools for detecting wildlife in aerial images using active learning
* [AirNet](https://github.com/mathildor/TF-SegNet) - SegNet-like network implemented in TensorFlow to use for segmenting aerial images.
* [aviary](https://github.com/geospaitial-lab/aviary) - Pythonic Framework for AI Inference on Geospatial Data.
* [Deep Learning ArcGIS](https://github.com/Esri/deep-learning-frameworks) - Deep Learning Libraries Installers for ArcGIS.
* [DeepForest](https://github.com/weecology/DeepForest) - Python Package for Tree Crown Detection in Airborne RGB imagery.
* [eo-learn](https://github.com/sentinel-hub/eo-learn) - Earth observation processing framework for machine learning in Python.
* [Hyperspectral](https://github.com/KGPML/Hyperspectral) - Deep Learning for Land-cover Classification in Hyperspectral Images.
* [Label Maker](https://github.com/developmentseed/label-maker) - Data Preparation for Satellite Machine Learning.
* [libtorch-yolov3](https://github.com/walktree/libtorch-yolov3) - A Libtorch implementation of the YOLO v3 object detection algorithm.
* [LightNet](https://github.com/ansleliu/LightNet) - LightNet: Light-weight Networks for Semantic Image Segmentation (Cityscapes and Mapillary Vistas Dataset)
* [mmsegmentation](https://github.com/open-mmlab/mmsegmentation) - MMSegmentation is an open source semantic segmentation toolbox based on PyTorch. It is a part of the OpenMMLab project.
* [Pixel Decoder](https://github.com/Geoyi/pixel-decoder) - A machine learning python package to run deep learning with satellite imagery.
* [PixelLib](https://github.com/ayoolaolafenwa/PixelLib) - Pixellib is a library for performing segmentation of images. It suports both Semantic Segmentation as Instance Segmentation.
* [platypus](https://github.com/maju116/platypus) - R package for object detection and image segmentation.
* [Presto](https://github.com/nasaharvest/presto) - Lightweight, Pre-trained Transformers for Remote Sensing Timeseries.
* [Raster Vision](https://github.com/azavea/raster-vision) - An open source framework for deep learning on satellite and aerial imagery.
* [SamGIS](https://github.com/trincadev/samgis-be) – Image Segmentation machine learning based (Segment Anything by Meta - Facebook) applied to GIS and geo data also with GPU requirements. A Segment Anything HuggingFace demo [here](https://huggingface.co/spaces/aletrn/samgis) and an HuggingFace [demo](https://huggingface.co/spaces/aletrn/samgis-lisa-on-cuda) with natural language-based image segmentation capabilities via [LISA](https://github.com/dvlab-research/LISA).
* [segment-geospatial](https://github.com/opengeos/segment-geospatial) - Meta AI' Segment Anything Model (SAM) for Geospatial Data
* [sentinel-tree-cover](https://github.com/wri/sentinel-tree-cover) - Image segmentations of trees outside forest.
* [ShelfNet](https://github.com/juntang-zhuang/ShelfNet) - Implementation of a CNN model for real-time semantic segmentation.
* [SIMRDWN](https://github.com/avanetten/simrdwn) - The Satellite Imagery Multiscale Rapid Detection with Windowed Networks (SIMRDWN) codebase combines some of the leading object detection algorithms into a unified framework designed to detect objects both large and small in overhead imagery.
* [SNIPER](https://github.com/mahyarnajibi/SNIPER) - SNIPER is an efficient multi-scale object detection algorithm.
* [Solaris](https://github.com/cosmiq/solaris) - CosmiQ Works Geospatial Machine Learning Analysis Toolkit.
* [srcnn](https://github.com/WarrenGreen/srcnn) - Super Resolution for Satellite Imagery.
* [synapse-sr](https://github.com/SharadhNaidu/synapse-sr) - Super-resolution of Sentinel-2 imagery from 10 m to 2 m that stays consistent with the original measurement, with per-pixel trust maps.
* [Temporal Convolutional Neural Network](https://github.com/charlotte-pel/temporalCNN) - Temporal Convolutional Neural Network for the Classification of Satellite Image Time Series.
* [TernausNetV2](https://github.com/ternaus/TernausNetV2) - TernausNetV2: Fully Convolutional Network for Instance Segmentation.
* [TorchGeo](https://github.com/microsoft/torchgeo) - TorchGeo is a PyTorch domain library, similar to torchvision, that provides datasets, transforms, samplers, and pre-trained models specific to geospatial data.
* [TorchSat](https://github.com/sshuair/torchsat) - TorchSat is an open-source PyTorch framework for satellite imagery analysis.
* [tsl](https://github.com/TorchSpatiotemporal/tsl) - PyTorch library for processing spatiotemporal data.
* [WaterNet](https://github.com/treigerm/WaterNet) - A convolutional neural network that identifies water in satellite images.
* [YOLT](https://github.com/avanetten/yolt) - You Only Look Twice: Rapid Multi-Scale Object Detection In Satellite Imagery.

## MCP Servers

* [CARTO for Agents](https://docs.carto.com/carto-for-agents?utm_source=awesome-geospatial&utm_medium=listing&utm_campaign=mcp-marketplace-listings) - Official remote MCP server for CARTO, the Agentic GIS platform. Query governed warehouse data, run spatial analysis, create or edit maps and workflows, and render interactive maps in the conversation; every tool call runs inside your own data warehouse (BigQuery, Snowflake, Databricks, Redshift, or PostgreSQL).
* [emem](https://github.com/Vortx-AI/emem) - Earth memory MCP server that gives AI agents signed geospatial facts and cite-able receipts for place-based questions.
* [League of Spin](https://leagueofspin.com/api/mcp) - Remote MCP server for finding 27,000+ outdoor ping-pong tables worldwide, built on OpenStreetMap data, with spot details and live playing conditions.
* [Microsoft Planetary Computer Pro MCP Tools](https://marketplace.visualstudio.com/items?itemName=ms-planetarycomputer.mpc-pro-mcp-tools) - A Model Context Protocol (MCP) server that enables GitHub Copilot to interact with Microsoft Planetary Computer Pro.
* [NetLoc8 MCP](https://github.com/netloc8/netloc8-mcp) - Model Context Protocol server giving AI assistants geolocation tools to lookup country, city, region, timezone, coordinates, and ASN.
* [OSM Edit MCP](https://github.com/skywinder/osm-edit-mcp) - Python MCP server for inspecting OpenStreetMap data and previewing version-checked road-edit proposals from selected local GPX survey segments. Applying changes requires explicit user confirmation of the proposal digest. Alpha.
* [roadstyle MCP server](https://github.com/Khoshkhah/roadstyle) - Lets an AI agent draw styled, interactive, offline road maps of any place (OpenStreetMap via OSMnx) or road file, and check each map from a PNG preview. `uvx roadstyle-mcp`.
* [ShowMeOnMap MCP](https://showmeonmap.com/developers) - Remote MCP server (OAuth or API key) that turns a plain-English question into a rendered, shareable map from live, cited public data, with spatial-analysis tools; also on npm as @showmeonmap/mcp.

## Agent Skills

* [geoai-skills](https://github.com/muend/geoai-skills) - Vendor-neutral Agent Skills (SKILL.md) that make an AI coding agent check coordinate reference systems, spatial validation, comparability and uncertainty before a result becomes a claim. Works with Claude Code, Codex, Cursor and GitHub Copilot; ships a paired evaluation against a skills-disabled control arm, including the quality gate it fails.
* [GeoAI Skills by TerraLab](https://github.com/TerraLabAI/geoai-skills) - Reusable geospatial Agent Skills for coding assistants, covering coordinate systems, PyQGIS, remote sensing, open data, geoprocessing and map quality checks.
* [roadstyle skill](https://github.com/Khoshkhah/roadstyle/blob/main/skills/roadstyle/SKILL.md) - Agent Skill (SKILL.md) for writing roadstyle code: the one call, the road-edge data contract, the map's JavaScript API and known traps.

## C

* [Datamaps](https://github.com/ericfischer/datamaps) - This is a tool for indexing large lists of geographic points or lines and dynamically generating map tiles from the index for display.
* [FORCE](https://github.com/davidfrantz/force) - Framework for Operational Radiometric Correction for Environmental monitoring.
* [H3](https://github.com/uber/h3) - Hexagonal hierarchical geospatial indexing system.
* [libpostal](https://github.com/openvenues/libpostal) - A C library for parsing/normalizing street addresses around the world. Powered by statistical NLP and open geo data.
* [libvips](https://github.com/libvips/libvips) - A fast image processing library with low memory needs.
* [Shapefile C Library](http://shapelib.maptools.org/) - Provides the ability to write simple C programs for reading, writing and updating (to a limited extent) .shp and .dbf files.
* [udunits2](https://github.com/Unidata/UDUNITS-2) - API and utility for arithmetic manipulation of units of physical quantities.
* [YOLT](https://github.com/CosmiQ/yolt) - You Only Look Twice: Rapid Multi-Scale Object Detection In Satellite Imagery.

## C++

* [Boost Geometry](http://www.boost.org/doc/libs/1_61_0/libs/geometry/doc/html/index.html) - Part of collection of the Boost C++ Libraries, defines concepts, primitives and algorithms for solving geometry problems.
* [copc-lib](https://github.com/RockRobotic/copc-lib) - copc-lib provides an easy-to-use interface for reading and creating Cloud Optimized Point Clouds.
* [cpd](https://github.com/gadomski/cpd) - Coherent Point Drift (CPD) is a point-set registration algorithm.
* [depthmapX](https://github.com/varoudis/depthmapX) - Multi-platform Spatial Network Analysis Software.
* [dreich_algorithm](https://github.com/csdms-contrib/dreich_algorithm) - Algorithm for extracting channel networks from high resolution topographic data.
* [entwine](https://github.com/connormanning/entwine) - Entwine is a data organization library for massive point clouds, designed to conquer datasets of hundreds of billions of points as well as desktop-scale point clouds.
* [GDAL](http://www.gdal.org/) - Geospatial Data Abstraction Library (GDAL) is a computer library that serve as a translator library for raster and vector geospatial data formats.
* [gdalcubes](https://github.com/appelmar/gdalcubes) - gdalcubes is a library to represent collections of Earth Observation (EO) images as on demand data cubes (or multidimensional arrays).
* [geo-utils-cpp](https://github.com/gistrec/geo-utils-cpp) - Header-only C++17 library for spherical (lat/lng) geometry: distance, bearing, area, point-in-polygon.
* [geojson-vt-cpp](https://github.com/mapbox/geojson-vt-cpp) - Port to C++ of JS GeoJSON-VT for slicing GeoJSON into vector tiles on the fly.
* [GEOS](https://trac.osgeo.org/geos/) - GEOS (Geometry Engine - Open Source) is a C++ port of the Java Topology Suite (JTS).
* [gSLICr](https://github.com/carlren/gSLICr) - Real-time super-pixel segmentation.
* [Halide](https://github.com/halide/Halide) - Halide is a programming language designed to make it easier to write high-performance image processing code on modern machines.
* [hmm](https://github.com/fogleman/hmm) - Heightmap meshing utility
* [hydroflow](https://github.com/sistemalabgis/hydroflow) - Compute drainage orders in drainage basins using Strahler and Shreve methods.
* [ITK](https://itk.org/) - ITK is an open-source, cross-platform system that provides developers with an extensive suite of software tools for image analysis.
* [LASzip](https://github.com/LASzip/LASzip) - Quickly turns bulky LAS files into compact LAZ files without information loss.
* [laz-perf](https://github.com/hobu/laz-perf) - Alternative LAZ implementation for C++ and JavaScript.
* [libGeoTiff](https://trac.osgeo.org/geotiff/) - Manipulate TIFF based interchange format for georeferenced raster imagery.
* [libspatialindex](https://github.com/libspatialindex/libspatialindex) - C++ implementation of R*-tree, an MVR-tree and a TPR-tree with C API.
* [Mapbox GL Native](https://github.com/mapbox/mapbox-gl-native) - Render Mapbox styles in mobile, desktop, and node applications using C++ and OpenGL.
* [Mapbox Maps SDK for Qt](https://www.mapbox.com/qt/) - Qt Automotive Map Suite.
* [Mapnik Vector Tile](https://github.com/mapbox/mapnik-vector-tile) - Mapnik C++ implemention of Mapbox Vector Tile specification.
* [Mapnik](http://mapnik.org/) - C++ library for map rendering.
* [Mapzen Tangram-ES](https://github.com/tangrams/tangram-es) - C++ library for rendering 2D and 3D maps using OpenGL ES 2 with custom styling and interactions
* [networkit](https://github.com/networkit/networkit) - NetworKit is a growing open-source toolkit for large-scale network analysis.
* [OpenDroneMap](https://github.com/OpenDroneMap/OpenDroneMap) - OpenDroneMap is a tool to postprocess drone, balloon, kite, and street view data to geographic data including orthophotos, point clouds, & textured mesh.
* [OpenOrienteering Mapper](https://github.com/OpenOrienteering/mapper) - OpenOrienteering Mapper is a software for creating maps for the orienteering sport.
* [Orfeo ToolBox](https://www.orfeo-toolbox.org/) - Orfeo TooLBox (OTB) is an open-source C++ library for remote sensing images processing, distributed under the Apache v2.0 licence.
* [osgearth](https://github.com/gwaldron/osgearth) - A free open source C++ geospatial toolkit.
* [OSMExpress](https://github.com/protomaps/OSMExpress) - Fast database file format for OpenStreetMap.
* [OSRM (Open Source Routing Machine)](http://project-osrm.org/) - High performance routing engine written in C++, designed to run on OpenStreetMap data. Services available: Nearest, Route, Table, Match, Trip, Tile.
* [otbtf](https://github.com/remicres/otbtf) - Deep learning with otb.
* [pprepair](https://github.com/tudelft3d/pprepair) - Validation and Automatic Repair of Planar Partitions.
* [prepair](https://github.com/tudelft3d/prepair) - Automatic repair of single polygons (according to the OGC Simple Features / ISO19107 rules) using a constrained triangulation.
* [Pronto Raster](https://github.com/ahhz/raster) - C++ library for geographical raster data analysis.
* [RichDEM](https://github.com/r-barnes/richdem) - High-performance Terrain and Hydrology Analysis.
* [RoutingKit](https://github.com/RoutingKit/RoutingKit) - RoutingKit is a C++ library that provides advanced route planning functionality.
* [RSGISLib](http://rsgislib.org/) - The Remote Sensing and GIS software library (RSGISLib) is a collection of tools for processing remote sensing and GIS datasets. The tools are accessed using Python bindings or an XML interface.
* [S2 Geometry](https://github.com/google/s2geometry) - Computational geometry and spatial indexing on the sphere.
* [Selene](https://github.com/kmhofmann/selene) - A C++14 image representation, processing and I/O library.
* [SFCGAL](https://www.sfcgal.org/) - a C++ wrapper library around [CGAL](https://www.cgal.org/) with the aim of supporting ISO 19107:2013 and OGC Simple Features Access 1.2 for 3D operations.
* [Spatial](https://sourceforge.net/projects/spatial/) - Spatial is a generic header-only C++ library providing multi-dimensional in-memory containers, iterators and functionals.
* [Supercluster](https://github.com/mapbox/supercluster.hpp) - A C++14 port of supercluster, a fast 2D point clustering library for use in interactive maps.
* [TauDEM](https://github.com/dtarb/TauDEM) - Terrain Analysis Using Digital Elevation Models (TauDEM) software for hydrologic terrain analysis and channel network extraction.
* [Terralib](http://www.dpi.inpe.br/terralib5/wiki/doku.php?id=start) - TerraLib is a GIS classes and functions open source library.
* [TIN Terrain](https://github.com/heremaps/tin-terrain) - A command-line tool for converting heightmaps in GeoTIFF format into tiled optimized meshes.
* [tippecanoe](https://github.com/mapbox/tippecanoe) - Build vector tilesets from large collections of GeoJSON features.
* [valhalla](https://github.com/valhalla/valhalla) - Open Source Routing Engine for OpenStreetMap.
* [Vector Tiles Producer](https://github.com/vross/vector-tiles-producer) - Command line tool in C++ to creates vector tiles for a given area at chosen zoom levels using a Mapnik XML.
* [VROOM](https://github.com/VROOM-Project/vroom) - VROOM is an open-source optimization engine written in C++17 that aim at providing good solutions to various real-life vehicle routing problems (VRP) within a small computing time.

## C Sharp
* [ArcBruTile](https://github.com/ArcBruTile/ArcBruTile) - ArcBruTile displays a collection of maps in ArcGIS Pro 2.0 and ArcMap 10.0 - 10.6.
* [AzureMapsRestServices](https://github.com/perfahlen/AzureMapsRestServices) - .Net Standard 2.0 library to access AzureMaps Services.
* [Bing Maps REST Toolkit](https://github.com/Microsoft/BingMapsRESTToolkit) - This is a portable class library which makes it easy to access the Bing Maps REST services from .NET.
* [Bing Maps Spatial Data Services Toolkit](https://github.com/Microsoft/BingMapsSDSToolkit) - This toolkit makes it easy to use the Bing Maps Spatial Data Services (SDS) in .NET.
* [Bing Maps WPF SDK ](https://msdn.microsoft.com/en-us/library/hh750210.aspx) - The Bing Maps WPF API.
* [Bing-Maps-Fleet-Tracker](https://github.com/Microsoft/Bing-Maps-Fleet-Tracker) - The Bing Maps Fleet Tracker is a tracking solution for small to medium sized teams. Easily track vehicles and mobile devices.
* [BruTile](https://github.com/BruTile/BruTile) - BruTile is a .NET library to access tile services like those of OpenStreetMap, MapBox or GeodanMaps.
* [DEM Net Elevation API](https://github.com/dem-net/DEM.Net) - 3D terrain generation library, provides access to global DEM datasets (OpenTopography, Nasa ASTER) and tiled imagery services. GlTF and STL export formats supported. [Live demo](https://elevationapi.com)
* [DotSpatial](https://github.com/DotSpatial/DotSpatial) - DotSpatial is a geographic information system library written for .NET 4.
* [Earth-Lens](https://github.com/Microsoft/Earth-Lens) - Earth Lens, a Microsoft Garage project is an iOS iPad application that helps people and organizations quickly identify and classify objects in aerial imagery through the power of machine learning.
* [GDAL/OGR CSharp](https://trac.osgeo.org/gdal/wiki/GdalOgrInCsharp) - C# bindings for GDAL and OGR.
* [Geo](https://github.com/sibartlett/Geo) - A geospatial library for .NET
* [GeoJSON.Net](https://github.com/GeoJSON-Net/GeoJSON.Net) - .Net library for GeoJSON types & corresponding Json.Net (de)serializers.
* [GeoJSON4EntityFramework](https://github.com/alatas/GeoJSON4EntityFramework) - Create GeoJSON from Entity Framework Spatial Data or WKT.
* [Mapbox Maps SDK for Unity](https://www.mapbox.com/unity-sdk/) - The Maps SDK for Unity is a collection of tools for building Unity applications from real map data.
* [MaxRev.Gdal.Core](https://github.com/MaxRev-Dev/gdal.netcore) - Bindings for GDAL and OGR (both win-x64 and linux-x64).
* [NTS Net Topology Suite](https://github.com/NetTopologySuite/NetTopologySuite) - A .NET GIS solution that is fast and reliable for the .NET platform.
* [osmsharp](http://www.osmsharp.com/) - OsmSharp is a C# library to work with OpenStreetMap (OSM) data.
* [Sanchez](https://github.com/nullpainter/sanchez) - False-colour geostationary satellite image compositor.
* [SharpKml](https://github.com/samcragg/sharpkml) - Is able to read/write both KML files and KMZ files.
* [SharpMap](https://github.com/SharpMap/SharpMap) - SharpMap is an easy-to-use mapping library for use in web and desktop applications.
* [Windows UWP map control](https://msdn.microsoft.com/en-us/library/windows/apps/xaml/dn642089.aspx) - The Bing Maps control built into the Windows UWP platform.

## Clojure

* [geo](https://github.com/Factual/geo) - Clojure library for working with geohashes, polygons, and other world geometry.


## Crystal

* [geo](https://github.com/geocrystal/geo) - Geospatial primitives and algorithms for Crystal.
* [lidar](https://github.com/jblindsay/lidar) - A Crystal language library for reading and writing LiDAR data in LAS format.

## CSS

* [CartoCSS](https://www.mapbox.com/tilemill/docs/manual/carto/) - TileMills language.
* [MapCSS](http://wiki.openstreetmap.org/wiki/MapCSS) - MapCSS is a CSS-like language for map stylesheets.

## Dart

* [turf_dart](https://github.com/dartclub/turf_dart) - A turf.js-like geospatial analysis library working with GeoJSON, written in pure Dart.

## Delphi

* [DSpatial](http://dspatial.sourceforge.net/) - DSpatial is an Open Source software development project to provide developers using Delphi with a library of tools for the use, manipulation, and visualization of spatial data.

## Elixir

* [distance](https://github.com/pkinney/distance) - Provides a set of distance functions for use in GIS or graphic applications.
* [geo](https://github.com/bryanjos/geo) - A collection of GIS functions for Elixir.
* [geocalc](https://github.com/yltsrc/geocalc) - Geographic calculations for Elixir.
* [Geometry Library](https://github.com/pkinney/topo) - A Geometry library for Elixir that calculates spatial relationships between two geometries.
* [GeoPostGIS](https://github.com/bryanjos/geo_postgis) - PostgreSQL extension for the PostGIS data types.
* [Proj](https://github.com/CandyGumdrop/proj) - Elixir coordinate conversion library using OSGeo's PROJ.4.
* [SRTM](https://github.com/adriankumpf/srtm) - Query locations for elevation data from the NASA Shuttle Radar Topography Mission.
* [Topo](https://github.com/pkinney/topo) - A Geometry library for Elixir that calculates spatial relationships between two geometries.

## Fortran
* [6S](http://6s.ltdri.org/) - Second Simulation of the Satellite Signal in the Solar Spectrum (6S) open source algorithm.
* [FortranGIS](https://github.com/ARPA-SIMC/fortrangis) - A collection of Fortran interfaces to the most common Open Source GIS libraries.
* [SPECFEM3D_GLOBE](https://github.com/geodynamics/specfem3d_globe) - SPECFEM3D_GLOBE simulates global and regional (continental-scale) seismic wave propagation.
* [SWAT](https://github.com/WatershedModels/SWAT) - Implementation of SWAT model.

## Go

* [BoxTree](https://github.com/tidwall/boxtree) - An R-tree implementation for Go.
* [BuntDB](https://github.com/tidwall/buntdb) - BuntDB is an embeddable, in-memory key/value database for Go with custom indexing and geospatial support.
* [cogger](https://github.com/airbusgeo/cogger) - cogger is a fast geotiff to COG converter.
* [Draw2D](https://github.com/llgcode/draw2d) - 2D rendering for different output (raster, pdf).
* [geom](https://github.com/ctessum/geom) - Geometry objects and functions for Go.
* [Go GDAL](https://github.com/lukeroth/gdal) - Go (golang) wrapper for GDAL, the Geospatial Data Abstraction Library.
* [go-geom](https://github.com/twpayne/go-geom) - Go library for handling geometries.
* [Go-proj-4](https://github.com/pebbe/go-proj-4) - Go bindings for the Cartographic Projections Library PROJ.4.
* [Go-shp](https://github.com/jonas-p/go-shp) - Go library for reading and writing ESRI Shapefiles. Pure Golang implementation based on the ESRI Shapefile technical description.
* [go-spatial](https://github.com/jblindsay/go-spatial) - GoSpatial is a simple command-line interface program for manipulating geospatial data.
* [godal](https://github.com/airbusgeo/godal) - Godal aims at providing an idiomatic go wrapper around the GDAL library.
* [gopostal](https://github.com/openvenues/gopostal) - Go (cgo) interface to libpostal for fast international address parsing/normalization.
* [GoSpatial](https://github.com/jblindsay/go-spatial) - GoSpatial is a simple command-line interface program for manipulating geospatial data.
* [lidario](https://github.com/jblindsay/lidario) - A small Go library for reading and writing LiDAR (LAS) files.
* [orb](https://github.com/paulmach/orb) - A set of types for working with 2d geo and planar/projected geometric data in Golang
* [pg_featureserv](https://github.com/CrunchyData/pg_featureserv) - Lightweight RESTful Geospatial Feature Server for PostGIS in Go.
* [pg_tileserv](https://github.com/CrunchyData/pg_tileserv) - A very thin PostGIS-only tile server in Go. Takes in HTTP tile requests, executes SQL, returns MVT tiles.
* [S2](https://github.com/golang/geo) - S2 is a library for spherical geometry that aims to have the same robustness, flexibility, and performance as the best planar geometry libraries.
* [Tegola](https://github.com/go-spatial/tegola) - Tegola is a vector tile server delivering Mapbox Vector Tiles with support for PostGIS and GeoPackage data providers.

## Groovy

* [GeoScript Groovy](https://github.com/geoscript/geoscript-groovy) - GeoScript Groovy is the Groovy implementation of GeoScript.

## Haskell

* [HGeometry](https://github.com/noinia/hgeometry) - HGeometry is a library for computing with geometric objects in Haskell. It defines basic geometric types and primitives, and it implements some geometric data structures and algorithms.
* [hgis](https://hackage.haskell.org/package/hgis) - Package containing functions to make graphs, read shapefiles, and compute areas/perimeters of geographic features.
* [Naqsha](https://github.com/naqsha/naqsha) - Naqsha is a Haskell library to work with geospatial data types.
* [TerraHS](https://wiki.haskell.org/TerraHS) - TerraHS is a software component that enables the development of geographical applications in a functional language, using the data handling capabilities and spatial operations of TerraLib.
## IDL

* [LandTrendr](https://github.com/KennedyResearch/LandTrendr-2012) - LandTrendr (Landsat-based Detection of Trends in Disturbance and Recovery) attempt to capture, label, and map changes in Earth's surface for use in science, natural resource management, and education.

## Java

* [Apache SIS](http://sis.apache.org/) - Apache Spatial Information System (SIS) is a free software, Java language library for developing geospatial applications.
* [asgbook](https://github.com/lakshmanok/asgbook) - Implementation of GIS/RS features in Java. Its also the code accompanying the book "Automating the Analysis of Spatial Grids" by Valliappa Lakshmanan.
* [GDAL Warp Bindings](https://github.com/geotrellis/gdal-warp-bindings) - Thread-safe bindings for GDAL's Warp functionality.
* [Geoapi](http://www.geoapi.org/) - GeoAPI provides a set of Java language programming interfaces for geospatial applications.
* [Geo Assist](https://github.com/thegeekyasian/geo-assist) - Geo Assist is an open source API for indexing and querying spatial data in the most efficient manner. It allows you to store 2D spatial data in-memory and support features such as find nearest neighbors, find in bounding box, etc.
* [Geonetwork](http://geonetwork-opensource.org/) - GeoNetwork is a catalog application to manage spatially referenced resources.
* [GeoServer](http://geoserver.org/) - GeoServer is open source server for sharing geospatial data.
* [Geotools](http://www.geotools.org/) - GeoTools is an open source Java library that provides tools for geospatial data.
* [GeoWebCache](http://www.geowebcache.org/) - a Java web application used to cache map tiles coming from a variety of sources such as OGC Web Map Service (WMS). It implements various service interfaces (such as WMS-C, WMTS, TMS, Google Maps KML, Virtual Earth) in order to accelerate and optimize map image delivery. It can also recombine tiles to work with regular WMS clients.
* [GeOxygene](https://sourceforge.net/projects/oxygene-project/) - Provide an open framework which implements OGC/ISO specifications for the development and deployment of GIS applications.
* [Gisgraphy](http://www.gisgraphy.com/) - Open source framework that offers the ability to do geolocalisation and geocoding via Java APIs or REST webservices.
* [GraphHopper Routing Engine](https://github.com/graphhopper/graphhopper) - GraphHopper is a fast and memory efficient Java routing engine, released under Apache License 2.0. By default it uses OpenStreetMap and GTFS data, but it can import other data sources.
* [JGeocoder](http://jgeocoder.sourceforge.net/) - Free Java Geocoder.
* [jpostal](https://github.com/openvenues/jpostal) - Java/JNI bindings to libpostal for fast international street address parsing/normalization.
* [JTS Topology Suite](https://github.com/locationtech/jts) - JTS Topology Suite is an API of 2D spatial predicates and functions.
* [LuciadLightspeed](http://www.luciad.com/solutions/luciadlightspeed) - A Java library that provides the foundations for advanced geospatial analytics applications
* [MapFish Print](https://mapfish.github.io/mapfish-print-doc/) - The purpose of Mapfish Print is to create reports that contain maps (and map related components) within them. The project is a Java based servlet/library/application based on the mature Jasper Reports Library.
* [Openmap](https://github.com/openmap-java/openmap) - Open Source JavaBeans-based programmer's toolkit.
* [PDAL-Java](https://github.com/PDAL/java) - Java extension and bindings for PDAL.
* [Photon](https://github.com/komoot/photon) - Photon is an open source geocoder built for OpenStreetMap data. It is based on elasticsearch.
* [Proj4j](https://github.com/locationtech/proj4j) - Java port of the Proj.4 library for coordinate reprojection.
* [Spatial4j](https://github.com/locationtech/spatial4j) - Spatial4j is a general purpose geospatial ASL licensed open-source Java library.
* [Weka](http://www.cs.waikato.ac.nz/ml/weka/) - Weka is a collection of machine learning algorithms for data mining tasks written in Java.
* [World Wind Java SDK](http://worldwind.arc.nasa.gov/java/) - Nasa cross-platform Java SDK.

## JavaScript
* [Arabesque](https://github.com/gflowiz/arabesque) - Arabesque is a web application for thematic mapping of flow and networks datasets.
* [arc.js](https://github.com/springmeyer/arc.js) - Calculate great circles routes as lines in GeoJSON or WKT format.
* [ArcGIS Maps SDK for JavaScript](https://developers.arcgis.com/javascript/) - ArcGIS Maps SDK for JavaScript is a proprietary toolkit that enables developers to build web-based mapping and spatial analysis applications that integrate with the ArcGIS ecosystem.
* [Bertin.js](https://github.com/neocarto/bertin) - A JavaScript library for visualizing geospatial data and make thematic maps for the web.
* [Bing Maps V8 Code Samples](https://github.com/Microsoft/BingMapsV8CodeSamples) - A large collection of open source code samples for Bing Maps V8.
* [Bing Maps V8 Interactive SDK](https://www.bing.com/api/maps/sdkrelease/mapcontrol/isdk#loadMapWithOptions+JS) - An interactive code sample gallery for Bing Maps V8.
* [Bing Maps V8 TypeScript Definitions ](https://github.com/Microsoft/Bing-Maps-V8-TypeScript-Definitions) - TypeScript Definitions for the Bing Maps V8 web control.
* [Bing Maps V8 Web Control](https://msdn.microsoft.com/en-us/library/mt712542.aspx) - Bing Maps API for JavaScript.
* [CesiumJS](https://github.com/AnalyticalGraphicsInc/cesium) - An open-source JavaScript library for world-class 3D globes and maps.
* [d3-geomap](https://d3-geomap.github.io/) - A library for creating geographical maps based on D3.js.
* [de9im](https://github.com/dpmcmlxxvi/de9im) - A collection of fast functions for DE-9IM spatial operations.
* [deck.gl](https://github.com/uber/deck.gl) - WebGL2 powered geospatial visualization layers.
* [Euclid.ts](https://github.com/mathigon/euclid.js) - 2D Euclidean geometry classes, utilities, and drawing tools.
* [eurostat-map.js](https://github.com/eurostat/eurostat-map.js) - Reusable library to quickly create and customise web maps showing Eurostat data directly retrieved from Eurostat database.
* [flatbush](https://github.com/mourner/flatbush) - A really fast static spatial index for 2D points and rectangles in JavaScript.
* [FlatGeoBuf](https://github.com/flatgeobuf/flatgeobuf) - A performant binary encoding for geographic data based on flatbuffers.
* [flatten-js](https://github.com/alexbol99/flatten-js) - For manipulating geometrical shapes, finding intersections, checking inclusion, calculating distance, transformations, and more.
* [Galton](https://github.com/urbica/galton) - Lightweight Node.js isochrone server. Build isochrones using OSRM, Turf and concaveman.
* [gdal-js](https://github.com/ddohler/gdal-js/) - An Emscripten port of GDAL 2.1.
* [gdal3.js](https://github.com/bugra9/gdal3.js) - Convert raster and vector geospatial data to various formats using GDAL in the browser.
* [Geo-Three](https://github.com/tentone/geo-three) - Tile based geographic world map visualization library for threejs.
* [geoblaze](https://github.com/GeoTIFF/geoblaze) - Geoblaze is a geospatial raster processing engine written purely in javascript.
* [geobuf](https://github.com/mapbox/geobuf) - A compact binary encoding for geographic data.
* [Geodesy](https://github.com/chrisveness/geodesy) - Libraries of geodesy functions implemented in JavaScript.
* [GeoExt](https://geoext.github.io/geoext3/) - Open Source and enables building desktop-like GIS applications through the web. It is a JavaScript framework that combines the GIS functionality of OpenLayers with the user interface of the ExtJS library provided by Sencha.
* [geojson-merge](https://github.com/mapbox/geojson-merge) - Merge multiple GeoJSON files into one FeatureCollection.
* [Geokit](https://github.com/developmentseed/geokit) - Geokit is a command-line interface (CLI) tool written in javascript, that contains all the basic functionalities for measurements, conversions and operations of geojson files.
* [geolib](https://github.com/manuelbieh/geolib) - Library to provide basic geospatial operations like distance calculation and rotation.
* [Geometric.js](https://github.com/HarryStevens/geometric) - A JavaScript library for doing geometry.
* [GeoPackage.js](https://github.com/ngageoint/geopackage-js) - GeoPackage JS is an implementation of the OGC GeoPackage spec. This library works in both the browser and Node 4+.
* [geopouch](https://github.com/pouchdb/geopouch) - Spatial plugin from PouchDB extracted and supporting N dimensional coordinates.
* [geotiff.js](https://github.com/geotiffjs/geotiff.js) - geotiff.js is a small library to parse TIFF files for visualization or analysis.
* [geotoolbox](https://github.com/neocarto/geotoolbox) - is javascript tool for geographers. It allows to simply deal with geojson properties (attribute data) and provides several GIS operations useful for thematic cartography.
* [geoverview ](https://github.com/neocarto/geoverview) - Based on maplibre-gl, geoverview is a tool for giving a quick and easy geographic overview of any geojson (and the information it contains).
* [Ginkgoch](https://ginkgoch.com) - Ginkgoch is a GIS visualization, analyze library on Node.js. It allows to build cross-platform GIS services, desktop and mobile apps.
* [gmaps.js](https://github.com/hpneo/gmaps) - gmaps.js allows you to use the potential of Google Maps in a simple way.
* [Google Maps API](https://developers.google.com/maps/documentation/javascript/?hl=pt-br) - Google Maps API for JavaScript.
* [Heatcanvas.js](https://github.com/sunng87/heatcanvas) - Yet another heatmap implementation for Javascript.
* [Heatmap.js](https://www.patrick-wied.at/static/heatmapjs/) - A heatmap implementation for Javascript.
* [hyperleaflet](https://hyperleaflet.dev/) - A library that allows you to use the popular Leaflet library with just HTML attributes.
* [iTowns](http://www.itowns-project.org/) - A Three.js-based framework written in Javascript/WebGL for visualizing 3D geospatial data. It can connect to WMS/WMTS/TMS servers including elevation data and load many different data formats (3dTiles, gpx, KML and much much more).
* [JSTS](https://github.com/bjornharrtell/jsts) - Port of the Java JTS library.
* [jVectorMap](https://jvectormap.com/) - jVectorMap is a vector-based, cross-browser and cross-platform component for interactive geography-related data visualization on the web. It provides numerious features like smooth zooming and panning, fully-customizable styling, markers, labels and tooltips.
* [kepler.gl](https://kepler.gl/) - kepler.gl is a data-agnostic, high-performance web-based application for visual exploration of large-scale geolocation data sets.
* [Koop](https://koopjs.github.io/) - An open source geospatial data server. Transform geospatial data on the fly and serve as GeoJSON, Vector Tiles, Feature Services and more.
* [landsat8.earth](https://github.com/kylebarron/landsat8.earth) - 2D/3D WebGL-powered Landsat 8 satellite imagery analysis.
* [landspeed.js](https://github.com/springmeyer/landspeed.js) - WMS server using node-mapnik.
* [leaflet](http://leafletjs.com/) - Open-Source JavaScript Library for Mobile-Friendly Interactive Maps.
* [leaflet TimeDimension](https://github.com/socib/Leaflet.TimeDimension) - Add time dimension capabilities on a Leaflet map.
* [leaflet-elevation](https://github.com/Raruto/leaflet-elevation) - Leaflet plugin that allows to add elevation profiles using d3js
* [leaflet-providers](https://github.com/leaflet-extras/leaflet-providers) - An extension to Leaflet that contains configurations for various free tile providers.
* [Loam](https://github.com/azavea/loam) - Javascript wrapper for GDAL in the browser.
* [LuciadRIA](http://www.luciad.com/solutions/luciadria) - A JavaScript library for 3D globes and maps, with support for military symbology and desktop-like performance
* [mapbox-gl-draw](https://github.com/mapbox/mapbox-gl-draw) - Draw tools for mapbox-gl-js.
* [mapboxgl-powerbi](https://github.com/mapbox/mapboxgl-powerbi) - Mapbox GL PowerBI custom visual.
* [mapshaper-proj](https://github.com/mbloch/mapshaper-proj) - A JavaScript port of the Proj.4 map projection library.
* [math.gl](https://github.com/uber-web/math.gl) - JavaScript math library focused on Geospatial and 3D use cases.
* [Moveet](https://github.com/ivannovazzi/moveet) - Real-time vehicle fleet simulator with A* pathfinding on real road networks.
* [NASA WebWorldWind](https://github.com/NASAWorldWind/WebWorldWind) - The NASA WorldWind Javascript SDK (WebWW) includes the library and examples for creating geo-browser web applications and for embedding a 3D globe in HTML5 web pages.
* [openaq](https://github.com/nickolasclarke/openaq) - A JS client for the OpenAQ API. OpenAQ is a non-profit organization empowering communities around the globe to clean their air by harmonizing, sharing, and using open air quality data.
* [OpenGlobus](https://www.openglobus.org/) - A javascript library designed to display interactive 3d maps and planets with map tiles, imagery and vector data, markers and 3d objects. It uses the WebGL technology, open source and completely free.
* [OpenLayers](http://openlayers.org/) - Open source AJAX library.
* [openrouteservice-js](https://github.com/GIScience/openrouteservice-js) - The JavaScript API to consume openrouteservice(s) painlessly!
* [OpenSphere](https://github.com/ngageoint/opensphere#opensphere) - A pluggable, single-page, GIS web application that supports both 2D and 3D views.
* [OSM Building](https://osmbuildings.org) - A JavaScript library for visualizing OpenStreetMap building geometry on 2D and 3D maps.
* [overpass-turbo](https://github.com/tyrasd/overpass-turbo) - A web based data mining tool for OpenStreetMap using Overpass API.
* [PGRestAPI](https://github.com/spatialdev/PGRestAPI) - Node.js REST API for PostGres Spatial Entities.
* [pixelmatch](https://github.com/mapbox/pixelmatch) - The smallest, simplest and fastest JavaScript pixel-level image comparison library.
* [pouchdb-geospatial](https://github.com/dpmcmlxxvi/pouchdb-geospatial) - The PouchDB Geospatial plugin provides spatial querying of GeoJSON objects right in the browser.
* [procedural-gl-js](https://github.com/felixpalmer/procedural-gl-js) - Procedural GL JS is a library for creating 3D map experiences on the web, written in JavaScript and WebGL. It is built on top THREE.js.
* [proj4js](https://github.com/proj4js/proj4js) - JavaScript library to transform coordinates from one coordinate system to another, including datum transformations.
* [PureJsImage](https://github.com/a-r-d/PureJsImage) - Zero-dependency TypeScript library for GeoTIFF, COG, GeoZarr, ENVI, and range-backed raster access in browsers and Node.js.
* [railroute-ts](https://github.com/mayurrawte/railroutes) - Shortest rail route and distance between two points or station codes over OpenStreetMap / FRA rail networks (Europe, India, North America, China, CIS), with gauge, electrification and train-ferry awareness. TypeScript, runs in browser or Node, GeoJSON output.
* [rbush](https://github.com/mourner/rbush) - A high-performance JavaScript library for 2D spatial indexing.
* [react-leaflet](https://github.com/PaulLeCam/react-leaflet) - React components for Leaflet maps.
* [react-map-gl](https://github.com/uber/react-map-gl) - React friendly API wrapper around MapboxGL JS.
* [reproject](https://github.com/perliedman/reproject) - Change, convert, transform, reproject GeoJSON between different projections/CRS.
* [searoute-ts](https://github.com/mayurrawte/searoute-ts) - Shortest maritime route between ports (UN/LOCODE) or coordinates on the Eurostat marnet, with canal/strait restrictions, vessel draft, ECA zones and CO₂e estimates. TypeScript, GeoJSON output.
* [Spatial](https://github.com/troufster/spatial) - A 2d spatial hash module for node.js.
* [spl.js](https://github.com/jvail/spl.js) - SpatiaLite and friends - sqlite, geos, proj, rttopo - for node (sync API) and browser (async API).
* [SQLite3](https://github.com/mapbox/node-sqlite3) - Asynchronous, non-blocking SQLite3 bindings for Node.js.
* [statsbreaks](https://github.com/riatelab/statsbreaks) - Split a quantitative dataset into classes for thematic mapping.
* [Supercluster](https://github.com/mapbox/supercluster) - A crazy fast geospatial point clustering library for browsers and Node.
* [SuperMap iClient for JavaScript](http://iclient.supermap.io) - Cloud GIS web client development platform supportted by SuperMap.
* [Terra Draw](https://github.com/JamesLMilner/terra-draw) - A cross provider JavaScript library for drawing on maps
* [TerriaJS](https://github.com/TerriaJS/terriajs) - A library for building rich, web-based geospatial data explorers.
* [Thermo.js](https://github.com/dazuma/thermo.js) - Another heatmap implementation for Javascript.
* [tilegarden](https://github.com/azavea/tilegarden) - Serverless raster and vector map tile generation using Mapnik and AWS Lambda.
* [tilelive-postgis](https://github.com/stepankuzmin/tilelive-postgis) - Implements the tilelive API for generating mapnik vector tiles from PostGIS.
* [TileMantle](https://github.com/naturalatlas/tilemantle) - A tool to warm up your tile server cache. Give it a URL template, geometry, and list of zoom levels and it will request tiles incrementally to warm it up.
* [TileStrata](https://github.com/naturalatlas/tilestrata) - A pluggable Node.js map tile server.
* [tilestrata-mapnik](https://github.com/naturalatlas/tilestrata-mapnik) - TileStrata provider for rendering tiles with mapnik.
* [Turf.js](http://turfjs.org/) - Advanced geospatial analysis for browsers and node.
* [ui-leaflet](https://github.com/angular-ui/ui-leaflet) - AngularJS directive to embed an interact with maps managed by Leaflet library.
* [Vue2L