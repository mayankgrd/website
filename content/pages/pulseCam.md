Title: PulseCam: High-resolution blood perfusion imaging using a camera and a pulse oximeter
Slug: pulseCam
url: pulseCam/
save_as: pulseCam/index.html
status: hidden


<p class="text-center"><a href="http://www.ece.rice.edu/~mk28/" target="_blank">Mayank Kumar</a>, <a href="http://www.ece.rice.edu/~av21/" target="_blank"> Ashok Veeraraghavan </a> and <a href="http://www.ece.rice.edu/~ashu/" target="_blank">Ashu Sabharwal </a></p>
<p class="text-center text-muted">6100 Main Street, Rice University, Houston, Tx, 77005, USA</p>


## The Problem

<p class="text-justify">Blood perfusion is the flow of oxygen-rich blood to the end organs and tissue through the blood vessels in the body. Blood perfusion is vital in ensuring oxygen delivery to the cells and in maintaining metabolic homeostasis. Measuring peripheral perfusion (or microcirculatio) is needed to monitoring critical care patients in ICU and to diagnose peripheral arterial disease. Significant research has demonstrated that regional blood flow is not well-captured by currently measured macro-circulatory parameters, like blood pressure and heart rate. Therefore, critical care doctors require information about micro-circulatory parameters to quantify regional blood flow in different body parts. But, existing point modalities to measure regional blood flow such as laser Doppler flowmeter and perfusion index (measured using pulse oximeter) is not effective as they don’t capture spatial variations in blood flow which has diagnostic value. Therefore, one needs an imaging device which can continuously measure maps of regional blood flow. </p>

## Our Solution

<p class="text-justify">PulseCam is a new multi-sensor blood flow imaging device. PulseCam leverages the advantages in Image sensors and illumination to capture videos of skin surface, and relies on computational imaging, signal recovery and computer vision algorithms to peek inside the skin surface and measure blood flow.  PulseCam measures peripheral blood flow using a patent pending algorithm which combines the video recording of the skin surface and a photoplethysmogram waveform recorded using a pulse oximeter. </p>

<p class="text-justify"> PulseCam combines a traditional pulse oximeter with a video camera in a unique way to provide low noise and high-resolution blood perfusion maps. Our proposed multi-sensor modality improves per pixel signal to noise ratio of the perfusion map by up to 3 dB and produces perfusion maps with 2 − 3 times better spatial resolution compared to best known camera-only methods. Blood perfusion measured in the palm using PulseCam during a post-occlusive reactive hyperemia (POHR) test replicates data using existing laser Doppler perfusion monitor but with much lower cost and a portable setup making it suitable for further development as a clinical device. </p>

<div>
	<img src="{filename}/images/pulseCam-steps-involved.png" class="img-responsive center-block" alt="paper image" width = '80%'>
	<p class="text-center"><b>Processing steps involved in PulseCam:</b> Raw video frames from the camera are processed to estimate noisy blood volume waveform from each camera pixel, and the simultaneously recorded reliable blood volume waveform from the pulse oximeter is filtered; Spatiotemporal variations in blood perfusion is estimated by combining the processed videos from the camera and the pulse oximeter recordings</p> 
</div>

## Paper 
Kumar, M., Suliburk, J., Veeraraghavan, A., & Sabharwal, A. (2016). PulseCam: High-resolution blood perfusion imaging using a camera and a pulse oximeter. In 2016 38th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC) (pp. 3904–3909). IEEE. <mark> <a href="{filename}/pdfs/PulseCam.pdf"> PDF </a></mark>

<b>Cite (BibTex) </b>
<pre>
@INPROCEEDINGS{7591581, 
author={M. Kumar and J. Suliburk and A. Veeraraghavan and A. Sabharwal}, 
booktitle={2016 38th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC)}, 
title={PulseCam: High-resolution blood perfusion imaging using a camera and a pulse oximeter}, 
year={2016}, 
pages={3904-3909}, 
keywords={biomedical optical imaging;blood flow measurement;medical signal processing;oximetry;video cameras;PulseCam setup;camera-only system;clinical device;disease;high-resolution blood perfusion imaging;high-resolution blood perfusion maps;injury;laser Doppler flowmetry device;medical care;multisensor modality;noisy low-resolution blood perfusion maps;palm;portable camera-based blood perfusion measurement system;post-occlusive reactive hyperemia;signal to noise ratio;spatial resolution;standard PORH response curve;traditional pulse oximeter;video camera;Blood;Cameras;Noise measurement;Pulse measurements;Signal to noise ratio;Skin}, 
doi={10.1109/EMBC.2016.7591581}, 
ISSN={1557-170X}, 
month={Aug},}
</pre>

## Testing PulseCam during an occlusion event
<div class="container">
	<div class="row clearfix">
		<div class="col-md-6 column">
			</br>
			<div class="embed-responsive embed-responsive-4by3">
  				<iframe class="embed-responsive-item" width="500" height="313" src="https://player.vimeo.com/video/210254783" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
			</div>
			</br> </br>
			<p class="text-center">False color video during the occlusion test: Bright regions have higher blood flow, dark region have lower blood flow. Blood flow in the palm occluded by putting pressure cuff in the arm.
 			</p>
 		</div>
		<div class="col-md-6 column"> 
			<img src="{filename}/images/pulseCam-PORH.png" class="img-responsive center-block" alt="paper image" width = '90%'>
			<p class="text-center">Temporal variation of average blood perfusion in the palm before, during and after an occlusion (post occlusive reactive hyperemia or PORH), RF is the resting flux (perfusion) before the occlusion, MF is the maximum flux just after the occlusion </p>
		</div>
	</div>
</div>
