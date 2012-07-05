from distutils.core import setup

setup(
    name="plop",
    packages=["plop", "plop.test"],
    package_data={
        "plop.test": ["testdata/tornado_tests.pstats"],
        "plop": [
            "templates/index.html",
            "templates/force.html",
            "static/force.js",
            "static/d3.v2.js",
            ],
        }
    )