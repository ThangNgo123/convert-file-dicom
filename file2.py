import pydicom as dicom
# import matplotlib
# matplotlib.use('TkAgg')

import matplotlib.pyplot as plt


path = "./img/D0189.dcm"
x = dicom.dcmread(path)
plt.imshow(x.pixel_array, cmap=plt.cm.gray)
# plt.show()
plt.axis('off')
plt.savefig("output.png", bbox_inches='tight', pad_inches=0)