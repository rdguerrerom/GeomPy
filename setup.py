from distutils.core import setup
setup(
  name = 'geompy',
  packages = ['geompy'],
  version = '0.1',
  description = 'A super cool differential geometry library',
  author = 'Alex Karacaoglu',
  author_email = 'karacaog@bc.edu',
  url = 'https://github.com/AlexKaracaoglu/geompy', 
  download_url = 'https://github.com/AlexKaracaoglu/geompy/archive/0.1.tar.gz',
  keywords = ['mathematics', 'geometry'],
  classifiers = [],
  install_requires=['numpy','sympy'],
)
