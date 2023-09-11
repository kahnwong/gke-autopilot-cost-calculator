from setuptools import find_packages
from setuptools import setup

if __name__ == "__main__":
    setup(
        name="gke_autopilot_cost_calculator",
        version="0.1",
        description="",
        long_description=open("README.md").read(),
        long_description_content_type="text/markdown",
        url="https://github.com/kahnwong/gke-autopilot-cost-calculator",
        author="Karn Wong",
        author_email="karn@karnwong.me",
        license="MIT",
        project_urls={
            "Documentation": "https://github.com/kahnwong/gke-autopilot-cost-calculator",
            "Source": "https://github.com/kahnwong/gke-autopilot-cost-calculator",
        },
        packages=find_packages(exclude=["tests"]),
        install_requires=[],
        python_requires=">=3.11",
    )
