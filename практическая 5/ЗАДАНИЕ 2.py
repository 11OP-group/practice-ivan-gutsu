weight,height=map(float, input("Введите вес (кг) и рост (см): ").split())
imt= weight / height * height
print(f"Индекс массы тела: {imt:.1f}")