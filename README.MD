# TrainingData.Solutions Interview Task #3
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Test task for the position of technical support trainee with knowledge of Python at [TrainingData](https://trainingdata.notion.site/TrainingData-Solutions-716057e76ab64e0988c39f381a8987ec)


## Description
`3. Mask task`

Your task is to make masks based on the given data.

In the [Задание2](Задание2) folder there are masks.xml and an “images” folder with 8 photos. The masks.xml file contains the markup of 8 photos. The task is to make 2 types of masks:
1) place a mask on the original,
2) make a mask on a black background. The Ignore class should be black on the mask and transparent in the photo.

Below is an example:

<img src="Untitled (2).png" width=600/ alt="mask-on-a-black-background" />

Explanations:

> To draw masks, you should use the Pillow library.

> Pay attention to the sequence of layer overlays when drawing a mask.

## Getting Started

### Installing
1. Clone the repository:
```
git clone <repo>
```
2. Install the required packages:
```
python -m pip install -r ./requirements.txt
```

### Executing program
Run the script:
```
python masks.py
```