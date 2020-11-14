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

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** 0.5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    else:
      width = "*" * self.width
      picture = (width + "\n") * self.height
      return picture

  def get_amount_inside(self, rectangle):
    if rectangle.width > self.width or rectangle.height > self.height:
      return 0
    else:
      times_height = int(self.width / rectangle.width)
      times_width = int(self.height / rectangle.height)
      return times_height * times_width
    


  def __repr__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

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
  
  def __repr__(self):
    return f"Square(side={self.width})"
      




rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())