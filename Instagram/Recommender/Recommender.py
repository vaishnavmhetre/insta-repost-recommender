from app import MAX_RECOMMENDATIONS


class Recommender:

    def __init__(self, externalPosts, recommendationsCount=MAX_RECOMMENDATIONS):
        self.externalPosts = externalPosts
        self.recommendationsCount = recommendationsCount

        filtered = self.applyFilters()
        aggregated = self.aggregateResults(filtered)

        self.recommended = aggregated

    def applyFilters(self):
        maxLikesTrue = self.filterMaxLikesTrue()
        return [maxLikesTrue]

    def aggregateResults(self, results=[]):
        return results[0]

    def filterMaxLikesTrue(self):
        return sorted(self.externalPosts, key=lambda k: k['like_count'], reverse=True)[:self.recommendationsCount]
