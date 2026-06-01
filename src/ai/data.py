TEXT_TO_CHUNK = '''
Machine learning is a subfield of artificial intelligence that enables computers to learn from data without being explicitly programmed. The core idea is that an algorithm finds patterns in examples and uses them to make predictions on new unseen data. There are three main approaches: supervised learning, unsupervised learning, and reinforcement learning. In supervised learning, a model is trained on labeled data consisting of input-output pairs. The model adjusts its internal parameters until its predictions closely match the expected outputs.

Neural networks are one of the most powerful tools in machine learning, loosely inspired by the structure of the human brain. They consist of layers of nodes, each of which applies a transformation to its inputs. Deep learning refers to neural networks with many layers and has revolutionized fields like computer vision and natural language processing. Convolutional neural networks excel at image recognition tasks by detecting local patterns like edges and textures. Recurrent neural networks were designed to handle sequential data like text and time series.

Transformers are a neural network architecture that underpins modern language models like GPT and BERT. The attention mechanism allows the model to weigh the relevance of every word relative to every other word in a sentence. This made transformers dramatically more effective at understanding language than previous architectures. Large language models are trained on billions of text examples and develop surprisingly rich internal representations of concepts, facts, and reasoning patterns.
'''

sentences = [
    'Neural networks have made a breakthrough in natural language processing.',
    'Modern deep learning algorithms analyze huge amounts of data.',
    'The development of artificial intelligence requires powerful computing resources.',
    'Machine translation technology is improving every year.',
    'The use of vector representations helps computers understand the meaning of text.',
    'Language models are trained on massive datasets of web pages and books.',
    'Semantic search allows finding information by meaning, not just by keywords.',
    'Companies are actively implementing chatbots to automate customer support.',
    'Data security has recently become a top priority for software developers.',
    'Cloud computing provides unlimited opportunities for scaling projects.',
    'Saint Petersburg attracts tourists with its rich history and architecture.',
    'The commuter train from Saint Petersburg to Kirishi takes about two and a half hours.',
    'Leningrad Oblast is famous for its dense forests and picturesque lakes.',
    'In spring, the active season for gathering wild berries begins in these parts.',
    'In winter, the air temperature here often drops below freezing.',
    'A morning walk in the forest perfectly charges you with energy for the whole day.',
    'Many local residents prefer to spend their weekends at the dacha.',
    'A good book helps to distract from the everyday hustle and bustle of the city.',
    'Delicious hot coffee is the perfect start to a productive morning.',
    'The ability to listen to your interlocutor is an important part of effective communication.',
]


test_embeddings_queries = [
    'How long does a commuter train ride to Kirishi take?',
    'Optimizing customer operations through automated dialogue systems.',
    'An invigorating warm breakfast drink helps to get into a working mood.',
    'Vector NLP models have fundamentally changed the field of text analytics.',
    'Countryside landscapes of the Northwest region are known for dense arrays of trees.'
]