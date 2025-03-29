#	Feedback Rank
#	Behrang Mehrparvar - Synaptosearch
#	synaptosearch@gmail.com
######################################

import os
import pickle
import numpy as np


model_location = "models/"

def login(user_id, password):
	return 1

def load_model(user_id, password, session_id, dimension):
	if not login(user_id, password):
		raise Exception("Login failed: Unauthorized (check credentials)")
	filename = model_location + user_id + "_" + session_id
	if not os.path.exists(filename):	
		W = np.zeros((dimension, dimension)) + np.eye(dimension, dimension)
		return W
	with open(filename, "rb") as file:
		W = pickle.load(file)
		return W
		
def save_model(user_id, password, session_id, W):
	if not login(user_id, password):
		raise Exception("Login failed: Unauthorized (check credentials)")
	filename = model_location + user_id + "_" + session_id
	with open(filename, "wb") as file:
		pickle.dump(W, file)
		
#	Entry point
def rank(user_id, password, session_id, target_vector_array, query_vector):
	if not len(query_vector) == len(target_vector_array[0]):
		raise Exception("Error: Vector sizes do not match.")
	W = load_model(user_id, password, session_id, len(query_vector))
	energies = [-0.5 * np.dot(query_vector, np.dot(W, target_vector_array[i])) for i in range(len(target_vector_array))]
	ranks = np.argsort(energies)
	return ranks

#	Entry point	
def feedback(user_id, password, session_id, target_vector_array, query_vector_array, feedback_array, rank_array):
	learning_rate = 1
	if not len(query_vector_array[0]) == len(target_vector_array[0]):
		raise Exception("Error: Vector sizes do not match.")
	W = load_model(user_id, password, session_id, len(query_vector_array[0]))
	#outer_product = (np.outer(target_vector_array, query_vector_array))
	#W = W + learning_rate * feedback_array * outer_product
	W = W + learning_rate * sum(feedback_array[i] * np.outer(target_vector_array[i], query_vector_array[i]) for i in range(len(feedback_array)))
	save_model(user_id, password, session_id, W)
	
def main():
	# Generate a dataset of 100 samples
	num_samples = 100
	vector_size = 10

	# Initialize empty lists for vectors and labels
	vectors1 = []
	labels = []

	for _ in range(num_samples):
		vector1 = np.random.rand(vector_size)
		label = np.random.randint(0, 2)  # Binary label (0 or 1)
		
		# Append to respective lists
		vectors1.append(vector1)
		labels.append(label)
	vector2 = np.random.rand(vector_size)

	# Convert lists to NumPy arrays
	vectors1_array = np.array(vectors1)
	vector2_array = np.array(vector2)
	labels_array = np.array(labels)

	ranks = rank("behrang", "123456", "1", vectors1_array, vector2_array)
	print(ranks)
	feedback("behrang", "123456", "1", vectors1_array, np.tile(vector2_array, (len(vectors1_array),1)), labels_array, ranks)
	ranks = rank("behrang", "123456", "1", vectors1_array, vector2_array)
	print(ranks)
	
if __name__ == "__main__":
	main()