from setuptools import setup, find_packages

REQUIREMENTS = ["django", "python-dateutil", "pyquerystring"]
DEV_REQUIREMENTS = ["tox"]

setup(
    name="django-scrobble_server",
    version="0.1.0",
    description="Django app implementing the server-side Audioscrobbler protocol",
    author="jlieth",
    url="https://github.com/musicbanana/django-scrobble-server",
    license="GPLv3",
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*"]),
    python_requires=">=3.5",
    install_requires=REQUIREMENTS,
    tests_require=DEV_REQUIREMENTS,
    keywords="scrobbling",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Internet :: WWW/HTTP",
    ],
)
