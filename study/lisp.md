apt-get install clisp


(defparameter *nodes* '((living-room (you are in the living-room.
a wizard is snoring loudly on the couch.))
(garden (you are in a beautiful garden.
there is a well in front of you.))
(attic (you are in the attic.
there is a giant welding torch in the corner.))))

(assoc 'garden *nodes*)

(defun describe-location (location nodes)
(cadr (assoc location nodes)))

(describe-location 'living-room *nodes*)

(defparameter *edges* '((living-room (garden west door)
(attic upstairs ladder))
(garden (living-room east door))
(attic (living-room downstairs ladder))))



(defun describe-path (edge)
`(there is a ,(caddr edge) going ,(cadr edge) from here.))

(defun describe-paths (location edges)
(apply #'append (mapcar #'describe-path (cdr (assoc location edges)))))

(defparameter *objects* '(whiskey bucket frog chain))

(defparameter *object-locations* '((whiskey living-room)
(bucket living-room)
(chain garden)
(frog garden)))



(defun objects-at (loc objs obj-locs)
(labels ((at-loc-p (obj)
(eq (cadr (assoc obj obj-locs)) loc)))
(remove-if-not #'at-loc-p objs)))


(defun describe-objects (loc objs obj-loc)
(labels ((describe-obj (obj)
`(you see a ,obj on the floor.)))
(apply #'append (mapcar #'describe-obj (objects-at loc objs obj-loc)))))

(defparameter *location* 'living-room)

(defun look ()
(append (describe-location *location* *nodes*)
(describe-paths *location* *edges*)
(describe-objects *location* *objects* *object-locations*)))



(defun walk (direction)
(let ((next (find direction
(cdr (assoc *location* *edges*))
:key #'cadr)))
(if next
(progn (setf *location* (car next))
(look))
'(you cannot go that way.))))

(walk 'west)

(defun pickup (object)
(cond ((member object
(objects-at *location* *objects* *object-locations*))
(push (list object 'body) *object-locations*)
`(you are now carrying the ,object))
(t '(you cannot get that.))))

(defun inventory ()
(cons 'items- (objects-at 'body *objects* *object-locations*)))

(loop for i
below (* 50000 50000)
do (print i))

(defun random-animal ()
(nth (random 5) '("dog" "tick" "tiger" "walrus" "kangaroo")))

(loop repeat 10
do (format t "~5t~a ~15t~a ~25t~a~%"
(random-animal)
(random-animal)
(random-animal)))

