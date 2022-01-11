import re
def UNIFY(x,y,sub):
    print(x,y,sub)
    if sub == -1:print("minus 1"); return -1
    elif x == y:print("same"); return sub
    elif VARIABLE(x):print("var x"); return UNIFY_VAR(x,y,sub)
    elif VARIABLE(y):print("var y"); return UNIFY_VAR(y,x,sub) 
    elif COMPOUND(x) and COMPOUND(y):
        print("coumpound");
        return UNIFY(ARGS(x),ARGS(y),UNIFY(OP(x),OP(y),sub))
    elif LIST(x) and LIST(y) and len(x) == len(y):
        print("list");
        return UNIFY(x[1:],y[1:],UNIFY(x[0],y[0],sub))
    else:print("none"); return -1

def VARIABLE(x):
    if type(x) == list: return False
    elif re.search("^[a-z]$",x): return True
    else: return False

def COMPOUND(x):
    if type(x) == list: return False
    return re.search("^.+\(.*\)$", x)

def ARGS(x):
    arg = re.findall("\((.*)\)", x)[0].split(",")
    if len(arg) == 1:
        return arg[0]
    else:
        return arg

def OP(x):
    return re.findall("^([a-zA-Z]+)\(.*\)$", x)[0]

def LIST(x):
    return True if type(x) == list else False
def UNIFY_VAR(var, x, sub):
    if var in sub: return UNIFY(sub[var],x,sub)
    elif x in sub: return UNIFY(var,sub[var],sub)
    elif OCCUR_CHECK(var,x): return -1
    else:
        sub[var]=x
        return sub

def OCCUR_CHECK(x,y):
    if x in y: return True
    else: return False

s1 = "Knows(x,Father(y),d)"
s2 = "Knows(John,Father(Hello),Mother(Mary))"
substitution = UNIFY(s1,s2,{})
if (substitution == -1):
    print("Substitution not possible!")
else:
    print("Successfull:", substitution)

