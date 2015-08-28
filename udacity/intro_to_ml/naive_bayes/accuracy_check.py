from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData
from classify import NBAccuracy

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl


features_train, labels_train, features_test, labels_test = makeTerrainData()

def submitAccuracy(m):
    accuracy = NBAccuracy(features_train, labels_train, features_test, labels_test, method=m)
    return accuracy

print "method 1: %s" % (submitAccuracy(1))
print "method 2: %s" % (submitAccuracy(2))
