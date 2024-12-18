###
### Name of project: PyTesting.py
###
### Author: CyberCoral
###
### Description of project: It contains two custom exceptions,
###                         for debugging purposes; and a class 
###                         with four methods, which can be used
###                         for unit testing in Python.
###
### Date of project: 18 / December / 2024
###
### Current version: 2.3
###

class TestFailureError(Exception):
    '''
    Error raised when tests' success rate
    has been lower than the 
    established threshold.
    '''
    
    def __init__(self, tests, success_rate, threshold):
        self.tests = tests
        self.success_rate = success_rate
        self.threshold = threshold
        
    def __str__(self):
        return str(f"The tests\n({self.tests})\nhave reached the success rate of {self.success_rate:%}, but they have not achieved the threshold of {self.threshold:%}.")

class CannotBeHashedError(Exception):
    '''
    Error raised when an object cannot be hashed
    properly.
    '''
    
    def __init__(self, obj, type_obj):
        self.obj = obj
        self.type_obj = type_obj
        
    def __str__(self):
        return str(f"The object ({self.obj}) of type ({self.type_obj}) cannot be hashed.")

class UnitaryTests:
    '''
    This class contains 
    the procedures to test any 
    block of code, using a
    specific method and 
    test syntax.
    '''
    
    @staticmethod
    def TestingResults(test_str: str, expected_result: type | None, scope: dict = globals()) -> tuple[bool | None, str]:
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
        
        The scope is a dictionary that
        contains the variables,
        functions or everything that
        the method can use while 
        executing the tests.

        By default
        the scope is globals().
        '''
        
        # Executes the code and
        # assigns the result to the global variable result,
        # so it can be used later to check
        # if it's the same as expected_result.
        
        try:
            result = scope["result"]
        except KeyError:
            raise KeyError("The result variable cannot be found in the given scope.\nCheck again if 'result' is defined on the scope you used.")
        
        
        try:
            exec(compile(f"result = ({test_str})", "<string>","exec"),scope)
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
    def TestingMethod(tests: list, *, print_: bool = True, scope: dict = globals()) -> dict[tuple[str, type]: bool | None]:
        '''
        It generalizes unit testing
        by creating a template for
        making them, so it's
        easier to do.
        
        The scope is a dictionary that
        contains the variables,
        functions or everything that
        the method can use while 
        executing the tests. 
        By default
        the scope is globals().
        
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
        
        # Check the scope variable.
        if not isinstance(scope, dict):
            raise TypeError("The scope must be a dictionary.")
        elif len(list(scope.keys())) == 0:
            raise IndexError("The scope must have at least one entry.")
    
        # The test results
        test_results: dict = {}
        
        # Automatized test check
        for test, i in zip(tests, range(1,len(tests)+1)):
            
            scope.update({"result":0})
                        
            test_res = UnitaryTests.TestingResults(test[0], test[1], scope = scope)
            
            # Remove previous result so the variable can be used again freely.
            try:
                scope.pop("result")
            except Exception:
                pass
            
            # Reformats test so, in case of not being able to be 
            # hashed of their components, try to convert to tuple
            # by recreating the test and check if it can hash.
            
            # If that is possible, dummy_var is popped from locals()
            # and the loop breaks.
            
            # If that is not possible, raise custom error.
            while True:
                try:
                    dummy_var = {(test[0], test[1]) : 0}
                    locals().pop("dummy_var")
                    break
                except TypeError:
                    
                    if isinstance(test[0], list) and not isinstance(test[0], tuple):
                        if print_:
                            print(f"test[0] ({test[0]}) is going to be converted into a tuple.")
    
                        test = (tuple(test[0]), test[1])

                        if print_:
                            print(f"test[0] ({test[0]}) is now a tuple.")
                            
                    elif isinstance(test[1], list) and not isinstance(test[1], tuple):
                        if print_:
                            print(f"test[1] ({test[1]}) is going to be converted into a tuple.")
                        
                        test = (test[0], tuple(test[1]))

                        
                        if print_:
                            print(f"test[1] ({test[1]}) is now a tuple.")
                        
                    else:
                        raise CannotBeHashedError(test, [type(i) for i in test])
                        
            
            # Prints the result.
            if print_ == True:
                print("Test"+str(i)+": ", test_res[1],"\n")
                
            # Appends the result as a {key: value} to the final dictionary.
            test_results.update({(test[0], test[1]): test_res[0]})
            
        return test_results
    
    @staticmethod
    def TestingAnalysis(test_results: dict, mode: str = "simple", *, print_: bool = True, threshold: float = 0.80) -> dict:
        '''
        It analizes the test_results 
        and it returns data according
        to the results' values.
        
        It has 3 modes:
        · "simple": It only returns
        the number of True, False
        or None result values.
        
        · "detailed": It returns simple's
        results, but also with their ratio 
        proportional to the total. The program
        will also return a list with the tests,
        sorting based on the resulting values..
        
        ·"strict": It returns detailed's
        results and forces a (default)
        minimum 80 percent success rate 
        that the tests must achieve to pass.
        
        · Example: 
            {"1 + 1" : True}
            There is 1 True value (simple),
            100% percent of the tests checked True (detailed),
            the test has achieved more than the 80 percent
            success rate (100%), it has passed (strict).
        '''
        
        # Check to print_, so it's a bool value.
        if not isinstance(print_, bool):
            raise TypeError("The variable print_ must be a boolean value.")
        
        # The modes of the analysis program.
        modes = ["simple", "detailed", "strict"]
        
        # The test_results's items.
        test_items = list(test_results.items())
        
        # Variable checks.
        if not isinstance(mode, str):
            raise TypeError("The mode must be a string value, it represents the function's mode.")
        elif mode not in modes:
            raise ValueError("The introduced mode is not a valid mode..")
          
            
        if not isinstance(test_results, dict):
            raise TypeError("The test_results variable must be a dictionary,\neach item must have a str key and a value (True, False or None).")
        elif len(list(test_results.values())) == 0:
            raise IndexError("There are no entries in test_results. It is not possible to analyse an empty test_results dict properly.")
        
        elif [isinstance(test_items[i][0], tuple) for i in range(len(test_items))].count(False) != 0:
            raise TypeError("Each of the test_results items' key must be a tuple with two values.")
        elif [len(test_items[i][0]) == 2 for i in range(len(test_items))].count(False) != 0:
            raise IndexError("There must be only two elements per tuple.")
        elif [isinstance(test_items[i][0][0], str) for i in range(len(test_items))].count(False) != 0:
            raise TypeError("Each of the tuple's first element must be a string value.")
        
        elif [test_items[i][1] in [True, False, None] for i in range(len(test_items))].count(False) != 0:
            raise TypeError("Each of the test_results items' value must be either True, False or None.")
        
        
        if not isinstance(threshold, float):
            raise TypeError("The threshold must be a float value, which must be greater or equal than 0 but less or equal than 1.")
        elif threshold < 0 or threshold > 1:
            raise ValueError("The threshold value must be between 0 (inclusive) and 1 (inclusive)")
            
        # The simple analysis function.
        def SimpleAnalysis(test_items: list, mode: str, *, print_: bool = False):
            '''
            Does simple analysis,
            returns the number of True,
            False and None values in test_items.
            
            Used in "simple",
            "detailed" and "strict".
            '''
            
            test_vals = [i[1] for i in test_items]
            
            # The variables that store the values.
            true_vals = test_vals.count(True)
            false_vals = test_vals.count(False)
            none_vals = test_vals.count(None)
            
            # It prints information if print_ is True and mode is "simple".
            if print_ and mode == "simple":
                print(f"""
                      Simple analysis:
                         \n· Number of True values: ({true_vals}).
                         \n· Number of False values: ({false_vals}).
                         \n· Number of None values: ({none_vals}).
                         
                      \nEnd of Simple Analysis.\n
                      """)
            
            # It returns True, False and None values from test_items.
            return [true_vals, false_vals, none_vals]
        
        simple_results = SimpleAnalysis(test_items, mode, print_ = print_)
        
        # Returns results from SimpleAnalysis()
        if mode == "simple":
            return simple_results
        
        def DetailedAnalysis(test_items: list, simple_results: list, mode: str, *, print_: bool = False):
            '''
            Does detailed analysis,
            returns the ratios of the 
            True, False and None values
            proportional to the total number
            of values.
            
            It also sorts tests
            based on their values.
            
            Used in "detailed" and "strict".
            '''
            
            test_vals = simple_results
            total_tests = sum(simple_results)
            
            # These two variable store the proportions, and the tests sorted by value.
            proportions = [simple_results[i] / total_tests for i in range(len(simple_results))]
        
            sorted_tests = \
                [
                [test_items[i][0] for i in range(len(test_items)) if test_items[i][1] == True],
                [test_items[i][0] for i in range(len(test_items)) if test_items[i][1] == False],
                [test_items[i][0] for i in range(len(test_items)) if test_items[i][1] == None]
                ]
            
            # It prints information if print_ is True and mode is "detailed".
            if print_ and mode == "detailed":
                print(f"""
                      Detailed analysis:
                      \n· Number of True values: {test_vals[0]}\nPercentage of True values: {proportions[0]:%}\n
                      \n· Number of False values: {test_vals[1]}\nPercentage of False values: {proportions[1]:%}\n
                      \n· Number of None values: {test_vals[2]}\nPercentage of None values: {proportions[2]:%}\n
                      
                      \nEnd of Detailed Analysis.\n
                      """)
                      
            return proportions, sorted_tests
        
        detailed_results, sorted_tests = DetailedAnalysis(test_items, simple_results, mode, print_= print_)
                
        # Returns results from DetailedAnalysis()
        if mode == "detailed":
            return {k:(v,w) for k, v, w in zip([True, False, None], simple_results, detailed_results)}, sorted_tests
        
        def StrictAnalysis(test_items: list, simple_results: list, detailed_results: list, threshold: float, mode: str, *, print_: bool = False):
            '''
            Does strict analysis,
            returns the same results
            as UnitaryTests.DetailedAnalysis().
            
            It raises a TestFailureError when 
            the ratio of True tests does not
            achieve the minimum threshold.
            
            Used in "strict".
            '''
            
            test_vals = simple_results
            
            # The success_rate of a group of tests is the ratio of
            # True tests per total tests.
            proportions = detailed_results
            success_rate = proportions[0]
            
            # If the success_rate is less than the threshold,
            # raise TestFailureError
            if success_rate < threshold:
                raise TestFailureError(test_items, success_rate, threshold)
      
            # It prints information if print_ is True and mode is "strict"
            if print_ and mode == "strict":
                print(f"""
                      Strict analysis:
                      \n· Number of True values: {test_vals[0]}\nPercentage of True values: {proportions[0]:%}\n
                      \n· Number of False values: {test_vals[1]}\nPercentage of False values: {proportions[1]:%}\n
                      \n· Number of None values: {test_vals[2]}\nPercentage of None values: {proportions[2]:%}\n
                      \n
                      \n The tests have passed, with {success_rate:%}, more than the {threshold:%} threshold.\n
                      
                      \nEnd of Strict Analysis.\n
                      """)
        
        # Returns results from StrictAnalysis().
        if mode == "strict":
            StrictAnalysis(test_items, simple_results, detailed_results, threshold, mode, print_ = print_)
            return {k:(v,w) for k, v, w in zip([True, False, None], simple_results, detailed_results)}, sorted_tests

            
        raise IndexError("There are no more modes in this function.")
        
    @staticmethod
    def UnitTestingAnalyze(tests: list, mode: str, *, print_: bool = True, threshold: float = 0.80, scope: dict = globals()) -> dict:
        '''
        Does Unit Testing for 
        the specified tests, then analyzes
        the results based on the available
        modes that TestingAnalysis() provides.
        
        It uses all UnitaryTests's methods
        to return the analysis, along with the data.
        '''
        
        # The test_results.
        test_results = UnitaryTests.TestingMethod(tests, print_ = print_, scope = scope)
        print("\n",30*"-","\n")
        
        # The analysis results.
        test_analysis = UnitaryTests.TestingAnalysis(test_results, mode, print_ = print_, threshold = threshold)
        print("\n",30*"-","\n")
        
        return test_results, test_analysis
    
    
if __name__ == "__main__":
    print("""This program alone does not do testing,
          \nbut it offers great tools to do so (UnitaryTests.TestingMethod(), UnitaryTests.TestingResults(), UnitaryTests.TestingAnalysis() for individual tasks,\n UnitaryTests.UnitTestingAnalyze() for all the tasks).
          \nUse the class UnitaryTests and its methods.
          \nThanks for checking the code out, have a nice day :D""")
