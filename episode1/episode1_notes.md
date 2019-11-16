# Step 1

    pip3 install virutalenvwrapper

# Step 2

    find the virtualenvwrapper.sh and virtualenv binary paths

        $ find / pattern | grep pattern

# Step 3

    Add the following exports to bash profile

        (using zshell; ~/.bashrc if using bash)

            $ vim ~/.zshrc 
    
    Append the following:

        export WORKON_HOME=/path/to/save/virtualenvs
        export VIRTUALENVWRAPPER_PYTHON=/path/to/python/binary
        export VIRTUALENVWRAPPER_VIRTUALENV=/path/to/virtualenv/binary
        source /path/to/virtualenvwrapper.sh

# Step 4

    Create a new virtual environment

        $ mkvirtualenv nameofvirtualenv

    To start the virtual environment after deactivating

        $ workon nameofvirtualenv
