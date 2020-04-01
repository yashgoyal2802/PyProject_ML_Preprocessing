import pickle

def read_pickle():
    data = pickle.load(open('numpy_images_with_labels.pckl', 'rb'))
    output = open('pickle_to_text.txt', 'w')
    output.write(str(data))
    output.flush()
    output.close()