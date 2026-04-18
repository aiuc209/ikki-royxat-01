def hisobla(tezlik, vaqt):
    masofa = []
    for i in range(len(tezlik)):
        masofa.append((tezlik[i] * vaqt[i]) / 60)
    return masofa

tezlik = [50, 60, 70]
vaqt = [30, 45, 60]
print(hisobla(tezlik, vaqt))
