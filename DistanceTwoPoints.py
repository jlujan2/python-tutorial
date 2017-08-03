import numpy as np
import random
import scipy.stats as ss
import matplotlib.pyplot as plt

def distance(p1,p2):
	"""Find the distance between points p1 and p2."""
	return np.sqrt(np.sum(np.power(p2-p1, 2)))

def majority_vote(votes):
	"""xxx"""
	vote_counts = {}
	for vote in votes:
		if vote in vote_counts:
			vote_counts[vote] += 1
		else:
			vote_counts[vote] = 1
	
	winners = []
	max_count = max(vote_counts.values())
	for vote, count in vote_counts.items():
		if count == max_count:
			winners.append(vote)
		
	return random.choice(winners)

def majority_vote_short(votes):
	"""return the most commom element in votes"""
	mode, count = ss.mstats.mode(votes)		
	return mode

def find_nearest_neighbors(p, points, k=5):
	"""Find the k neares neighbors of point p and return their indices"""
	distances = np.zeros(points.shape[0])
	for i in range(len(distances)):
		distances[i] = distance(p, points[i])
	ind = np.argsort(distances)
	return ind[:k]

def knn_predict(p, points, outcomes, k=5):
	ind = find_nearest_neighbors(p, points, k)
	return majority_vote(outcomes[ind])

def generate_synth_data(n=50):
	"""create two sets of points from bivariate normal distributions."""
	points = np.concatenate((ss.norm(0,1).rvs((n,2)), ss.norm(1,1).rvs((n,2))), axis=0)
	outcomes = np.concatenate((np.repeat(0,n), np.repeat(1,n)))
	return (points, outcomes)
	
def make_prediction_grid(predictors, outcomes, limits, h, k):
    """Classify each point on the prediction grid"""
    (x_min, x_max, y_min, y_max) = limits
    xs = np.array(x_min, x_max, h)
    ys = np.array(y_min, y_max, h)
    xx, yy = np.meshgrid(xs, ys)
    
    prediction_grid = np.zeros(xx.shape, dtype = int)
    for i,x in enumerate(xs):
        for j,y in enumerate(ys):
            p = np.array([x,y])
            prediction_grid[j,i] = knn_predict(p, predictors, outcomes, k)
            
    return (xx, yy, prediction_grid)
	
votes = [1,2,3,3,3,3,1,2,2,1,2,3,2,1,2,3,1,3,1,1,2,2,2,4,4,5,5]
vote_counts = majority_vote(votes)
print (vote_counts)
vote_counts2 = majority_vote_short(votes)
print (vote_counts2)
p1 = np.array([1,1])
p2 = np.array([4,4])
print (distance(p1,p2))


points = np.array([[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3]])
p = np.array([2.5,2])

ind = find_nearest_neighbors(p, points, 2)
print (ind)

outcomes = np.array([0,0,0,0,1,1,1,1,1])
knn_predict(np.array([2.5,2.7]), points, outcomes, k=2)

n = 20
(points, outcomes) = generate_synth_data(n)
plt.figure()	
plt.plot(points[:n,0], points[:n,1], "ro")
plt.plot(points[n:,0], points[n:,1], "bo")
plt.savefig("bivardata.pdf")

plt.plot(p[0], p[1], "bo")
plt.axis([0.5,3.5,0.5,3.5])
plt.show()