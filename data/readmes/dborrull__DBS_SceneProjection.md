![DBS_SceneProjection: one frame to a projection setup in Nuke](docs/images/banner.jpg)

# DBS_SceneProjection

By David Borrull, VFX compositor. MIT licence (see LICENSE). Version 0.9.0 (see CHANGELOG.md).

Nuke gizmo: from one frame of a plate, builds a projection camera and geometry (floor, walls,
backdrop, and each object as a fitted primitive: box, cylinder, cone, sphere, revolve, or card;
or relief meshes) and wires them into a projection setup, in Nuke's USD 3D system or the
classic one. Optionally a Gaussian splat of the plate (Apple SHARP) in the same world.

![One frame of a street plaza (left) and the setup it builds in Nuke's 3D viewer: camera, floor, walls and fitted shapes with the frame projected on them (right)](docs/images/example_street.jpg)

![A street corner (left) and its setup in Nuke's 3D viewer with the urban label preset: walls as planes, floor and the shot camera (right)](docs/images/example_alley.jpg)

![The same frame as plate, cards, boxes, shapes, relief, and relief with a Gaussian splat (SHARP)](docs/images/geometry_types.jpg)

Standalone: it talks to your ComfyUI directly (MoGe 2 for depth, SAM 3 for masks). It does
not need DBS_ComfyBridge.

With a tracked camera and its point cloud connected, the geometry is snapped to the tracker's
own 3D points, so projected paint stays on the plate: on a real handheld truck shot, the
projection slides under 1.2 px (median, on a 1280-wide plate) across 188 frames.

```
Nuke (DBS_SceneProjection)  frame -> PNG through the Viewer transform
  -> ComfyUI          MoGe 2: metric point map, normals, focal   (SaveMoGeGeometry: float EXR/NPZ/JSON)
                      SAM3: one mask per instance of each label  (SegmentLabels: seg.npz)
                      SHARP (optional): Gaussian splat             (SharpSplat: PLY)
  -> Blender -b       geofit: floor / walls / ceiling planes from their labels, one primitive per
                      object instance (or relief meshes), depth check -> scene.abc + scene.usd
  -> Nuke             USD:     FrameHold -> Project3DShader <- Camera4, GeoImport(abc)
                               -> GeoBindMaterial -> GeoTransform -> GeoScene -> ScanlineRender2
                      classic: FrameHold -> Project3D2 <- Camera3, ReadGeo2(abc)
                               -> TransformGeo -> Scene -> ScanlineRender
```

Labels are `text:role` (or `text:object:shape`) lines on the node (`floor`, `wall`, `ceiling`,
`object`, `backdrop`, `ignore`); the default list covers interiors and exteriors (extra prompts are cheap: SAM3 encodes
the image once). Where masks overlap, ignore > object (smaller wins) > floor > ceiling > wall >
backdrop; overlapping object masks from different prompts keep the most confident one, and
weak (< 0.40) or backdrop-enclosed object masks are dropped. Floor = one loose plane through
everything labelled ground (bumpy grass included), never one that would roll the camera more
than 20° (that is a slope: an embankment, a verge). When little level ground is labelled (under
5% of the frame, e.g. an unlabelled road between two verges), the largest near-horizontal
plane below the camera among the ground and unlabelled samples is used if bigger; fit.json says
which (`floor` primitive, `source`: `labels` / `geometry`). Backdrop = one vertical plane behind all
objects that fills the frame (trees, hills). Unlabelled areas get no geometry. With
segmentation off, floor / walls / boxes are guessed from geometry alone (fine for clean rooms,
wrong on real interiors: it took a dining table for the floor).

## Install

- **ComfyUI**: MoGe weights in `models/geometry_estimation`
  (`moge_2_vitl_normal_fp16.safetensors`) and `comfy_nodes/nuke_geo_projection` in
  `custom_nodes` (copy or link the folder). For segmentation, [ComfyUI-RMBG](https://github.com/1038lab/ComfyUI-RMBG) (its SAM3, `models/sam3/sam3.pt`).
  The first build with segmentation downloads `sam3.pt` (about 3.4 GB), so it takes longer once.
  Tested with ComfyUI-RMBG 3.1.0: the gizmo uses its SAM3 directly, so if a later version
  breaks segmentation, the error says so; go back to 3.1.0 until the gizmo is updated.
  Restart ComfyUI. First run after a restart loads SAM3 (~15 s); then a plate takes ~15 s in all.
- **Gaussian splat** (optional): [ComfyUI-Sharp](https://github.com/PozzettiAndrea/ComfyUI-Sharp)
  in `custom_nodes` (its SHARP weights download to `models/sharp` on first use). Needs Nuke 17.1+
  (native splats) and the USD 3D system. See *Model licences* below: the SHARP weights are for
  research / non-commercial use only.
- **Blender** 4.2+ (tested 5.0). Found automatically in Program Files, or set the `blender` knob
  / `$GEO_PROJECTION_BLENDER`.
- **Nuke** (tested 17.1 Non-commercial), in `~/.nuke/menu.py`:
  ```python
  nuke.pluginAddPath("/path/to/nuke_geo_projection/nuke")
  import geo_projection
  geo_projection.install_menu()
  ```
  Then **DBS › DBS_SceneProjection** in the Nodes toolbar (also in **Nodes › 3D**). `DBS_` is
  the prefix of David Borrull Silva's tools, so they never clash with other gizmos. The icon,
  `nuke/geo_projection.png` (+ `@2x`), is drawn by `tools/make_icon.py`.

## Use

<img src="docs/images/panel.png" alt="The DBS_SceneProjection node panel in Nuke" width="560">

1. Select the plate, create **DBS_SceneProjection**, set the **reference frame** (or **set to current
   frame**). Plates with non-square pixels (DVCPRO HD, anamorphic) are sent to ComfyUI
   stretched to square pixels; the camera maths use the display aspect.
2. Camera:
   - **cam input**: connect your shot camera (Camera3 or Camera4). Its lens at the reference
     frame is used, the geometry is placed in its space and the setup Group's `cam` input is
     connected to it, so the render follows it. A window offset (`win_translate`) is taken into
     account: the geometry is rebuilt for its off-centre principal point.
     **Cameras tracked elsewhere** (3DEqualizer, PFTrack, SynthEyes, Blender...): load the
     FBX / Alembic into a Camera (*read from file*) and connect it; its world matrix is read,
     so a hierarchy in the file is fine. Connect the **undistorted** plate (with the tracker's
     own lens data: its Nuke lens nodes or STMap) and distort the render back afterwards.
     Plain Nuke is enough; NukeX is only needed for the CameraTracker. Prefer Alembic: a camera
     and point cloud written by Blender read back exactly. FBX conventions differ between apps
     (a Blender FBX camera comes into Nuke in cm and turned 90° about Y), so with FBX check the
     camera lines up with the plate before building.
     **Scale**: MoGe has its own units, the track others; with a moving camera the geometry
     must be in the track's or it slides. Each run matches features (SIFT) between the
     reference frame and another frame of the plate (the extra frames, else the one where the
     camera is farthest away), lifts them to 3D with MoGe and picks the scale that reprojects
     them best through the tracked camera (ComfyUI node `SolveTrackScale`). It becomes the
     Group's **scene scale**; the info line says `track scale 1.67 (853 pts, 1.3 px)`. A nodal
     pan needs none. On the synthetic sequence: solved 1.67, true 1.70 (MoGe's floor height
     said 1.41).
   - **points input** (recommended with a tracked camera): the tracker's point cloud
     (CameraTrackerPointCloud, or a ReadGeo / GeoImport of exported points or locators; works
     for cameras tracked in Nuke and elsewhere). The points the camera sees at the reference
     frame fix the scale directly (no SolveTrackScale), and MoGe's depth is then corrected
     region by region (each object, the floor, each backdrop card) to pass through the points
     on it: depth changes only along the camera rays, so the reference frame still lines up,
     and a tilted plane is straightened. Regions without enough points keep MoGe's shape. After
     the build the info line and the Script Editor give the slide in px per object over the
     plate's range (each tracker point against its point on the geometry), in plate px and,
     for plates that are not 1920 wide, in px of a 1920-wide frame (`@HD`); objects over 2 px `@HD`
     are flagged. Backdrop cards (trees) always slide some: use relief or the splat there.
     No point cloud? The build triangulates SolveTrackScale's matches with your tracked camera
     at the two frames and uses those points the same way (`track scale 1.2 from 640
     triangulated points`): snap and slide check in plain Nuke too. It needs real parallax
     between the frames (rays over 1° apart) and at least 30 points; otherwise only the scale
     is solved. The tracking team's locators or NukeX's **PointCloudGenerator** are still
     better: they come from the whole sequence, not two frames.
   - **track check**: when the camera comes from a Nuke CameraTracker (Create Camera), the info
     line shows its solve error and warns over 1 px `@HD` (over 2 px: the projection will slide).
     For cameras tracked elsewhere it says `track check n/a`, and with a point cloud it warns
     when over 30% of the points disagree with the rest (about 7% on a good track).
   - **silhouette check** (with labels): each object's proxy against its SAM3 mask. A proxy
     that leaves out over 25% of its mask is listed as `silhouette off: table_1 misses 45%`
     (misplaced or too small: try another shape or more precision). One whose footprint is
     over 50% background (a chair or table as a box, filling between the legs) counts as a
     `loose fit`: relief fits those better. Per object figures in the Script Editor.
   - **extra frames** (sequence mode, needs the shot camera): more frames projected onto the
     same geometry, typed (`25 50`) or added with **add current frame** at the Viewer's frame.
     The reference frame stays on top; each extra frame, in the order listed, fills what the
     frames before it did not see, e.g. the side of a box the camera turns to. Each projection
     is occluded by the geometry (`occlusion_mode world`), so it only lands where its camera
     saw. The geometry still comes from the reference frame only. Inside the Group: per frame
     `Hold_<f>` -> `Alpha_<f>` -> `Project_<f>` <- `Camera_<f>` (the shot camera baked at that
     frame), layered into `Blend` (MergeMat / MergeLayerShader). Synthetic sequence, render at
     frame 19 of 25: coverage 92.5% -> 99.7%, pixels clearly wrong 7.2% -> 5.3%; at the
     reference frame the render is the plate, as without extra frames.
   - Without it: set **focal** / **film back width** if you know the lens (MoGe's own estimate
     is ~10–20% off). **camera height** (e.g. 1.6) gives real-world units; 0 keeps MoGe's.
3. Labels: pick a **label preset** (all, interior, exterior, urban, or your own) and add
   **extra labels**, one per line: `text:role`, or `text:object:shape` to force a shape
   (`lamp:object:revolve`, `plant pot:object:cylinder`, `column:object:box`), or relief for
   that label only, the rest staying shapes (`rock:object:relief`, `tree:backdrop:relief`: its
   own surface as a mesh, no box or card). A label already in
   the preset takes the new role / shape. **show labels** lists what will be sent.
   **Generated mesh** (`sofa:object:mesh`, experimental): each instance of that label is cropped from the plate
   and turned into a closed mesh by Pixal3D in ComfyUI (geometry only, about a minute per
   object on an 8 GB card, at most 8 per build), then placed on its SAM3 mask and on MoGe's
   depth. Unlike a primitive it has the object's shape, and it goes on behind whatever
   covers part of it. Depth along the camera ray is the model's own guess: one frame cannot
   check it. If the mesh does not match the mask (IoU under 0.6) the label falls back to the
   best fitted shape and the info line says so. Works best on whole, well-seen objects
   standing on something (chair, sculpture, sofa, truck: IoU 0.76-0.91); objects cut by the
   frame edge are borderline or fall back, and hanging ones (a pendant lamp) fall back.
   Meshes are reused from earlier versions of the
   node while the plate and the object's mask are the same. Needs ComfyUI with the Pixal3D /
   TRELLIS.2 nodes (built in from late 2026) and three files from
   [Comfy-Org/Pixal3D](https://huggingface.co/Comfy-Org/Pixal3D) (about 7.9 GB):
   `diffusion_models/pixal3d_int8_convrot.safetensors`, `clip_vision/dino_v3_L_naf_fp32.safetensors`,
   `vae/trellis_2_shape_vae_bf16.safetensors`.
4. **geometry** (what each object becomes; floor / walls / ceiling / backdrop are planes in all;
   a shape forced by a label, `truck:object:box`, wins in every mode):
   - **shapes** (default): the primitive that fits each object best — box, cylinder, cone,
     sphere or revolve (a lathe profile: vases, lamps, pots) — unless the label forces one. A
     card is never picked automatically (it is no volume), only on request;
   - **boxes**: a box each;
   - **cards**: a camera-facing card each (lightest);
   - **relief**: MoGe's own surface as meshes, one per object instance / floor / wall /
     backdrop / other, with the floor / wall planes pushed just behind as fill. ~200k vertices,
     ~25 MB Alembic at HD.
   Backdrop instances (trees, hills) get a card each at their own distance, cut to the
   instance's shape (its mask, slightly grown, and straight down to the floor): a rectangle
   would stand in front of whatever is farther inside it, e.g. the trees behind a `forest`
   card. In relief the cards sit just behind each tree's mesh as fill, so its holes show the
   tree's own distance, not the far backdrop.
   **card margin (px)**: how far each card grows past its object, in pixels of the plate
   (0 by default: cut to the object as above). For painting or adding things past the
   outline, as on a card larger than the object, cut by the paint's own alpha. Inside that
   band a card can stand in front of farther things, which then slide with the camera. It
   applies to backdrop cards and, in `cards`, to the object cards.
   **precision (px)**: sample spacing of the fit (and the relief's vertex spacing); 4 by
   default, 2–3 for more detail. Nodes made before 0.5 keep their old detail level (low =
   boxes at 6 px, medium = boxes at 4 px, high = relief at 3 px).
   Objects that float rest on what is under them: on a labelled object right below (a vase on
   a table), on the floor when unlabelled points fill the column under them (a lamp's
   pedestal, which then becomes part of the object), or on the floor when their foot is hidden
   behind something nearer (a sofa arm); otherwise they hang (wall cabinets, niches).
   The colour tells the geometry type at a glance, on the gizmo (live) and on each setup Group
   (as built): shapes teal, boxes orange, cards blue, relief purple. The gizmo's label shows
   its last build and the current type / 3D system; each Group's label, how it was built
   (`v011 shapes USD`).
5. **Gaussian splat (SHARP)** (USD only): also makes a splat of the plate at MoGe's focal,
   scaled to MoGe's depth and placed in the same world as the geometry. The setup Group gets
   `Splat` (GeoImport) -> `SplatXform` (linked to Xform) -> `SplatRender`, and an **output** menu:
   projection, splat, or projection over splat (the splat fills what the geometry misses).
6. **3D system**: **USD** (default) or **classic** — which Nuke 3D nodes the setup is built
   with. Both give the same result. DBS_SceneProjection nodes created before v0.3.0 (no menu) build
   the classic setup.
7. **Build camera + geometry**. Each run writes `vNNN/` (plate PNG, geo.exr/json/npz, seg.npz,
   labels.json, fit.json, scene.abc, scene.blend, blender.log) and pastes **one Group,
   `GeoProj_vNNN`**, under the gizmo. Its output is the render; Ctrl+Enter opens it.
   - Inputs: `plate` (from the gizmo) and, if a shot camera was used, `cam` (connected to it:
     the render follows that camera; the projection uses it as it was at the reference frame).
   - Knob **scene scale**: live scale of the geometry about the projection camera (the
     projection does not change), to match a tracked scene's scale.
   - Projections land on front faces only (`project on: front`), so paint never shows through
     on the far side of a box.
   - **show only** / **pattern** (USD and classic): show just one object, a group or a mask; the
     projection and render follow, nothing else to disable. The menu lists `all`, the groups
     (`objects/*`, `structure/*`, `backdrop/*`, `other/*`) and every object. The pattern takes
     names or paths, space separated, with `*` / `?`; a name without a leading `/` is searched
     at any depth: `lamp_1`, `*chair*`, `vase* sofa_1`, `/structure/floor`.
   - **extract for paint** (USD and classic): pick an object or group in **show only** (or a
     **pattern**) and press it. To the right of the Group it pastes loose nodes in a backdrop
     titled `paint lamp_1 frame 001`, named after the object (`lamp_1_…`):
     ```
     plate -> lamp_1_Hold (FrameHold) -> lamp_1_Paint (RotoPaint, "paint here", rgb)
           -> lamp_1_Project <- lamp_1_CamHold (FrameHold) <- camera
           -> lamp_1_Geo (only that object) -> lamp_1_Xform -> lamp_1_Render <- camera
     ```
     The camera is your shot camera (a Dot `lamp_1_Cam` linked to it: projection held at the
     reference frame, render following it) or, without one, the baked projection camera
     (`lamp_1_Camera`). Classic: ReadGeo2 -> TransformGeo -> ScanlineRender, as built by hand.
     USD: GeoImport -> GeoBindMaterial -> GeoTransform -> GeoVisibility -> GeoScene ->
     ScanlineRender2 (don't rename `lamp_1_Project`: the bind finds its material by that
     name). The scene scale is baked into the Xform at the time of the extract. Each extract
     goes one backdrop further right. Groups built before v0.6 cannot extract: build them
     again.
   - **card from CornerPin**: pin an image (sign, poster, patch) onto the plate with a
     CornerPin2D at the reference frame, in the plate's format (Reformat before it), left
     unconnected to the gizmo. Select it and press the button on the Group: a card is put on
     its four corners and the pinned image is projected onto it, in a backdrop beside the
     Group like an extract. The menu beside the button says where the card goes:
     - **standing, facing camera** (default, the usual card): upright and turned to the
       camera, its bottom edge (to1–to2) standing where MoGe sees it. The pin already has the
       perspective; the projection keeps it.
     - **on the surface**: lying on the floor or wall MoGe sees under the four corners
       (snapped to the track) — the same as texturing that surface with the image.

     Either way the corners land exactly on the CornerPin's at the reference frame and the
     card does not depend on the setup's geometry. It renders over everything: anything
     passing in front (a person) needs its own matte.
   - Inside, fixed names: Hold (FrameHold), Camera (projection), Project, Geo, Bind and
     Isolate (USD only), Xform (scene scale + shot camera space), Scene, Render.
   - The geometry is organised by group: `/structure/floor`, `/structure/wall_1`,
     `/objects/lamp_1`, `/backdrop/card_3`, `/other/…` (each object `/<group>/<name>/<name>`).
     `scene.usd` has the same hierarchy (Z up, metres as fitted) for other DCCs.
   - Nothing refers to node names outside the Group: copying, pasting or renaming it, the
     gizmo or the shot camera breaks nothing (to switch cameras, reconnect `cam`).

### Label presets

Text files, one `text:role` per line, `#` comments. Built-ins in `nuke/geoproj/label_presets`;
your own in `~/.nuke/geo_projection_labels` (or `$GEO_PROJECTION_LABELS`) — same name replaces
a built-in. New presets show up in the menu of newly created nodes.

### Notes

- The gizmo passes the plate through untouched. A run touches at most four Node objects (the
  gizmo, the shot camera, the Viewer, the graph it pastes into), an extract two (the Group,
  its graph); pasted setups connect themselves by name (`push [node …]`), so nothing below the
  gizmo or the plate is rewired. Nuke Non-commercial allows 10 per session.
- USD system: projection is a `Project3DShader` material bound by `GeoBindMaterial` to the
  Alembic's geometry prims, listed by name (`/floor /wall_1 …`), with the material path set
  explicitly (`/materials/NukeMaterialOps/Project_NdkSurfaceShader`, after the Project node
  inside the Group). Not `/*`: the stage roots also hold `/materials` and the Alembic camera.
  The `Project3D` class is the classic one and makes no material there.
- Known limitation: with a shot camera that has a window offset, the USD setup's render depth
  is ~0.6–0.9% off the fit (Camera4 reads the offset slightly differently from Camera3; the
  classic setup is exact). The projected image is unaffected: projection and render use the
  same camera.

## Model licences

DBS_SceneProjection is MIT, but it runs third-party models in your ComfyUI, each under its own
licence. It does not ship any weights. Check them before commercial work:

- **MoGe 2** (Microsoft): [github.com/microsoft/MoGe](https://github.com/microsoft/MoGe).
- **SAM 3** (Meta, via comfyui-rmbg): the SAM License,
  [huggingface.co/facebook/sam3](https://huggingface.co/facebook/sam3/blob/main/LICENSE).
- **SHARP** (Apple, via comfyui-sharp; only with **Gaussian splat** on): the weights are under
  Apple's research licence, for research / non-commercial use only,
  [github.com/apple/ml-sharp](https://github.com/apple/ml-sharp).
- **Pixal3D** (TencentARC; only with `:mesh` labels): MIT as repackaged by Comfy-Org,
  [huggingface.co/TencentARC/Pixal3D](https://huggingface.co/TencentARC/Pixal3D). Its DINOv3
  image encoder comes from Meta, under Meta's DINOv3 licence: check it too.

## Tests (`tests/`)

- `make_synthetic_plate.py` — Blender scene with known camera and boxes (ground truth;
  `GT_STEP` env var sets its sampling).
- `eval_moge.py`, `eval_fit.py` — MoGe depth / fitted primitives against ground truth.
- Sequence: `SEQ_FRAMES=25 SEQ_TRUCK=2.4 blender ... make_synthetic_plate.py` renders a moving
  camera; `nuke_e2e.py .../plate.%04d.png --shot ground_truth.json --last=25 --frames=25,13
  --render-frame=19` + `compare_sequence.py` (render against the real plate at that frame);
  `solve_scale_offline.py` checks the scale solve alone (ComfyUI's Python).
- `nuke_extract.py` (Nuke `--nc -t`: build a Group from a run, extract an object, render both)
  + `compare_extract.py` (the extract must match the full render where both show).
- `nuke_e2e.py` (Nuke `--nc -t`, options `--system`, `--shot`, `--win`, `--detail`, `--preset`)
  + `compare_nuke_depth.py` (render depth must match the fit) + `compare_nuke_rgb.py` (render
  through the projection camera must give the plate back).
- `nuke_track_points.py` (Nuke `--nc -t`: build on a tracked shot with its point cloud on
  'points'; `--ref=N`, `--geometry=boxes`) prints the scale and the per-object slide.
- `compare_depth_models.py` — MoGe 2 against Depth Anything 3 (focal, scale, shape, edges).

## Credits

`geoproj/comfy_client.py`, `geoproj/colour.py` and the template / paste helpers are copied from
[ComfyBridge](https://github.com/dborrull/nuke-comfy-pipe) (MIT, David Borrull).
