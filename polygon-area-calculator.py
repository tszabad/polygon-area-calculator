class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
  
  def set_width(self, width):
    self.width = width
    return True

  def set_height(self, height):
    self.height = height
    return True

  def get_area(self):
    return self.width * self.height
  
  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_picture(self):
    if self.width or self.height > 50:
      return "Too big for picture."

  def get_amount_inside():
    pass




class Square(Rectangle):
  def __init__(self, width, height):
      super().__init__(width, height)