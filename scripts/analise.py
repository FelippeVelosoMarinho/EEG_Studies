import mne
import os

# --- CONFIGURAÇÃO DE CAMINHO ---
# Pega o diretório onde este script/notebook está rodando
base_dir = os.getcwd()

# Constrói o caminho para o arquivo. 
# AJUSTE 'datasets' se sua pasta estiver em outro lugar relativo ao notebook.
vhdr_path = os.path.join(base_dir, '..', 'datasets', 'ds005863', 'sub-001', 'eeg', 'sub-001_task-Flanker_eeg.vhdr')

# Normaliza o caminho (resolve os '..') para evitar confusão do Windows
vhdr_file = os.path.normpath(vhdr_path)

print(f"Lendo arquivo em: {vhdr_file}")

# Verifica se o arquivo existe antes de tentar ler
if not os.path.exists(vhdr_file):
    print("ERRO: Arquivo não encontrado. Verifique se o nome da tarefa é 'Flanker' (maiúsculo) ou 'flanker' (minúsculo) na pasta.")
else:
    try:
        # --- CARREGAR DADOS ---
        raw = mne.io.read_raw_brainvision(vhdr_file, preload=True)

        # --- INFO ---
        print("\n--- SUCESSO! ---")
        print(f"Taxa de amostragem: {raw.info['sfreq']} Hz")
        print(f"Canais encontrados: {len(raw.ch_names)}")
        
        # Filtra apenas EEG para mostrar os nomes
        eeg_chans = raw.copy().pick_types(eeg=True).ch_names
        print(f"Primeiros 5 canais EEG: {eeg_chans[:5]}")
        
        # Plota para confirmar visualmente
        raw.plot(duration=5, n_channels=10, title="Sinal Real")

    except Exception as e:
        print(f"Erro ao ler: {e}")