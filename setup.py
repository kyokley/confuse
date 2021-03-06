from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='confuse',
      version='0.1.1',
      description='Convert ascii strings to commonly confused unicode characters',
      long_description=readme(),
      url='http://github.com/kyokley/confuse',
      author='Kevin Yokley',
      author_email='kyokley2@gmail.com',
      license='MIT',
      packages=['confuse'],
      install_requires=['polib'],
      test_suite='nose.collector',
      tests_require=['nose',
                     'mock',],
      entry_points={
          "console_scripts": [
              "confuse = confuse.main:main",
          ],
      },
      zip_safe=False)
