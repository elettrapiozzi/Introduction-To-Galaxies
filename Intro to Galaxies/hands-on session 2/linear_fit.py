import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 1. Dati sperimentali (Esempio per la Temperatura T)
# Sostituisci T_val con [1e3, 1e4, 1e5] a seconda del tuo set di dati
T_val = np.array([5, 10, 15, 20]) # Esempio di temperature
masse_jeans = np.array([0.5e9, 1.02e9, 1.54e9, 2.14e9]) 

# 2. Calcolo errori basato sulla bisezione (1%)
# Errore assoluto sulla massa
err_massa_assoluto = masse_jeans * 0.01

# Trasformazione per il fit in scala logaritmica (log10)
log_T = np.log10(T_val)
log_M = np.log10(masse_jeans)

# L'errore del logaritmo (base 10) si ricava dalla propagazione:
# delta(log10(x)) = delta(x) / (x * ln(10))
# Se delta(x)/x = 0.01 (1%), allora l'errore sui log è costante!
err_log_M = 0.01 / np.log(2.3025) # circa 0.0043

# 3. Definizione funzione lineare per il fit
def model_lin(x, m, q):
    return m * x + q

# 4. Esecuzione del Fit (pesato con gli errori)
popt, pcov = curve_fit(model_lin, log_T, log_M, sigma=np.ones_like(log_M)*err_log_M)
m_fit, q_fit = popt
m_err = np.sqrt(pcov[0,0])

# 5. Plotting
plt.figure(figsize=(8, 6))

# Punti sperimentali con barre d'errore
plt.errorbar(log_T, log_M, yerr=err_log_M, fmt='o', capsize=5, 
             label='Simulation data (Error 1%)', color='navy')

# Linea del fit
x_fit = np.linspace(min(log_T), max(log_T), 100)
plt.plot(x_fit, model_lin(x_fit, *popt), '--', color='crimson', 
         label=f'Fit: slope = {m_fit:.3f} ± {m_err:.3f}')

# Formattazione
plt.xlabel(r'$\log_{10}(L \ [K])$', fontsize=12)
plt.ylabel(r'$\log_{10}(M_J \ [M_{\odot}])$', fontsize=12)
plt.title('Scaling Relation: Jeans Mass vs Box Size Length', fontsize=14)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()

# Stampa i risultati per la relazione
print(f"m : {m_fit:.3f} +/- {m_err:.3f}")
print(f"q : {q_fit:.3f}")

plt.show()