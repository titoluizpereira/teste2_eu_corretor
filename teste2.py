def merge_intervals(intervals):
    
    # Função aninhada que tem objetivo de pegar o início do intervalo
    def inicio_intervalo(intervalo):
        return intervalo[0]

    # Ordena os intervalos baseado em seus pontos de início
    intervals.sort(key=inicio_intervalo)

    resultado = [intervals[0]]

    # Uso do for para percorrer os intervalos e verificar se há sobreposição com o último intervalo adicionado.
    for intervalo_atual in intervals[1:]:
        ultimo_intervalo = resultado[-1]

        # Verifica sobreposição
        if intervalo_atual[0] <= ultimo_intervalo[1]:
            # Atualiza o fim do último intervalo para o máximo entre os dois intervalos
            ultimo_intervalo[1] = max(ultimo_intervalo[1], intervalo_atual[1])
        else:
            # Se não há sobreposição, adiciona o intervalo à lista de resultados
            resultado.append(intervalo_atual)

    return resultado

# Testes
print(merge_intervals([[15,18], [1,3], [2,12], [8,10]]))  # Saída esperada: [[1, 6], [8, 10], [15, 18]]
print(merge_intervals([[1,4], [4,5]]))                  # Saída esperada: [[1, 5]]

