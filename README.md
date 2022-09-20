## Implementing U-Net 11
Based on the [Teranus implementation of UNet 11.](https://github.com/ternaus/robot-surgery-segmentation)

Set up a Google Cloud VM
- n1-standard-4
- NVIDIA Tesla V100
- 50 GB boot disk
- Ubuntu Pro 16.04

Run following commands

```bash
## CUDA (can be run as one block)
wget http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/cuda-repo-ubuntu1604_9.2.148-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu1604_9.2.148-1_amd64.deb
sudo apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/7fa2af80.pub
sudo apt-get update
sudo apt-get install cuda

nvidia-smi

## Conda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
sh Miniconda3-latest-Linux-x86_64.sh
source .bashrc

conda

## Conda Environment
conda create --name torch python=3.6
conda activate torch
conda install pytorch=0.4.1 cuda92 -c pytorch
conda install torchvision=0.2
pip install opencv-python==3.3.0.10 tqdm==4.19.4 albumentations==0.0.4

sudo apt install unzip
unzip Dataset.zip

## Prepare Data
cd robot-surgery-segmentation
python3 prepare_data.py

## Training 
screen -m bash -c "./train.bash"

```
