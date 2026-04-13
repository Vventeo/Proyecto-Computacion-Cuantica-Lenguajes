from qiskit_ibm_runtime import QiskitRuntimeService

service = QiskitRuntimeService()

# Listar backends disponibles ordenados por cola
backends = service.backends(operational=True, simulator=False)
backends_ordenados = sorted(backends, key=lambda b: b.status().pending_jobs)

print(f"Conexión exitosa. Backends disponibles: {len(backends)}\n")
for b in backends_ordenados[:5]:
    status = b.status()
    print(f"{b.name} | qubits: {b.num_qubits} | cola: {status.pending_jobs} jobs")