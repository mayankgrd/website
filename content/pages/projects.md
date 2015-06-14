Title: Projects
save_as: projects.html

### DistancePPG ###
**Robust non-contact vital signs monitoring using a camera** 

<div class="container">
	<div class="row clearfix">
		<div class="col-md-8 column">
		<p class="text-justify"> <b>DistancePPG</b> is a photoplethysmogram (PPG) estimation algorithm which address two major challenges in camera-based vital sign monitoring: (i) extremely low signal strength of PPG signal, particularly for people with darker skin tones, and/or under low lighting conditions, (ii) motion artifacts due to movement of a person in front of a camera. DistancePPG proposes a new method of combining skin-color change signals from different regions of the face using a weighted average, where the weights depend on the blood perfusion and incident light intensity in the region, to improve the signal-to-noise ratio (SNR) of camera-based PPG estimate. The gains in SNR of camera-based PPG estimated using distancePPG translate into reduction of the error in vital sign estimation, and thus expand the scope of camera-based vital sign monitoring to potentially new scenarios. </p>
		</div>
		<div class="col-md-4 column">
			<div class="embed-responsive embed-responsive-4by3">
  				<iframe class="embed-responsive-item" width="500" height="375" src="https://www.youtube.com/embed/-jwGlLBxuH8" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
			</div>
		</div>
	</div>
</div>

<br/> <br /> 

| **Paper:** <span class="label label-warning"><a href="https://www.osapublishing.org/boe/abstract.cfm?uri=boe-6-5-1565" target="_blank"> Link </a></span> &nbsp;&nbsp;&nbsp; <span class="text-danger"> (Patent Pending)</span> | [Dataset]({filename}distancePPG-dataset.md) |

** Know more: **<a href="{filename}distancePPG.md"><mark>Project webpage</mark> <a>
### ScaleMed ###
**A Platform for at-Scale mHealth Research and Development **

ScaleMed is an end-to-end platform being developed at Rice University for conducting at-scale mHealth research and development. ScaleMed is specifically targeted towards mobile health diagnostic and measurement applications, and focuses on the information technology piece of scaling mobile health trials. ScaleMed has three key components:

1. **Medical App Modules, Libraries, and Templates**: These  modules and libraries help quickly develop mhealth research apps on smartphones by abstracting out few standard steps e.g. bluetooth connectivity, sensor data storage, basic UI, connecting to cloud for data-sync. We are also developing scenario specific template apps which can be easily extended for particular use.  
2. **Cloud control and management**: Central data synchronization and control is a critical component of any mid or large-scale health-care trial. Thus, we will be developing a ScaleMed cloud which connects to all ScaleMed nodes (smartphone/tablets), and provides central command, control, storage and management for the whole network of nodes used in a particular study. 
3. **Hardware Adaptor**: The hardware adaptor is designed to help researchers easiily integrate connectivity (e.g. bluetooth) into their custom sensor design so that  they can take advantage of ScaleMed smartphone libraries and the ScaleMed cloud.  

| <a href="https://github.com/Rice-Scalable-Health/scaleMed" target="_blank">Github link </a> | 

 

