import csv
import random
import time
from datetime import datetime
import os

# Configurações
OUTPUT_PATH = "data_lake/trades.csv"
NUM_EVENTS = 50 # Quantos eventos vamos gerar agora

# Dados fictícios para simular o mercado
MARKETS = [
    "Will Bitcoin hit $100k by 2025?",
    "Will AI replace programmers?",
    "Will Brazil win the next World Cup?"
]
SIDES = ["buy", "sell"]

def generate_trade():
    """Gera uma transação aleatória"""
    return {
        "timestamp": datetime.now().isoformat(),
        "market": random.choice(MARKETS),
        "side": random.choice(SIDES),
        "price": round(random.uniform(0.01, 0.99), 2), # Preço entre 1 centavo e 99 centavos
        "quantity": random.randint(1, 100),
        "user_id": f"user_{random.randint(1, 10)}"
    }

def main():
    print(f"Iniciando geração de {NUM_EVENTS} eventos...")
    
    # Garante que a pasta existe (embora você já tenha criado)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    
    # Abre o arquivo para escrever (modo 'w' sobrescreve, 'a' adiciona)
    with open(OUTPUT_PATH, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["timestamp", "market", "side", "price", "quantity", "user_id"])
        writer.writeheader()
        
        for _ in range(NUM_EVENTS):
            event = generate_trade()
            writer.writerow(event)
            # time.sleep(0.05) # Simula um pequeno delay se quiser ver rodando devagar
            
    print(f"Sucesso! Arquivo gerado em: {OUTPUT_PATH}")

if __name__ == "__main__":
    main()