import nltk

def analyze_blog_post(text):
    # Tokenize the text into words
    words = nltk.word_tokenize(text)
    
    # Remove stop words
    stop_words = nltk.corpus.stopwords.words("english")
    words = [word for word in words if word not in stop_words]
    
    # Perform stemming
    stemmer = nltk.stem.PorterStemmer()
    words = [stemmer.stem(word) for word in words]
    
    # Calculate some statistical measures
    num_words = len(words)
    num_unique_words = len(set(words))
    lexical_diversity = num_unique_words / num_words
    num_sentences = len(nltk.sent_tokenize(text))
    average_sentence_length = num_words / num_sentences
    
    # Print the results
    print(f"Number of words: {num_words}")
    print(f"Number of unique words: {num_unique_words}")
    print(f"Lexical diversity: {lexical_diversity:.2f}")
    print(f"Number of sentences: {num_sentences}")
    print(f"Average sentence length: {average_sentence_length:.2f}")

# Read the blog post from a file
with open("blog_post.txt", "r") as f:
    text = f.read()

# Analyze the blog post
analyze_blog_post(text)