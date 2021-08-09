import subprocess
import os
import sys

# if a project name was passed as a cli argument.
if len(sys.argv) > 1:
    # extract the template to the new project directory
    try:
        subprocess.run(
            ["7z", "x", "react_project_template.7z", "-o./" + sys.argv[1]],
            stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        exit(0)
    except IndexError:
        print("Failed!")
    else:
        print("Successfully created the new project " + sys.argv[1])
else:
    print('Updating...')

# update procedure from here on
# extract the template
try:
    subprocess.run(
        ["7z", "x", "react_project_template.7z", "-o./react_project_template"],
        stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
except OSError:
    print("Couldn't find: react_project_template.7z")
else:
    print("Successfully extracted the react_project_template.7z file")

# get the path
dir_path = os.path.dirname(os.path.realpath(__file__))
extracted_path = dir_path + "/react_project_template/"

# update the template
try:
    # Change Working Directory and update
    subprocess.run(
        ["npm", "update"], cwd=extracted_path)
except OSError:
    print("Couldn't update node packages")
else:
    print("Successfully updated template")

# repackage the template
try:
    subprocess.run(
        ["7z", "u", "react_project_template", "./react_project_template/."],
        stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
except OSError:
    print("Couldn't Overwrite: react_project_template.7z")
else:
    print("Successfully updated react_project_template.7z")

# cleanup
try:
    # delete the intermidiate folder
    subprocess.run(
        ["rm", "-rf", "./react_project_template"])
except OSError:
    print("Couldn't delete intermidiate folder: react_project_template")
else:
    print("Successfully deleted the intermidiate folder")
