# ChatGPT Generated Programs

### 🤖️ Input: "Using the programming language PROCESSING, write a program to draw a psychedelic fractal zoom"

Source: [pyschedelic_fractal.pde](https://github.com/kennycason/chatgpt_code/blob/main/psychedelic_fractal.pde)

[Video](https://v.usetapes.com/tN8SdeBlYD)

Output: 
> Here is a simple implementation of a psychedelic fractal zoom in the programming language Processing:
> This code generates a psychedelic fractal zoom by drawing a series of lines with random colors at each iteration. The zoom level is gradually increased over time, resulting in a constantly changing and mesmerizing visual effect.

Worked after moving `size(500, 500);` into the `setup()` function.

<img src="https://github.com/kennycason/chatgpt_code/blob/main/output/psychedelic_fractal02.png?raw=true" width="33%"/><img src="https://github.com/kennycason/chatgpt_code/blob/main/output/psychedelic_fractal03.png?raw=true" width="33%"/><img src="https://github.com/kennycason/chatgpt_code/blob/main/output/psychedelic_fractal04.png?raw=true" width="33%"/>



### 🤖️ Input: "Write python code to control dc motor with L298N Motor Driver Controller with reverse and forward"

Source: [dc_motor_with_l298n.py](https://github.com/kennycason/chatgpt_code/blob/main/dc_motor_with_l298n.py)

I was quite surprised as to the breadth of ChatGPT with this one. 
It was able to generate a working Python code to control two DC motors via the L298N Motor Driver Controller with reverse and forward.
The generated code had a minor bug that prevented reverse from working, otherwise it worked out-of-the-box. 
I tested it on a robotic tank I have been working on.



### 🤖️ Input: "Using the programming language PROCESSING (java mode), write john conway's game of life and then simplify the code and remove code comments"

[Video](https://v.usetapes.com/h4XFbxRH9F)

Source: [game_of_life.py](https://github.com/kennycason/chatgpt_code/blob/main/game_of_life.pde)


Worked after minor edits and asking ChatGPT to write specific functions separately due to the length of the program. 
This surprisingly worked quite well, and I only needed reference ChatGPT in order to write this program. 
Additionally, this is my first project to use Processing. (I have since learned you can just tell ChatGPT to "Continue on".)

<img src="https://github.com/kennycason/chatgpt_code/blob/main/output/game_of_life_running.png?raw=true" />

<img src="https://github.com/kennycason/chatgpt_code/blob/main/output/game_of_life01.png?raw=true" width="50%"/><img src="https://github.com/kennycason/chatgpt_code/blob/main/output/game_of_life02.png?raw=true" width="50%"/><img src="https://github.com/kennycason/chatgpt_code/blob/main/output/game_of_life03.png?raw=true" width="50%"/><img src="https://github.com/kennycason/chatgpt_code/blob/main/output/game_of_life04.png?raw=true" width="50%"/>



### 🤖️ Input: "Using python programming language write a mandelbrot zoom program in pygame"

Source: [mandelbrot_zoom.py](https://github.com/kennycason/chatgpt_code/blob/main/mandelbrot_zoom.py)

I was again happily surprised that the code both compiled and ran. The only issue I encountered was that the Mandelbrot Zoom was being re-rendered every game loop instead of only when there were changes to its zoom & position. This was an easy update, and below are some example GIFs that I compiled from some output screenshots. I'm pretty confident that I could have just asked ChatGPT to make such improvements, and even handle the image output, but I was hitting rate-limit issues with the API.

<img src="https://github.com/kennycason/chatgpt_code/blob/main/output/mandelbrot_zoom1.gif?raw=true" width="33%" /><img src="https://github.com/kennycason/chatgpt_code/blob/main/output/mandelbrot_zoom2.gif?raw=true" width="33%" /><img src="https://github.com/kennycason/chatgpt_code/blob/main/output/mandelbrot_zoom3.gif?raw=true" width="33%" />



### 🤖️ Input: "Write a simple neural network in python and then remove code comments"

Source: [neural_network.py](https://github.com/kennycason/chatgpt_code/blob/main/neural_network.py)

Code worked as-is. 

Target Vector: `[0, 1, 1, 0]`
Output:
```bash
[[0.03896381]
 [0.95923365]
 [0.96770453]
 [0.04000064]]
```



### 🤖️ Input: "Using the python programming language that please write a program for visually pleasing infinite psychedelic pattern."

I was indeed pleased with the result!

Source: [visually_pleasing_infinite_pattern.py](https://github.com/kennycason/chatgpt_code/blob/main/visually_pleasing_infinite_pattern.py)

[Video](https://v.usetapes.com/lhoOLUoir8)

<img src="https://github.com/kennycason/chatgpt_code/blob/main/output/visually_pleasing_infinite_pyschedelic_pattern.png?raw=true" />


### 🤖️ Input:  "Write python code to read camera data via picamera2 and detect faces with opencv."

Source: [opencv_face_detection.py](https://github.com/kennycason/chatgpt_code/blob/main/opencv_face_detection.py)

### 🤖️ Input: "Write python code for blackjack game"

File: [blackjack.py](https://github.com/kennycason/chatgpt_code/blob/main/blackjack.py)

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

Source: [blackjack2.py](https://github.com/kennycason/chatgpt_code/blob/main/blackjack2.py)

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

Source: [pokemon_like_techno.py](https://github.com/kennycason/chatgpt_code/blob/main/pokemon_like_techno.py)



### 🤖️ Input: "Using the python programming language and pygame library and only geometry shapes, write a simple bomberman game**"

The generated code had a couple issues such as `bomberman_x` and `bomberman_y` being undefined, and the player + background colors were the same.
I was still impressed that I was able to get nearly working `PyGame` starter program with working Joystick controls. 

Source: [bomberman.py](https://github.com/kennycason/chatgpt_code/blob/main/bomberman.py)

<img src="https://github.com/kennycason/chatgpt_code/blob/main/output/bomberman_pygame.png?raw=true" width="50%"/>



### 🤖️ Input: "Using the programming language PROCESSING (java mode), write a program to draw a psychedelic pattern"

Source: [pyschedelic_pattern.pde](https://github.com/kennycason/chatgpt_code/blob/main/pyschedelic_pattern.pde)

Worked after minor editing.

<img src="https://github.com/kennycason/chatgpt_code/blob/main/output/psychedelic_pattern01.png?raw=true" width="33%"/><img src="https://github.com/kennycason/chatgpt_code/blob/main/output/psychedelic_pattern03.png?raw=true" width="33%"/>


### 🤖️ Short Stories

[Hell](https://github.com/kennycason/chatgpt_code/blob/main/short_story_hell.txt) - "Write short story about reality hell and god that will give me an existential crisis"

[Transcension](https://github.com/kennycason/chatgpt_code/blob/main/short_story_transcension.txt) - "Write a short story about transcension and the full realization of absolute infinity"

