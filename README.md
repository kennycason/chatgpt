# ChatGPT Generated Programs


### 🤖️ Input: "Using the programming language PROCESSING (java mode), write john conway's game of life and then simplify the code and remove code comments"

[Video](https://v.usetapes.com/h4XFbxRH9F)

Source: [game_of_life.py](https://github.com/kennycason/chatgpt/blob/main/game_of_life.pde)


Worked after minor edits and asking ChatGPT to write specific functions separately due to the length of the program. 
This surprisingly worked quite well, and I only needed reference ChatGPT in order to write this program. 
Additionally, this is my first project to use Processing. (I have since learned you can just tell ChatGPT to "Continue on".)

<img src="https://github.com/kennycason/chatgpt/blob/main/output/game_of_life_running.png?raw=true" />

<img src="https://github.com/kennycason/chatgpt/blob/main/output/game_of_life01.png?raw=true" width="50%"/><img src="https://github.com/kennycason/chatgpt/blob/main/output/game_of_life02.png?raw=true" width="50%"/><img src="https://github.com/kennycason/chatgpt/blob/main/output/game_of_life03.png?raw=true" width="50%"/><img src="https://github.com/kennycason/chatgpt/blob/main/output/game_of_life04.png?raw=true" width="50%"/>



### 🤖️ Input: "Using python programming language write a mandelbrot zoom program in pygame"

Source: [mandelbrot_zoom.py](https://github.com/kennycason/chatgpt/blob/main/mandelbrot_zoom.py)

I was again happily surprised that the code both compiled and ran. The only issue I encountered was that the Mandelbrot Zoom was being re-rendered every game loop instead of only when there were changes to its zoom & position. This was an easy update, and below are some example GIFs that I compiled from some output screenshots. I'm pretty confident that I could have just asked ChatGPT to make such improvements, and even handle the image output, but I was hitting rate-limit issues with the API.

<img src="https://github.com/kennycason/chatgpt/blob/main/output/mandelbrot_zoom1.gif?raw=true" width="33%" /><img src="https://github.com/kennycason/chatgpt/blob/main/output/mandelbrot_zoom2.gif?raw=true" width="33%" /><img src="https://github.com/kennycason/chatgpt/blob/main/output/mandelbrot_zoom3.gif?raw=true" width="33%" />



### 🤖️ Input: "Using the programming language PROCESSING, write a program to draw a psychedelic fractal zoom"

Source: [pyschedelic_fractal.pde](https://github.com/kennycason/chatgpt/blob/main/psychedelic_fractal.pde)

[Video](https://v.usetapes.com/tN8SdeBlYD)

Output: 
> Here is a simple implementation of a psychedelic fractal zoom in the programming language Processing:
> This code generates a psychedelic fractal zoom by drawing a series of lines with random colors at each iteration. The zoom level is gradually increased over time, resulting in a constantly changing and mesmerizing visual effect.

Worked after moving `size(500, 500);` into the `setup()` function.

<img src="https://github.com/kennycason/chatgpt/blob/main/output/psychedelic_fractal02.png?raw=true" width="33%"/><img src="https://github.com/kennycason/chatgpt/blob/main/output/psychedelic_fractal03.png?raw=true" width="33%"/><img src="https://github.com/kennycason/chatgpt/blob/main/output/psychedelic_fractal04.png?raw=true" width="33%"/>



### 🤖️ Input: "Write python code to control dc motor with L298N Motor Driver Controller with reverse and forward"

Source: [dc_motor_with_l298n.py](https://github.com/kennycason/chatgpt/blob/main/dc_motor_with_l298n.py)

I was quite surprised as to the breadth of ChatGPT with this one. 
It was able to generate a working Python code to control two DC motors via the L298N Motor Driver Controller with reverse and forward.
The generated code had a minor bug that prevented reverse from working, otherwise it worked out-of-the-box. 
I tested it on a robotic tank I have been working on.



### 🤖️ Input: "Write a simple neural network in python and then remove code comments"

Source: [neural_network.py](https://github.com/kennycason/chatgpt/blob/main/neural_network.py)

Code worked as-is.

Target Vector: `[0, 1, 1, 0]`
Output:
```bash
[[0.03896381]
[0.95923365]
[0.96770453]
[0.04000064]]
```

### 🤖️ Input: "Write code using tensorflow for a simple auto-encoder with training data random 4d vectors"

Source: [autoencoder.py](https://github.com/kennycason/chatgpt/blob/main/autoencoder.py)

Code worked as-is, though I modified logging + epoch count.

Output:
```bash
Original input: [[0.27955452 0.20003414 0.38206231 0.71578143]]
Decoded output: [[0.21143627 0.1500811  0.30098823 0.6853668 ]]
Noisy input: [[0.36291848 0.20566826 0.39934306 0.81038985]]
Decoded Noise output: [[0.28726333 0.15678793 0.31848305 0.7758708 ]]
```



### 🤖️ Input: "Using the python programming language that please write a program for visually pleasing infinite psychedelic pattern."

I was indeed pleased with the result!

Source: [visually_pleasing_infinite_pattern.py](https://github.com/kennycason/chatgpt/blob/main/visually_pleasing_infinite_pattern.py)

[Video](https://v.usetapes.com/lhoOLUoir8)

<img src="https://github.com/kennycason/chatgpt/blob/main/output/visually_pleasing_infinite_pyschedelic_pattern.png?raw=true" />


### 🤖️ Input:  "Write python code to read camera data via picamera2 and detect faces with opencv."

Source: [opencv_face_detection.py](https://github.com/kennycason/chatgpt/blob/main/opencv_face_detection.py)

### 🤖️ Input: "Write python code for blackjack game"

File: [blackjack.py](https://github.com/kennycason/chatgpt/blob/main/blackjack.py)

I finished the final lines of code myself due to ChatGPT output buffer max length.

```shell
Your hand:
10 of Hearts
3 of Spades
Dealer's hand:
10 of Diamonds
Your hand:
10 of Hearts
3 of Spades
10 of Clubs
You busted! Dealer wins.
```
```shell
Your hand:
5 of Spades
1 of Diamonds
Dealer's hand:
10 of Clubs
Your hand:
5 of Spades
1 of Diamonds
2 of Spades
Your hand:
5 of Spades
1 of Diamonds
2 of Spades
1 of Hearts
Your hand:
5 of Spades
1 of Diamonds
2 of Spades
1 of Hearts
10 of Clubs
You win!
```

Source: [blackjack2.py](https://github.com/kennycason/chatgpt/blob/main/blackjack2.py)

Worked as-is

```shell
Your hand:
7 of Hearts
10 of Clubs
Dealer's hand:
2 of Clubs
Dealer's hand:
2 of Clubs
7 of Spades
10 of Hearts
You Lose!
```



### 🤖️ Input: "Using the Python programming language write code to generate pokemon like techno music"

While not particularly Pokémon like, I was surprised this program worked. I only needed to download a few WAV files.

Source: [pokemon_like_techno.py](https://github.com/kennycason/chatgpt/blob/main/pokemon_like_techno.py)



### 🤖️ Input: "Using the python programming language and pygame library and only geometry shapes, write a simple bomberman game**"

The generated code had a couple issues such as `bomberman_x` and `bomberman_y` being undefined, and the player + background colors were the same.
I was still impressed that I was able to get nearly working `PyGame` starter program with working Joystick controls. 

Source: [bomberman.py](https://github.com/kennycason/chatgpt/blob/main/bomberman.py)

<img src="https://github.com/kennycason/chatgpt/blob/main/output/bomberman_pygame.png?raw=true" width="50%"/>



### 🤖️ Input: "Using the programming language PROCESSING (java mode), write a program to draw a psychedelic pattern"

Source: [pyschedelic_pattern.pde](https://github.com/kennycason/chatgpt/blob/main/pyschedelic_pattern.pde)

Worked after minor editing.

<img src="https://github.com/kennycason/chatgpt/blob/main/output/psychedelic_pattern01.png?raw=true" width="33%"/><img src="https://github.com/kennycason/chatgpt/blob/main/output/psychedelic_pattern03.png?raw=true" width="33%"/>



### 🤖️ Improve Chinese Blog Post - 遗传算法与重现画像

[Google Doc 遗传算法与重现画像](https://docs.google.com/document/d/1hLsP1NeJ-Huv7-mNarOGKzyI_FoeC15tJae2-86gt9U/edit#)

This was a blog post I wrote in Chinese previously on the subject of generating images using genetic algorithms. Linked below is a Google Doc which shows the before and after for each paragraph. I was quite impressed with the results and ChatGPT was even able to explain it's reasoning for its changes.




### 🤖️ Chinese Lesson - 显微镜与微生物 / Microscopes & Microorganisms

Lesson: [chinese_lesson_microscopes_microorganisms.md](https://github.com/kennycason/chatgpt/blob/main/chinese_lesson_microscopes_microorganisms.md)

This project/experiment was motivated by the success I had using ChatGPT to improve my Chinese post on genetic algorithms.



### 🤖️ Short Stories

[Hell](https://github.com/kennycason/chatgpt/blob/main/short_story_hell.txt) - "Write short story about reality hell and god that will give me an existential crisis"

[Transcension](https://github.com/kennycason/chatgpt/blob/main/short_story_transcension.txt) - "Write a short story about transcension and the full realization of absolute infinity"

