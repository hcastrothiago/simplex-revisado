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
    logs = []

    while True:
        iteracao_log = {
            "iteracao": iteracoes,
            "tableau": tableau.tolist(),
            "variaveis_basicas": [x+1 for x in base],
            "variaveis_nao_basicas": [x+1 for x in non_base]
        }

        # Encontrar variável de entrada
        enter_col = np.argmin(tableau[0, non_base])
        enter_var = non_base[enter_col]
        iteracao_log["variavel_entrada"] = enter_var + 1

        # Condição de ótimo
        if tableau[0, enter_var] >= 0:
            z = -tableau[0, -1]
            x = np.zeros(n)
            for i in range(m):
                if base[i] < n:
                    x[base[i]] = tableau[i+1, -1]

            solucao_otima = {
                "variaveis_basicas": {},
                "variaveis_nao_basicas": {},
                "valor_objetivo": float(Fraction(z).limit_denominator()),
                "numero_iteracoes": iteracoes
            }

            for i, val in enumerate(x, 1):
                if val != 0:
                    solucao_otima["variaveis_basicas"][f"x{i}"] = float(Fraction(val).limit_denominator())

            for var in range(1, n+1):
                if var-1 not in base and x[var-1] == 0:
                    solucao_otima["variaveis_nao_basicas"][f"x{var}"] = 0

            logs.append(iteracao_log)
            return {"solucao": solucao_otima, "logs": logs}

        # Teste da razão mínima
        ratios = []
        for i in range(1, m+1):
            if tableau[i, enter_var] > 0:
                ratio = tableau[i, -1] / tableau[i, enter_var]
                ratios.append((ratio, i))

        if not ratios:
            iteracao_log["erro"] = "Problema Ilimitado"
            logs.append(iteracao_log)
            return {"erro": "Problema Ilimitado", "logs": logs}

        # Pivô
        _, leave_row = min(ratios)
        pivot = tableau[leave_row, enter_var]
        iteracao_log["variavel_saida"] = base[leave_row-1] + 1
        iteracao_log["elemento_pivo"] = float(pivot)

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

        logs.append(iteracao_log)
        iteracoes += 1

    return {"erro": "Máximo de iterações alcançado", "logs": logs}

def main():
    # Exemplo de uso
    c = np.array([2, 3, 4])
    A = np.array([
        [1, 2, -3],
        [-2, 0, 3],
        [1, 1, 0]
    ])
    b = np.array([10, 15, 8])

    resultado = simplex_revisado(c, A, b)
    print(resultado)

if __name__ == "__main__":
    main()
