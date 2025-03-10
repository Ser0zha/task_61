class GeometryFileLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        objects = []
        try:
            with open(self.file_path, 'r') as file:
                for line in file:
                    line = line.strip()
                    if not line or ":" not in line:
                        continue

                    parts = line.split(":")
                    if len(parts) != 2:
                        print(f"Неверный формат строки: {line}")
                        continue

                    shape_type, values = parts
                    values = values.strip()

                    try:
                        if shape_type == "point":
                            x, y = map(float, values.split(","))
                            objects.append((shape_type, x, y))
                        elif shape_type == "line":
                            x1, y1, x2, y2 = map(float, values.split(","))
                            objects.append((shape_type, x1, y1, x2, y2))
                        elif shape_type == "circle":
                            x, y, radius = map(float, values.split(","))
                            objects.append((shape_type, x, y, radius))
                        else:
                            print(f"Неизвестный тип объекта: {shape_type}")
                    except ValueError:
                        print(f"Неверный формат данных: {values}")
                        continue
        except FileNotFoundError:
            print(f"Файл {self.file_path} не найден.")

        return objects
