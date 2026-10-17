# Data-Driven CFD Surrogate Modeling Using Deep Learning

### Author
Afzal Hussain

### Preface
This January, during the starting of the 7th semester I completed Andrew Ng’s [Deep Learning Specialization](https://www.coursera.org/specializations/deep-learning) from Coursera. This work was motivated by the potential application of deep learning algorithms in mechanical engineering. The core hypothesis was that deep learning models could predict fluid simulation outcomes, which motivated this research.

This report documents the complete pipeline, from simulation generation to deep learning model development and evaluation.

### Case Setup
For this research, I have used [OpenFOAM](https://openfoam.org/), a C++ open source implementation for pre-processing, solving and post-processing CFD simulation. The reason behind choosing OpenFOAM because of its flexibility and automation. Here [supersonic flow over a forward-facing step](https://www.openfoam.com/documentation/tutorial-guide/3-compressible-flow/3.2-supersonic-flow-over-a-forward-facing-step) is investigated. The problem description involves a flow of Mach 3 at an inlet to a rectangular geometry with a step near the inlet region that generates shock waves. The geometry is shown below:

<p align="center">
  <img src="assets/geometry.png">
</p>

### Generating simulation 
This was the most resource-intensive phase — generating sufficiently varied simulations for training requires substantial computational resources. Deep learning requires large datasets; accordingly, thousands of simulations of varying geometries were generated to enable prediction on unseen configurations. For this purpose, I changed the position of step from near the inlet region to the outlet i.e.  0.1 < x < 2.9, ranging it height 0.1 < y < 0.4. This was accomplished via a Python script. Making the dataset contains the following steps:
  1. Make 1500 random coordinates within some constraints.
  2. Remove previous simulation file (if it exists).
  3. Copy the OpenFOAM _forwardStep_ directory.
  4. Remove _blockMeshDict_ file from system directory.
  5. Execute `gen_blockMeshDict.py` to write _blockMeshDict_ and _cellInformation_ file.
     _cellInformation_ consists cell number of three rectangle (x_cell * y_cell) (2D simulation). 
  6. Move _blockMeshDict_ file to system directory
  7. Move _cellInformation_ file to home directory
  8. Now execute `sim_cmd` from terminal. 
  9. It uses _sonicFoam_ to run simulation.
10. And _foamToVTK_ to convert the simulation result into .vtk file.

This process generated approximately 168 GB of raw simulation data. But all this data is not necessary for training, I extract only velocity at x & y direction, pressure, and temperature of each cell. The dl_data_generation script was used for this extraction.

### Convolutional LSTM
For long-range dependencies in time-series data, [LSTM](http://colah.github.io/posts/2015-08-Understanding-LSTMs/) has been using for a longer period of time, that has proven stable and powerful. But typical LSTM implementation deals with 1-D series data only, as fluid simulations involve spatial data, this work employs a variant of LSTM, proposed by [X Shi et al.](https://arxiv.org/abs/1506.04214), where state-to-state and input-to-state transitions are replaced by convolution operation. The key equations are shown below, where ‘∗’ denotes the [convolution operator](https://en.wikipedia.org/wiki/Convolution) and ‘◦’ denotes the [Hadamard product](https://en.wikipedia.org/wiki/Hadamard_product_(matrices)):

<p align="center">
  <img height="500" width="750" src="assets/C-LSTM.png">
</p>

### Deep Learning Model 

As fluid simulation is time-dependent I have used three [TimeDistributed](https://keras.io/api/layers/recurrent_layers/time_distributed/) [Conv2D](https://keras.io/api/layers/convolution_layers/convolution2d/) followed by a TimeDistributed [MaxPooling2D](https://keras.io/api/layers/pooling_layers/max_pooling2d/). After that [ConvLSTM2D](https://keras.io/api/layers/recurrent_layers/conv_lstm2d/) has been performed. This model initially exhibited slow convergence, so a ResNet-style architecture was incorporated to accelerate convergence. Using ResNet has significantly improved the model performance and accuracy. The whole model is shown below:

<p align="center">
  <img src="assets/my_model.png">
</p>

### Results and Discussion

The model was evaluated on geometries unseen during training. The obtained results are realistic, competitive in accuracy; it successfully shows discontinuities in shock waves, emanating from ahead of the base of the step, and also captures the time-dependent development of the shock-waves. While this work has been performed on one problem specification, it illustrates the viability of data-driven approaches in computational fluid dynamics. Below a comparison between actual simulation and the predicted one by the model is shown for velocity, pressure and temperature at t = 1, 2 \& 3 seconds.

##### Velocity

<p align="center">
  <img src="assets/plots/U/1s.png">
  <img src="assets/plots/U/3s.png">
  <img src="assets/plots/U/5s.png">
</p>

##### Pressure

<p align="center">
  <img src="assets/plots/p/1s.png">
  <img src="assets/plots/p/3s.png">
  <img src="assets/plots/p/5s.png">
</p>

##### Temperature

<p align="center">
  <img src="assets/plots/T/1s.png">
  <img src="assets/plots/T/3s.png">
  <img src="assets/plots/T/5s.png">
</p>

### Conclusion

In the past few years, deep learning has exhibited unprecedented competency and efficiency in image classification, speech recognition, weather forecasting, self-driving cars and many other domains, due to the large availability of data. In this work, we propose an end-to-end deep learning model operating on spatiotemporal flow field sequences, where both the input and output are grid-based representations of the domain, having convolutional structures in both the input-to-state and state-to-state transitions. The proposed model is trained and evaluated on supersonic flow over a forward-facing step; the obtained results are realistic, competitive in accuracy while illustrating the viability of data-driven approaches in computational fluid dynamics.

### Related Research

[Turbulence Modeling Gateway](https://tmbwg.github.io/turbmodels/) \
[Maziar Raissi's Research](https://github.com/maziarraissi) \
[Data-driven Fluid Simulations using Regression Forests](https://cgl.ethz.ch/Downloads/Publications/Papers/2015/Jeo15a/Jeo15a.pdf) \
[Convolutional Neural Networks for Steady Flow Approximation](https://www.research.autodesk.com/publications/convolutional-neural-networks-for-steady-flow-approximation/) \
[Application of Convolutional Neural Network to Predict Airfoil Lift Coefficient](https://arxiv.org/abs/1712.10082)
