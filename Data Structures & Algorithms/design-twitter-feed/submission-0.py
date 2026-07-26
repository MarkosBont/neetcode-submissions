class Twitter:

    def __init__(self):
        self.minHeap = []

        self.following = {}
        self.tweetCounter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.minHeap, [-self.tweetCounter, tweetId, userId])
        self.tweetCounter += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        news = []
        heapCopy = self.minHeap.copy()

        while len(news) < 10 and heapCopy:
            tweet = heapq.heappop(heapCopy)
            if tweet[2] in self.following.get(userId, []) or tweet[2] == userId:
                news.append(tweet[1])
        
        return news


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId] = self.following.get(followerId, set())
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following.get(followerId, set()):
            self.following[followerId].remove(followeeId)
        
