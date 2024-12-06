###
### Name of project: Unitary_Testing.py
###
### Author: CyberCoral
###
### Description of project: It contains a class with
###                         two methods, which can be used
###                         for unit testing in Python.
###
### Date of project: 06 / December / 2024
###
### Current version: 1.0
###

class UnitaryTests:
    '''
    This class contains 
    the procedures to test any 
    block of code, using a
    specific method and 
    test syntax.
    '''
    
    @staticmethod
    def TestingResults(test_str: str, expected_result: type | None) -> tuple[bool | None, str]:
        '''
        It executes the code and, depending of
        the result, returns:
        · True, if test has passed
        (test results are as expected),
        
        · False, if test has failed.
        It returns the error in a specific format
        (for better debugging),
        
        · None, if test_str's execution raises
        an Exception.
        '''
        
        # Result is used globally, so it works with exec(compile())
        global result
        
        # Executes the code and
        # assigns the result to the global variable result,
        # so it can be used later to check
        # if it's the same as expected_result.
        try:
            exec(compile(f"result = ({test_str})", "<string>","exec"),globals())
        except Exception as e:
            # It gave error, but it was expected.
            if expected_result == None:
                
                return True, f"Test ({test_str}) has raised an error ({e}) as expected."
            
            # It gave an unexpected error.
            return None, f"Test ({test_str}) has failed because it has raised an unexpected error ({e})."
    
        # The test was successful, without giving errors.
        if result == expected_result:
            return True, f"Test ({test_str}) has returned the expected result ({expected_result})."
        
        # The test failed, because the result was not the expected one.
        return False, f"Test ({test_str}) has returned an unexpected result ({result}) instead of the expected result ({expected_result})."

    
    @staticmethod
    def TestingMethod(tests: list, *, print_: bool = True) -> dict[str: bool | None]:
        '''
        It generalizes unit testing
        by creating a template for
        making them, so it's
        easier to do.
        
        The tests must have this format:
        (test_in_str, expected_value)
        
        · The test unit must be a 
        tuple with 2 elements.
        
        · The test itself (test_in_str)
        must be a str object 
        that represents
        what you want to test.
        
        · The expected result (expected_result)
        must be the result you expect from
        the execution of the test.
        
        · Example: 
            ("1 + 1", 2)
            The test should return True,
            because 1 + 1, as stated, is 2.
        '''
        
        # Check to print_, so it's a bool value.
        if not isinstance(print_, bool):
            raise TypeError("The variable print_ must be a boolean value.")
        
        # Check to tests type, tests' elements' type,
        # their structure (tuple with two elements) 
        # and the type of the first element.
        if not isinstance(tests, list):
            raise TypeError("The variable tests must be a list with tuples of two elements each.")
        elif [isinstance(tests[i], tuple) for i in range(len(tests))].count(False) != 0:
            raise TypeError("Tests' elements must be tuples.")
        elif [len(tests[i]) == 2 for i in range(len(tests))].count(False) != 0:
            raise IndexError("Tests' elements must be tuples and have two elements each: the first one must be a string.")
        elif [isinstance(tests[i][0], str) for i in range(len(tests))].count(False) != 0:
            raise TypeError("The first element of any of tests' tuples must be a string.")
        
        # Check if result variable is in globals,
        # so it does not get manipulated in the program.
        if "result" in globals():
            raise Warning("The variable result, which is in globals(), will be redefined and deleted.")

        # The test results
        test_results: dict = {}
        
        # Automatized test check
        for test, i in zip(tests, range(1,len(tests)+1)):
            test_res = UnitaryTests.TestingResults(test[0], test[1])
            # Remove previous result so the variable can be used again freely.
            try:
                globals().pop("result")
            except Exception:
                pass
            
            # Prints the result.
            if print_ == True:
                print("Test"+str(i)+": ", test_res[1],"\n")
                
            # Appends the result as a {key: value} to the final dictionary.
            test_results.update({test[0]: test_res[0]})
            
        return test_results
    
if __name__ == "__main__":
    print("""This program alone does not do testing,
          \nbut it offers great tools to do so (UnitaryTests.TestingMethod() and UnitaryTests.TestingResults()).
          \nUse the class UnitaryTests and its methods.
          \nThanks for checking the code out, have a nice day :D""")