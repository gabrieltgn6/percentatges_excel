import pandas as pd

# Ruta del archivo original
ruta_csv = "CotesAltimetriquespunts.csv"

# Carga el archivo CSV
df = pd.read_csv(ruta_csv)

# Divide los datos: 60% aleatorio y 40% restante
df_60 = df.sample(frac=0.6, random_state=42)  # 60% de las filas
df_40 = df.drop(df_60.index)  # El resto (40%)

# Guarda ambos subconjuntos en archivos separados
df_60.to_csv("valores_60_por_ciento.csv", index=False)
df_40.to_csv("valores_40_por_ciento.csv", index=False)

# Mensaje de confirmación
print(f"60% guardado en 'valores_60_por_ciento.csv' con {len(df_60)} filas.")
print(f"40% guardado en 'valores_40_por_ciento.csv' con {len(df_40)} filas.")
