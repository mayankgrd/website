Title: PulseCam: a camera-based, motion-robust and highly sensitive blood perfusion imaging modality
Slug: pulseCam
url: pulseCam/
save_as: pulseCam/index.html
status: hidden


<p class="text-center"><a href="http://www.ece.rice.edu/~mk28/" target="_blank">Mayank Kumar</a>, <a href="https://www.bcm.edu/people/view/james-suliburk-m-d-facs/b264d8d6-ffed-11e2-be68-080027880ca6" target="_blank">Dr. James Suliburk </a>, <a href="http://www.ece.rice.edu/~av21/" target="_blank"> Ashok Veeraraghavan </a> and <a href="http://www.ece.rice.edu/~ashu/" target="_blank">Ashu Sabharwal </a></p>
<p class="text-center text-muted">6100 Main Street, Rice University, Houston, Tx, 77005, USA</p>


## The Problem

<p class="text-justify"> Measuring peripheral blood perfusion, i.e. the flow of blood to end-organs and tissue through the blood vessels, has widespread clinical applications such as assessment of wounds and burns, diagnosing peripheral arterial disease (especially in patients suffering from diabetes), monitoring micro-circulation to identify shock in critical care, and for monitoring blood flow at surgical sites, e.g. during plastic surgeries and surgical revascularization procedures. Popular clinical markers of local or peripheral perfusion such as center-to-toe temperature difference, skin mottling and capillary refill time are subjective indicators that lack the required sensitivity and specificity to identify patients with compromised peripheral perfusion. Moreover, contact-based optical modalities such as Laser Doppler Flowmetry, Near-infrared Spectroscopy (NIRS), and pulse oximeter that are routinely used in clinical practice can only measure blood flow and hemoglobin related parameters at a specific location on the skin surface, i.e., at the point-of-contact, and their measurements are sensitive to the exact placement of the probe. The high spatial variability in blood perfusion across tissue such as the skin limits the clinical utility of such single point contact-based modalities. </p> 




## Our Solution

<p class="text-justify"> We develop PulseCam, a new camera-based blood perfusion imaging modality that enables clinicians and surgeons to visualize real-time, accurate, three-dimensional spatio-temporal maps of pulsatile blood perfusion underneath the skin surface using only the video of the skin surface or internal tissue. PulseCam achieves 2-3x higher sensitivity compared to the current standard of care in perfusion measurement. In contrast to existing methods that only provide a single point estimate of blood perfusion, PulseCam provides quantitative spatio-temporal blood pulsation maps achieving 1 mm spatial resolution and 1 frame-per-second temporal resolution. PulseCam achieves all these using only a video recording from a standard camera and pulse recording from a standard pulse oximeter as input making the system orders of magnitude cheaper than alternatives such as infrared thermography and Laser Doppler Perfusion Imaging.  </p>

<p class="justify"> We have evaluated PulseCam both in a lab setting as well as in a clinical context. We demonstrate that: (i) PulseCam-derived pulsatile perfusion estimates can easily detect arterial and venous blood flow occlusion that is difficult to identify using existing modalities, e.g. using perfusion index measured using a pulse oximeter, (ii) has at least two times better sensitivity and three times better response time in detecting blood flow occlusion compared to an infrared thermal camera, and (ii) is robust and reliable in an operationally challenging surgery-room setting where PulseCam is evaluated in a clinical setting during a surgery in which general anesthesia is used.  Overall, PulseCam represents a new paradigm in low-cost and easy-to-use blood perfusion imaging system providing a holistic view of a patient's hemodynamic state in real-time. We anticipate that PulseCam will be used both at the bedside as well as a point-of-care blood perfusion imaging device to visualize and analyze blood perfusion in an easy-to-use and cost-effective manner.</p>



<div>
	<img src="{filename}/images/pulseCam_fig1.webp" class="img-responsive center-block" alt="paper image" width = '80%'>
	<p class="text-center"> <b>PulseCam - A camera-based multi-sensor blood perfusion imaging modality: </b> (a) PulseCam combines the video recording of the skin surface (or internal tissue) and a reference blood volume waveform to reliably obtain blood perfusion map over the entire imaged skin surface or tissue region, (b) a schematic diagram of PulseCam used as a bedside perfusion imaging system in critical care and the operating room, (c) a schematic diagram of PulseCam used as a hand-held imaging tool to visualize blood perfusion at surgical sites, wounds and ulcers 
</div>

## Papers

### Journal
Kumar, M., Suliburk, J.W., Veeraraghavan, A. et al. PulseCam: a camera-based, motion-robust and highly sensitive blood perfusion imaging modality. Sci Rep 10, 4825 (2020). https://doi.org/10.1038/s41598-020-61576-0 (Patent pending) <mark>  <a href="{filename}/pdfs/pulseCam_journal.pdf">  PDF </a></mark>
| <mark> <a href="https://rdcu.be/b3xep"> Web </a> </mark>

<b>Cite (BibTex) </b> 
<pre>
@Article{Kumar2020,
author={Kumar, Mayank
and Suliburk, James W.
and Veeraraghavan, Ashok
and Sabharwal, Ashutosh},
title={PulseCam: a camera-based, motion-robust and highly sensitive blood perfusion imaging modality},
journal={Scientific Reports},
year={2020},
volume={10},
number={1},
pages={4825},
issn={2045-2322},
doi={10.1038/s41598-020-61576-0},
url={https://doi.org/10.1038/s41598-020-61576-0}
}

</pre>

### Conference
Kumar, M., Suliburk, J., Veeraraghavan, A., & Sabharwal, A. (2016). PulseCam: High-resolution blood perfusion imaging using a camera and a pulse oximeter. In 2016 38th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC) (pp. 3904–3909). IEEE. <mark> <a href="{filename}/pdfs/PulseCam.pdf"> PDF </a></mark> | <mark> <a href = "https://ieeexplore.ieee.org/document/7591581"> Web</a> </mark>

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



## Evaluating PulseCam in a lab and a clinic 
<div class="container">
	<div class="row clearfix">
		<div class="col-md-4 column">
			<h3 class="text-center">Arterial and venous occlusion </h3> 
			<div class="embed-responsive embed-responsive-4by3">
  				<iframe src="https://player.vimeo.com/video/407491075" width="500" height="313" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>
			</div>
			<p class="text-center">The video shows the blood perfusion map in the palm of a participant while we occlude the arterial blood flow using a manual pressure cuff at 140 mmHg. PulseCam can faithfully recover reduction in pulsatile blood flow in the palm during occlusion and a sudden increase in blood flow after release. </p>
		</div>
		<div class="col-md-4 column">
			<h3 class="text-center">Incremental vascular occlusion </h3> 
			<div class="embed-responsive embed-responsive-4by3">
  				<iframe src="https://player.vimeo.com/video/407492678" width="500" height="313" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>
			</div>
			<p class="text-center">The video shows the blood perfusion map in both the palms while we occlude the the flow of blood to one of the palm (left palm). We use manual pressure cuff to incrementally occlude the blood flow with 10 mmHg, 20 mmHg . . . 100 mmHg occlusion pressure. PulseCam can easily detect blood perfusion changes due to even 10-20 mmHg occlusion pressure difference that is difficult to identify using existing modalities. </p> 
		</div>
		<div class="col-md-4 column">
			<h3 class="text-center">Anesthesia monitoring </h3> 
			<div class="embed-responsive embed-responsive-4by3">
  				<iframe src="https://player.vimeo.com/video/407493245" width="500" height="313" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>
			</div>
			<p class="text-center">The video shows the blood perfusion map in the palm of a patient undergoing surgery in which general anesthesia is used. Anesthesia induction is known to cause an increase in peripheral blood perfusion. PulseCam can easily detect an increase in blood perfusion in the palm just after anesthesia induction. Also, PulseCam can recover these perfusion changes in a challenging clinical setting.</p>
		</div>
	</div>
</div>



## Testing PulseCam during an arterial occlusion and reactive hyperemia 
<div class="container">
	<div class="row clearfix">
		<div class="col-md-8 column">
			<img src="{filename}/images/sample_result.png" class="img-responsive center-block" alt="paper image" width = '90%'>
			<p class="text-justify"><b>Measuring spatial and temporal blood perfusion variations during a blood flow occlusion experiment using PulseCam</b>: Temporal and spatial variations of blood perfusion in the palm for a participant before, during and after a blood flow occlusion experiment: (a) Image inlet at the top shows four sample ROIs for which the temporal trend in the blood perfusion is shown (ROI $1-4$); also shown for comparison is the contact-based perfusion index measurement done using a pulse oximeter (blue plot), (b) Image inlets shows spatial map of blood perfusion in the palm at different stages of the blood flow occlusion using false color map. Obtaining such spatial maps using existing contact-based modality is not feasible.</p>
		</div>
		<div class="col-md-4 column">
			<div class="embed-responsive embed-responsive-4by3">
  				<iframe class="embed-responsive-item" width="500" height="313" src="https://player.vimeo.com/video/210254783" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
			</div>
			<p class="text-center">False color video showing spatial map of perfusion in the palm during a blood flow occlusion test: Red regions have higher blood flow, dark region have lower blood flow. Blood flow in the palm occluded by putting pressure cuff in the arm. More blood flows into the palm just after release of occlusion, thereby hinting that PulseCam can capture the blood flow dynamics associated with a post occlusive reactive hyperemia. 
 			</p>
 		</div>
	</div>
</div>



