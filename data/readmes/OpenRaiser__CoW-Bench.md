# COW-BENCH

## Table of Contents

<p><strong><a href="#modal">Modal</a></strong></p>
<ul>
<li><a href="#modal--subj-attr">Subj-Attr</a>
<ul>
<li><a href="#modal--subj-attr01--prompt"><em>Generate a fish with the same material.</em></a></li>
<li><a href="#modal--subj-attr02--prompt"><em>Generate a car with the same style.</em></a></li>
<li><a href="#modal--subj-attr03--prompt"><em>Generate a dog with the same style.</em></a></li>
</ul>
</li>
<li><a href="#modal--local-edit">Local-Edit</a>
<ul>
<li><a href="#modal--local-edit01--prompt"><em>Only change the digital clock display: simulate the time on the digital clock ch…</em></a></li>
<li><a href="#modal--local-edit02--prompt"><em>Only make the clock's hands rotate: simulate the clock's minute hand moving from…</em></a></li>
<li><a href="#modal--local-edit03--prompt"><em>Only make the clock's hands rotate: simulate the hands moving as if time is pass…</em></a></li>
</ul>
</li>
<li><a href="#modal--multi-const">Multi-Const</a>
<ul>
<li><a href="#modal--multi-const01--prompt"><em>Generate a realistic image containing only three subjects, and satisfy all bindi…</em></a></li>
<li><a href="#modal--multi-const02--prompt"><em>Generate a realistic image containing only three subjects, and satisfy all bindi…</em></a></li>
<li><a href="#modal--multi-const03--prompt"><em>Produce a realistic image containing exactly three subjects: Gardener C: wearing…</em></a></li>
</ul>
</li>
</ul>

<p><strong><a href="#modalxspatial">ModalxSpatial</a></strong></p>
<ul>
<li><a href="#modalxspatial--sem-mv">Sem-MV</a>
<ul>
<li><a href="#modalxspatial--sem-mv01--prompt"><em>Rotate the camera 360 degrees to display multiple viewpoints from different angl…</em></a></li>
<li><a href="#modalxspatial--sem-mv02--prompt"><em>Rotate the camera slightly to the left to show four discrete viewpoints of the s…</em></a></li>
<li><a href="#modalxspatial--sem-mv03--prompt"><em>As the camera rotates to the left, generate a sequence where the apple must rema…</em></a></li>
</ul>
</li>
<li><a href="#modalxspatial--sem-hier">Sem-Hier</a>
<ul>
<li><a href="#modalxspatial--sem-hier01--prompt"><em>Put only the pear inside the bowl. The orange and banana must remain outside and…</em></a></li>
<li><a href="#modalxspatial--sem-hier02--prompt"><em>First, put the red ball inside the box. Then, without moving the yellow block, e…</em></a></li>
<li><a href="#modalxspatial--sem-hier03--prompt"><em>Take only the apple out of the bowl and place it next to the bowl. The banana an…</em></a></li>
</ul>
</li>
<li><a href="#modalxspatial--sem-planar">Sem-Planar</a>
<ul>
<li><a href="#modalxspatial--sem-planar01--prompt"><em>The yellow star moves upward. The red star moves rightward. The blue star moves…</em></a></li>
<li><a href="#modalxspatial--sem-planar02--prompt"><em>The feathered bird flies upward and then stops. The other two birds fly downward…</em></a></li>
<li><a href="#modalxspatial--sem-planar03--prompt"><em>The dog with the collar moves to the right. The other two dogs move to the left.</em></a></li>
</ul>
</li>
</ul>

<p><strong><a href="#modalxtemporal">ModalxTemporal</a></strong></p>
<ul>
<li><a href="#modalxtemporal--attr-dyn">Attr-Dyn</a>
<ul>
<li><a href="#modalxtemporal--attr-dyn01--prompt"><em>A floating sphere in a dark room. The sphere is red in the first frame. The sphe…</em></a></li>
<li><a href="#modalxtemporal--attr-dyn02--prompt"><em>The sun sets, stars appear, and the moon rises. This cycle takes 10 seconds. The…</em></a></li>
<li><a href="#modalxtemporal--attr-dyn03--prompt"><em>A spinning top on a table. The top's color must cycle in this exact order: blue…</em></a></li>
</ul>
</li>
<li><a href="#modalxtemporal--trigger-event">Trigger-Event</a>
<ul>
<li><a href="#modalxtemporal--trigger-event01--prompt"><em>The phone must stay off until the power button is pressed. At the moment the but…</em></a></li>
<li><a href="#modalxtemporal--trigger-event02--prompt"><em>When a hand is detected under the sensor, the faucet turns on instantly and wate…</em></a></li>
<li><a href="#modalxtemporal--trigger-event03--prompt"><em>The lantern must stay closed until it gets dark. At the moment it gets dark, the…</em></a></li>
</ul>
</li>
<li><a href="#modalxtemporal--long-horizon">Long-Horizon</a>
<ul>
<li><a href="#modalxtemporal--long-horizon01--prompt"><em>The dog runs in a park. The red collar must remain exactly the same</em></a></li>
<li><a href="#modalxtemporal--long-horizon02--prompt"><em>The car drives along the road. The blue stripe must remain exactly the same</em></a></li>
<li><a href="#modalxtemporal--long-horizon03--prompt"><em>The car speeds through straightaways and curves. The logo must remain exactly th…</em></a></li>
</ul>
</li>
</ul>

<p><strong><a href="#spatial">Spatial</a></strong></p>
<ul>
<li><a href="#spatial--mv-3d">MV-3D</a>
<ul>
<li><a href="#spatial--mv-3d01--prompt"><em>Rotate the camera and zoom in to show four viewpoints of the same static office.…</em></a></li>
<li><a href="#spatial--mv-3d02--prompt"><em>Move the camera to the left and rotate it to show three viewpoints of the same b…</em></a></li>
<li><a href="#spatial--mv-3d03--prompt"><em>Rotate and pan the camera to the left and slightly downward to show three differ…</em></a></li>
</ul>
</li>
<li><a href="#spatial--occ-contain">Occ-Contain</a>
<ul>
<li><a href="#spatial--occ-contain01--prompt"><em>Slowly close the drawer. The book should be gradually occluded as the drawer clo…</em></a></li>
<li><a href="#spatial--occ-contain02--prompt"><em>Move the box to the right. The book should be fully revealed.</em></a></li>
<li><a href="#spatial--occ-contain03--prompt"><em>Move the cloud slowly upward. The sun and mountains should be gradually revealed…</em></a></li>
</ul>
</li>
<li><a href="#spatial--planar-2d">Planar-2D</a>
<ul>
<li><a href="#spatial--planar-2d01--prompt"><em>The left cat moves to the left, and the right cat moves to the right. Keep the c…</em></a></li>
<li><a href="#spatial--planar-2d02--prompt"><em>The left balloon moves upward, and the right balloon moves downward.</em></a></li>
<li><a href="#spatial--planar-2d03--prompt"><em>The left ball rolls to the left and stops, while the right ball rolls to the rig…</em></a></li>
</ul>
</li>
</ul>

<p><strong><a href="#spatialxtemporal">SpatialxTemporal</a></strong></p>
<ul>
<li><a href="#spatialxtemporal--3d-loop">3D-Loop</a>
<ul>
<li><a href="#spatialxtemporal--3d-loop01--prompt"><em>Navigate through the hallway into a sequence of connected rooms—a bedroom, a bat…</em></a></li>
<li><a href="#spatialxtemporal--3d-loop02--prompt"><em>Step out from the bedroom onto a balcony overlooking a city skyline during dayti…</em></a></li>
<li><a href="#spatialxtemporal--3d-loop03--prompt"><em>Exit the warm cabin into a blizzard outdoors, experience snow and wind effects,…</em></a></li>
</ul>
</li>
<li><a href="#spatialxtemporal--maze">maze</a>
<ul>
<li><a href="#spatialxtemporal--maze01--prompt"><em>This is a maze diagram. The objective is to guide the red dot from the bottom-le…</em></a></li>
<li><a href="#spatialxtemporal--maze02--prompt"><em>This is a maze diagram. The objective is to guide the red dot from the bottom-le…</em></a></li>
<li><a href="#spatialxtemporal--maze03--prompt"><em>This is a maze diagram. The objective is to guide the red dot from the bottom-le…</em></a></li>
</ul>
</li>
<li><a href="#spatialxtemporal--occ-motion">Occ-Motion</a>
<ul>
<li><a href="#spatialxtemporal--occ-motion01--prompt"><em>Camera remains static, but a foreground car moves horizontally from left to righ…</em></a></li>
<li><a href="#spatialxtemporal--occ-motion02--prompt"><em>Camera tracks alongside a moving car to the left in a suburban environment.</em></a></li>
<li><a href="#spatialxtemporal--occ-motion03--prompt"><em>Camera zooms in during rain, with raindrops on a windshield.</em></a></li>
</ul>
</li>
</ul>

<p><strong><a href="#temporal">Temporal</a></strong></p>
<ul>
<li><a href="#temporal--slow-evol">Slow-Evol</a>
<ul>
<li><a href="#temporal--slow-evol01--prompt"><em>One hour passes.</em></a></li>
<li><a href="#temporal--slow-evol02--prompt"><em>Several hours pass.</em></a></li>
<li><a href="#temporal--slow-evol03--prompt"><em>Thirty minutes pass.</em></a></li>
</ul>
</li>
<li><a href="#temporal--stage-order">Stage-Order</a>
<ul>
<li><a href="#temporal--stage-order01--prompt"><em>Demolish a house built with building blocks.</em></a></li>
<li><a href="#temporal--stage-order02--prompt"><em>Paint a portrait with oil paints.</em></a></li>
<li><a href="#temporal--stage-order03--prompt"><em>A butterfly undergoes metamorphosis from egg to adult.</em></a></li>
</ul>
</li>
<li><a href="#temporal--worldline">Worldline</a>
<ul>
<li><a href="#temporal--worldline01--prompt"><em>A ceiling fan rotates continuously , with blades spinning smoothly and housing u…</em></a></li>
<li><a href="#temporal--worldline02--prompt"><em>A pendulum with engraved markings swings back and forth for ten minutes.</em></a></li>
<li><a href="#temporal--worldline03--prompt"><em>The sun sets steadily over thirty minutes, with the sky colors and shadows evolv…</em></a></li>
</ul>
</li>
</ul>


<a name="modal"></a>

## **Modal**

<a name="modal--subj-attr"></a>

### Subj-Attr

<a name="modal--subj-attr01--prompt"></a>

#### Generate a fish with the same material.

Prompt

```text
Generate a fish with the same material.
```

Input image

<div style="text-align: left;">
  <img src="model_output/Modal/input/inv01/inv01.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</div>

<a name="modal--subj-attr01--gpt-image-15"></a>

##### GPT image 1.5

<p align="left">
  <img src="model_output/Modal/GPT image 1.5/Subj-Attr01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1.5/Subj-Attr01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1.5/Subj-Attr01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1.5/Subj-Attr01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr01--nano-banana-pro"></a>

##### Nano Banana Pro

<p align="left">
  <img src="model_output/Modal/Nano Banana Pro/Subj-Attr01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana Pro/Subj-Attr01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana Pro/Subj-Attr01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana Pro/Subj-Attr01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr01--veo-31"></a>

##### Veo 3.1

<p align="left">
  <img src="model_output/Modal/Veo 3.1/Subj-Attr01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Veo 3.1/Subj-Attr01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Veo 3.1/Subj-Attr01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Veo 3.1/Subj-Attr01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr01--seedream-50"></a>

##### Seedream 5.0

<p align="left">
  <img src="model_output/Modal/Seedream 5.0/Subj-Attr01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 5.0/Subj-Attr01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 5.0/Subj-Attr01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 5.0/Subj-Attr01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr01--gpt-image-1"></a>

##### GPT image 1

<p align="left">
  <img src="model_output/Modal/GPT image 1/Subj-Attr01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1/Subj-Attr01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1/Subj-Attr01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1/Subj-Attr01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr01--nano-banana"></a>

##### Nano Banana

<p align="left">
  <img src="model_output/Modal/Nano Banana/Subj-Attr01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana/Subj-Attr01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana/Subj-Attr01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana/Subj-Attr01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr01--nano-banana-2"></a>

##### Nano Banana 2

<p align="left">
  <img src="model_output/Modal/Nano Banana 2/Subj-Attr01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana 2/Subj-Attr01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana 2/Subj-Attr01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana 2/Subj-Attr01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr01--emu35"></a>

##### Emu3.5

<p align="left">
  <img src="model_output/Modal/Emu3.5/Subj-Attr01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Emu3.5/Subj-Attr01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Emu3.5/Subj-Attr01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Emu3.5/Subj-Attr01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr01--kling"></a>

##### kling

<p align="left">
  <img src="model_output/Modal/kling/Subj-Attr01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/kling/Subj-Attr01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/kling/Subj-Attr01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/kling/Subj-Attr01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr01--seedream-45"></a>

##### Seedream 4.5

<p align="left">
  <img src="model_output/Modal/Seedream 4.5/Subj-Attr01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.5/Subj-Attr01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.5/Subj-Attr01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.5/Subj-Attr01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr01--sora"></a>

##### sora

<p align="left">
  <img src="model_output/Modal/sora/Subj-Attr01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/sora/Subj-Attr01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/sora/Subj-Attr01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/sora/Subj-Attr01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr01--seedream-40"></a>

##### Seedream 4.0

<p align="left">
  <img src="model_output/Modal/Seedream 4.0/Subj-Attr01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.0/Subj-Attr01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.0/Subj-Attr01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.0/Subj-Attr01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr01--skyreels-v2"></a>

##### SkyReels-V2

<p align="left">
  <img src="model_output/Modal/SkyReels-V2/Subj-Attr01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/SkyReels-V2/Subj-Attr01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/SkyReels-V2/Subj-Attr01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/SkyReels-V2/Subj-Attr01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr01--wan22-i2v-14b"></a>

##### Wan2.2-I2V-14B

<p align="left">
  <img src="model_output/Modal/Wan2.2-I2V-14B/Subj-Attr01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Wan2.2-I2V-14B/Subj-Attr01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Wan2.2-I2V-14B/Subj-Attr01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Wan2.2-I2V-14B/Subj-Attr01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr01--bagel"></a>

##### BAGEL

<p align="left">
  <img src="model_output/Modal/BAGEL/Subj-Attr01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/BAGEL/Subj-Attr01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/BAGEL/Subj-Attr01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/BAGEL/Subj-Attr01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr01--hunyuanvideo"></a>

##### HunyuanVideo

<p align="left">
  <img src="model_output/Modal/HunyuanVideo/Subj-Attr01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/HunyuanVideo/Subj-Attr01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/HunyuanVideo/Subj-Attr01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/HunyuanVideo/Subj-Attr01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr01--qwen-image"></a>

##### Qwen-Image

<p align="left">
  <img src="model_output/Modal/Qwen-Image/Subj-Attr01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Qwen-Image/Subj-Attr01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Qwen-Image/Subj-Attr01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Qwen-Image/Subj-Attr01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

---

<a name="modal--subj-attr02--prompt"></a>

#### Generate a car with the same style.

Prompt

```text
Generate a car with the same style.
```

Input image

<div style="text-align: left;">
  <img src="model_output/Modal/input/inv02/inv02.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</div>

<a name="modal--subj-attr02--gpt-image-15"></a>

##### GPT image 1.5

<p align="left">
  <img src="model_output/Modal/GPT image 1.5/Subj-Attr02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1.5/Subj-Attr02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1.5/Subj-Attr02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1.5/Subj-Attr02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr02--nano-banana-pro"></a>

##### Nano Banana Pro

<p align="left">
  <img src="model_output/Modal/Nano Banana Pro/Subj-Attr02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana Pro/Subj-Attr02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana Pro/Subj-Attr02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana Pro/Subj-Attr02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr02--veo-31"></a>

##### Veo 3.1

<p align="left">
  <img src="model_output/Modal/Veo 3.1/Subj-Attr02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Veo 3.1/Subj-Attr02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Veo 3.1/Subj-Attr02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Veo 3.1/Subj-Attr02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr02--seedream-50"></a>

##### Seedream 5.0

<p align="left">
  <img src="model_output/Modal/Seedream 5.0/Subj-Attr02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 5.0/Subj-Attr02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 5.0/Subj-Attr02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 5.0/Subj-Attr02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr02--gpt-image-1"></a>

##### GPT image 1

<p align="left">
  <img src="model_output/Modal/GPT image 1/Subj-Attr02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1/Subj-Attr02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1/Subj-Attr02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1/Subj-Attr02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr02--nano-banana"></a>

##### Nano Banana

<p align="left">
  <img src="model_output/Modal/Nano Banana/Subj-Attr02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana/Subj-Attr02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana/Subj-Attr02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana/Subj-Attr02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr02--nano-banana-2"></a>

##### Nano Banana 2

<p align="left">
  <img src="model_output/Modal/Nano Banana 2/Subj-Attr02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana 2/Subj-Attr02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana 2/Subj-Attr02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana 2/Subj-Attr02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr02--emu35"></a>

##### Emu3.5

<p align="left">
  <img src="model_output/Modal/Emu3.5/Subj-Attr02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Emu3.5/Subj-Attr02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Emu3.5/Subj-Attr02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Emu3.5/Subj-Attr02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr02--kling"></a>

##### kling

<p align="left">
  <img src="model_output/Modal/kling/Subj-Attr02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/kling/Subj-Attr02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/kling/Subj-Attr02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/kling/Subj-Attr02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr02--seedream-45"></a>

##### Seedream 4.5

<p align="left">
  <img src="model_output/Modal/Seedream 4.5/Subj-Attr02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.5/Subj-Attr02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.5/Subj-Attr02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.5/Subj-Attr02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr02--sora"></a>

##### sora

<p align="left">
  <img src="model_output/Modal/sora/Subj-Attr02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/sora/Subj-Attr02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/sora/Subj-Attr02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/sora/Subj-Attr02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr02--seedream-40"></a>

##### Seedream 4.0

<p align="left">
  <img src="model_output/Modal/Seedream 4.0/Subj-Attr02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.0/Subj-Attr02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.0/Subj-Attr02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.0/Subj-Attr02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr02--skyreels-v2"></a>

##### SkyReels-V2

<p align="left">
  <img src="model_output/Modal/SkyReels-V2/Subj-Attr02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/SkyReels-V2/Subj-Attr02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/SkyReels-V2/Subj-Attr02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/SkyReels-V2/Subj-Attr02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr02--wan22-i2v-14b"></a>

##### Wan2.2-I2V-14B

<p align="left">
  <img src="model_output/Modal/Wan2.2-I2V-14B/Subj-Attr02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Wan2.2-I2V-14B/Subj-Attr02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Wan2.2-I2V-14B/Subj-Attr02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Wan2.2-I2V-14B/Subj-Attr02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr02--bagel"></a>

##### BAGEL

<p align="left">
  <img src="model_output/Modal/BAGEL/Subj-Attr02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/BAGEL/Subj-Attr02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/BAGEL/Subj-Attr02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/BAGEL/Subj-Attr02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr02--hunyuanvideo"></a>

##### HunyuanVideo

<p align="left">
  <img src="model_output/Modal/HunyuanVideo/Subj-Attr02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/HunyuanVideo/Subj-Attr02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/HunyuanVideo/Subj-Attr02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/HunyuanVideo/Subj-Attr02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr02--qwen-image"></a>

##### Qwen-Image

<p align="left">
  <img src="model_output/Modal/Qwen-Image/Subj-Attr02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Qwen-Image/Subj-Attr02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Qwen-Image/Subj-Attr02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Qwen-Image/Subj-Attr02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

---

<a name="modal--subj-attr03--prompt"></a>

#### Generate a dog with the same style.

Prompt

```text
Generate a dog with the same style.
```

Input image

<div style="text-align: left;">
  <img src="model_output/Modal/input/inv03/inv03.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</div>

<a name="modal--subj-attr03--gpt-image-15"></a>

##### GPT image 1.5

<p align="left">
  <img src="model_output/Modal/GPT image 1.5/Subj-Attr03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1.5/Subj-Attr03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1.5/Subj-Attr03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1.5/Subj-Attr03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr03--nano-banana-pro"></a>

##### Nano Banana Pro

<p align="left">
  <img src="model_output/Modal/Nano Banana Pro/Subj-Attr03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana Pro/Subj-Attr03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana Pro/Subj-Attr03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana Pro/Subj-Attr03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr03--veo-31"></a>

##### Veo 3.1

<p align="left">
  <img src="model_output/Modal/Veo 3.1/Subj-Attr03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Veo 3.1/Subj-Attr03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Veo 3.1/Subj-Attr03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Veo 3.1/Subj-Attr03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr03--seedream-50"></a>

##### Seedream 5.0

<p align="left">
  <img src="model_output/Modal/Seedream 5.0/Subj-Attr03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 5.0/Subj-Attr03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 5.0/Subj-Attr03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 5.0/Subj-Attr03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr03--gpt-image-1"></a>

##### GPT image 1

<p align="left">
  <img src="model_output/Modal/GPT image 1/Subj-Attr03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1/Subj-Attr03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1/Subj-Attr03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1/Subj-Attr03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr03--nano-banana"></a>

##### Nano Banana

<p align="left">
  <img src="model_output/Modal/Nano Banana/Subj-Attr03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana/Subj-Attr03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana/Subj-Attr03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana/Subj-Attr03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr03--nano-banana-2"></a>

##### Nano Banana 2

<p align="left">
  <img src="model_output/Modal/Nano Banana 2/Subj-Attr03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana 2/Subj-Attr03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana 2/Subj-Attr03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana 2/Subj-Attr03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr03--emu35"></a>

##### Emu3.5

<p align="left">
  <img src="model_output/Modal/Emu3.5/Subj-Attr03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Emu3.5/Subj-Attr03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Emu3.5/Subj-Attr03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Emu3.5/Subj-Attr03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr03--kling"></a>

##### kling

<p align="left">
  <img src="model_output/Modal/kling/Subj-Attr03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/kling/Subj-Attr03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/kling/Subj-Attr03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/kling/Subj-Attr03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr03--seedream-45"></a>

##### Seedream 4.5

<p align="left">
  <img src="model_output/Modal/Seedream 4.5/Subj-Attr03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.5/Subj-Attr03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.5/Subj-Attr03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.5/Subj-Attr03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr03--sora"></a>

##### sora

<p align="left">
  <img src="model_output/Modal/sora/Subj-Attr03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/sora/Subj-Attr03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/sora/Subj-Attr03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/sora/Subj-Attr03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr03--seedream-40"></a>

##### Seedream 4.0

<p align="left">
  <img src="model_output/Modal/Seedream 4.0/Subj-Attr03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.0/Subj-Attr03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.0/Subj-Attr03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.0/Subj-Attr03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr03--skyreels-v2"></a>

##### SkyReels-V2

<p align="left">
  <img src="model_output/Modal/SkyReels-V2/Subj-Attr03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/SkyReels-V2/Subj-Attr03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/SkyReels-V2/Subj-Attr03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/SkyReels-V2/Subj-Attr03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr03--wan22-i2v-14b"></a>

##### Wan2.2-I2V-14B

<p align="left">
  <img src="model_output/Modal/Wan2.2-I2V-14B/Subj-Attr03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Wan2.2-I2V-14B/Subj-Attr03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Wan2.2-I2V-14B/Subj-Attr03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Wan2.2-I2V-14B/Subj-Attr03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr03--bagel"></a>

##### BAGEL

<p align="left">
  <img src="model_output/Modal/BAGEL/Subj-Attr03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/BAGEL/Subj-Attr03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/BAGEL/Subj-Attr03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/BAGEL/Subj-Attr03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr03--hunyuanvideo"></a>

##### HunyuanVideo

<p align="left">
  <img src="model_output/Modal/HunyuanVideo/Subj-Attr03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/HunyuanVideo/Subj-Attr03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/HunyuanVideo/Subj-Attr03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/HunyuanVideo/Subj-Attr03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--subj-attr03--qwen-image"></a>

##### Qwen-Image

<p align="left">
  <img src="model_output/Modal/Qwen-Image/Subj-Attr03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Qwen-Image/Subj-Attr03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Qwen-Image/Subj-Attr03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Qwen-Image/Subj-Attr03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

---

<a name="modal--local-edit"></a>

### Local-Edit

<a name="modal--local-edit01--prompt"></a>

#### Only change the digital clock display: simulate the time on the digital clock ch…

Prompt

```text
Only change the digital clock display: simulate the time on the digital clock changing from 12:00 to 12:30 over a few seconds.
```

Input image

<div style="text-align: left;">
  <img src="model_output/Modal/input/loc01/loc01.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</div>

<a name="modal--local-edit01--gpt-image-15"></a>

##### GPT image 1.5

<p align="left">
  <img src="model_output/Modal/GPT image 1.5/Local-Edit01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1.5/Local-Edit01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1.5/Local-Edit01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1.5/Local-Edit01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit01--nano-banana-pro"></a>

##### Nano Banana Pro

<p align="left">
  <img src="model_output/Modal/Nano Banana Pro/Local-Edit01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana Pro/Local-Edit01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana Pro/Local-Edit01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana Pro/Local-Edit01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit01--veo-31"></a>

##### Veo 3.1

<p align="left">
  <img src="model_output/Modal/Veo 3.1/Local-Edit01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Veo 3.1/Local-Edit01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Veo 3.1/Local-Edit01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Veo 3.1/Local-Edit01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit01--seedream-50"></a>

##### Seedream 5.0

<p align="left">
  <img src="model_output/Modal/Seedream 5.0/Local-Edit01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 5.0/Local-Edit01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 5.0/Local-Edit01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 5.0/Local-Edit01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit01--gpt-image-1"></a>

##### GPT image 1

<p align="left">
  <img src="model_output/Modal/GPT image 1/Local-Edit01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1/Local-Edit01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1/Local-Edit01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1/Local-Edit01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit01--nano-banana"></a>

##### Nano Banana

<p align="left">
  <img src="model_output/Modal/Nano Banana/Local-Edit01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana/Local-Edit01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana/Local-Edit01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana/Local-Edit01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit01--nano-banana-2"></a>

##### Nano Banana 2

<p align="left">
  <img src="model_output/Modal/Nano Banana 2/Local-Edit01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana 2/Local-Edit01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana 2/Local-Edit01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana 2/Local-Edit01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit01--emu35"></a>

##### Emu3.5

<p align="left">
  <img src="model_output/Modal/Emu3.5/Local-Edit01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Emu3.5/Local-Edit01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Emu3.5/Local-Edit01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Emu3.5/Local-Edit01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit01--kling"></a>

##### kling

<p align="left">
  <img src="model_output/Modal/kling/Local-Edit01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/kling/Local-Edit01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/kling/Local-Edit01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/kling/Local-Edit01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit01--seedream-45"></a>

##### Seedream 4.5

<p align="left">
  <img src="model_output/Modal/Seedream 4.5/Local-Edit01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.5/Local-Edit01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.5/Local-Edit01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.5/Local-Edit01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit01--sora"></a>

##### sora

<p align="left">
  <img src="model_output/Modal/sora/Local-Edit01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/sora/Local-Edit01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/sora/Local-Edit01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/sora/Local-Edit01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit01--seedream-40"></a>

##### Seedream 4.0

<p align="left">
  <img src="model_output/Modal/Seedream 4.0/Local-Edit01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.0/Local-Edit01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.0/Local-Edit01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.0/Local-Edit01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit01--skyreels-v2"></a>

##### SkyReels-V2

<p align="left">
  <img src="model_output/Modal/SkyReels-V2/Local-Edit01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/SkyReels-V2/Local-Edit01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/SkyReels-V2/Local-Edit01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/SkyReels-V2/Local-Edit01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit01--wan22-i2v-14b"></a>

##### Wan2.2-I2V-14B

<p align="left">
  <img src="model_output/Modal/Wan2.2-I2V-14B/Local-Edit01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Wan2.2-I2V-14B/Local-Edit01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Wan2.2-I2V-14B/Local-Edit01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Wan2.2-I2V-14B/Local-Edit01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit01--bagel"></a>

##### BAGEL

<p align="left">
  <img src="model_output/Modal/BAGEL/Local-Edit01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/BAGEL/Local-Edit01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/BAGEL/Local-Edit01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/BAGEL/Local-Edit01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit01--hunyuanvideo"></a>

##### HunyuanVideo

<p align="left">
  <img src="model_output/Modal/HunyuanVideo/Local-Edit01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/HunyuanVideo/Local-Edit01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/HunyuanVideo/Local-Edit01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/HunyuanVideo/Local-Edit01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit01--qwen-image"></a>

##### Qwen-Image

<p align="left">
  <img src="model_output/Modal/Qwen-Image/Local-Edit01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Qwen-Image/Local-Edit01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Qwen-Image/Local-Edit01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Qwen-Image/Local-Edit01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

---

<a name="modal--local-edit02--prompt"></a>

#### Only make the clock's hands rotate: simulate the clock's minute hand moving from…

Prompt

```text
Only make the clock's hands rotate: simulate the clock's minute hand moving from 12 to 9 over a few seconds, while the hour hand adjusts accordingly.
```

Input image

<div style="text-align: left;">
  <img src="model_output/Modal/input/loc02/loc02.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</div>

<a name="modal--local-edit02--gpt-image-15"></a>

##### GPT image 1.5

<p align="left">
  <img src="model_output/Modal/GPT image 1.5/Local-Edit02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1.5/Local-Edit02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1.5/Local-Edit02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1.5/Local-Edit02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit02--nano-banana-pro"></a>

##### Nano Banana Pro

<p align="left">
  <img src="model_output/Modal/Nano Banana Pro/Local-Edit02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana Pro/Local-Edit02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana Pro/Local-Edit02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana Pro/Local-Edit02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit02--veo-31"></a>

##### Veo 3.1

<p align="left">
  <img src="model_output/Modal/Veo 3.1/Local-Edit02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Veo 3.1/Local-Edit02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Veo 3.1/Local-Edit02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Veo 3.1/Local-Edit02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit02--seedream-50"></a>

##### Seedream 5.0

<p align="left">
  <img src="model_output/Modal/Seedream 5.0/Local-Edit02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 5.0/Local-Edit02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 5.0/Local-Edit02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 5.0/Local-Edit02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit02--gpt-image-1"></a>

##### GPT image 1

<p align="left">
  <img src="model_output/Modal/GPT image 1/Local-Edit02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1/Local-Edit02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1/Local-Edit02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1/Local-Edit02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit02--nano-banana"></a>

##### Nano Banana

<p align="left">
  <img src="model_output/Modal/Nano Banana/Local-Edit02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana/Local-Edit02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana/Local-Edit02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana/Local-Edit02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit02--nano-banana-2"></a>

##### Nano Banana 2

<p align="left">
  <img src="model_output/Modal/Nano Banana 2/Local-Edit02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana 2/Local-Edit02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana 2/Local-Edit02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana 2/Local-Edit02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit02--emu35"></a>

##### Emu3.5

<p align="left">
  <img src="model_output/Modal/Emu3.5/Local-Edit02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Emu3.5/Local-Edit02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Emu3.5/Local-Edit02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Emu3.5/Local-Edit02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit02--kling"></a>

##### kling

<p align="left">
  <img src="model_output/Modal/kling/Local-Edit02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/kling/Local-Edit02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/kling/Local-Edit02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/kling/Local-Edit02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit02--seedream-45"></a>

##### Seedream 4.5

<p align="left">
  <img src="model_output/Modal/Seedream 4.5/Local-Edit02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.5/Local-Edit02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.5/Local-Edit02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.5/Local-Edit02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit02--sora"></a>

##### sora

<p align="left">
  <img src="model_output/Modal/sora/Local-Edit02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/sora/Local-Edit02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/sora/Local-Edit02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/sora/Local-Edit02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit02--seedream-40"></a>

##### Seedream 4.0

<p align="left">
  <img src="model_output/Modal/Seedream 4.0/Local-Edit02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.0/Local-Edit02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.0/Local-Edit02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.0/Local-Edit02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit02--skyreels-v2"></a>

##### SkyReels-V2

<p align="left">
  <img src="model_output/Modal/SkyReels-V2/Local-Edit02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/SkyReels-V2/Local-Edit02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/SkyReels-V2/Local-Edit02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/SkyReels-V2/Local-Edit02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit02--wan22-i2v-14b"></a>

##### Wan2.2-I2V-14B

<p align="left">
  <img src="model_output/Modal/Wan2.2-I2V-14B/Local-Edit02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Wan2.2-I2V-14B/Local-Edit02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Wan2.2-I2V-14B/Local-Edit02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Wan2.2-I2V-14B/Local-Edit02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit02--bagel"></a>

##### BAGEL

<p align="left">
  <img src="model_output/Modal/BAGEL/Local-Edit02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/BAGEL/Local-Edit02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/BAGEL/Local-Edit02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/BAGEL/Local-Edit02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit02--hunyuanvideo"></a>

##### HunyuanVideo

<p align="left">
  <img src="model_output/Modal/HunyuanVideo/Local-Edit02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/HunyuanVideo/Local-Edit02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/HunyuanVideo/Local-Edit02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/HunyuanVideo/Local-Edit02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit02--qwen-image"></a>

##### Qwen-Image

<p align="left">
  <img src="model_output/Modal/Qwen-Image/Local-Edit02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Qwen-Image/Local-Edit02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Qwen-Image/Local-Edit02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Qwen-Image/Local-Edit02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

---

<a name="modal--local-edit03--prompt"></a>

#### Only make the clock's hands rotate: simulate the hands moving as if time is pass…

Prompt

```text
Only make the clock's hands rotate: simulate the hands moving as if time is passing, but the clock face and everything else (wall, furniture, decorations) must remain exactly the same as in the initial image.
```

Input image

<div style="text-align: left;">
  <img src="model_output/Modal/input/loc03/loc03.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</div>

<a name="modal--local-edit03--gpt-image-15"></a>

##### GPT image 1.5

<p align="left">
  <img src="model_output/Modal/GPT image 1.5/Local-Edit03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1.5/Local-Edit03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1.5/Local-Edit03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1.5/Local-Edit03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit03--nano-banana-pro"></a>

##### Nano Banana Pro

<p align="left">
  <img src="model_output/Modal/Nano Banana Pro/Local-Edit03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana Pro/Local-Edit03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana Pro/Local-Edit03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana Pro/Local-Edit03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit03--veo-31"></a>

##### Veo 3.1

<p align="left">
  <img src="model_output/Modal/Veo 3.1/Local-Edit03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Veo 3.1/Local-Edit03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Veo 3.1/Local-Edit03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Veo 3.1/Local-Edit03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit03--seedream-50"></a>

##### Seedream 5.0

<p align="left">
  <img src="model_output/Modal/Seedream 5.0/Local-Edit03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 5.0/Local-Edit03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 5.0/Local-Edit03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 5.0/Local-Edit03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit03--gpt-image-1"></a>

##### GPT image 1

<p align="left">
  <img src="model_output/Modal/GPT image 1/Local-Edit03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1/Local-Edit03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1/Local-Edit03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1/Local-Edit03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit03--nano-banana"></a>

##### Nano Banana

<p align="left">
  <img src="model_output/Modal/Nano Banana/Local-Edit03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana/Local-Edit03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana/Local-Edit03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana/Local-Edit03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit03--nano-banana-2"></a>

##### Nano Banana 2

<p align="left">
  <img src="model_output/Modal/Nano Banana 2/Local-Edit03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana 2/Local-Edit03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana 2/Local-Edit03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana 2/Local-Edit03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit03--emu35"></a>

##### Emu3.5

<p align="left">
  <img src="model_output/Modal/Emu3.5/Local-Edit03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Emu3.5/Local-Edit03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Emu3.5/Local-Edit03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Emu3.5/Local-Edit03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit03--kling"></a>

##### kling

<p align="left">
  <img src="model_output/Modal/kling/Local-Edit03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/kling/Local-Edit03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/kling/Local-Edit03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/kling/Local-Edit03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit03--seedream-45"></a>

##### Seedream 4.5

<p align="left">
  <img src="model_output/Modal/Seedream 4.5/Local-Edit03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.5/Local-Edit03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.5/Local-Edit03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.5/Local-Edit03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit03--sora"></a>

##### sora

<p align="left">
  <img src="model_output/Modal/sora/Local-Edit03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/sora/Local-Edit03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/sora/Local-Edit03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/sora/Local-Edit03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit03--seedream-40"></a>

##### Seedream 4.0

<p align="left">
  <img src="model_output/Modal/Seedream 4.0/Local-Edit03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.0/Local-Edit03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.0/Local-Edit03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.0/Local-Edit03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit03--skyreels-v2"></a>

##### SkyReels-V2

<p align="left">
  <img src="model_output/Modal/SkyReels-V2/Local-Edit03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/SkyReels-V2/Local-Edit03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/SkyReels-V2/Local-Edit03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/SkyReels-V2/Local-Edit03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit03--wan22-i2v-14b"></a>

##### Wan2.2-I2V-14B

<p align="left">
  <img src="model_output/Modal/Wan2.2-I2V-14B/Local-Edit03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Wan2.2-I2V-14B/Local-Edit03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Wan2.2-I2V-14B/Local-Edit03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Wan2.2-I2V-14B/Local-Edit03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit03--bagel"></a>

##### BAGEL

<p align="left">
  <img src="model_output/Modal/BAGEL/Local-Edit03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/BAGEL/Local-Edit03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/BAGEL/Local-Edit03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/BAGEL/Local-Edit03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit03--hunyuanvideo"></a>

##### HunyuanVideo

<p align="left">
  <img src="model_output/Modal/HunyuanVideo/Local-Edit03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/HunyuanVideo/Local-Edit03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/HunyuanVideo/Local-Edit03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/HunyuanVideo/Local-Edit03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--local-edit03--qwen-image"></a>

##### Qwen-Image

<p align="left">
  <img src="model_output/Modal/Qwen-Image/Local-Edit03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Qwen-Image/Local-Edit03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Qwen-Image/Local-Edit03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Qwen-Image/Local-Edit03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

---

<a name="modal--multi-const"></a>

### Multi-Const

<a name="modal--multi-const01--prompt"></a>

#### Generate a realistic image containing only three subjects, and satisfy all bindi…

Prompt

```text
Generate a realistic image containing only three subjects, and satisfy all bindings: Person A: wearing a gray hoodie, holding a backpack in the left hand, and giving a water bottle to Person B with the right hand. Person B: wearing a orange t-shirt, holding a skateboard in the right hand, and giving a cap to Person A with the left hand. A squirrel: with brown fur, sitting on a tree branch, and looking at Person B. Negative constraints: No other people or animals;
```

<a name="modal--multi-const01--gpt-image-15"></a>

##### GPT image 1.5

<p align="left">
  <img src="model_output/Modal/GPT image 1.5/Multi-Const01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1.5/Multi-Const01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1.5/Multi-Const01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1.5/Multi-Const01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const01--nano-banana-pro"></a>

##### Nano Banana Pro

<p align="left">
  <img src="model_output/Modal/Nano Banana Pro/Multi-Const01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana Pro/Multi-Const01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana Pro/Multi-Const01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana Pro/Multi-Const01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const01--veo-31"></a>

##### Veo 3.1

<p align="left">
  <img src="model_output/Modal/Veo 3.1/Multi-Const01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Veo 3.1/Multi-Const01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Veo 3.1/Multi-Const01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Veo 3.1/Multi-Const01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const01--seedream-50"></a>

##### Seedream 5.0

<p align="left">
  <img src="model_output/Modal/Seedream 5.0/Multi-Const01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 5.0/Multi-Const01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 5.0/Multi-Const01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 5.0/Multi-Const01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const01--gpt-image-1"></a>

##### GPT image 1

<p align="left">
  <img src="model_output/Modal/GPT image 1/Multi-Const01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1/Multi-Const01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1/Multi-Const01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1/Multi-Const01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const01--nano-banana"></a>

##### Nano Banana

<p align="left">
  <img src="model_output/Modal/Nano Banana/Multi-Const01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana/Multi-Const01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana/Multi-Const01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana/Multi-Const01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const01--nano-banana-2"></a>

##### Nano Banana 2

<p align="left">
  <img src="model_output/Modal/Nano Banana 2/Multi-Const01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana 2/Multi-Const01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana 2/Multi-Const01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana 2/Multi-Const01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const01--emu35"></a>

##### Emu3.5

<p align="left">
  <img src="model_output/Modal/Emu3.5/Multi-Const01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Emu3.5/Multi-Const01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Emu3.5/Multi-Const01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Emu3.5/Multi-Const01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const01--kling"></a>

##### kling

<p align="left">
  <img src="model_output/Modal/kling/Multi-Const01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/kling/Multi-Const01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/kling/Multi-Const01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/kling/Multi-Const01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const01--seedream-45"></a>

##### Seedream 4.5

<p align="left">
  <img src="model_output/Modal/Seedream 4.5/Multi-Const01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.5/Multi-Const01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.5/Multi-Const01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.5/Multi-Const01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const01--sora"></a>

##### sora

<p align="left">
  <img src="model_output/Modal/sora/Multi-Const01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/sora/Multi-Const01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/sora/Multi-Const01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/sora/Multi-Const01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const01--seedream-40"></a>

##### Seedream 4.0

<p align="left">
  <img src="model_output/Modal/Seedream 4.0/Multi-Const01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.0/Multi-Const01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.0/Multi-Const01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.0/Multi-Const01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const01--skyreels-v2"></a>

##### SkyReels-V2

<p align="left">
  <img src="model_output/Modal/SkyReels-V2/Multi-Const01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/SkyReels-V2/Multi-Const01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/SkyReels-V2/Multi-Const01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/SkyReels-V2/Multi-Const01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const01--wan22-i2v-14b"></a>

##### Wan2.2-I2V-14B

<p align="left">
  <img src="model_output/Modal/Wan2.2-I2V-14B/Multi-Const01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Wan2.2-I2V-14B/Multi-Const01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Wan2.2-I2V-14B/Multi-Const01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Wan2.2-I2V-14B/Multi-Const01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const01--bagel"></a>

##### BAGEL

<p align="left">
  <img src="model_output/Modal/BAGEL/Multi-Const01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/BAGEL/Multi-Const01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/BAGEL/Multi-Const01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/BAGEL/Multi-Const01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const01--hunyuanvideo"></a>

##### HunyuanVideo

<p align="left">
  <img src="model_output/Modal/HunyuanVideo/Multi-Const01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/HunyuanVideo/Multi-Const01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/HunyuanVideo/Multi-Const01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/HunyuanVideo/Multi-Const01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const01--qwen-image"></a>

##### Qwen-Image

<p align="left">
  <img src="model_output/Modal/Qwen-Image/Multi-Const01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Qwen-Image/Multi-Const01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Qwen-Image/Multi-Const01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Qwen-Image/Multi-Const01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

---

<a name="modal--multi-const02--prompt"></a>

#### Generate a realistic image containing only three subjects, and satisfy all bindi…

Prompt

```text
Generate a realistic image containing only three subjects, and satisfy all bindings: Person A: wearing a yellow jacket, holding a camera in the left hand, and giving a hat to Person B with the right hand. Person B: wearing a purple sweater, holding a map in the right hand, and giving a scarf to Person A with the left hand. A bird: with red feathers, standing on a perch, and looking at Person B. Negative constraints: No other people or animals;
```

<a name="modal--multi-const02--gpt-image-15"></a>

##### GPT image 1.5

<p align="left">
  <img src="model_output/Modal/GPT image 1.5/Multi-Const02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1.5/Multi-Const02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1.5/Multi-Const02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1.5/Multi-Const02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const02--nano-banana-pro"></a>

##### Nano Banana Pro

<p align="left">
  <img src="model_output/Modal/Nano Banana Pro/Multi-Const02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana Pro/Multi-Const02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana Pro/Multi-Const02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana Pro/Multi-Const02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const02--veo-31"></a>

##### Veo 3.1

<p align="left">
  <img src="model_output/Modal/Veo 3.1/Multi-Const02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Veo 3.1/Multi-Const02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Veo 3.1/Multi-Const02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Veo 3.1/Multi-Const02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const02--seedream-50"></a>

##### Seedream 5.0

<p align="left">
  <img src="model_output/Modal/Seedream 5.0/Multi-Const02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 5.0/Multi-Const02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 5.0/Multi-Const02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 5.0/Multi-Const02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const02--gpt-image-1"></a>

##### GPT image 1

<p align="left">
  <img src="model_output/Modal/GPT image 1/Multi-Const02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1/Multi-Const02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1/Multi-Const02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1/Multi-Const02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const02--nano-banana"></a>

##### Nano Banana

<p align="left">
  <img src="model_output/Modal/Nano Banana/Multi-Const02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana/Multi-Const02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana/Multi-Const02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana/Multi-Const02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const02--nano-banana-2"></a>

##### Nano Banana 2

<p align="left">
  <img src="model_output/Modal/Nano Banana 2/Multi-Const02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana 2/Multi-Const02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana 2/Multi-Const02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana 2/Multi-Const02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const02--emu35"></a>

##### Emu3.5

<p align="left">
  <img src="model_output/Modal/Emu3.5/Multi-Const02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Emu3.5/Multi-Const02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Emu3.5/Multi-Const02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Emu3.5/Multi-Const02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const02--kling"></a>

##### kling

<p align="left">
  <img src="model_output/Modal/kling/Multi-Const02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/kling/Multi-Const02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/kling/Multi-Const02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/kling/Multi-Const02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const02--seedream-45"></a>

##### Seedream 4.5

<p align="left">
  <img src="model_output/Modal/Seedream 4.5/Multi-Const02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.5/Multi-Const02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.5/Multi-Const02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.5/Multi-Const02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const02--sora"></a>

##### sora

<p align="left">
  <img src="model_output/Modal/sora/Multi-Const02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/sora/Multi-Const02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/sora/Multi-Const02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/sora/Multi-Const02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const02--seedream-40"></a>

##### Seedream 4.0

<p align="left">
  <img src="model_output/Modal/Seedream 4.0/Multi-Const02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.0/Multi-Const02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.0/Multi-Const02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.0/Multi-Const02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const02--skyreels-v2"></a>

##### SkyReels-V2

<p align="left">
  <img src="model_output/Modal/SkyReels-V2/Multi-Const02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/SkyReels-V2/Multi-Const02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/SkyReels-V2/Multi-Const02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/SkyReels-V2/Multi-Const02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const02--wan22-i2v-14b"></a>

##### Wan2.2-I2V-14B

<p align="left">
  <img src="model_output/Modal/Wan2.2-I2V-14B/Multi-Const02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Wan2.2-I2V-14B/Multi-Const02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Wan2.2-I2V-14B/Multi-Const02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Wan2.2-I2V-14B/Multi-Const02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const02--bagel"></a>

##### BAGEL

<p align="left">
  <img src="model_output/Modal/BAGEL/Multi-Const02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/BAGEL/Multi-Const02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/BAGEL/Multi-Const02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/BAGEL/Multi-Const02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const02--hunyuanvideo"></a>

##### HunyuanVideo

<p align="left">
  <img src="model_output/Modal/HunyuanVideo/Multi-Const02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/HunyuanVideo/Multi-Const02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/HunyuanVideo/Multi-Const02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/HunyuanVideo/Multi-Const02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const02--qwen-image"></a>

##### Qwen-Image

<p align="left">
  <img src="model_output/Modal/Qwen-Image/Multi-Const02_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Qwen-Image/Multi-Const02_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Qwen-Image/Multi-Const02_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Qwen-Image/Multi-Const02_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

---

<a name="modal--multi-const03--prompt"></a>

#### Produce a realistic image containing exactly three subjects: Gardener C: wearing…

Prompt

```text
Produce a realistic image containing exactly three subjects: Gardener C: wearing gardening gloves, trimming a bush with shears in the right hand, and holding a watering can in the left hand. Child D: wearing a sun hat, watering flowers with a hose in the right hand, and holding a toy in the left hand. A bird: with blue feathers, perched on a branch, and watching Child D. Negative constraints: No gardening tools other than specified; no labels or writing on any item; the scene must use only green and brown colors.
```

<a name="modal--multi-const03--gpt-image-15"></a>

##### GPT image 1.5

<p align="left">
  <img src="model_output/Modal/GPT image 1.5/Multi-Const03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1.5/Multi-Const03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1.5/Multi-Const03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1.5/Multi-Const03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const03--nano-banana-pro"></a>

##### Nano Banana Pro

<p align="left">
  <img src="model_output/Modal/Nano Banana Pro/Multi-Const03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana Pro/Multi-Const03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana Pro/Multi-Const03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana Pro/Multi-Const03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const03--veo-31"></a>

##### Veo 3.1

<p align="left">
  <img src="model_output/Modal/Veo 3.1/Multi-Const03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Veo 3.1/Multi-Const03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Veo 3.1/Multi-Const03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Veo 3.1/Multi-Const03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const03--seedream-50"></a>

##### Seedream 5.0

<p align="left">
  <img src="model_output/Modal/Seedream 5.0/Multi-Const03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 5.0/Multi-Const03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 5.0/Multi-Const03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 5.0/Multi-Const03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const03--gpt-image-1"></a>

##### GPT image 1

<p align="left">
  <img src="model_output/Modal/GPT image 1/Multi-Const03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1/Multi-Const03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1/Multi-Const03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/GPT image 1/Multi-Const03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const03--nano-banana"></a>

##### Nano Banana

<p align="left">
  <img src="model_output/Modal/Nano Banana/Multi-Const03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana/Multi-Const03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana/Multi-Const03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana/Multi-Const03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const03--nano-banana-2"></a>

##### Nano Banana 2

<p align="left">
  <img src="model_output/Modal/Nano Banana 2/Multi-Const03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana 2/Multi-Const03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana 2/Multi-Const03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Nano Banana 2/Multi-Const03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const03--emu35"></a>

##### Emu3.5

<p align="left">
  <img src="model_output/Modal/Emu3.5/Multi-Const03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Emu3.5/Multi-Const03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Emu3.5/Multi-Const03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Emu3.5/Multi-Const03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const03--kling"></a>

##### kling

<p align="left">
  <img src="model_output/Modal/kling/Multi-Const03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/kling/Multi-Const03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/kling/Multi-Const03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/kling/Multi-Const03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const03--seedream-45"></a>

##### Seedream 4.5

<p align="left">
  <img src="model_output/Modal/Seedream 4.5/Multi-Const03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.5/Multi-Const03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.5/Multi-Const03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.5/Multi-Const03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const03--sora"></a>

##### sora

<p align="left">
  <img src="model_output/Modal/sora/Multi-Const03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/sora/Multi-Const03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/sora/Multi-Const03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/sora/Multi-Const03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const03--seedream-40"></a>

##### Seedream 4.0

<p align="left">
  <img src="model_output/Modal/Seedream 4.0/Multi-Const03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.0/Multi-Const03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.0/Multi-Const03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Seedream 4.0/Multi-Const03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const03--skyreels-v2"></a>

##### SkyReels-V2

<p align="left">
  <img src="model_output/Modal/SkyReels-V2/Multi-Const03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/SkyReels-V2/Multi-Const03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/SkyReels-V2/Multi-Const03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/SkyReels-V2/Multi-Const03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const03--wan22-i2v-14b"></a>

##### Wan2.2-I2V-14B

<p align="left">
  <img src="model_output/Modal/Wan2.2-I2V-14B/Multi-Const03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Wan2.2-I2V-14B/Multi-Const03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Wan2.2-I2V-14B/Multi-Const03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Wan2.2-I2V-14B/Multi-Const03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const03--bagel"></a>

##### BAGEL

<p align="left">
  <img src="model_output/Modal/BAGEL/Multi-Const03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/BAGEL/Multi-Const03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/BAGEL/Multi-Const03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/BAGEL/Multi-Const03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const03--hunyuanvideo"></a>

##### HunyuanVideo

<p align="left">
  <img src="model_output/Modal/HunyuanVideo/Multi-Const03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/HunyuanVideo/Multi-Const03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/HunyuanVideo/Multi-Const03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/HunyuanVideo/Multi-Const03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modal--multi-const03--qwen-image"></a>

##### Qwen-Image

<p align="left">
  <img src="model_output/Modal/Qwen-Image/Multi-Const03_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Qwen-Image/Multi-Const03_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Qwen-Image/Multi-Const03_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/Modal/Qwen-Image/Multi-Const03_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

---

<a name="modalxspatial"></a>

## **ModalxSpatial**

<a name="modalxspatial--sem-mv"></a>

### Sem-MV

<a name="modalxspatial--sem-mv01--prompt"></a>

#### Rotate the camera 360 degrees to display multiple viewpoints from different angl…

Prompt

```text
Rotate the camera 360 degrees to display multiple viewpoints from different angles. The 'CAUTION' sign must always be the closest object in all viewpoints, and the relative positions of the smartphone, keyboard, and printer should remain consistent.
```

Input image

<div style="text-align: left;">
  <img src="model_output/ModalxSpatial/input/semmv01/semmv01.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</div>

<a name="modalxspatial--sem-mv01--gpt-image-15"></a>

##### GPT image 1.5

<p align="left">
  <img src="model_output/ModalxSpatial/GPT image 1.5/Sem-MV01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/ModalxSpatial/GPT image 1.5/Sem-MV01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/ModalxSpatial/GPT image 1.5/Sem-MV01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/ModalxSpatial/GPT image 1.5/Sem-MV01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modalxspatial--sem-mv01--nano-banana-pro"></a>

##### Nano Banana Pro

<p align="left">
  <img src="model_output/ModalxSpatial/Nano Banana Pro/Sem-MV01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/ModalxSpatial/Nano Banana Pro/Sem-MV01_2.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/ModalxSpatial/Nano Banana Pro/Sem-MV01_3.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/ModalxSpatial/Nano Banana Pro/Sem-MV01_4.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
</p>

<a name="modalxspatial--sem-mv01--veo-31"></a>

##### Veo 3.1

<p align="left">
  <img src="model_output/ModalxSpatial/Veo 3.1/Sem-MV01_1.jpg" width="180" style="margin-right: 8px;" loading="lazy" />
  <img src="model_output/ModalxSpatial/Veo 3.1/Sem-MV01_2.jpg" width="180" style="margin-right: 8px;" loading="l