
# Recebe um array e um elemento para buscar dentro do array
def linear_search(arr, target):
    # Percorre todos os elementos dentro do array
    for i in range(len(arr)):
        # Assim que ele encontrar deve retornar a posição do elemento
        if arr[i] == target:
            return i

# O(n)