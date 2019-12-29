from robot.api import ExecutionResult, ResultVisitor

passed_suites = []
failed_suites = []
test_list = []
res_dict ={}

class SuiteResults(ResultVisitor):
    '''
    Uses inherited methods from ResultVisitor to parse the robot output xml file.
    start_test method iterates over all the tests in output xml file.
    start_suite method iterates over all the suites in output xml file.
    '''

    def start_test(self,test):
        # print( 'location:', test.longname.split('.')[-2])
        global test_list
        if test.status == "FAIL":
            test_list.append((test.parent, test.name, test.status, test.message))
        else:
            test_list.append((test.parent, test.name, test.status))

    def start_suite(self,suite):
        suite_test_list = suite.tests
        if not suite_test_list:
            pass
        else:     
            if suite.status== "PASS":
                res_dict[suite] = suite.status
            else:
                # global failed_suite
                res_dict[suite] = suite.status

def get_stats(xml_file):
    '''
    This function does the separation of passed suites and failed suites and returns a dictionary containing them as keys.
    passed suites key contains value as list of dictionaries which consist of suite name as key and testcases as values.
    failed suites key contains value as list of dictionaries which consist of suite name as key and testcases as values.

    *Parameters:* xml_file is a output.xml file generated by robot framework.

    *Return:* Returns a dictionary containing passed suites and failed suites
    Example:
    {'passed_suites': [{'suite1': [('test1', 'PASS'),('test2', 'PASS')]}], 'failed_suites': [{'suite2': [('test1', 'FAIL', 'device not responding'), ('test2', 'PASS')]}]}

    '''
    result = ExecutionResult(xml_file)
    result.visit(SuiteResults())
    temp_passed_suites = []
    temp_failed_suites = []
    for item in test_list:
        if res_dict[item[0]] == 'PASS':
            if passed_suites:
                for each in passed_suites:
                    temp_passed_suites.append(list(each.keys())[0])

                if item[0] in temp_passed_suites:
                    for each in passed_suites:
                        if item[0] == list(each.keys())[0]:
                            each[item[0]].append((item[1], item[2]))
                else:
                    passed_suites.append({item[0] : [(item[1], item[2])]})
            else:
                passed_suites.append({item[0] : [(item[1], item[2])]})

        else:
            if failed_suites:
                for each in failed_suites:
                    temp_failed_suites.append(list(each.keys())[0])

                if item[0] in temp_failed_suites:
                    for each in failed_suites:
                        if item[0] == list(each.keys())[0]:
                            if item[2] == 'PASS':
                                each[item[0]].append((item[1], item[2]))
                            else:
                                each[item[0]].append((item[1], item[2], item[3]))
                else:
                    if item[2] == 'PASS':
                        failed_suites.append({item[0] : [(item[1], item[2])]})
                    else:
                        failed_suites.append({item[0] : [(item[1], item[2], item[3])]})
            else:
                if item[2] == 'PASS':
                    failed_suites.append({item[0] : [(item[1], item[2])]})
                else:
                    failed_suites.append({item[0] : [(item[1], item[2], item[3])]})

    return {'passed_suites': passed_suites , 'failed_suites' : failed_suites}


if __name__ == '__main__':
    
    print(get_stats('output.xml'))