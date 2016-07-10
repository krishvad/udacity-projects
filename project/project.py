
import random
import questions
from functions import checkAnswers, whichQuestion, qScore
import globalVariables


whichQuestion ()
currentQuestion = globalVariables.currentQuestion
globalVariables.correctAnswerCount = globalVariables.correctAnswerCount

while True:
	print globalVariables.currentQuestion
	if globalVariables.correctAnswerCount !=3:
		rawInputString = "\nEnter answer for blank #" + str(globalVariables.correctAnswerCount+1) + "\t"
		userAnswer = raw_input (rawInputString)
	else:
		break
	if checkAnswers(userAnswer, globalVariables.nextBlank):
		if globalVariables.correctAnswerCount!=3:
			globalVariables.currentQuestion = globalVariables.currentQuestion.replace ('____'+str(globalVariables.correctAnswerCount+1)+'____', userAnswer.upper())
		globalVariables.correctAnswerCount += 1
		globalVariables.retriesLeft = 3
		globalVariables.nextBlank += 1
		if globalVariables.nextBlank == globalVariables.correctAnswerCount == 3:
			print "You have answered this question correctly"
			globalVariables.dictCorrectAnsweresByType['HARD'] = globalVariables.dictCorrectAnsweresByType['HARD'] + 1
			if len(globalVariables.answeredToughQuestions) != 4:
				whichQuestion()
			else:
				qScore()
				break
		continue
	else:
		globalVariables.retriesLeft -= 1
		print "Length"+str(len(globalVariables.answeredToughQuestions))
		if globalVariables.retriesLeft == 0 and len(globalVariables.answeredToughQuestions) != 4:
			print "You have exhaused all the retries. The next question in the category chosen will be displayed next"
			whichQuestion()
		elif globalVariables.retriesLeft == 0 and len(globalVariables.answeredToughQuestions) == 4:
			print "\nYou have answered all questions, lets see your score"
			qScore()
			break
		else:
			print "Try again, you have "+str(globalVariables.retriesLeft)+" retries left for this blank\n"
			continue
	


