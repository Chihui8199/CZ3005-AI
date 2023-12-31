%%Define Relations and Rules 
child_of(charles,elizabeth).
child_of(andrew,elizabeth).
child_of(ann,elizabeth).
child_of(edward,elizabeth).

younger_than(ann,charles).
younger_than(andrew,ann).
younger_than(edward,andrew).

%%Define rule for age
is_younger(X,Y):- younger_than(X,Y).
is_younger(X,Y):- younger_than(X,Z),is_younger(Z,Y).

%%Define Sorting algorithm by succession
insert(A,[B|C],[B|D]):- (is_younger(A,B)),!,insert(A,C,D).
insert(A,C,[A|C]).

ordering_by_birth([A|B],SortList):- ordering_by_birth(B,Tail), insert(A,Tail,SortList).
ordering_by_birth([],[]).

% Return succession list according to sort
line_of_succession(X,Line_of_Succession):- findall(Y,child_of(Y,X),ChildNodes),ordering_by_birth(ChildNodes,Line_of_Succession).