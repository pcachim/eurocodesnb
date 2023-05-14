# EurocodesNB

EurocodesNB is a project that contains a series of Jupyter Notebooks to work with the structural Eurocodes. The Eurocodes are a set of European standards for the design of buildings and other civil engineering works. They provide a common approach to the design of structures and are used throughout Europe.

EurocodesNB has a collection of notebooks for the design of structures according to the Eurocodes. The notebooks cover various topics related to Eurocodes, including structural analysis, steel design, concrete design, timber design, and geotechnical design.

## Installation

To use these notebooks, you will need to have Python installed on your system along with several packages such as NumPy, SciPy, and Matplotlib. To use EurocodesNB, you will also need to have Jupyter Notebook installed on your computer. You can install JupyterLab using pip:

```sh
pip install jupyterlab
```

Once you have Jupyter Notebook installed, you can clone this repository to your local machine by running the following command:

```bsh
git clone https://github.com/pcachim/eurocodesnb.git
```

## Usage

To use EurocodesNB, navigate to the directory where you downloaded the project and start JupyterLab:

```shell
cd eurocodesnb
jupyter lab
```

This should open a new tab in your web browser showing the Jupyter Notebook interface. From here, you can browse the notebooks and run them by clicking on the `.ipynb` files and start working with the Eurocodes.

Alternatively, you can use standalone applications to work with Jupyter Notebooks, such as [Visual Studio Code](https://code.visualstudio.com) or [JupyterLab Desktop](https://github.com/jupyterlab/jupyterlab-desktop).

You can try the notebooks without any installation via [mybinder.org](https://mybinder.org/v2/gh/pcachim/eurocodesnb/HEAD?urlpath==lab) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/pcachim/eurocodesnb/HEAD?urlpath==lab)

## Available notebooks

### Eurocode 1 (EC1)

EC0 (EN 1990) and EC1 (EN 1991) notebooks can be found [here](ec1/ec1-base.ipynb)

### Eurocode 2 (EC2)

EC2 (EN 1992-1-1) notebooks can be found [here](./ec2/ec2-base.ipynb).

EC2 (EN 1992-1-2) notebooks on fire design can be found [here](./ec2/fire/ec2-fire-base.ipynb).

### Eurocode 5 (EC5)

EC5 (EN 1995) notebooks can be found [here](ec5/ec5-base.ipynb).

### Additional tools

There are also some tools to help in some common tasks that can be usefull:

[Read an Excel file](ec-read-from-excel.ipynb)

## Contributing

We welcome contributions from the community! If you find any errors or have suggestions for improving the notebooks, please feel free to open an issue or submit a pull request. If you would like to contribute to EurocodesNB, please fork the project on GitHub and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
