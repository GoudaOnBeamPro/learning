;;; This program computes the number of ways to give change with coins ranging
;;; from half-dollars to pennies for an amount represented in terms of cents
;;; (which is the dollar amount * 100). This program is also tree recursive,
;;; and has similar computation redundancies to the fib-tree. It isn't
;;; obvious how we can create a better algorithm from this, for now, so
;;; that will be a challenge for later.
;;;
;;; As always, this isn't meant to be compiled. Run it in an interpreter.

(define (count-change amount)
  (cc amount 5))
(define (cc amount kinds-of-coins)
  (cond ((= amount 0) 1)
	((or (< amount 0) (= kinds-of-coins 0)) 0)
	(else (+ (cc amount
		     (- kinds-of-coins 1))
		 (cc (- amount
			(first-denomination kinds-of-coins))
		     kinds-of-coins)))))
(define (first-denomination kinds-of-coins)
  (cond ((= kinds-of-coins 1) 1)
	((= kinds-of-coins 2) 5) 
	((= kinds-of-coins 3) 10)
	((= kinds-of-coins 4) 25)
	((= kinds-of-coins 5) 50)))
