Title: DistancePPG dataset
Slug: distancePPG-dataset
url: distancePPG/dataset/
save_as: distancePPG/dataset/index.html
status: hidden

## Experimental Setup 
For all single channel video recording in this study, we used Flea 3® USB 3.0 FL-U3-13E4MC monochrome camera operated at 30 frames per second, with a  esolution of 1280 x 1024, and 8 bits per pixel. We added a 40 nm full-width half-max (FWHM) Green filter (FB550-40 from Thor labs ®) in front of the monochrome camera. We selected green filter since the absorption spectra of Hb and HbO2 peaks in this wavelength region. Moreover, all commercial color camera have highest number of pixel having green filter (Bayer pattern). For color video recording, we used Flea 3® USB 3.0 FL-U3-13E4C-C color camera operated at 30 frames per second with RGB Bayer pattern having a total resolution of 1280 x 1024, and 8 bits per pixel.

**Ground Truth**: We used Texas Instruments AFE4490SPO2EVM pulse oximeter module to record  contact-based PPG signal for comparison. It operates at a sampling rate of 500  Hz. The distance between camera and subject was 0:5m. Both the camera system and the pulse-oximeter were started simultaneously, and the data is recorded in a PC workstation. 

<div class="alert alert-info" role="alert">
Dataset will be released soon. Contact <a href="mailto:mk28@rice.edu">author</a> for further details. 
</div> 


We varied three main three main parameters of interest for camera-based PPG and vital sign estimation: (i) skin tone of people, (ii) motion, (iii)
ambient light intensity. 

### Dataset 1 (skin tone)
This dataset contain single channel (green) video data from 12 subjects (7
Male, 5 Female) with different skin tones (from light, pale white to dark brown/black). For this dataset, subjects were asked to face the camera and be static for a duration of 40 sec (involuntary motions were not restricted).

### Dataset 2 (motion)
This dataset contain natural motion video (single green channel) under three natural motion scenarios - (i) reading on computer, (ii) watching video, (iii) talking. The motion scenarios are representative of a general class of motion exhibit by users of tablet, phone, or laptops while facing the screen. For each of the motion scenarios, 80 second video recordings for 5 subjects having different skin tones are recorded, along with their stationary video recording for baseline comparison.

### Dataset 3 (light intensity)
This dataset contains video  (single green channel) recording at diiferent illumination level from 50 lux upto 650 lux (ambient light is around 400-500 lux). Each video is for a duration of 40 seconds under each lighting conditions for two subjects having pale-white and brown skin tones

### Dataset 4 (Color video set)
This contains two sets of data: (i) static dataset comprising of color video (red, green, blue) of 4 subjects of varying skin tones (only nonCaucasian) for a duration of 60 seconds at 500 lux illumination, (ii) talking dataset comprising of color video of 4 subjects of varying skin tone (non-Caucasian), with 3 subjects having 500 lux illumination, and 1 subject having 300 lux illumination. This set is deliberately chosen to be extremely harsh (lower light, non-Caucasian skin tones, and large motion during talking) to highlight scenario where current known algorithms (including distancePPG) fails, and provide dataset where future algorithms can improve


