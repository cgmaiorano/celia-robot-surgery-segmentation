## Implementing U-Net 11

This repo is based on the [Teranus implementation of UNet 11.](https://github.com/ternaus/robot-surgery-segmentation)

### Start to Finish Execution

First, set up a Google Cloud VM with the following properties:
- n1-standard-4
- NVIDIA Tesla V100
- 50 GB boot disk
- Ubuntu Pro 16.04
- Spot instance (optional, but significantly cheaper)

Then, run the following commands one-by-one unless specified otherwise:

```bash
## CUDA (can be run as one block)
wget http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/cuda-repo-ubuntu1604_9.2.148-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu1604_9.2.148-1_amd64.deb
sudo apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/7fa2af80.pub
sudo apt-get update
sudo apt-get install cuda

# Verification: make sure a GPU shows up here
nvidia-smi

## Conda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
sh Miniconda3-latest-Linux-x86_64.sh
source .bashrc

# Verification: this command runs
conda

## Conda Environment
conda create --name torch python=3.6
conda activate torch
conda install pytorch=0.4.1 cuda92 -c pytorch
conda install torchvision=0.2
pip install opencv-python==3.3.0.10 tqdm==4.19.4 albumentations==0.0.4

# Self-verification: try importing things in the python3 console

## Get Code & Data
git clone https://github.com/nkalupahana/robot-surgery-segmentation.git
wget <LINK_TO_DATSET_ZIP> # you may need to Ctrl-C after it says the file has saved
sudo apt install unzip
unzip Dataset.zip

## Preprocess Data
cd robot-surgery-segmentation
python3 prepare_data.py

## Training (takes around five hours)
screen -m bash -c "./train.bash"
# Detach screen by pressing Ctrl-A, then d
# Attach the screen to look at progress by running screen -r

# Because training runs in screen, you can exit your terminal session and come 
# back later as long as your VM remains on.
```

I chose the best performing model by choosing the one that had 
the lowest loss and highest jaccard score during training. 
Training was done with k-fold, with four folds.