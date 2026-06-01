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

