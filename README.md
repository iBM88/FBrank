## Feedback-based Rank
The code provides a new ranking algorithm that takes into account the feedback provided by the caller application to learn a new distance measure.
The application of the code is presented in the _main.p_ file.
The two entry points to the algorithm are the _rank()_ and _feedback()_ functions.
The _rank()_ function takes a vector array as the documents (vectors1_array) and another vector array (vector2_array) as the question as inpyt and returns the ranks of the first array based on the similarity with the second vector:

ranks = rank("behrang", "123456", "1", vectors1_array, vector2_array)

The second function gives feedback to the algorithm on how the ranking was.
The _feedback()_ function gets two arrays of vectors as input and also the label (0 for not similar and 1 for similar) and also the output rank of the previous function (optional: this is just used to measure the MRR performance and not required):

feedback("behrang", "123456", "1", vectors1_array, np.tile(vector2_array, (len(vectors1_array),1)), labels_array, ranks)

Note that in both functions, the first and second input variables could be used for user access and the _session_ wariable enables each user to work with multiple models at the same time.

We have tested the algorithm on Wikipedia retrieval dataset:https://huggingface.co/datasets/ellamind/wikipedia-2023-11-retrieval-multilingual-qrels
The performance is increased from 0.3 to 0.4 on MRR.

For any questions and feedback pleas contact us through: synaptosearch@gmail.com

## License
This project is free for personal and academic use.  
Commercial use requires a paid license. Contact synaptosearch@gmail.com for details.
