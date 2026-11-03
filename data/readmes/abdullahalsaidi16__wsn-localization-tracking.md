# Localization and Tracking in a Wireless Sensor Network

Work out where a moving target is — and where it is going — inside a wireless sensor
network, using nothing but the signal strength it registers at fixed anchor nodes.

Received Signal Level (RSL) is one of the stronger signals available for this, but writing
a closed-form model that maps RSSI readings back to a position is awkward and empirical.
So the mapping is **learned** instead: an SVM regressor, and a Random Fourier Features
approximation of the same kernel. Tracking is then treated as localization applied
repeatedly over time, with a **Kalman filter** and the target's accelerometer smoothing the
per-step estimates into a trajectory.

> Graduation project, Department of Computer and Automation Engineering, Faculty of
> Mechanical and Electrical Engineering, **Damascus University**.

## The simulated network

16 stationary anchor sensors over a 200 × 200 m field. The blue crosses are the offline
positions used to build the training set.

![The simulated sensor network](WSN/WSN.png)

## Results

**Tracking a trajectory.** True path against the two learned estimators, each refined by the
Kalman filter — both follow the turns, with the RFF variant tracking about as closely as the
full SVM.

![Real trajectory vs RFF+Kalman and SVM+Kalman](Results/tra3_k1.png)

**How many Fourier features you actually need.** SVM + KF is the flat baseline; RFF + KF
meets it at 60 components, which is the point of the exercise — the approximation buys you
the same accuracy far more cheaply.

![Error against number of RFF components](Results/kalman_imp.png)

**Learning curve.** Mean absolute error falls from roughly 7 at 100 training examples to
around 4 by 1000.

![RFF learning curves with the Kalman filter](Results/learning%20curv.png)

More plots live in [`Results/`](Results).

## What is in here

| Path | What it does |
| --- | --- |
| [`WSN/`](WSN) | Builds the network: places the anchors, generates RSSI readings and the training points. Used as a library by everything else. |
| [`model/`](model) | Tunes the SVM regressor's parameters and saves the fitted model. |
| [`Random Fourier Features/`](Random%20Fourier%20Features) | Experiments for choosing the RFF parameters and component count. |
| [`Lib/`](Lib) | Kalman filter implementation, in motion models of order 1, 2 and 3. |
| [`trajectory/`](trajectory) | Generates the trajectories used in the study. |
| [`Results/`](Results) | Saved figures from the runs. |
| [` main.py`](%20main.py) | The study itself — runs the network, evaluates each algorithm and plots every result above. |

Motion models investigated: order 1, 2 and 3. Estimators: SVM, and SVM approximated with
Random Fourier Features.

## Running it

Python with:

```
scipy
numpy
scikit-learn
matplotlib
```

Then run the study:

```sh
python " main.py"
```

> **Note** — the entry script is committed with a leading space in its filename
> (`" main.py"`), so it has to be quoted. Worth renaming if you fork this.

## Author

[**Abdullah Alsaidi**](https://github.com/abdullahalsaidi16) — see also the
[contributors](https://github.com/abdullahalsaidi16/wsn-localization-tracking/graphs/contributors).

## License

[GNU GPL-3.0](LICENSE.md).
