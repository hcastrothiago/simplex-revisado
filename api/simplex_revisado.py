import numpy as np
from fractions import Fraction

def simplex_revisado(c, A, b):
    m, n = A.shape
    tableau = np.zeros((m+1, n+m+1))
    tableau[1:m+1, :n] = A
    tableau[1:m+1, n+m] = b
    tableau[0, :n] = -c
    
    base = list(range(n, n+m))
    non_base = list(range(n))
    
    iteracoes = 0
    while True:
        print(f"\n--- Iteração {iteracoes} ---")
        print("Tableau atual:")
        print(tableau)
        
        print("\nVariáveis Básicas:", [x+1 for x in base])
        print("Variáveis Não-Básicas:", [x+1 for x in non_base])
        
        # Encontrar variável de entrada
        enter_col = np.argmin(tableau[0, non_base])
        enter_var = non_base[enter_col]
        print(f"\nVariável que entra na base: x{enter_var+1}")
        
        # Condição de ótimo
        if tableau[0, enter_var] >= 0:
            z = -tableau[0, -1]
            x = np.zeros(n)
            for i in range(m):
                if base[i] < n:
                    x[base[i]] = tableau[i+1, -1]
            
            print("\nSolução Ótima:")
            print("Variáveis Básicas:")
            for i, val in enumerate(x, 1):
                if val != 0:
                    # Converte para fração se não for inteiro
                    frac_val = Fraction(val).limit_denominator()
                    if frac_val.denominator != 1:
                        print(f"x{i} = {frac_val}")
                    else:
                        print(f"x{i} = {int(val)}")
            
            print("\nVariáveis Não Básicas:")
            non_basic_vars = [i for i in range(1, n+1) if i-1 not in base and x[i-1] == 0]
            for var in non_basic_vars:
                print(f"x{var} = 0")
            
            # Converte valor objetivo para fração se não for inteiro
            frac_z = Fraction(z).limit_denominator()
            if frac_z.denominator != 1:
                print(f"\nValor Objetivo: {frac_z}")
            else:
                print(f"\nValor Objetivo: {int(z)}")
            
            print(f"Número de Iterações: {iteracoes}")
            return x, z
        
        # Teste da razão mínima
        ratios = []
        for i in range(1, m+1):
            if tableau[i, enter_var] > 0:
                ratio = tableau[i, -1] / tableau[i, enter_var]
                ratios.append((ratio, i))
        
        if not ratios:
            print("Problema Ilimitado")
            return None
        
        # Pivô
        _, leave_row = min(ratios)
        pivot = tableau[leave_row, enter_var]
        print(f"Variável que sai da base: x{base[leave_row-1]+1}")
        print(f"Elemento pivô: {pivot}")
        
        # Atualizar tableau
        tableau[leave_row] /= pivot
        
        for i in range(m+1):
            if i != leave_row:
                fator = tableau[i, enter_var]
                tableau[i] -= fator * tableau[leave_row]
        
        # Atualizar variáveis básicas e não básicas
        base[leave_row-1] = enter_var
        non_base.remove(enter_var)
        non_base.append(base[leave_row-1])
        
        iteracoes += 1
    
    print("Máximo de iterações alcançado")
    return None


def main():
    # Coeficientes da função objetivo
    c = np.array([2, 3, 4])
    
    # Matriz de restrições
    A = np.array([
        [1, 2, -3],
        [-2, 0, 3],
        [1, 1, 0]
    ])
    
    # Lado direito das restrições
    b = np.array([10, 15, 8])
    
    # Resolver
    simplex_revisado(c, A, b)

if __name__ == "__main__":
    main()