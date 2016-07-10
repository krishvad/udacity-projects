
import questions
import random
import globalVariables



def checkAnswers(userAnswer, nextBlank):
	correctAnswer = questions.toughList[globalVariables.nextQuestionIndex][globalVariables.nextBlank]
	if userAnswer.upper() == correctAnswer.upper():
		return True
	else:
		return False

def setVariables():
	

def whichQuestion():
	while  True:
		globalVariables.nextQuestionIndex = random.randint(0,3)
		if globalVariables.nextQuestionIndex not in globalVariables.answeredToughQuestions and len(globalVariables.answeredToughQuestions)<4:
			globalVariables.retriesLeft = 3
			globalVariables.correctAnswerCount = 0
			globalVariables.correctAnswerCount = 0
			globalVariables.nextBlank = 0
			break
	globalVariables.currentQuestion = questions.toughList[globalVariables.nextQuestionIndex][globalVariables.questionIndex]
	globalVariables.answeredToughQuestions.append(globalVariables.nextQuestionIndex)
	print "\nQuestion "+str(len(globalVariables.answeredToughQuestions))+" of 4\n"+ "-"*50
	return globalVariables.nextQuestionIndex

def qScore():
	print "-"*25+"Your score"+"-"*25
	print "You have answered "+str(globalVariables.dictCorrectAnsweresByType['HARD'])+ " out of 4 hard questions correctly\n"
	print "You have answered "+str(globalVariables.dictCorrectAnsweresByType['MEDIUM'])+ " out of 4 medium questions correctly\n"
	print "You have answered "+str(globalVariables.dictCorrectAnsweresByType['EASY'])+ " out of 4 easy questions correctly\n"
	print "-"*25+"Your score"+"-"*25
