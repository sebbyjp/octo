from setuptools import find_packages, setup

setup(
    name="octo",
    version="0.0.1",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
      "jax==0.4.23",
      "jaxlib==0.4.23",
      "opencv-python==4.9.0.80",
      "flax==0.7.5",
      "distrax==0.1.5",
      "einops==0.7.0",
      "huggingface-hub==0.20.2",
      "transformers==4.36.2",
      "git+https://github.com/google/array_record.git@2ac1d904f6be31e5aa2f09549774af65d84bff5a",
      "git+https://github.com/kvablack/dlimp@d08da3852c149548aaa8551186d619d87375df08",
    ],
)
