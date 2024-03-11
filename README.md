# Specification

1. Import *SentencePiece* to use for tokenizing our data
2. Prepare the dataset of Hacker News titles and upvote scores
   * Obtain the data from the database `postgres://arcanum:c1af7a45f6a59656cc89fbc4@pg.mlx.institute:5432/arcanum`
   * Tokenise the titles using SentencePiece
3. Implement and train an architecture to obtain word embeddings in the style of the *word2vec* paper
   [https://arxiv.org/pdf/1301.3781.pdf](https://arxiv.org/pdf/1301.3781.pdf)
   using either the **continuous bag of words (CBOW)* or *Skip-gram* model (or both).
4. Implement a regression model to predict a Hacker News upvote score from the pooled average of the word embeddings in each title.
5. *Extension* : train your word embeddings on a different dataset, such as

* More Hacker News content, such as comments
* A completely different corpus of text, like (some of) Wikipedia



* Take in a Hacker News title
* Convert it to a list of token embeddings using our word2vec architecture
* Take the average of those embeddings (this is called **average pooling** and it is actually quite a crude technique; we will see how you can do better next week with RNNs).
* Pass this averaged embedding through a series of hidden layers with widths and activation functions of your choice.
* Pass the result through an output layer, which should be a linear layer with a single neuron, in order to product a single number representing the network's prediction for the upvote score.
* Compare the predicted score with the true score (the  *label* ) via an *Mean Square Error* loss function.


The suggested Workflow will consist of 4 main Steps:

1. Develop your FastAPI serve that provides inference for your model locally on your laptop.
2. Turn your application into a Docker Image and push to [DockerHub](https://hub.docker.com/).
3. Pull your image from DockerHub, either on your local machine or the server from which inference will be done, and then instanciate a container.
4. Whenever you have a new version of your image with your model, tear down your old container and start another.
