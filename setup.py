from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()
    
setup(
    name = "flet_route",
    version = "0.3.3",
    author="Saurabh Wadekar [ INDIA ]",
    packages=["flet_route","cli"],
    license="MIT",
    maintainer="Saurabh Wadekar",
    maintainer_email="saurabhwadekar420@gmail.com",
    keywords=["flet","routing","flet_route","routes","flet app","flet-route","flet simple routing"],
    description="This makes it easy to manage multiple views with dynamic routing.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/saurabhwadekar/flet_route",
    include_package_data=True,
    install_requires=[
        'click==8.1.3',
        "repath",
    ],
    entry_points= {
        'console_scripts': 
        ['flet-route=cli:make_app']
    }, 
)
