import pydicom as dicom

path = "./img/D0189.dcm"
x = dicom.dcmread(path)
print(x)
