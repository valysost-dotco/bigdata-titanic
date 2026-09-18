"""
Punto de entrada del proyecto.

Ejecuta el pipeline completo:
    1. Carga de datos crudos (data/train.csv)
    2. Análisis exploratorio de datos (EDA)
    3. Preprocesamiento y limpieza
    4. Guardado del dataset procesado (data/train_procesado.csv)

Uso:
    python main.py
"""

from src.data_loader import cargar_datos
from src.eda import ejecutar_eda
from src.preprocessing import preprocesar, guardar_procesado


def main() -> None:
    print("1) Cargando datos...")
    df = cargar_datos()
    print(f"   -> {df.shape[0]} filas, {df.shape[1]} columnas\n")

    print("2) Ejecutando análisis exploratorio (EDA)...")
    ejecutar_eda(df)

    print("\n3) Preprocesando datos...")
    df_procesado = preprocesar(df)
    print(f"   -> Dataset procesado: {df_procesado.shape[0]} filas, "
          f"{df_procesado.shape[1]} columnas")
    print("\n   Primeras filas del dataset procesado:")
    print(df_procesado.head())

    print("\n4) Guardando dataset procesado...")
    out_path = guardar_procesado(df_procesado)
    print(f"   -> Guardado en: {out_path}")

    print("\n✅ Pipeline ejecutado correctamente. Proyecto reproducible.")


if __name__ == "__main__":
    main()
