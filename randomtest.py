import pandas as pd
import random

# Les données complètes avec la liste pour l'Âge et le Salaire
donnees = {
    'Âge':[random.randint(1,24) for i in range(1,6)],
    'Salaire': [45000, 52000, 58000, 65000, 120000]
}

print(f"raw data\n {donnees}")

df = pd.DataFrame(donnees)
print(df)

print(df.describe())

