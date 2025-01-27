# ai-models-graphcast

[Google Colab](https://colab.research.google.com/drive/13RHUKtwzjxB32QqU6auoIyoMa7Ibx3hX?usp=sharing)
[Youtube Walkthrough of Colab](https://www.youtube.com/watch?v=BTyhgp9Hugc)

`ai-models-graphcast` is an [ai-models](https://github.com/ecmwf-lab/ai-models) plugin to run Google Deepmind's [GraphCast](https://github.com/deepmind/graphcast).

GraphCast: Learning skillful medium-range global weather forecasting, arXiv preprint: 2212.12794, 2022. https://arxiv.org/abs/2212.12794

GraphCast was created by Remi Lam, Alvaro Sanchez-Gonzalez, Matthew Willson, Peter Wirnsberger, Meire Fortunato, Ferran Alet, Suman Ravuri, Timo Ewalds, Zach Eaton-Rosen, Weihua Hu, Alexander Merose, Stephan Hoyer, George Holland, Oriol Vinyals, Jacklynn Stott, Alexander Pritzel, Shakir Mohamed and Peter Battaglia.

The model weights are made available for use under the terms of the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0). You may obtain a copy of the License at: https://creativecommons.org/licenses/by-nc-sa/4.0/.

## Installation


you will need python 3.10 or greater
```bash
sudo apt install python-is-python3
sudo apt install python3-pip
sudo apt install nvidia-cuda-toolkit
```

This will install the package and most of its dependencies.

Then to install graphcast dependencies (and Jax on GPU):

### Graphcast and Jax

Graphcast depends on Jax, which needs special installation instructions for your specific hardware.

Please see the [installation guide](https://github.com/google/jax#installation) to follow the correct instructions.

pip install -U "jax[cuda12_local]" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html has worked in the past

We have prepared two `requirements.txt` you can use. A CPU and a GPU version:

For the preferred GPU usage:
```
pip install -r requirements-gpu.txt -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html
```

For the slower CPU usage:
```
pip install -r requirements.txt
```
