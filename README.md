# birdvision

This repository contains work for my computer vision project, BirdVision. The goal of this project is to create an image classifier capable of identifying a bird's species and differentiating unique birds within a given species. I want to eventually connect the image classifier to a camera using a RaspberryPi or something similar.

# First Species Classifier
I've started by following a PyTorch Finetuning tutorial to finetune the Resnet-18 Deep Learning Image Recognition model on a dataset of 200 species of birds. It is still unknown what the full dataset will look like as there are over 11,000 species of birds worldwide and training is expensive even for this dataset of 200. A final prototype of this classifier might include some sort of 

Training for 30 epochs took almost 10 hours to complete and resulted in a best accuracy of 78.65%. Refer to SpeciesClassifier.ipynb for more details

# Identifying unique birds
The most difficult part of this project is teaching the model to recognize and identify unique birds. Initially I feel like this problem leans closer to facial recognition than to image classification, so resources on facial recognition might be useful. First it is important to understand how birds differ within a species. I would think there are markings, feather patterns, and color differences that can allow different birds to be distinguished from eachother. Another idea is to incorporate the bird's chirping and calling to distinguish unique birds, as there might be differences in the frequencies at which birds call that can allow us to uniquely identify them. 


## Prototype features
- HD camera with audio and video capabiliities.
- Software linked to the camera that hosts a pretrained model with its weights on a RaspberryPi computer locally.
- Camera can send pictures and audio to the model for inference
- Unique birds are tagged, recorded, and saved to a library

### Image and Audio Processsing
1. The camera takes a picture of a bird and records some audio of its calling/chirping.
2. Images and audio recordings are saved and sent to the model for inference
3. The model predicts the bird's species and identifies it as a new/seen species, and identifies it as a new/seen bird.
4. 
