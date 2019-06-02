## Humpback Whale Identification

https://www.kaggle.com/c/humpback-whale-identification/overview/evaluation

the project purpose was to identify a whale by a picture of its tale.

#### Exploratory phase:

- observing data which showed that some of the training pictures were unclear and damaged and some of the pictures were grayscale
- calculating the share of the grayscale photos in the training data( i did this part)
- estimate share of the damaged photos by sampling
- reading other peoples experiences and discussions in this competition and the playground competition (i contributed in this part)
- searching about the whales themselves
- observe that the number of classes was so high so we couldn't use classic CNN's and we had to solve a problem like "face detection"

#### Feature Selection:

cause we used some type of CNN networks we couldn't specify the features ourselves
but we could somehow edit the input picture so we came up with techniques:

- segment the picture into 2 parts: "whale" and "the rest" 
   so the network learn to ignore the rest
   (at last, we came up just to a bounding box)
   - I did a lot of research at this part and I found 
      1. a segmentation network which required a lot of train data
      2. k-means based algorithms which didn't work well 
      3. "bounding box solution" which people used before and it was ok
- use SIFT from opencv to emphasize some parts
  (i did this part)
- coloring grayscale pictures
- detecting edges of the whale

#### Machine Learning Approach:

we used Siamese Networks cause this problem was similar to a face detection problem. (I searched in this part)
but training this network needed pairs of pictures and the share of "true pairs" and "false pairs" was important we used "lapjv" algorithm to select pairs

#### Evaluation Phase:

evaluation function was  Mean Average Precision which you can read more about in the kaggle link

for better evaluation, we split a part of data as test data and tested our code results on that
(Cause upload limit was 5 times a day)
(I implemented MAP for offline evaluation)