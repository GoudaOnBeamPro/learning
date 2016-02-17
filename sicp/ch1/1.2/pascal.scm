;;; This is a program that will find the value of a certain position on
;;; Pascal's Triangle by means of a recursive process. To do this, each
;;; element of the traingle is viewed as a coordinate (col,row), where
;;; col is the column of the element from left to right, and row is the
;;; row of the element. To compute the value of the element, the value
;;; of the element in the same column of the previous row is added to
;;; the value of the preceding column of the previous row. In this,
;;; we are only dealing with positive integers, so if the column or row
;;; are less than or equal to zero, the value of zero is returned.
;;; If at any point the value of the column is equal to one OR if the
;;; value of the column is equal to the value of the row, then one is
;;; returned.
;;;
;;; TL;DR Lookup up Pascal's Triangle online. It's neat.
;;;
;;; Rememebr, this is meant for an interpreter. Do not compile!

(define (pascal-t c r)
  (cond ((or (> c r) (<= c 0) (<= r 0)) 0)
	((or (= c 1) (= c r)) 1)
	(else (+ (pascal-t (- c 1)
			   (- r 1))
		 (pascal-t c (- r 1))))))
