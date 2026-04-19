from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# ── 1. Crear el circuito ──────────────────────────────────────────
# 1 qubit cuántico, 1 bit clásico para guardar la medición
qc = QuantumCircuit(1, 1)

qc.h(0)        # Compuerta Hadamard: pone el qubit en superposición
qc.measure(0, 0)  # Mide el qubit y guarda el resultado en el bit clásico

# ── 2. Visualizar el circuito ─────────────────────────────────────
print("Circuito cuántico:")
print(qc.draw(output="text"))

# ── 3. Simular ────────────────────────────────────────────────────
simulator = AerSimulator()
job = simulator.run(qc, shots=1000)  # Ejecutar 1000 veces
resultado = job.result()
conteos = resultado.get_counts()

# ── 4. Mostrar resultados ─────────────────────────────────────────
print("\nResultados después de 1000 ejecuciones:")
for estado, cantidad in sorted(conteos.items()):
    porcentaje = (cantidad / 1000) * 100
    barra = "█" * (cantidad // 20)
    print(f"  |{estado}⟩ : {cantidad:4d} veces ({porcentaje:.1f}%) {barra}")