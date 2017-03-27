Title: DistancePPG: Robust non-contact vital signs monitoring using a camera 
Slug: distancePPG
url: distancePPG/
save_as: distancePPG/index.html
status: hidden


<p class="text-center"><a href="http://www.ece.rice.edu/~mk28/" target="_blank">Mayank Kumar</a>, <a href="http://www.ece.rice.edu/~av21/" target="_blank"> Ashok Veeraraghavan </a> and <a href="http://www.ece.rice.edu/~ashu/" target="_blank">Ashu Sabharwal </a></p>
<p class="text-center text-muted">6100 Main Street, Rice University, Houston, Tx, 77005, USA</p>


## The Problem

<p class="text-justify">Measuring and monitoring any patient's vital signs is essential for their care- in fact, all care first begins by collecting vital signs like heart rate and blood pressure. The current standard of care is based on monitoring devices that require contact - electrocardiograms, pulse-oximeter, blood pressure cuffs, and chest straps. However, contact-based methods have serious limitations for monitoring vital signs of neonates as they have extremely sensitive skin and most contact-based vital sign monitoring techniques result in skin abrasions, peeling and damage every time the leads or patches are removed. This results in potentially dangerous sites for infection increasing the mortality risk to the neonates. </p>

## Our Solution

<p class="text-justify">We propose to use normal camera to measure the vital signs of a patient by simply recording video of their face in a non-contact manner. From the recorded video of the face, our algorithm, distancePPG, extracts pulse rate (PR), pulse rate variability (PRV) and breathing rate (BR). The algorithm is based on estimating tiny changes in skin color due to changes in blood volume underneath the skin surface (these changes are invisible to the naked eye, but can be captured by a camera).</p>

<p class="text-justify"> Our algorithm, distancePPG (patent pending), achieves clinical grade accuracy for all skin tones, under low light conditions and can account for natural motion of subjects. It does so by intelligently combining skin color change signal from different regions of the visible skin in a manner that improves the overall signal strength. Our algorithm results in as much as 6dB of SNR improvement in harsh scenarios, rapidly expanding the scope, viability, reach and utility of CameraVitals as a replacement for traditional contact-based vital sign monitor. </p>

<div>
	<img src="{filename}/images/paper-header.png" class="img-responsive center-block" alt="paper image" width = '80%'>
	<p class="text-center">Four basic steps in distancePPG: <b>Step (i)</b> Extract landmark points such as eyes, nose, mouth and face boundary from face image, <b>Step (ii) </b> Face is divided into seven regions, each region tracked over the video using computer vision tracker, <b>Step (iii) </b> Each tracked region is further divided into small regions of interest (ROI), <b>Step (iv) </b> DistancePPG computes the goodness metric associated with each ROI based only on the video recordings, and estimate camera-based PPG signal with much higher SNR (signal to noise ratio). For more details, please read our paper.</p> 
</div>
## Media Coverage 
<div class="container">
    <div class="row">
        <div class="col-md-2 thumb">
            <a class="thumbnail" href="http://www.techbriefs.com/component/content/article/ntb/tech-briefs/imaging/22261" target="_blank">
            <img class="img-responsive" src="{filename}/images/nasa_tech.jpg" alt="Nasa Tech Briefs"> </a>
        </div>
        <div class="col-md-2 thumb">
            <a class="thumbnail" href="http://www.dailymail.co.uk/sciencetech/article-3027887/Your-face-reveal-health-Researchers-reveal-new-algorithm-monitors-vital-signs-video.html" target="_blank">
            <img class="img-responsive" src="{filename}/images/dailymailcom_sml.png" alt="The Daily Mail"> </a>
        </div>
        <div class="col-md-2 thumb">
            <a class="thumbnail" href="http://www.medgadget.com/2015/04/new-camera-technique-detects-heart-respiratory-rates-nearly-people.html" target="_blank">
            <img class="img-responsive" src="{filename}/images/medgadget-noheadline.png" alt="MedGadget"> </a>
        </div>
        <div class="col-md-2 thumb">
            <a class="thumbnail" href="https://e2e.ti.com/blogs_/b/thinkinnovate/archive/2015/06/09/untethered-a-new-idea-to-measure-vital-signs-in-preemies" target="_blank">
            <img class="img-responsive" src="{filename}/images/texas_instruments.png" alt="Texas Instruments"> </a>
        </div>
        <div class="col-md-2 thumb">
            <a class="thumbnail" href="http://optics.org/news/6/4/12" target="_blank">
            <img class="img-responsive" src="{filename}/images/optics.png" alt="SPIE Optics"> </a>
        </div>
        <div class="col-md-2 thumb">
            <a class="thumbnail" href="http://economictimes.indiatimes.com/magazines/panache/new-system-uses-video-of-your-face-to-track-health/articleshow/46839033.cms" target="_blank">
            <img class="img-responsive" src="{filename}/images/economic_times.cms" alt="The Economic Times"> </a>
        </div>
    </div>
</div>

## Paper 
M. Kumar, A. Veeraraghavan, and A. Sabharwal, "DistancePPG: Robust non-contact vital signs monitoring using a camera," Biomed. Opt. Express  6, 1565-1588 (2015) <mark> (Patent Pending) </mark> 

<b>Cite (BibTex) </b>
<pre>
@article{kumar_distanceppg:_2015,
author = {Kumar, Mayank and Veeraraghavan, Ashok and Sabharwal, Ashutosh},
doi = {10.1364/BOE.6.001565},
issn = {2156-7085},
journal = {Biomedical Optics Express},
mendeley-groups = {photoplethysmography},
month = may,
number = {5},
pages = {1565},
shorttitle = {DistancePPG},
title = {{DistancePPG: Robust non-contact vital signs monitoring using a camera}},
url = {https://www.osapublishing.org/boe/abstract.cfm?uri=boe-6-5-1565},
volume = {6},
year = {2015}
}
</pre>

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









