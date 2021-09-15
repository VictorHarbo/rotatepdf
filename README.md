# rotatepdf
This is a python script to rotate pdf files. It is run through the command line and can process multiple files that has to be rotated the same way. The script supports single file use and batch processing.

## Setup:
To run this script you have to make sure you have the requirements installed. These modules can be installed from the requirements.txt file by running:
    
    pip install -r requirements.txt
    
## Use:
### Single file:
To rotate a single .pdf-files with this script run the following line in the command line:
    
    python rotatepdf.py path/to/inputfile.pdf path/to/outputfile.pdf
        
Next you input how many degrees clockwise you want your file to be rotated.
### Batch processing:
To run the script on multiple files at once you run the following line in the command line:
    
    python rotatepdf.py -b input output

Now the script asks you what folder the files are located in. Here you enter the input directory and press enter.

## Help
It is possible to access some further information about the script, when calling it from the commandline. This can be done like this:
    
    python rotatepdf.py -h

## Planned features:
Right now the way to input batch files is not perfect. Idealy I would like to make the second input superfluous, by integrating the INPUT argument into the batch part of the script. 
