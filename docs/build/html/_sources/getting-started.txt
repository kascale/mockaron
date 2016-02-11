Getting started
===============

To generate a logo you can write:
::
  from mockaron.generators.logo import LogoGenerator, IconText

  icon_text = IconText(logo_size=(250, 150),
                       icon_size=(100, 100),
                       margin_left=10,
                       margin_right=10,
                       space=10,
                       icon_path='/path/to/the/icon.png',
                       font_path='/path/to/the/font.ttf',
                       text='Mockaron',
                       color=(0, 0, 0, 255),
                       max_font_size=80)

  logo_generator = LogoGenerator()
  logo_generator.set_layout(icon_text)
  # the output image format is inferred by the filename extension
  logo_generator.generate('/path/to/the/logo.png')
