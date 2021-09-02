# TODO: create the User class
# it must support rank, progress, and the inc_progress(rank) method

class User:
    def __init__(self, rank=-8, progress=0):
        self.rank = rank
        self.progress = progress
        
    def inc_progress(self, activity_rank):
        self.validate_activity_rank(activity_rank)
        point = self.cal_point(activity_rank)   
        inc_rank, inc_point = divmod(self.progress+point, 100)
        print("rank : {}, progress : {}, activity_rank : {}, inc_rank : {}, inc_point : {}".format(self.rank, self.progress, activity_rank, inc_rank, inc_point))
        self.progress = inc_point
        
        if self.rank + inc_rank >= 8:
            self.rank = 8
            self.progress = 0
        elif self.rank < 0 and self.rank + inc_rank >= 0:
            self.rank = self.rank + inc_rank + 1
        else:
            self.rank = self.rank + inc_rank

    def cal_point(self, activity_rank):
        if activity_rank == -1 and self.rank == 1:
            return 1
        elif activity_rank+1 == self.rank:
            return 1
        elif activity_rank == self.rank:
            return 3
        elif activity_rank+1 < self.rank:
            return 0
        else:
            d = activity_rank - self.rank - 1 if self.rank < 0 and activity_rank > 0 else activity_rank - self.rank
            point = 10 * d * d
            return point

    def validate_activity_rank(self, activity_rank):
        if activity_rank < -8 or activity_rank > 8 or activity_rank == 0:
            raise Exception('error')

        
if __name__ == "__main__":
    user = User()
print(user.rank)
print(user.progress)
user.inc_progress(-7)
print(user.progress)
user.inc_progress(-5)
print(user.progress)
print(user.rank)
    