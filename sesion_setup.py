from qiskit_ibm_runtime import QiskitRuntimeService
from dotenv import load_dotenv
import os

# Cargar variables del .env
load_dotenv()

# Obtener la API KEY
IBM_API_KEY = os.getenv("IBM_API_KEY")
IBM_CRN = os.getenv("IBM_CRN")

QiskitRuntimeService.save_account(
    
    token=IBM_API_KEY,
    instance=IBM_CRN
)

print("Credenciales guardadas correctamente.")