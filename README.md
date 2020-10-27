# Metaballs

This project shows a pygame application > metaballs < which has been optimized with numpy and cupy.

 1. [metaballs.py](Metaballs/metaballs.py) -> pure python/pygame implementation
 2. [metaballs_numpy.py](Metaballs/metaballs_numpy.py) ->  speedup with numpy
 3. [metaballs_cupy.py](Metaballs/metaballs_cupy.py) ->  speedup with cupy ( Nvidia CUDA )

 On my PC with an intel I5-6600k @ 3.5Ghz & NVIDIA GeForce GTX 1060 6GB

|variant| fps |
|---------|--|
|pure python      |~0.6  |
|numpy 	          |  ~17 |
|cupy             |~111   |


&nbsp; 

![metaballs.py](https://raw.githubusercontent.com/Pog3k/Metaballs/main/images/metaballs.gif) ![metaballs_numpy.py](https://raw.githubusercontent.com/Pog3k/Metaballs/main/images/metaballs_numpy.gif) ![metaballs_cupy.py](https://raw.githubusercontent.com/Pog3k/Metaballs/main/images/metaballs_cupy.gif)

## How to run

This project has been tested with Python 3.8.3.  
Make sure you have pygame, numpy, and cupy installed on your python interpreter.  
For cupy it is mandatory that you have the nvidia toolkit in the exact same version installed.  
See https://docs.cupy.dev/en/stable/install.html.

Install necessary python packages with pip if you don't have them installed yet:

	pip install -r requirements.txt

Run:

    python metaballs.py
    python metaballs_numpy.py
    python metaballs_cuda.py
