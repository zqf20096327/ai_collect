# flow around stuff

`fas` predicts the steady incompressible flow around a body from its surface mesh: surface pressure and friction, drag and lift, and pressure, velocity and vorticity at any points. Inference only.

Post and interactive demo: [flow-around-stuff.com](https://flow-around-stuff.com)

```
pip install git+https://github.com/jonasw247/flow-around-stuff
fas body.stl --re 1e6 --aref 0.5
```

The weights (1 GB) are downloaded from [Hugging Face](https://huggingface.co/JonasW247/flow-around-stuff) on the first run. Before that, once: request access on that page (granted at once) and log in with `hf auth login`.

A GPU is recommended; it also runs on a CPU.

- Flow along +x, lift along +z, in the coordinates of the mesh (any format trimesh reads). The mesh should be a closed surface; a warning is printed if it is not.
- `--re`: Reynolds number based on the length of the body along its longest axis. Trained for 0.1 to 2e6; a warning is printed outside this range.
- `--floor Z`: moving ground at z = Z (mesh units), e.g. for cars. At or below the lowest point of the body.
- `--aref A`: reference area, one number in mesh units² (e.g. the frontal area of a car, the planform area of a wing). Without it the three force areas are printed: `drag_area` (along +x), `side_area` (+y), `lift_area` (+z), each the force / dynamic pressure (½ρU²), i.e. Cd·A, Cs·A, Cl·A. With it also Cd, Cs, Cl = force area / A. Force in newtons = force area (in m²) × ½ρU².
- `--points pts.npy`: (N, 3) points in mesh units to get the flow at. Points inside the body, below the floor or outside the model's box (4.5 body lengths upstream, to the sides, above and below the body's centre, 12.5 downstream) give NaN.
- `--draws N`: average over N random samplings of the input (default 1).
- `--weights`: path of the weights (default: `fas-large.safetensors` in the working directory, else the download).

`result.npz`: per face of the (subdivided) mesh `centres`, `areas`, `normals`, `cp`, `cf` (wall shear stress / dynamic pressure, as a vector, with the sign of the stress on the fluid: it points against the flow where the flow is attached; the friction force on the body is −`cf` × area); per point `point_cp`, `point_u` (velocity / free-stream speed), `point_vorticity` (|vorticity| × length / free-stream speed).

From Python:

```python
import fas
model = fas.load()
r = fas.predict(model, *fas.mesh_faces("body.stl"), re=1e6)
```

## Model

256 M parameters. Points around the body are grouped into balls; a transformer over the ball tokens predicts the fields, decoded point by point.

The results are estimates of a learned model, not a simulation.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), code and weights: free to use, change and share, also commercially, as long as you give credit: flow-around-stuff (fas) by Jonas Weidner, Julian McGinnis and Benedikt Wiestler, with a link to this repository and to the licence, and a note if you changed something.
