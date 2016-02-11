import os
from PIL import Image, ImageDraw
import tempfile
import unittest

try:
  import mockaron
except ImportError:
  import sys
  sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
  import mockaron

from mockaron.generators.logo import IconText, LogoGenerator

class LogoGeneratorTestCase(unittest.TestCase):
  def get_icon_text_params(self):
    tests_dir = os.path.dirname(os.path.abspath(__file__))
    icon_path = os.path.join(tests_dir, 'icon.png')
    font_path = os.path.join(tests_dir, 'Ubuntu-R.ttf')
    params = {'logo_size': (250, 150), 'icon_size': (100, 100),
              'margin_left': 10, 'margin_right': 10, 'space': 10,
              'icon_path': icon_path, 'font_path': font_path,
              'text': "Mockaron", 'color': None, 'max_font_size': 80}
    return params

  def get_icon_text(self, params=None):
    if params is None:
      params = self.get_icon_text_params()
    icon_text = IconText(params['logo_size'], params['icon_size'],
                         params['margin_left'], params['margin_right'],
                         params['space'], params['icon_path'],
                         params['font_path'], params['text'], params['color'],
                         params['max_font_size'])
    return icon_text

  def test_icon_text_layout_constructor(self):
    params = self.get_icon_text_params()
    icon_text = self.get_icon_text(params)
    self.assertEqual(params['logo_size'], icon_text.logo_size)
    self.assertEqual(params['icon_size'], icon_text.icon_size)
    self.assertEqual(params['margin_left'], icon_text.margin_left)
    self.assertEqual(params['margin_right'], icon_text.margin_right)
    self.assertEqual(params['space'], icon_text.space)
    self.assertEqual(params['icon_path'], icon_text.icon_path)
    self.assertEqual(params['font_path'], icon_text.font_path)
    self.assertEqual(params['text'], icon_text.text)
    self.assertEqual(params['color'], icon_text.color)
    self.assertEqual(params['max_font_size'], icon_text.max_font_size)

  def test_icon_text_get_icon(self):
    icon_text = self.get_icon_text()
    icon = icon_text.get_icon(icon_text.icon_path)
    icon.close()

  def test_icon_text_select_font_size(self):
    icon_text = self.get_icon_text()
    im = Image.new("RGBA", (100, 100))
    draw = ImageDraw.Draw(im)
    font_path = icon_text.font_path
    text = icon_text.text
    max_text_width = 100
    max_font_size = 100
    font, width, height = icon_text.select_font_size(draw, font_path, text,
                                                     max_text_width,
                                                     max_font_size)

    self.assertTrue(0 < width and width <= max_text_width)
    self.assertTrue(0 < height and height <= 100)

  def test_logo_generator_icon_text(self):
    icon_text = self.get_icon_text()
    with tempfile.TemporaryDirectory() as tmp_dir:
      tmp_file = os.path.join(tmp_dir, 'logo.png')
      logo_generator = LogoGenerator()
      logo_generator.set_layout(icon_text)
      logo = logo_generator.generate(tmp_file)
      self.assertTrue(0 < os.path.getsize(tmp_file))

if __name__ == '__main__':
  unittest.main()
