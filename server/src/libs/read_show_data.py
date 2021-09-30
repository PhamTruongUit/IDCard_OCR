import cv2
import matplotlib.pyplot as plt

def read(path, gray=False):
    # opencv read img with BGR
    raw_img = cv2.imread(path)
    if gray:
        return cv2.cvtColor(raw_img, cv2.COLOR_BGR2GRAY)
    # if opencv==False:
    return cv2.cvtColor(raw_img, cv2.COLOR_BGR2RGB)

def show(imgs, names, title = '', figsize=(15,7)):
    fig = plt.figure(figsize=figsize)
    fig.suptitle(title, fontsize=16)
    nrow,ncol = 1, len(imgs)    
    for i in range(ncol):
        fig.add_subplot(nrow, ncol, i + 1)
        plt.imshow(imgs[i], cmap='gray' if len(imgs[i].shape)==2 else None)
        if names:
            plt.title(names[i])
    plt.show()