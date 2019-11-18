# '#' 안을 채워주세요
from sklearn.cluster import KMeans
from collections import deque
def recolor_image(img, k=5):

    img = mpimg.imread('C:/temp/d.jpg')
    pixels = [pixel for row in img for pixel in row]

    clusterer=KMeans(n_clusters=k,init='k-means++',n_init=10,max_iter=300,tol=0.0001,precompute_distances='auto',verbose=0,copy_x=True,n_jobs=1,algorithm='auto')
    clusterer.fit(pixels)
    ##
    def recolor(pixel):
        return clusterer.predict(pixel)
         # index of the closest cluster
         # mean of the closest cluster


    new_img = [[recolor(pixel) for pixel in row]
               for row in img]

    plt.imshow(new_img)
    plt.axis('off')
    plt.show()

#이미지는 마음대로 선정해서 이미지 있는 파일 자료까지 넣으면된다.이미지를 색깔로 묶기