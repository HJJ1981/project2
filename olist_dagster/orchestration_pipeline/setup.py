from setuptools import find_packages, setup

setup(
    name="orchestration_pipeline",
    packages=find_packages(exclude=["orchestration_pipeline_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
