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

eval_text = '''
The history of space exploration began in earnest during the mid-twentieth century, driven largely by competition between the United States and the Soviet Union. The Soviet Union achieved the first major milestones: launching Sputnik, the first artificial satellite, in 1957, and sending Yuri Gagarin into orbit in 1961, making him the first human in space. The United States responded with the Apollo program, which successfully landed astronauts on the Moon in 1969. Neil Armstrong became the first person to walk on the lunar surface, famously declaring it a small step for man but a giant leap for mankind.

After the Moon landings, attention shifted toward long-duration spaceflight and orbital stations. The Soviet Union operated the Mir space station for fifteen years, accumulating invaluable data on how the human body adapts to microgravity. Later, international cooperation produced the International Space Station, which has been continuously inhabited since the year 2000 and serves as a laboratory for science, medicine, and technology development.

In recent decades, private companies have transformed the landscape of space exploration. SpaceX, founded by Elon Musk, developed reusable rocket technology that dramatically reduced launch costs. Blue Origin and Virgin Galactic began offering suborbital flights, opening the door to space tourism. NASA returned its focus to the Moon through the Artemis program, aiming to land the first woman and next man on the lunar surface using the Space Launch System rocket.

Mars has become the next major destination. Robotic missions including NASA's Perseverance rover and China's Zhurong rover have explored the Martian surface searching for signs of ancient life. SpaceX has announced ambitions to send humans to Mars within this decade, though significant technical and biological challenges remain, including radiation exposure during the journey and the effects of low gravity on the human body over extended periods.
'''

questions = [
    ('Who was the first human to travel to space?', 1),
    ('What was the name of the first artificial satellite?', 0),
    ('When did humans first land on the Moon?', 1),
    ('How long did the Mir space station operate?', 2),
    ('When did continuous habitation of the ISS begin?', 3),
    ('What technology did SpaceX develop to reduce launch costs?', 4),
    ('What is the name of NASAs program to return to the Moon?', 5),
    ('What are the names of the Mars rovers mentioned in the text?', 6),
    ('What biological challenges are mentioned for a Mars mission?', 7),
    ('What did Neil Armstrong say when he landed on the Moon?', -1),
]

