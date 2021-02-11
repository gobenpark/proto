import setuptools

setuptools.setup(
    name="benproto",
    version="1.0.0",
    license='BSD 3-Clause License',
    author="benproto",
    author_email="qjadn0914@naver.com",
    description="for stock use grpc proto",
    long_description=open('README.md').read(),
    url="github url 등",
    packages=setuptools.find_packages(),
    classifiers=[
        "stock",
        "grpc",
        "private"
    ],
)