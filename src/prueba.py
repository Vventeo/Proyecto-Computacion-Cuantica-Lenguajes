from qiskit import qiskit, QuantumCircuit
from qiskit.visualization import plot_histogram     #Visualizacion
from qiskit_aer import AerSimulator     #Simulacion
from qiskit_ibm_runtime import SamplerV2 as Sampler, QiskitRuntimeService   #Ejecucion Real

bell = QuantumCircuit(2)

bell.h(0)
bell.cx(0,1)


bell.measure_all()
print("Circuito cuántico:")

bell.draw("mpl")
# print(qc.draw(output="text"))