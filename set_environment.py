# set up conda env
'''conda create -n mlx4-2'''

# activate environment
'''conda activate mlx4-2'''

# install utilitiy packages
'''conda install pip ipykernel python-dotenv'''

# install pytorch - bloated version (can also just install pytorch, without torchvision or torchaudio)
'''conda install pytorch-nightly::pytorch torchvision torchaudio -c pytorch-nightly'''
