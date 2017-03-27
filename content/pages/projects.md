Title: Projects
save_as: projects.html

### PulseCam ###
**High-resolution blood perfusion imaging using a camera and a pulse oximeter** 

<div class="container">
	<div class="row clearfix">
		<div class="col-md-8 column">
		<p class="text-justify"><b> PulseCam </b >is a new multi-sensor blood flow imaging device. PulseCam leverages the advantages in Image sensors and illumination to capture videos of skin surface, and relies on computational imaging, signal recovery and computer vision algorithms to peek inside the skin surface and measure blood flow.  PulseCam measures peripheral blood flow using a patent pending algorithm which combines the video recording of the skin surface and a pulse oximeter. At each pixel, pulseCam reliably estimates the amplitude of the photoplethysmogram (PPG) waveform or the blood volume waveform. Thus, it is similar to the Perfusion Index (PI) measurement produced by many conventional contact pulse oximeters. But, since PulseCam is an imaging modality, it produces “spatial maps of perfusion index” over the imaged skin surface, as opposed to a point measure such as perfusion index.  </p>
		</div>
		<div class="col-md-4 column">
			<img src="{filename}/images/PulseCam-steps-short.png" class="img-responsive center-block" alt="paper image" width = '100%'>
		</div>
	</div>
</div>

**Know more: ** <a href="{filename}pulseCam.md"><mark>Project webpage</mark> </a>

**Paper:** <mark> <a href="http://ieeexplore.ieee.org/document/7591581/" target="_blank"> Link </a></mark> &nbsp;&nbsp; |  <mark> <a href="pdfs/PulseCam.pdf"> PDF </a></mark>

<hr size="20"> 

### CameraVitals ###
**Robust non-contact vital signs monitoring using a camera** 

<div class="container">
	<div class="row clearfix">
		<div class="col-md-8 column">
		<p class="text-justify"><b>DistancePPG</b> is a camera-based photoplethysmogram (PPG) estimation algorithm. DistancePPG address two major challenges in camera-based vital sign monitoring: (i) extremely low signal strength of PPG signal, particularly for people with darker skin tones, and/or under low lighting conditions, (ii) motion artifacts due to movement of a person in front of a camera. DistancePPG proposes a new method of combining skin-color change signals from different regions of the face using a weighted average, where the weights depend on the blood perfusion and incident light intensity in the region, to improve the signal-to-noise ratio (SNR) of camera-based PPG estimate. The gains in SNR of camera-based PPG estimated using distancePPG translate into reduction of the error in vital sign estimation, and thus expand the scope of camera-based vital sign monitoring to potentially new scenarios. </p>
		</div>
		<div class="col-md-4 column">
			<div class="embed-responsive embed-responsive-4by3">
  				<iframe class="embed-responsive-item" width="500" height="375" src="https://www.youtube.com/embed/-jwGlLBxuH8" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
			</div>
		</div>
	</div>
</div>

**Know more: ** <a href="{filename}distancePPG.md"><mark>Project webpage</mark> </a>

**Paper:** <mark> <a href="https://www.osapublishing.org/boe/abstract.cfm?uri=boe-6-5-1565" target="_blank"> Link </a></mark> &nbsp;&nbsp; |  <mark> <a href="pdfs/distancePPG.pdf"> PDF </a></mark> |<a href="{filename}distancePPG-dataset.md"> <mark> Dataset  </mark></a> 

<hr size="20"> 
### ScaleMed ###
**A Platform for at-Scale mHealth Research and Development** 


<div class="container">
<div class="row clearfix">
<div class="col-md-8 column">
		<p class="text-justify"> ScaleMed is an end-to-end platform being developed at Rice University for conducting at-scale mHealth research and development. ScaleMed is specifically targeted towards mobile health diagnostic and measurement applications, and focuses on the information technology piece of scaling mobile health trials. ScaleMed has three key components: </p>

		<ol> 
		<li> <b>Medical App Modules, Libraries, and Templates</b>: These  modules and libraries help quickly develop mhealth research apps on smartphones by abstracting out few standard steps e.g. bluetooth connectivity, sensor data storage, basic UI, connecting to cloud for data-sync. We are also developing scenario specific template apps which can be easily extended for particular use.  
		<li> <b>Cloud control and management </b>: Central data synchronization and control is a critical component of any mid or large-scale health-care trial. Thus, we will be developing a ScaleMed cloud which connects to all ScaleMed nodes (smartphone/tablets), and provides central command, control, storage and management for the whole network of nodes used in a particular study. 
		<li> <b> Hardware Adaptor </b>: The hardware adaptor is designed to help researchers easiily integrate connectivity (e.g. bluetooth) into their custom sensor design so that  they can take advantage of ScaleMed smartphone libraries and the ScaleMed cloud.  
		</ol> 
</div>
<div class="col-md-4 column">
<img src="{filename}/images/scalemed.jpg" class="img-responsive center-block" alt="paper image" width = '100%'>
<p class="text-center"> Using ScaleMed platform, mHealth researchers can validate and test their innovation by conducting at-scale human trials quickly and easily. ScaleMed supports end-to-end lifecylce of a new mHealth innovation.  </p>
</div>
</div>
</div>

**Know more: ** <a href="https://github.com/Rice-Scalable-Health/scaleMed"><mark>Project webpage</mark> 

**Paper:** <mark> <a href="http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7454487&isnumber=7454459" target="_blank"> Link </a></mark> |  <mark> <a href="pdfs/scaleMed.pdf"> PDF </a></mark> 

 

