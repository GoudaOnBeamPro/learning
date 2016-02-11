;;; This is the program for exercise 1.11. This is the linear recursive 
;;; example of the function definition of f(n) = n if n < 3, and
;;; f(n) = f(n - 1) + 2f(n - 2) + 3f(n - 3) if n >= 3.
;;;
;;; Compared to the iterative procedure, this one is a breeze!
;;;
;;; Remember, this is meant for an interpreter. :)

(define (f n)
  (if (< n 3)
    n
    (+ (f (- n 1))
       ( * 2 (f (- n 2)))
       ( * 3 (f (- n 3))))))
