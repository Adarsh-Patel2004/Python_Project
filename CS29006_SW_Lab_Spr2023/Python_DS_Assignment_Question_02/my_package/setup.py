from setuptools import setup

setup(
   name='my_package',
   version='1.0',
   description='A useful module',
   author='Man Foo',
   author_email='foomail@foo.example',
   packages=['my_package'],  #same as name
   install_requires=['wheel', 'bar', 'greek'], #external packages as dependencies
   scripts=[
            'scripts/cool',
            'scripts/skype',
           ]
)
