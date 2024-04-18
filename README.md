# Export Part Views as DXF

This project contains a Python script that exports the face of a part to a DXF file using Alibre's API.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 2.7
- Alibre Design software

### Installing

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/ExportPartViewsAsDXF.git
```

Navigate to the cloned repository:

```bash
cd ExportPartViewsAsDXF
```

### Usage

Run the script with Python:

```bash
python "Export Part Views as DXF.py"
```

## Functionality

The script retrieves the installation path of Alibre Design from the Windows registry and adds a reference to the AlibreX.dll file, which allows access to Alibre's API.

The main function, `ExportFaceDXF`, exports the face of a part to a DXF file. It checks if the part face is selected and if the output file path is set. If these conditions are met, the face of the part is exported to a DXF file at the specified path.

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Contact

Your Name - YourEmail@example.com
```

Please replace the placeholders (like `yourusername`, `Your Name`, `YourEmail@example.com`) with your actual information. Also, you might want to create a `CONTRIBUTING.md` and `LICENSE.md` file if you don't have them yet.
