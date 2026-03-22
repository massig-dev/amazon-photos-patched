from setuptools import setup, find_packages

setup(
    name='amazon-photos',
    version='0.0.97.1',
    description='Amazon Photos API (patched for JP account + Python 3.14)',
    packages=find_packages(),
    python_requires='>=3.10',
    install_requires=[
        'aiofiles',
        'httpx[http2]',
        'numpy',
        'orjson',
        'pandas',
        'psutil',
        'tqdm',
    ],
)
