class Twitter:

    def __init__(self):
        self.user = {}
        self.tweets = []
        self.counter = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        tweet = (self.counter, userId, tweetId)
        self.tweets.append(tweet)
        self.counter += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        heapq.heapify(minHeap)

        followers = set(self.user.get(userId, []) + [userId])
        for tweet in self.tweets:
            if tweet[1] in followers:
                minHeap.append(tweet)
        
        while len(minHeap) > 10:
            heapq.heappop(minHeap)
        
        
        tweetIds = [x[2] for x in sorted(minHeap)]
        print(tweetIds)

        return tweetIds[::-1]


    def follow(self, followerId: int, followeeId: int) -> None:
        self.user[followerId] = self.user.get(followerId, [])

        if followeeId not in self.user[followerId]:
            self.user[followerId].append(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user.get(followerId, []):
            self.user[followerId].remove(followeeId)
        
