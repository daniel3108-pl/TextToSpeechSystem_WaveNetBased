from typing import *


training_config: Dict = {
    'model': {
        'encoder': {
            'epochs': 20,
            'batch-size': 10,
            'learning-rate': 0.01
        },
        'decoder': {
            'epochs': 20,
            'batch-size': 10,
            'learning-rate': 0.01
        },
        'wavenet': {
            'epochs': 20,
            'batch-size': 10,
            'learning-rate': 0.01
        },
        'output-file': "trained-model.pth"
    },
    'dataset': {
        'root-dir': './dataset/',
        'definition-file': 'metadata.csv',
        'audio-directory': 'wavs/'
    }
}

generator_config: Dict = {

}