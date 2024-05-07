import random

# Definimos la matriz de transición de segundo orden
transitions = {
    ('A', 'A'): {'A': 0.1, 'B': 0.8, 'C': 0.1},
    ('A', 'B'): {'A': 0.4, 'B': 0.3, 'C': 0.3},
    ('A', 'C'): {'A': 0.3, 'B': 0.6, 'C': 0.1},
    ('B', 'A'): {'A': 0.2, 'B': 0.6, 'C': 0.2},
    ('B', 'B'): {'A': 0.5, 'B': 0.2, 'C': 0.3},
    ('B', 'C'): {'A': 0.3, 'B': 0.4, 'C': 0.3},
    ('C', 'A'): {'A': 0.3, 'B': 0.4, 'C': 0.3},
    ('C', 'B'): {'A': 0.2, 'B': 0.3, 'C': 0.5},
    ('C', 'C'): {'A': 0.1, 'B': 0.7, 'C': 0.2}
}

# Función para generar una secuencia de estados
def generate_sequence(start_state, length):
    sequence = [start_state]
    current_state = start_state
    for _ in range(length - 1):
        # Verificar si hay transiciones definidas para el estado actual
        if (current_state, sequence[-1]) not in transitions:
            break
        next_state_probs = transitions[current_state, sequence[-1]]
        next_state = random.choices(list(next_state_probs.keys()), weights=list(next_state_probs.values()))[0]
        sequence.append(next_state)
        current_state = next_state
    return sequence

# Definimos el estado inicial y la longitud de la secuencia a generar
start_state = 'A'
sequence_length = 10

# Generamos la secuencia de estados
sequence = generate_sequence(start_state, sequence_length)
print("Secuencia generada:", sequence)
