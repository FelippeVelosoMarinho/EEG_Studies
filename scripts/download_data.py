import openneuro as on
import os

# Caminho para salvar (deve ser o mesmo que você está usando no seu notebook)
# Se o notebook está numa pasta e o dataset em '../datasets', ajuste aqui:
target_dir = '../datasets/ds005863' 

# Garante que a pasta existe
os.makedirs(target_dir, exist_ok=True)

print("Baixando os arquivos REAIS do sujeito 001...")

# Isso vai baixar o .vhdr, .vmrk e .eeg reais e substituir os ponteiros do git
on.download(
    dataset='ds005863',
    target_dir=target_dir,
    include=[
        'sub-001/*', 
        'dataset_description.json'
    ]
)

print("Download concluído. Agora o .vhdr é válido!")