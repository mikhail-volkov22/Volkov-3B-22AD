class GeometricFigure:
 def __init__(self, area, perimeter):
  self.area = area
  self.perimeter = perimeter

 def info(self):
  print(f"площадь - {self.area}, периметр - {self.perimeter}")
result = GeometricFigure(4, 8)
result.info()