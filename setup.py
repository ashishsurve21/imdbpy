from setuptools import setup

setup(name='imdbpy',
      version='0.1',
      description='python wrapper for imdb',
      url='https://github.com/ashishsurve21/imdbpy',
      author='pacifier',
      author_email='ashish.surve21@gmail.com',
      license='MIT',
      packages=['imdbpy'],
      install_requires=[
          'json', 'urllib2'
      ],
      zip_safe=False)
