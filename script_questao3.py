import os
import subprocess

OUTPUT_DIR = "results_questao3"

TAXA_CHEGADA = 9.4          
TEMPO_SERVICO = 0.88        
TEMPO_OBSERVACAO = 30       

SERVERS_RANGE = range(5, 15)

os.makedirs(OUTPUT_DIR, exist_ok=True)

def run_simulation(num_servidores):
    print(f"Executando simulação com {num_servidores} servidores "
          f"(Taxa de Chegada: {TAXA_CHEGADA} req/s, Tempo de Serviço: {TEMPO_SERVICO}s, Tempo de Observação: {TEMPO_OBSERVACAO}s)...")
    
    output_file = os.path.join(OUTPUT_DIR, f"servidores-{num_servidores}.txt")

    command = [
        "java", "-cp", "bin;lib/*", "ServidorWeb",
        str(TAXA_CHEGADA), str(TEMPO_SERVICO), str(num_servidores), str(TEMPO_OBSERVACAO)
    ]

    with open(output_file, "w") as f:
        subprocess.run(command, stdout=f)
    
    print(f"Resultados salvos em: {output_file}")

for num_servidores in SERVERS_RANGE:
    run_simulation(num_servidores)

print(f"Simulações concluídas! Verifique os resultados na pasta '{OUTPUT_DIR}'")
