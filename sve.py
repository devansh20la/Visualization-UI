import torch
import torch.nn as nn
import torch.optim as optim
from torch.autograd import Variable
import numpy as np
from torchvision import datasets,models,transforms
import os
import copy
from skimage import io
from PIL import Image


data_transforms = transforms.Compose([
	transforms.Scale(256),
	transforms.CenterCrop(224)])


imgnames = [fn for fn in os.listdir('data/') if fn.endswith('.jpg')]


for i in range(len(imgnames)):
	new_img = data_transforms(Image.open('data/' + imgnames[i]))
	io.imsave(imgnames[i].split(".")[0] + '.png', new_img)


