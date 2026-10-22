# neo.js
<b>neo.js</b> is an artificial neural network library written from scratch in vanila (pure) JavaScript.

<img src="Assets/Diagram/Example diagram of neo network.jpg" >

Build the neural network using `.build ([structure])`, train the model using `.train(traning_Datasets)` , run the model using `.run([actual_Datasets])` , save the model using `.save ( )` and load a pre-trained model using `.load (neo_model_data)` method.

<img src="Assets/ScreenShot.jpg" >

---
## Tables of contents
 - [What's new](#whats-new)
 - [How to include neo.js library in your project](#how-to-include-neojs-library-in-your-project)
 - [How to use this library](#how-to-use-this-library)
   - [Step 1, a new neo () object](#step-1-a-new-neo--object)
   - [Step 2, Building the network](#step-2-building-the-network)
   - [Step 3, Training for a better model](#step-3-training-for-a-better-model)
   - [Step 4, Running the model](#step-4-running-the-model)
 - [APIs (methods and properties)](#apis-methods-and-properties)
   - [`.build ()` method](#build--method)
   - [`.config` property](#config-property)
   - [`.train ()` method](#train--method)
   - [`.run ()` method](#run--method)
   - [`.save ()` and the `.load()` method](#save--and-the-load-method)
 - [License](#license)
 - [My other projects](#my-other-projects)
---
## What's new
 - ### v1.0.2
     1. <ins>Optimize the code:</ins> The length values of the loops are now cached to avoid repeated access to the length property, improving overall performance.
     2. <ins>Added `output_Transformation`:</ins> neo.js now supports 4+1 types of output transformation (`'normalize'`, `'softmax'`, `'hardmax'`, `'threshold'` and a default `'none'`) for transforming the result(s) of the output layer. The two new property `output_Transformation` and `transformation_Factor` are added to the `config` for adjusting the transformation.
     3. <ins>Added support for specifying the numeric precision:</ins> During the `.build( )` neo.js now allows to specify the floating-point number precision used to store weights and biases. This affects memory usage, numerical precision and overall performance of the neo.js. Supported options are `'f16'` for 'Float16', `'f32'` for 'Float32' and `'f64'` for 'Float64'. The default is `'f32'`.
     4. <ins>Updated the .neom (NEO's Model) data format version from v1.0.0 to v1.0.1:</ins> Updated the model data format to support the new numerical precision option and the output_Transformation feature. The `.save()` method now stored the model data in v1.0.1 neom format. The `.load()` method now loads only model data saved in the v1.0.1 format and rejects data saved in any other format version to ensure compatibility.

 - ### v1.0.1
     1. <ins>Added activation function name validation:</ins> Added an error message when an invalid or unsupported activation function name is provided.
     2. <ins>Optimized the `tanh` activation function:</ins> The implementation of the `tanh` activation function has been switched from the `Math.exp()` expression based approch to the native `Math.tanh()` based approch for better accuracy and efficiency.
     3. <ins>Fixed the iteration counter in `logMode`</ins> Fixed the iteration counter to display the proper iteration counting when `logMode` is enabled during the training.

 - ### v1.0.0
     1. Supports feed-forward neural network architecture.
     2. Supports customizable network structure with specified input and output nodes, hidden layers, and neurons per layer.
     3. Supports 5 activation functions:
        - `sigmoid`
        - `relu`
        - `leaky-relu`
        - `tanh`
        - `linear`
     4. Supports for configuration of activation function for hidden layers and output layer separately.
     5. Supports adjustable learning step.
     6. Supports various training options for customizing the training process:
        - `LogMode`
        - `Iterations`
        - `acceptable_MSE`
     7. Provides detailed training information during the traning(`let info = .train ()`)
     8. Supports for storing it's model data into text data using the built-in `.save ()` method for future use.
     9. Supports for loading a previously saved or a pre-trained model data using the built-in `.load ()` method.

---

[⬆ Back to the Tables of Contents ⬆](#tables-of-contents)

---
---

## How to include neo.js library in your project?
To use this library, firstly, you need to link **neo.js** to your project. You can do that by using two ways:

1. **Download / Clone and Use:** Download or clone the repository and use the **neo.js** file in your project.
2. **Use via CDN:**
     - Use the library directly via CDN using the following script tag: ```https://cdn.jsdelivr.net/gh/nirmalpaul383/neo.js@1.0.2/neo.js```
     - For using it in browser/webpage you can use ```<script src="https://cdn.jsdelivr.net/gh/nirmalpaul383/neo.js@1.0.2/neo.js"></script>```

---

[⬆ Back to the Tables of Contents ⬆](#tables-of-contents)

---
---

## How to use this library?
For example: teaching our neo network to learn the behavior of a XOR gate. <br><br>
XOR (for two input) outputs: 1 only when its two inputs are different or else outputs 0
```javascript
//For example: teaching our neo network to learn the behavior of a XOR gate
//XOR (for two input) outputs: 1 only when its two inputs are different or else outputs 0

//Traning data sets for XOR (2 input and 1 output)
const training_data_arry = [
  [ [0, 0],  [0] ] ,
  [ [0, 1],  [1] ] ,
  [ [1, 0],  [1] ] ,
  [ [1, 1],  [0] ]
];
```

### Step 1, Creating a `new neo ()` object:
<ins> Creating a new neo object:</ins> After including the <b> neo.js </b>, you will need to create a `new neo object` using the `neo class` :
```javascript
//After including the neo.js

//Creating a new neo object with the neo class
const neo_net = new neo();
```

### Step 2, Building the network: 
After creating a new neo object you will need to build a neo network structure with `.build ( )` method that suits the neural network application:

```javascript
//For a XOR gate where input nodes = 2, output nodes = 1:

//Building a neo network structure with 2 input node, 3 hidden layers (with respectively 6 , 4 and 5 neo cores (neurons) in its hidden layer) and 1 output node
neo_net.build (2, [6, 4, 5], 1);
```

### Step 3, Training for a better model:
The next step is to train the model of the neo network using the `.train ()` method
```javascript
//For traning the neo network with .train () method
neo_net.train(training_data_arry);
```

### Step 4, Running the model:
For running the neo network the `.run ()` method can be used
```javascript
//For running the neo network with .run () method and output to the console
console.log(neo_net.run([0,1])); //in my case the Output is: 0.9380

//For running the neo network with .run () method and output to the console
console.log(neo_net.run([0,0])); //in my case the Output is: 0

//For running the neo network with .run () method and output to the console
console.log(neo_net.run([1,1])); //in my case the Output is: 0.0211

```
> <b>Note:</b>
> The output may vary each time after the model is trained. To reproduce the same output, save a trained model by using the `.save()` method and load it using `.load()` method.

---

[⬆ Back to the Tables of Contents ⬆](#tables-of-contents)

---

---
## APIs (methods and properties)
A `neo` network objects has various methods and properties for doing various things.

### `.build ()` method
`.build ()` method creates the structure for neo network (input layer's nodes, hidden layers's nodes and output layer's nodes). It takes 3 parameters:

- <b>Parameter 1 (for defining input layer):</b> Expects the number of desired nodes in the input layer.

- <b>Parameter 2 (for defining hidden layers):</b> Expects array with the elements containing the number in its each element. The each element 's number defines that the how many nodes is desired in each hidden layer and the length of this array represents the number of desired hidden layers in the network.

- <b>Parameter 3 (for defining output layer):</b> Expects the number desired nodes in the output layer.

- <b>Parameter 4 (for specifying the numerical precision):</b> This optional parameter specifies the numerical precision of the neo network structure. This parameter affects the memory usage, numerical precision and the overall performance of the neo.js. Supported options are: `'f16'` for Float16, `'f32'` for Float32 and `'f64'` for Float64. Default is `'f32'`

```javascript
//Building a neo network structure with 4 input nodes, 4 hidden layers (with respectively 10 , 5, 15 and 20 neo cores (neurons) in its hidden layer), 2 output nodes and with float-32 numerical precision
neo_net.build (4, [10, 5, 15, 20], 2, 'f32');
```

> <b>[NOTE] :</b>
> The `.build ()` method can be used for creating as many input nodes, hidden layers, hidden-layer nodes, and output nodes as desired. However, adding more nodes and hidden layers makes the network more complex and may require more time to train.

---
### `.config` property
The <b>neo</b> network object has a `.config` property for configuring various setting for the neo network:
- <b>`hidden_Activation` :</b> This parameter can be used for specifying the activation function <ins>for the hidden layer</ins> 's neo cores (/ neurons). <br> `'sigmoid'`, `'relu'`, `'leaky-relu'`, `'tanh'` and `'linear'` option can be specifed ; default is `'relu'`

- <b>`output_Activation` :</b> This parameter can be used for specifying the activation function for <ins>the output layer</ins> 's neo cores (/ neurons). <br> `'sigmoid'`, `'relu'`, `'leaky-relu'`, `'tanh'` and `'linear'` option can be specifed ; default is `'relu'`

- <b>`learning_Step` :</b> This parameter specifies the learning step of the neo network durning the traning. A lower learning step means neo network can learn more accurately but may require more training time. A larger learning step means neo network can learn more quickly but may reduce the accuracy. Default is `0.1`

- <b>`alpha` :</b> This parameter can be used for specifying the alpha value for leaky-relu activation function. Default value is `0.01`

- <b>`output_Transformation` :</b> This parameter specifies the name of function for transforming the output layer's results. <b>neo.js</b> supports 4+1 output transformation functions (`'normalize'`, `'softmax'`, `'hardmax'` , `'threshold'` and a default `'none'`).
  
  - `'normalize'`: This function transforms each element relative to the total sum, ensuring that the final sum of all elements equals exactly 1 (or 0 if all inputs are zero).
  - `'softmax'`: The softmax function transforms each element into a value between 0 and 1, where the sum of all output values equals 1. The additional parameter (transformation_Factor) acts here as a 'temperature' parameter and it can control the behaviour of the softmax function.
  - `'hardmax'`: The hardmax function transforms the maximum valued element(s) into 1 and 0 to all other elements.
  - `'threshold'`: The threshold function transforms each element into 1 if that element is greater than or equal to the specified threshold value or otherwise 0. The additional parameter (transformation_Factor) acts here as threshold value holder.
  - `'none'`: If the output_Transformation function is set to 'none', then the output layer's results will NOT be transformed.

- <b>`transformation_Factor` :</b> This parameter can be used for specifying the additional value for the output_Transformation function (if needed). E.g. it can act as 'temperature' parameter in the 'softmax' output_Transformation function; or it can acts as the threshold 's value holder for the 'threshold' output_Transformation function.

```javascript
//Changing the learning_step setting in the neo network object
neo_net.config.learning_Step = 0.03
```
---

### `.train ()` method
Training of a neural network is a computationally expensive task and may take some time and system resources, depending on the complexity of the neo network structure and the size of the training dataset array.

- <b>Training dataset array:</b> The training dataset array contains the input data (s) and their corresponding expected output value(s) in array format. More data sets means more accurate model , but may requirs more time to train. <br> <br> Each data set contains an input array with its corresponding output array:
```javascript
//For example: A student Performance traning data sets with 4 input and 2 output
const stdnts_prfrmnce_dataSets = [

  //[  [input-1, input-2, input-3,..., input-n] , [output-1, output-2, ...output-n] ] ---> General structure for traning dataset

  //Inputs: study hours, attendance, assignments completed, previous score
  //Outputs: Exam score, pass (1) or fail (0)
  [ [2, 60, 5, 45],   [50, 0] ] ,  //Dataset 1
  [ [5, 80, 8, 65],   [72, 1] ] ,  //Dataset 2
  [ [6, 77, 7, 85],   [85, 1] ] ,  //Dataset 3
  [ [8, 95, 5, 80],   [87, 1] ] ,  //Dataset 4
  [ [8, 50, 3, 45],   [42, 0] ] ,  //Dataset 5
  [ [9, 65, 9, 55],   [60, 0] ]    //Dataset 6

]
```
- <b>`.train ()` method:</b> The `.train()` method of the neo class object can be used to train it's model and produce a better model for more accurate predictions using a training dataset array. <br><br> It supports a optional option object parameter for configuring the training process:
```javascript
//Traning the neo network using the train method
neo_net.train( stdnts_prfrmnce_dataSets , {

   logMode: true, //If true the current MSE willl be log throughout every iterations (default is false).

   iterations: 650, //Specifies the maximum times the optimise () method should be called (iteration count). More iteration means more accurate neo network but takes more time to be trained (default is 500).

   acceptable_MSE: 0.008  //Specifies the maximum acceptable Mean Squared Error (MSE). Training will be stoped when the calculated MSE is less than or equal to this value (default is 0.01)
   
});
```
- <ins>Return value of the .train () method:</ins> The .train () method returns a information string regarding the training:
```javascript
//Traning the neo network using the train method
let train_info = neo_net.train(stdnts_prfrmnce_dataSets);

console.log (train_info);
//Outputs:
//
// Iterations: 650 ; Traning time: 11467.8663 ms;
// Initial MSE: 35766.52587242568; Final MSE: 0.16878662959244073;
// Error (MSE) Reduction: 35766.35708579609 ; Error (MSE) Reduction (%): 99.99952808771478 % ;
// (approx) Time takes (in ms) / iteration : 17.64287123076923 ms ;
// (approx) Iteration completed / time (in ms) :  0.05668011668395541 Numbers

```

### `.run ()` method
The `neo` network can produce outputs based on it's network model data.
- `.run()` method can be used for running the current neo network model data and making the output(s) value in a array format:
```javascript
//For storing the actual input_data for testing the model
let input_data_arry = [6, 77, 7, 85];

//For running the neo network and storing the result into the result variable
let result = neo_net.run( input_data_arry ); //expected output: [85, 1]

//For outputing the prediction to the console
console.log(result); //Actual output: [ 84.9950, 1.0073 ]
```

### `.save ()` and the `.load()` method
The trained model of the neo network can be stored as a string using the `.save()` method. The `.load()` method can then use this string data to restore the network and the model whenever needed. <br>This is especially useful for preserving models that require significant time to train, allowing those to be re-used later without having to re-train the network from the scratch.

- `.save()` method:
```javascript
//For storing the model data into a string
let model_for_XOR = neo_net.save();

//It is basically a text based custom format where the ";" works as the data separator
```

- `.load()` method:
```javascript
//For creating another object with the neo class
const another_neo_obj = new neo();

//After storing the neo network 's model as a string representation
//For loading the previously saved model data into the newly created neo object
another_neo_obj.load(model_for_XOR);

//For testing the newly created neo object with the same actual data
console.log(another_neo_obj.run(input_data_arry)); //Outputs: [ 84.9950, 1.0073 ]  (Outputs are same as the neo_net)
```

> <b>Note:</b> You can store this model data into a file and load it later using:
> 1. `Blob` and `<input type="file">` in <b>web browser / runtime</b>.
> 2. `fs.writeFile()` and `fs.readFile()` in <b>Node.js</b>.
> 3. `Bun.write()` and `Bun.file()` in <b>Bun runtime</b>.

---

[⬆ Back to the Tables of Contents ⬆](#tables-of-contents)

---
---


## License:
<b>neo.js</b> is originally written by [me (N Paul)](https://github.com/nirmalpaul383) and it is licensed under the GNU General Public License v3.0 (GPLv3) .

Additionally, while not legally required, I kindly request that if you use, modify, or distribute this project, please give credit to the original author name, Nirmal Paul (N Paul) (https://github.com/nirmalpaul383). 
<br><br>
I have dedicated significant time for developing this project, ensuring that every line of code is clean, well-structured, and easy to understand. Your acknowledgment of the original authorship is greatly appreciated.

---

[⬆ Back to the Tables of Contents ⬆](#tables-of-contents)

---
---

## My other projects
If you think that the <b>`neo.js`</b> is a useful project, please consider giving a [star ☆ to the `neo.js` project](https://github.com/nirmalpaul383/neo.js) on the GitHub.<br>
You can find my other open source projects:
- [`ViewPoint.js`](https://github.com/nirmalpaul383/ViewPoint) : A Math expression parser and evaluator with support of runtime data-type checking written in native JS.
- [`MathPad+`](https://github.com/nirmalpaul383/MathPad_plus_) : MathPad+ is a lightweight mathematical expression playground powered by the ViewPoint evaluator.
- [`Voice Ccommands`](https://github.com/nirmalpaul383/Voice_Commands) : A customizable Voice Assistant that supports installable custom commands / functions via Voice Command Loader (.vcl) files. Users can extend its functionality by creating their own commands using JavaScript and distributing them through .vcl files.
- [`WebCell-Web-SpreadSheet`](https://github.com/nirmalpaul383/WebCell-Web-SpreadSheet) : A web SpreadSheet project written in web language (html, css and JavaScript). It can be run completely offline.
- and more from [my github profile](https://github.com/nirmalpaul383)

---

[⬆ Back to the Tables of Contents ⬆](#tables-of-contents)

---
---
