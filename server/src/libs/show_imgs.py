import matplotlib.pyplot as plt

def show_imgs(imgs, names, figsize=(15,7)):
    fig = plt.figure(figsize=figsize)
    nrow,ncol = 1, len(imgs)    
    for i in range(ncol):
        fig.add_subplot(nrow, ncol, i + 1)
        plt.imshow(imgs[i], cmap='gray' if len(imgs[i].shape)==2 else None)
        if names:
            plt.title(names[i])
    plt.show()