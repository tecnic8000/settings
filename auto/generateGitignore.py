
def create_gitignore():
    # Define the content for the .gitignore file
    content = ".DS_Store\nThumbs.db\nehthumbs.db\nDesktop.ini\n"
    
    # Open the .gitignore file in write mode
    with open(".gitignore", "w") as file:
        file.write(content)
    
    print(".gitignore file created")

# Run the function to create the .gitignore file
create_gitignore()