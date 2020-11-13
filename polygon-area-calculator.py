class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
  
  def set_width(self, width):
    self.width = width
    

  def set_height(self, height):
    self.height = height
   

  def get_area(self):
    return self.width * self.height
  
  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_picture(self, rectangle):
    if self.width or self.height > 50:
      return "Too big for picture."
    else:
      width = "*" * self.width
      picture = (width + "\n") * self.height

    return picture

  def get_amount_inside():
    pass




class Square(Rectangle):
  def __init__(self, length):
    super().__init__(length,length)

  def set_side(self, length):
    self.width = length
    self.height = length

  def set_width(self, length):
    self.set_side(length)
    
  def set_height(self, length):
    self.setside(length)

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())