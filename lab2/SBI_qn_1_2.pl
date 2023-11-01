/*relationships*/
competitor(sumsum,appy).
develop(sumsum,gs3).
boss(stevey,appy).
steal(stevey,gs3).
tech(gs3).

/*rules*/
rival(X,Y) :- competitor(X,Y);competitor(Y,X).
business(X) :- tech(X).
unethical(A) :- boss(A,X), steal(A,Y), rival(X,Z), develop(Z,Y), business(Y).
