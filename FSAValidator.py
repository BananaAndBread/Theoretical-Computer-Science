import re

def input_is_correct_e5(strings):
    """
    Return True if lines from the input are correct, False otherwise
    :param strings: array of lines from the input file
    :return: True if lines from the input are correct, False otherwise
    """
    #regular expressions for the lines
    reg1 = re.compile('(states)\=\{(\w+[,])*(\w+)*\}\n')
    reg2 = re.compile('(alpha)\=\{(\w+[,])*(\w+)*\}\n')
    reg3 = re.compile('(init.st)\=\{(\w+[,])*(\w+)*\}\n')
    reg4 = re.compile('(fin.st)\=\{(\w+[,])*(\w+)*\}\n')
    reg5 = re.compile('(trans)\=\{(\w*[>]\w*[>]\w*[,])*(\w*[>]\w*[>]\w*)*\\}')


    #check if they match
    c1=reg1.fullmatch(strings[0])
    c2=reg2.fullmatch(strings[1])
    c3=reg3.fullmatch(strings[2])
    c4=reg4.fullmatch(strings[3])
    c5=reg5.fullmatch(strings[4])

    if (c1 and c2 and c3 and c4 and c5):
        return True

    return False

def parse():
    """
    Parse the file fsa.txt. Recognises error E5
    :return: array arguments, where
        argument[0] : set of states
        argument[1] : set with alphabet
        argument[2] : set with only one initial state
        argument[3] : set of final states
        argument[4] : set of transitions
    or None if input is incorrect
    """
    f = open('fsa.txt', 'r')
    strings = f.readlines()
    if input_is_correct_e5(strings):
        arguments = list()
        for string in strings:
            after_the_bracket = (re.split(r'{', string))[1]
            inside_the_brackets = (re.split(r'}', after_the_bracket))[0]
            argument = (re.split(',', inside_the_brackets))
            arguments.append(set(argument))
        temp = list()
        for every in arguments[4]:

            argument = (re.split(r'>', every))
            temp.append(argument)
        arguments[4] = temp

        return arguments

    return None


def dfs(cur, created_graph):
    """

    :param cur: current vertex
    :param created_graph: graph represented as an adjacency list type of dictionary,
    key : name of vertex
    value : list with adjacent nodes' names
    :return: dictionary,
    key: name of vertex
    value: boolean, where True means it was encountered while traversing, False otherwise
    """

    usd = dict()
    def dfs_impl(cur, created_graph):

        usd[cur] = True
        adj_to_current = set(created_graph[cur])


        for every in adj_to_current:

            nxt = every

            if not usd.get(nxt):
                dfs_impl(nxt, created_graph)

        return usd
    return dfs_impl(cur,created_graph)


def input_is_correct_E2(created_graph):
    """
    Recognises error E2
    :param created_graph: graph represented as an adjacency list type of dictionary,
    key : name of vertex
    value : list with adjacent nodes' names
    :return: False if graph has more than one connected component, True otherwise
    """
    cnt=0;
    usd = dict()

    for every in created_graph:

        if not usd.get(every):
            usd.update(dfs(every, created_graph))
            cnt+=1
            if(cnt>1):
                return False
    return True



def build_directed_graph(relations):
    """

    :param relations: list, where:
        relation[0]: first state
        relation[1]: transition
        relation[2]: second state
    :return: directed graph represented as an adjacency list type of dictionary,
    key : name of vertex
    value : list with adjacent nodes' names
    """
    graph = dict()
    for relation in relations:
        graph[relation[0]] = list(list())
    for relation in relations:
        graph[relation[0]].append(relation[2])
    return graph


def build_undirected_graph(relations):
    """
    :param relations: list, where:
        relation[0]: first state
        relation[1]: transition
        relation[2]: second state
    :return: undirected graph represented as an adjacency list type of dictionary,
    key : name of vertex
    value : list with adjacent nodes' names

    """
    graph = dict()
    for relation in relations:
        graph[relation[0]] = list(list())
    for relation in relations:
        graph[relation[0]].append(relation[2])
        graph[relation[2]].append(relation[0])
    return graph



def input_is_correct_e1(arguments):
    """
    Recognises error E1
    :param arguments: list of arguments, where
        argument[0] : set of states
        argument[1] : set with alphabet
        argument[2] : set with only one initial state
        argument[3] : set of final states
        argument[4] : list of transitions
    :return:  True if a state s is in set of states, False otherwise
    """

    if(arguments[2]).issubset(arguments[0]):
        return True

    return False

def input_is_correct_e3(arguments):
    """
    Recognises error E3
    :param arguments: list of arguments, where
        argument[0] : set of states
        argument[1] : set with alphabet
        argument[2] : set with only one initial state
        argument[3] : set of final states
        argument[4] : list of transitions
    :return: False if  a transition a is not represented in the alphabet, True otherwise
    """
    result = True
    for every in arguments[4]:
            result = every[1] in arguments[1] and result
            if result == False:
                return [False, every[1]]
    return [result, "lol"]
def input_is_correct_e4(arguments):
    """
    Recognises error E4
    :param arguments: list of arguments, where
        argument[0] : set of states
        argument[1] : set with alphabet
        argument[2] : set with only one initial state
        argument[3] : set of final states
        argument[4] : list of transitions
    :return: False if  initial state is not defined, True otherwise
    """
    if arguments[2] == {''}:
        return False

    return True

def create_set_from_dict(dictionary):
    """
    Creates set from dict
    :param dictionary: dictionary,
    key: name of vertex
    value: boolean, where True means it will be added to the future dictionary, False otherwise
    :return: set created out of the dictionary
    """
    final_set = set()
    for every in dictionary:
        if dictionary[every] == True:
            final_set.add(every)
    return final_set

def input_is_correct_W2(created_graph, arguments):
    """
    Recognises warning W2
    :param created_graph:
    :param arguments: list of arguments, where
        argument[0] : set of states
        argument[1] : set with alphabet
        argument[2] : set with only one initial state
        argument[3] : set of final states
        argument[4] : list of transitions
    :return: False if some states are not reachable from initial state, True otherwise
    """
    initial_state = arguments[2].pop()

    usd = dfs(initial_state,created_graph)
    usd = create_set_from_dict(usd)

    difference = arguments[0].difference(usd)
    if difference:
        return False
    return True

def input_is_correct_W1(arguments):
    """
    Recognises warning W1
    :param arguments: list of arguments, where
        argument[0] : set of states
        argument[1] : set with alphabet
        argument[2] : set with only one initial state
        argument[3] : set of final states
        argument[4] : list of transitions
    :return: False if accepting state is not defined True otherwise
    """
    if arguments[3] == {''}:
        return False

    return True
def input_is_correct_W3(states_with_transitions):
    """

    :param states_with_transitions: dictionary, where
        key: state
        value: list of all state's transitions
    :return: False if FSA is nondeterministic, True otherwise
    """
    result = True
    for every in states_with_transitions:
        result=result and (len(set(states_with_transitions[every])) == len(states_with_transitions[every]))
    return result

def is_complete(arguments):
    """

    :param arguments: list of arguments, where
        argument[0] : set of states
        argument[1] : set with alphabet
        argument[2] : set with only one initial state
        argument[3] : set of final states
        argument[4] : list of transitions
    :return: True if FSA is complete, False otherwise
    """
    states_with_transitions = collect_states_with_transitions(arguments[4])
    result = True
    for every in states_with_transitions:
        result= result and set(states_with_transitions[every]) == arguments[1]
    return result



def collect_states_with_transitions(transitions):
    """

    :param transitions: list of transitions
    :return: dict(), where:
        key: state's name
        value: list of all its transitions
    """

    graph = dict()
    for transition in transitions:
        graph[transition[0]] = list(list())
    for transition in transitions:
        graph[transition[0]].append(transition[1])
    return graph

def collect_errors(f):
    """
    Check for errors, write in the output
    :return: True if any errors were found, false otherwise
    """
    if arguments == None:
        f.write("Error:\n"
              "E5: Input file is malformed\n")
        return True
    if not input_is_correct_e1(arguments):
        initial_state = arguments[2].pop()
        string = ("Error:\n" +
              "E1: A state '" + initial_state + "' is not in set of states\n")
        f.write(string)
        return True

    if not input_is_correct_e3(arguments)[0]:
        string = ("Error:\n"+
              "E3: A transition '"+input_is_correct_e3(arguments)[1]+"' is not represented in the alphabet\n")
        f.write(string)

        return True
    graph = build_undirected_graph(arguments[4])
    if not input_is_correct_E2(graph):
        f.write("Error:\n"
              "E2: Some states are disjoint\n")
        return True
    return False

def collect_warnings(f):
    """
    Check and collect warnings, define whether FSA is complete, write in the output
    """

    if is_complete(arguments):
        f.write('FSA is complete\n')
    if not is_complete(arguments):
        f.write('FSA is incomplete\n')
    resW1 = input_is_correct_W1(arguments)
    resW2 = input_is_correct_W2(build_directed_graph(arguments[4]), arguments)
    resW3 = input_is_correct_W3(collect_states_with_transitions(arguments[4]))

    if not (resW1 and resW2 and resW3):
        f.write("Warning:\n")
        if not resW1:
            f.write('W1: Accepting state is not defined\n')
        if not resW2:
            f.write('W2: Some states are not reachable from initial state\n')
        if not resW3:
            f.write('W3: FSA is nondeterministic\n')

def validateFSA():
    """
    validate FSA, write in the output.txt
    """
    f = open("result.txt", 'w+')

    if not collect_errors(f):

        collect_warnings(f)
    f.seek(0)
    lines = f.readlines()
    lines[-1]=lines[-1].rstrip()
    f.seek(0)
    for line in lines:
        f.write(line)
    f.truncate()
    f.close()



arguments = parse()
validateFSA()
