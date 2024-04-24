"""

    Scott Quashen
    London App Brewery
    100 Days of Python Code: Day 1
    April 23 2024

    ------
    Description: This program generates a band name based on user input
    ------
    
    ------
    Inputs: Request user's hometown, and first pets name
    ------
    
    ------
    Outputs: Outputs result into the console
    ------
    
    ------
    Dependencies: None.
    ------

    ------
    Assumptions: Developed and tested using Spyder 5.15.7, Python version 3.11.5 on macOS 14.4.1
    ------
    
"""

def main():
    """
    
    Description:    Creates band name
    ----------  
    Input:          Request hometown and pet name in console
    ----------                    
    Outputs:        Band name to console
    -------
        
    """
    home_town = input( 'What is your hometown?\n' )
    pet_name = input( 'what is your best pet\'s name?\n' )
    print( 'Your band name is:', home_town, pet_name )
    
# run main
if __name__ == '__main__':
    main()
    