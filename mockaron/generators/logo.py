from PIL import Image, ImageDraw, ImageFont

from mockaron.generators import Generator

class LogoLayout:
  pass

class IconText(LogoLayout):
  def __init__(self, logo_size=(250, 150), icon_size=(100, 100),
               margin_left=10, margin_right=10, space=10,
               icon_path=None, font_path=None, text=None, color=None,
               max_font_size=80):
    self.logo_size = logo_size
    self.icon_size = icon_size
    self.margin_left = margin_left
    self.margin_right = margin_right
    self.space = space
    self.icon_path = icon_path
    self.font_path = font_path
    self.text = text
    self.color = color
    self.max_font_size = max_font_size

  def set_layout(self, layout):
    self.layout = layout

  def get_layout(self):
    return self.layout

  def get_icon(self, icon_path):
    icon = Image.open(icon_path)
    return icon

  def get_icon_position(self):
    left = self.margin_left
    top = (self.logo_size[1] - self.icon_size[1]) // 2
    icon_pos = (left, top)
    return icon_pos

  def paste_icon(self, img, icon, icon_pos):
    img.paste(icon, icon_pos, icon)

  def get_max_text_width(self):
    diff = self.icon_size[0]
    diff += self.margin_left + self.margin_right
    diff += self.space
    max_text_width = self.logo_size[0] - diff
    return max_text_width

  def select_font_size(self, draw, font_path, text, max_text_width,
                       max_font_size=80):
    font = None
    font_size = max_font_size + 1
    width = max_text_width + 1
    height = 0
    while width > max_text_width:
      font_size -= 1
      font = ImageFont.truetype(font_path, font_size)
      width, height = draw.textsize(text, font=font)
    return (font, width, height)

  def get_text_position(self, height):
    left = self.margin_left + self.icon_size[0] + self.space
    top = (self.logo_size[1] - height) // 2
    text_pos = (left, top)
    return text_pos

  def draw_text(self, draw, text, text_pos, font, color):
    draw.text(text_pos, text, font=font, fill=color)

  def generate(self):
    logo_size = self.logo_size
    im = Image.new("RGBA", logo_size)

    icon = self.get_icon(self.icon_path)
    icon_pos = self.get_icon_position()
    self.paste_icon(im, icon, icon_pos)

    draw = ImageDraw.Draw(im)
    max_text_width = self.get_max_text_width()
    font, width, height = self.select_font_size(draw, self.font_path, self.text,
                                                max_text_width,
                                                self.max_font_size)

    text_pos = self.get_text_position(height)
    self.draw_text(draw, self.text, text_pos, font, self.color)

    return im

class LogoGenerator(Generator):
  def __init__(self):
    pass

  def set_layout(self, layout):
    self.layout = layout

  def get_layout(self):
    return self.layout

  def generate(self, logo_path):
    im = self.layout.generate()
    im.save(logo_path)
    return im
