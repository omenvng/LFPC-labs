import copy


def large(rules, let, voc):

    newDict = copy.deepcopy(rules)
    for key in newDict:
        values = newDict[key]
        for i in range(len(values)):
            if len(values[i]) > 2:
                for j in range(0, len(values[i]) - 2):
                    if j == 0:
                        rules[key][i] = rules[key][i][0] + let[0]
                    else:
                        rules.setdefault(newKey, []).append(values[i][j] + let[0])
                    voc.append(let[0])
                    newKey = copy.deepcopy(let[0])
                    let.remove(let[0])
                rules.setdefault(newKey, []).append(values[i][-2:])

    return rules, let, voc
# end of large function


def empty(rules, voc):

    emptyList = []

    new_dict = copy.deepcopy(rules)
    for key in new_dict:
        values = new_dict[key]
        for i in range(len(values)):
            if values[i] == 'e' and key not in emptyList:
                emptyList.append(key)
                rules[key].remove(values[i])
        if len(rules[key]) == 0:
            if key not in rules:
                voc.remove(key)
            rules.pop(key, None)

    new_dict = copy.deepcopy(rules)
    for key in new_dict:
        values = new_dict[key]
        for i in range(len(values)):
            if len(values[i]) == 2:

                if values[i][0] in emptyList and key != values[i][1]:
                    rules.setdefault(key, []).append(values[i][1])

                if values[i][1] in emptyList and key != values[i][0]:
                    if values[i][0] != values[i][1]:
                        rules.setdefault(key, []).append(values[i][0])

    return rules, voc
# end of empty function


def short(rules, voc):

    D = dict(zip(voc, voc))

    for key in D:
        D[key] = list(D[key])

    for letter in voc:
        for key in rules:
            if key in D[letter]:
                values = rules[key]
                for i in range(len(values)):
                    if len(values[i]) == 1 and values[i] not in D[letter]:
                        D.setdefault(letter, []).append(values[i])

    rules, D = shortUtil(rules, D)
    return rules, D
# end of short function


def shortUtil(rules, D):

    # remove short rules (with length in right side = 1)
    newDict = copy.deepcopy(rules)
    for key in newDict:
        values = newDict[key]
        for i in range(len(values)):
            if len(values[i]) == 1:
                rules[key].remove(values[i])
        if len(rules[key]) == 0:
            rules.pop(key, None)

    # replace each rule A->BC with A->B'C', where B' in D(B) and C' in D(C)
    for key in rules:
        values = rules[key]
        for i in range(len(values)):
            # search all possible B' in D(B)
            for j in D[values[i][0]]:
                # search all possible C' in D(C)
                for k in D[values[i][1]]:
                    # concatenate B' and C' and insert a new rule
                    if j+k not in values:
                        rules.setdefault(key, []).append(j + k)

    return rules, D
# end of short1 function


def finalRules(rules, D, S):

    for let in D[S]:
        # check if a key has no values
        if not rules[S] and not rules[let]:
            for v in rules[let]:
                if v not in rules[S]:
                    rules.setdefault(S, []).append(v)
    return rules
# end of finalRules function


def printRules(rules):
    for key in rules:
        values = rules[key]
        for i in range(len(values)):
            print(key + '->' + values[i])
    return 1
# end of printRules function
