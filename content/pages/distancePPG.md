Title: DistancePPG: Robust non-contact vital signs monitoring using a camera 
Slug: distancePPG
url: distancePPG/
save_as: distancePPG/index.html
status: hidden


<p class="text-center"><a href="http://www.ece.rice.edu/~mk28/" target="_blank">Mayank Kumar</a>, <a href="http://www.ece.rice.edu/~av21/" target="_blank"> Ashok Veeraraghavan </a> and <a href="http://www.ece.rice.edu/~ashu/" target="_blank">Ashu Sabharwal </a></p>
<p class="text-center text-muted">6100 Main Street, Rice University, Houston, Tx, 77005, USA</p>

## Abstract
<p class="text-justify">Vital signs such as pulse rate and breathing rate are currently measured using contact probes. But, non-contact methods for measuring vital signs are desirable both in hospital settings (e.g. in NICU) and for ubiquitous in-situ health tracking (e.g. on mobile phone and computers with webcams). Recently, camera-based non-contact vital sign monitoring have been shown to be feasible. However, camera-based vital sign monitoring is challenging for people having darker skin tone, under low lighting conditions, and/or during movement of an individual in front of the camera. In this paper, we propose distancePPG, a new camera-based vital sign estimation algorithm which addresses these challenges. DistancePPG proposes a new method of combining skin-color change signals from different tracked regions of the face using a weighted average, where the weights depend on the blood perfusion and incident light intensity in the region, to improve the signal-to-noise ratio (SNR) of camera-based estimate. One of our key contributions is a new automatic method for determining the weights based only on the video recording of the subject. The gains in SNR of camera-based PPG estimated using distancePPG translate into reduction of the error in vital sign estimation, and thus expand the scope of camera-based vital sign monitoring to potentially challenging scenarios. Further, a dataset is  released, comprising of synchronized video recordings of face and pulse oximeter based ground truth recordings from the earlobe for people with different skin tones, under different lighting conditions and for various motion scenarios.</p>

<div>
	<img src="{filename}/images/paper-header.png" class="img-responsive center-block" alt="paper image" width = '80%'>
	<p class="text-center">Four basic steps in distancePPG: <b>Step (i)</b> Extract landmark points such as eyes, nose, mouth and face boundary from face image, <b>Step (ii) </b> Face is divided into seven regions, each region tracked over the video using computer vision tracker, <b>Step (iii) </b> Each tracked region is further divided into small regions of interest (ROI), <b>Step (iv) </b> DistancePPG computes the goodness metric associated with each ROI based only on the video recordings, and estimate camera-based PPG signal with much higher SNR (signal to noise ratio). For more details, please read our paper.</p> 
</div>

**Paper:** <span class="label label-warning"><a href="http://arxiv.org/pdf/1502.08040v1.pdf" target="_blank"> PDF </a></span> &nbsp;&nbsp;&nbsp; <span class="text-danger"> (Patent Pending)</span>

## Vital sign and PPG Recovered from videos 
<div class="container">
	<div class="row clearfix">
		<div class="col-md-4 column">
			<h3 class="text-center">Non-Caucasian skin tones </h3> 
			<div class="embed-responsive embed-responsive-4by3">
  				<iframe class="embed-responsive-item" width="500" height="313" src="https://player.vimeo.com/video/121387474" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
			</div>
			<p class="text-center">Sample distancePPG performance on a <b> brown skin  tone </b> subject. DistancePPG works for all skin tones. </p>
		</div>
		<div class="col-md-4 column">
			<h3 class="text-center">Motion scenario </h3> 
			<div class="embed-responsive embed-responsive-4by3">
  				<iframe class="embed-responsive-item" width="500" height="375" src="https://player.vimeo.com/video/121416169" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
			</div>
			<p class="text-center">Sample distancePPG performance under <b>motion scenario </b> (talking). Performance deteriorates only when there is large motion or occlusion. </p>
		</div>
		<div class="col-md-4 column">
			<h3 class="text-center">Low lighting conditions </h3> 
			<div class="embed-responsive embed-responsive-4by3">
  				<iframe class="embed-responsive-item" width="500" height="375" src="https://player.vimeo.com/video/121419114" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
			</div>
			<p class="text-center">Sample distancePPG performance under <b> low light scenario </b> (less than 100 lux). Performance does not deteriorate.</p>
		</div>
	</div>
</div>


## Dataset 
We plan to release the dataset comprising of the video recording of people facing the camera and the simultaneous PPG recording from the pulse-oximeter attached to person's ear. We collected the dataset by varying three important parameters of interest for camera-based vital sign estimation: (i) skin tone of subject, (ii) motion, (iii) ambient light intensity. Details about the dataset can be found <mark><a href="{filename}distancePPG-dataset.md">here </a></mark>

## Funding 
The project has been partially funded by National Science Foundation till date, combined with a Rice graduate student fellowship.









