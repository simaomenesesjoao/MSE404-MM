##############################################################################################################################################
##############################################################################################################################################
##############################################################################################################################################
#                           This is a python file that will generate multiple input files for a convergence test.                            #
#                                                                                                                                            #
#   How to use: Copy and paste the text from your input file to common_content_template as shown below. Include converged value of ecutwfc.  #
#                               Change the kpoints section to: K_POINTS automatic and on the next line: {} {} {} 0 0 0                       #
#                               Make sure you are putting a space both sides of = sign when pasting.                                         #
#                                                                                                                                            #
#                                                   How to run: python3 kpt_build.py                                                         #
##############################################################################################################################################
##############################################################################################################################################
##############################################################################################################################################


# Directory where you want to create the files
output_directory = "./"

# Number of files to create
num_files = 15

# Common content template with a placeholder for the number
common_content_template = """
 &CONTROL
    pseudo_dir = '.'
    disk_io = 'none'
 /

 &SYSTEM
    ibrav = 2
    A = 3.567
    nat = 2
    ntyp = 1
    ecutwfc = 20.0
 /

 &ELECTRONS
    conv_thr = 1.0E-6
 /

ATOMIC_SPECIES
 C  12.011  C.pz-vbc.UPF

ATOMIC_POSITIONS crystal
 C 0.00 0.00 0.00
 C 0.25 0.25 0.25

K_POINTS automatic
  {} {} {} 0 0 0 
"""

# Loop to create the files
for i in range(1, num_files + 1):
    # Define the content for each file with the number replaced
    calc = round(0+2*i)
    content = common_content_template.format(calc, calc, calc)

    # Generate the file name
    file_name = f"{output_directory}/scf.kpt.{str(i).zfill(3)}.in"

    # Open and write to the file directly
    with open(file_name, 'w') as file:
        file.write(content)
