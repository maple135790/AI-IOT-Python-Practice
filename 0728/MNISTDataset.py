# -*- coding: utf-8 -*-
"""MNISTDataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_0nmu9PEnesgBEVa9F1K5VBOeNKFdIXV

import necessary packages
"""

import struct
import numpy

import torch
from torch.utils.data import Dataset

import google.colab.patches as colab

"""declare MNISTDataset class
: provide the interface for accessing MNIST hand-written digits dataset
"""

class MNISTDataset(Dataset):
  ##
  # MNISTDataset::__init__()
  ##
  def __init__(self, image_file, label_file):
    self.images = self.__unpack_image(image_file)
    self.labels = self.__unpack_label(label_file)

    if len(self.images) != len(self.labels):
      raise Exception('MNISTDataset::__init__(): num. of images and labels are mis-match!')  

  ##
  # MNISTDataset::getitem()
  #
  def getitem(self, index):
    # check the validity of index
    if index < 0 or index > len(self.images):
      raise Exception('MNISTDataset::__getitem__(): invalid index')

    return self.images[index], self.labels[index]

  ##
  # MNISTDataset::__getitem__()
  #
  def __getitem__(self, index):
    # invoke getitem to get the image and label
    image, label = self.getitem(index)
    
    # reshape the image with shape (h, w, 1)
    shape = image.shape
    image = image.reshape(shape[0], shape[1], 1)
    image = image.transpose(2,0,1)
    
    # normalize the image
    image = image / 255.0

    # convert to tensor image
    tensor_image = torch.from_numpy(image)
    tensor_image = tensor_image.type(torch.FloatTensor)
        
    return tensor_image, label

  ##
  # MNISTDataset::__len__()
  #
  def __len__(self):        
    return len(self.images)

  ##
  # MNISTDataset::__unpack_image
  #   
  # private method to unpack images
  ##
  def __unpack_image(self, image_file):
    # create image list
    images = list()
        
    # open the file and read in the data
    binary_file = open(image_file, 'rb')
    buffer = binary_file.read()
        
    # read the header of MNIST dataset
    magic, n_Images, n_Rows, n_Cols = struct.unpack_from('>IIII', buffer, 0)
    index = struct.calcsize('>IIII')
        
    # read the image from file
    for i in range(n_Images):
      # load the image
      image = struct.unpack_from('>784B', buffer, index)
            
      # move the index forward
      index = index + struct.calcsize('>784B')
            
      # conver the data to numpy array
      image = numpy.array(image, dtype='uint8')
      image = image.reshape(n_Rows, n_Cols, 1)
            
      # add image to image list
      images.append(image)

    return images
  
  ##
  # MNISTDataset::__unpack_label
  #   
  # private method to unpack labels
  ##
  def __unpack_label(self, label_file):
    # create label list
    labels = list()

    # open the file and read in the data
    binary_file = open(label_file, 'rb')
    buffer = binary_file.read()

    # read the header of MNIST dataset
    magic, n_Labels = struct.unpack_from('>II', buffer, 0)
    index = struct.calcsize('>II')

    # read the image from file
    for i in range(n_Labels):
      # load the image
      label = struct.unpack_from('>1B', buffer, index)

      # move the index forward
      index = index + struct.calcsize('>1B')
                        
      # add label to label list
      labels.append(label[0])
    
    # convert the data to the numpy
    labels = numpy.asarray(labels, dtype=numpy.int)
    return labels

"""define main function"""

if __name__ == "__main__":
  mnist_dataset = MNISTDataset("/content/drive/MyDrive/Colab Notebooks/LeNet/train-images.idx3-ubyte", 
                  "/content/drive/MyDrive/Colab Notebooks/LeNet/train-labels.idx1-ubyte")
  
  # get the first image
  image, label = mnist_dataset.getitem(1000)
  
  # show the image and its label
  print(f'{label}')
  colab.cv2_imshow(image)