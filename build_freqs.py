
# ```python
 def build_freqs(tweets, ys):
#     """Build frequencies.
#     Input:
#         tweets: a list of tweets
#         ys: an m x 1 array with the sentiment label of each tweet
#             (either 0 or 1)
#     Output:
#         freqs: a dictionary mapping each (word, sentiment) pair to its
#         frequency
#     """
#     # Convert np array to list since zip needs an iterable.
#     # The squeeze is necessary or the list ends up with one element.
#     # Also note that this is just a NOP if ys is already a list.
    yslist = np.squeeze(ys).tolist()
# 
#     # Start with an empty dictionary and populate it by looping over all tweets
#     # and over all processed words in each tweet.
    freqs = {}
     for y, tweet in zip(yslist, tweets):
         for word in process_tweet(tweet):
             pair = (word, y)
             if pair in freqs:
                 freqs[pair] += 1
             else:
                 freqs[pair] = 1    
     return freqs
# ```

# You can also do the for loop like this to make it a bit more compact:
# 
# ```python
#     for y, tweet in zip(yslist, tweets):
#         for word in process_tweet(tweet):
#             pair = (word, y)
#             freqs[pair] = freqs.get(pair, 0) + 1
# ```
