import pickle

data = pickle.load(open('numpy_images_with_labels.pckl', 'rb'))
output=open('write.txt', 'w')
output.write(str(data))
output.flush()
output.close()
