from itertools import cycle
test_images = ['1.jpg', '2.jpg', '3.jpg', '4.jpg']
train_images = ['000005.jpg', '000007.jpg', '000009.jpg', '000012.jpg']
test_images.extend(train_images)
all_images_itr = cycle(iter(test_images))


i=0%4
j=4%4
pass